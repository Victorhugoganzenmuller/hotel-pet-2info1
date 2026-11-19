from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.entities import Pet
from app.models.schemas import PetSchema

router = APIRouter(prefix="/pets", tags=["Pets"])


@router.get("", response_model=list[PetSchema], summary="Listar pets")
def listarpets(db: Session = Depends(get_db)):
    return db.query(Pet).order_by(Pet.id).all()


@router.get("/{pet_id}", response_model=PetSchema, summary="Consultar pet por ID")
def consultarpet(pet_id: int, db: Session = Depends(get_db)):
    pet = db.query(Pet).filter(Pet.id == pet_id).first()
    if pet is None:
        raise HTTPException(status_code=404, detail="Pet não encontrado")
    return pet
