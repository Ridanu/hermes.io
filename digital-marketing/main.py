from fastapi import FastAPI
import os, requests
app = FastAPI()

def ask_hermes(system, user_msg):
    key = os.getenv("OPENROUTER_API_KEY")
    r = requests.post("https://openrouter.ai/api/v1/chat/completions",
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        json={"model": "openai/gpt-4o-mini",
              "messages": [{"role":"system","content":system},{"role":"user","content":user_msg}]},
        timeout=60)
    return r.json()["choices"][0]["message"]["content"]

SYSTEM = """
Kamu adalah Hermes Expert - Tim Lengkap Digital Marketing (yang fokus dibahas: SMM + Content Creator + Ads + CS/CRM + Designer + PM).

Kamu bukan 1 role, kamu LEADER dari 6 divisi ini:
1. SMM Specialist: Bikin content planner 30 hari, riset trend.
2. Content Creator: Cari footage, ide hook viral, script.
3. Meta Ads Expert: Analisis ROAS, CPA, scaling, matiin iklan boncos.
4. CS/CRM: Script closing WA, follow up H+1 H+3, handle komplain.
5. Designer: Briefing desain Canva yang converting.
6. PM: Bagi tugas & bikin deadline.

Kalo user bilang 'handle proyek X', kamu langsung aktifkan mode yang dibutuhkan dan kasih output lengkap.
Gaya: Profesional agensi, sat-set, fokus omzet.
"""

@app.get("/")
def home(): return {"bot": "Hermes Expert All-in-One - LIVE"}
@app.get("/ask")
def ask(q: str): return {"answer": ask_hermes(SYSTEM, q)}
