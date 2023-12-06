from pydantic import BaseModel
from typing import Optional

class CategoriaOut(BaseModel):
    id: Optional[int] = None
    nome: str

    class Config:
        orm_mode = True
        from_attributes = True
        

