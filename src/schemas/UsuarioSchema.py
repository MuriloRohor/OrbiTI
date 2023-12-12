from pydantic import BaseModel
from typing import Optional

from .EnderecoSchema import EnderecoSchema
from .PermissaoUsuarioSchema import PermissaoUsuarioOut

class UsuarioOut(BaseModel):
    id: Optional[int] = None
    nome: str
    sobrenome: str
    data_nascimento: str
    cpf: int
    cargo: str
    login: str
    senha: str
    admin: bool
    endereco_id: int
    permissao: Optional[PermissaoUsuarioOut] = None
    endereco: Optional[EnderecoSchema] = None

    class Config:
        orm_mode = True
        from_attributes = True

    