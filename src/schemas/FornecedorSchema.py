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


class FornecedorSchemaUpdate(BaseModel):
    id: Optional[int] = None
    nome: str
    email: str
    cnpj: int
    telefone: int
    endereco_id: int
    endereco: Optional[EnderecoSchema] = None

    class Config:
        orm_mode = True
        from_attributes=True

class FornecedorSchemaId(BaseModel):
    id: int
    class Config:
        orm_mode = True
        
class FornecedorSchemaDelete(BaseModel):
    id: int
    endereco_id:int

    class Config:
        orm_mode = True

class FornecedorSchemaFilterName(BaseModel):
    nome: str
    pagina: int

    class Config:
        orm_mode = True

class FornecedorSchemaBasic(BaseModel):
    id: int
    nome: str
    cnpj: int

    class Config:
        orm_mode = True

    
