from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="RamTech ERP Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # luego afinamos solo para frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "🚀 Backend RamTech ERP activo y listo."}
