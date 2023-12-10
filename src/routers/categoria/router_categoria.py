from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from typing import List
from src.sql.config.database import get_session

from src.repository.CategoriaRepo import CategoriaRepo

from src.schemas.CategoriaSchema import CategoriaSchema, CategoriaSchemaFilterName

router = APIRouter()

@router.post('/listar/pornome', response_model=List[CategoriaSchema])
def get_all_catgorias(request: Request, filtro: CategoriaSchemaFilterName ,session: Session = Depends(get_session)):
    categorias = CategoriaRepo(session).FiltrandoPorNome(filtro.nome, filtro.pagina)
    return categorias