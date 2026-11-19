from pydantic import BaseModel, ConfigDict, Field


class TutorSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

    id: int
    nome: str
    telefone: str | None = None
    cpfCnpj: str | None = Field(default=None, serialization_alias="cpfCnpj", validation_alias="cpf_cnpj")
    email: str | None = None


class PetSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

    id: int
    nome: str
    especie: str
    tutorId: int = Field(serialization_alias="tutorId", validation_alias="tutor_id")
