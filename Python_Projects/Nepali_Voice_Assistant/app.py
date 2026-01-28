import os, tempfile, threading, datetime
import tkinter as tk
from tkinter import scrolledtext
import speech_recognition as sr
from gtts import gTTS
import playsound
import wikipedia
from dotenv import load_dotenv

# from utils.speech_utils import listen_nepali, speak_nepali
# from utils.ai_utils import ask_llm, generate_image

# ---------- Load environment ----------
load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_API_KEY", "")

# ---------- (Optional) LLM client ----------
client = None
if OPENAI_KEY:
    try:
        from openai import OpenAI  # modern SDK
        client = OpenAI(api_key=OPENAI_KEY)
    except Exception:
        client = None  # continue without LLM

# ---------- Core: Speech-to-Text (Nepali) ----------
def listen_nepali(status_cb=lambda s: None):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        status_cb("🎙 सुनिरहेको छु... (शान्त वातावरण राख्नुहोस्)")
        r.adjust_for_ambient_noise(source, duration=0.6)
        audio = r.listen(source, timeout=7, phrase_time_limit=12)
    try:
        text = r.recognize_google(audio, language="ne-NP")
        status_cb("✅ सुनेको छु")
        return text.strip()
    except sr.WaitTimeoutError:
        status_cb("⏱ समय समाप्त")
    except sr.UnknownValueError:
        status_cb("❌ मैले बुझिन")
    except Exception:
        status_cb("⚠️ सुन्ने क्रममा समस्या")
    return ""

# ---------- Core: Text-to-Speech (Nepali) ----------
def speak_nepali(text):
    if not text:
        return
    # use a temp file so parallel calls don’t clash
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tmp.close()
    try:
        gTTS(text=text, lang="ne").save(tmp.name)
        playsound.playsound(tmp.name)
    finally:
        try:
            os.remove(tmp.name)
        except Exception:
            pass

# ---------- (Optional) Ask LLM in Nepali ----------
def ask_llm(prompt):
    if not client:
        return "इण्टरनेट/एपीआई उपलब्ध छैन, कृपया पछि प्रयास गर्नुहोस्।"
    try:
        # Chat Completions (supported path in current SDK)
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "तिमी नेपालीमा नै उत्तर दिने सहायक हौ।"},
                {"role": "user", "content": prompt}
            ],
        )
        return resp.choices[0].message.content.strip()
    except Exception:
        return "सर्भरमा समस्या आयो।"

# ---------- Command Router ----------
wikipedia.set_lang("ne")

def process_command(cmd: str) -> str:
    c = cmd.strip()

    # 1) Time
    if "समय" in c or "टाइम" in c:
        now = datetime.datetime.now().strftime("%I:%M %p")
        return f"अहिलेको समय {now} हो।"

    # 2) Wikipedia (Nepali)
    if "विकिपीडिया" in c:
        topic = c.replace("विकिपीडिया", "").strip() or "नेपाल"
        try:
            summary = wikipedia.summary(topic, sentences=2)
            return summary
        except wikipedia.DisambiguationError as e:
            return f"थुप्रै नतिजा भेटियो, कृपया स्पष्ट गर्नुहोस्: {', '.join(e.options[:5])} ..."
        except wikipedia.PageError:
            return "माफ गर्नुहोस्, त्यो पृष्ठ भेटिएन।"

    # 3) Simple open commands (demo only)
    if "युट्युब" in c or "youtube" in c:
        os.startfile("https://www.youtube.com/")
        return "युट्युब खोल्दैछु।"
    if "गुगल" in c or "google" in c:
        os.startfile("https://www.google.com/")
        return "गुगल खोल्दैछु।"

    # 4) Fallback → LLM (if available)
    return ask_llm(c)

    # # 5) Image generation
    # if "चित्र" in c or "picture" in c:
    #     prompt = c.replace("चित्र", "").replace("picture", "").strip()
    # if not prompt: 
    #     return "कस्तो चित्र चाहिन्छ?"
    # try:
    #     url = generate_image(prompt)
    #     return f"चित्र तयार भयो: {url}"
    # except:
    #     return "चित्र बनाउन समस्या आयो।"


# ---------- GUI logic ----------
class App:
    def __init__(self, root):
        self.root = root
        root.title("नेपाली भ्वाइस असिस्टेन्ट")
        root.geometry("700x520")

        self.title = tk.Label(root, text="नेपाली भ्वाइस असिस्टेन्ट", font=("Arial", 18, "bold"))
        self.title.pack(pady=8)

        self.chat = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12))
        self.chat.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.status_var = tk.StringVar(value="तयार छ…")
        self.status = tk.Label(root, textvariable=self.status_var, fg="blue")
        self.status.pack(pady=4)

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=6)

        self.listen_btn = tk.Button(btn_frame, text="🎙 बोल्नुहोस्", font=("Arial", 13), bg="green", fg="white", command=self.start_listening)
        self.listen_btn.grid(row=0, column=0, padx=6)

        self.type_entry = tk.Entry(btn_frame, width=40, font=("Arial", 12))
        self.type_entry.grid(row=0, column=1, padx=6)
        self.send_btn = tk.Button(btn_frame, text="पठाउनुहोस्", command=self.send_text)
        self.send_btn.grid(row=0, column=2, padx=6)

        self.quit_btn = tk.Button(root, text="❌ बन्द गर्नुहोस्", bg="crimson", fg="white", command=root.quit)
        self.quit_btn.pack(pady=6)

    def set_status(self, s): self.status_var.set(s)

    def append_chat(self, who, text):
        self.chat.insert(tk.END, f"{who}: {text}\n")
        self.chat.see(tk.END)

    def _listen_thread(self):
        cmd = listen_nepali(self.set_status)
        if not cmd: 
            return
        self.append_chat("👤 तपाईं", cmd)
        if "बन्द" in cmd:
            speak_nepali("ठिक छ, बाइबाइ!")
            self.root.quit()
            return
        reply = process_command(cmd)
        self.append_chat("🤖 सहायक", reply)
        speak_nepali(reply)

    def start_listening(self):
        threading.Thread(target=self._listen_thread, daemon=True).start()

    def send_text(self):
        cmd = self.type_entry.get().strip()
        if not cmd: return
        self.type_entry.delete(0, tk.END)
        self.append_chat("👤 तपाईं (टाइप)", cmd)
        if "बन्द" in cmd:
            speak_nepali("ठिक छ, बाइबाइ!")
            self.root.quit()
            return
        reply = process_command(cmd)
        self.append_chat("🤖 सहायक", reply)
        speak_nepali(reply)

if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
