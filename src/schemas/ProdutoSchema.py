from pydantic import BaseModel
from typing import Optional

from .FornecedorSchema import FornecedorSchema
from .CategoriaSchema import CategoriaSchema

class ProdutoSchema(BaseModel):
    id: Optional[int] = None
    nome: str
    marca: str
    descricao: str
    diretorio_img: str
    categoria_id: int
    fornecedor_id: int
    categoria: Optional[CategoriaSchema] = None
    fornecedor: Optional[FornecedorSchema] = None

    class Config:
        orm_mode = True
        from_attributes = True



class ProdutoSchemaFilterName(BaseModel):
    nome: str
    pagina: str

    class Config:
        orm_mode = True
        from_attributes = True
