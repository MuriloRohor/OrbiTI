from pydantic import BaseModel
from typing import Optional

from .EnderecoSchema import EnderecoSchema


class FornecedorSchema(BaseModel):
    id: Optional[int] = None
    nome: str
    email: str
    cnpj: int
    telefone: int
    diretorio_img: str
    endereco_id: int
    endereco: Optional[EnderecoSchema] = None

    class Config:
        orm_mode = True
        from_attributes=True


class FornecedorSchemaDelete(BaseModel):
    id: int
    endereco_id:int

    class Config:
        orm_mode = True

    
