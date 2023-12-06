from pydantic import BaseModel
from typing import Optional

from .FornecedorSchema import FornecedorOut
from .CategoriaSchema import CategoriaOut

class ProdutoOut(BaseModel):
    id: Optional[int] = None
    nome: str
    marca: str
    descricao: str
    categoria_id: int
    fornecedor_id: int
    categoria: Optional[CategoriaOut] = None
    fornecedor: Optional[FornecedorOut] = None

    class Config:
        orm_mode = True
        from_attributes = True
