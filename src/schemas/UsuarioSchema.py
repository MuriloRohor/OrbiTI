from pydantic import BaseModel
from typing import Optional

from .EnderecoSchema import EnderecoOut
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
    endereco_id: int
    permissao_id: id
    permissao: Optional[PermissaoUsuarioOut] = None
    endereco: Optional[EnderecoOut] = None

    class Config:
        orm_mode = True
        from_attributes = True

    