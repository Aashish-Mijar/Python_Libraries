import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_llm(prompt, nepali=True):
    system_msg = "तिमी नेपालीमा नै उत्तर दिने सहायक हौ।" if nepali else "You are a helpful assistant."
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": system_msg},
                  {"role": "user", "content": prompt}]
    )
    return resp.choices[0].message.content.strip()

def generate_image(prompt, size="512x512"):
    resp = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size=size
    )
    return resp.data[0].url
