from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from typing import List
from src.sql.config.database import get_session

from src.repository.CategoriaRepo import CategoriaRepo

from src.schemas.CategoriaSchema import CategoriaSchema

router = APIRouter()

@router.get('/listar/pornome', response_model=List[CategoriaSchema])
def get_all_catgorias(request: Request, session: Session = Depends(get_session)):
    categorias = CategoriaRepo(session).FiltrandoPorNome()
    return categorias