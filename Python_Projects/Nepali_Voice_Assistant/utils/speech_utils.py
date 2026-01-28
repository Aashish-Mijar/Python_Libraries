import speech_recognition as sr
from gtts import gTTS
import playsound, os, tempfile

def listen_nepali(status_cb=lambda s: None):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        status_cb("🎙 सुनिरहेको छु...")
        r.adjust_for_ambient_noise(source, duration=0.6)
        audio = r.listen(source, timeout=7, phrase_time_limit=12)
    try:
        return r.recognize_google(audio, language="ne-NP").strip()
    except: return ""

def speak_nepali(text):
    if not text: return
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tmp.close()
    gTTS(text=text, lang="ne").save(tmp.name)
    playsound.playsound(tmp.name)
    os.remove(tmp.name)
