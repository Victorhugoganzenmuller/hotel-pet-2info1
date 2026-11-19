from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.entities import Tutor
from app.models.schemas import TutorSchema

router = APIRouter(prefix="/tutores", tags=["Tutores"])


@router.get("", response_model=list[TutorSchema], summary="Listar tutores")
def listartutores(db: Session = Depends(get_db)):
    return db.query(Tutor).order_by(Tutor.id).all()


@router.get("/{tutor_id}", response_model=TutorSchema, summary="Consultar tutor por ID")
def consultartutor(tutor_id: int, db: Session = Depends(get_db)):
    tutor = db.query(Tutor).filter(Tutor.id == tutor_id).first()
    if tutor is None:
        raise HTTPException(status_code=404, detail="Tutor não encontrado")
    return tutor
