from pydantic import BaseModel
from typing import Optional

class EnderecoOut(BaseModel):
    id: Optional[int] = None
    cep: int
    cidade: str
    logradouro: str
    bairro: str
    numero: int

    class Config:
        orm_mode = True
        from_attributes=True
