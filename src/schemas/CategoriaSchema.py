from pydantic import BaseModel
from typing import Optional

class CategoriaSchema(BaseModel):
    id: Optional[int] = None
    nome: str

    class Config:
        orm_mode = True
        

