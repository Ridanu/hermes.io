from fastapi import FastAPI
import os, requests
app = FastAPI()

def ask_hermes(system, user_msg):
    key = os.getenv("OPENROUTER_API_KEY")
    r = requests.post("https://openrouter.ai/api/v1/chat/completions",
        headers={"Authorization": f"Bearer {key}"},
        json={"model": "openai/gpt-4o-mini",
              "messages": [{"role":"system","content":system},{"role":"user","content":user_msg}]})
    return r.json()["choices"][0]["message"]["content"]

SYSTEM = "Kamu Hermes Digital Marketing ZeroMind.Media, bantu strategi funnel, FB/IG Ads, closing WA. Gaya santai Indonesia."

@app.get("/")
def home(): return {"bot": "Digital Marketing - LIVE"}
@app.get("/ask")
def ask(q: str): return {"answer": ask_hermes(SYSTEM, q)}