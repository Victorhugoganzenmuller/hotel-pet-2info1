import json
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, SessionLocal, engine
from app.models.entities import Pet, Tutor
from app.routes.pets import router as pets_router
from app.routes.tutores import router as tutores_router

app = FastAPI(
    title="Hotel Pet API",
    description="API do sistema de gerenciamento de tutores e pets.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tutores_router)
app.include_router(pets_router)


def importar_dados_iniciais() -> None:
    arquivo = Path(__file__).resolve().parents[2] / "db.json"
    if not arquivo.exists():
        return

    dados = json.loads(arquivo.read_text(encoding="utf-8"))
    with SessionLocal() as db:
        if db.query(Tutor).first() is None:
            for item in dados.get("tutores", []):
                db.add(Tutor(
                    id=int(item["id"]),
                    nome=item["nome"],
                    telefone=item.get("telefone"),
                    cpf_cnpj=item.get("cpfCnpj"),
                    email=item.get("email"),
                ))

        if db.query(Pet).first() is None:
            for item in dados.get("pets", []):
                db.add(Pet(
                    id=int(item["id"]),
                    nome=item["nome"],
                    especie=item["especie"],
                    tutor_id=int(item["tutorId"]),
                ))
        db.commit()


@app.on_event("startup")
def inicializar_banco() -> None:
    Base.metadata.create_all(bind=engine)
    importar_dados_iniciais()


@app.get("/", tags=["Informações"])
def raiz():
    return {"mensagem": "API do Hotel Pet funcionando", "documentacao": "/docs"}
