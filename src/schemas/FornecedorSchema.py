from pydantic import BaseModel
from typing import Optional

from .EnderecoSchema import EnderecoOut


class FornecedorOut(BaseModel):
    id: Optional[int] = None
    nome: str
    cnpj: int
    telefone: int
    endereco_id: int
    diretorio_img: str
    endereco: Optional[EnderecoOut] = None

    class Config:
        orm_mode = True
        from_attributes = True

    
