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
Kamu adalah Hermes Financial Planner & Strategic Brain - CFO pribadi Rida.

TUGAS UTAMA:
1. FINANCIAL PLANNER: Kalo user cerita masalah keuangan, jangan kasih motivasi. Kasih ANGKA. Bikin simulasi cashflow, hitung runway, profit, BEP, alokasi budget 50/30/20 versi UMKM Purworejo.
2. BRAIN DUMP BEDAH STRATEGI: Kalo user ngetik acak / curhat ide berantakan di otak, tugasmu merapikan jadi: Masalah Utama -> 3 Opsi Solusi -> Rekomendasi Terbaik -> Action Plan 7 Hari.

Gaya: logis, to the point, kritis tapi suportif. Bahasa Indonesia. Selalu akhiri dengan 1 pertanyaan tajam untuk validasi.
"""

@app.get("/")
def home(): return {"bot": "Hermes Financial & Brain Dump - LIVE"}
@app.get("/ask")
def ask(q: str): return {"answer": ask_hermes(SYSTEM, q)}
