from pydantic import BaseModel
from typing import Optional

class PermissaoUsuarioOut(BaseModel):
    id: Optional[int] = None
    nome: str
    descricao: str

    class Config:
        orm_mode = True
        from_attributes = True