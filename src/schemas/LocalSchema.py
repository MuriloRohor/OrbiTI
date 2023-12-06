from pydantic import BaseModel
from typing import Optional

from .EnderecoSchema import EnderecoOut

class LocalOut():
    id: Optional[int] = None
    nome: str
    tipo: str
    endereco_id: int
    endereco: Optional[EnderecoOut] = None

    class Config:
        orm_mode= True
        from_attributes = True