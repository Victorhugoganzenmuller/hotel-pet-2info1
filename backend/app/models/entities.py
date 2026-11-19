from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Tutor(Base):
    __tablename__ = "tutores"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nome: Mapped[str] = mapped_column(String(150), nullable=False)
    telefone: Mapped[str | None] = mapped_column(String(30))
    cpf_cnpj: Mapped[str | None] = mapped_column("cpfCnpj", String(20))
    email: Mapped[str | None] = mapped_column(String(150))

    pets: Mapped[list["Pet"]] = relationship(back_populates="tutor")


class Pet(Base):
    __tablename__ = "pets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    especie: Mapped[str] = mapped_column(String(50), nullable=False)
    tutor_id: Mapped[int] = mapped_column("tutorId", ForeignKey("tutores.id"), nullable=False)

    tutor: Mapped[Tutor] = relationship(back_populates="pets")
