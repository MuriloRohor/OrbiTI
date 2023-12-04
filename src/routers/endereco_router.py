from fastapi import Depends, APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.sql.models.EnderecoModel import Endereco
from src.sql.config.database import get_session
from src.schemas.EnderecoSchema import EnderecoSchema, EnderecoTest

templates = Jinja2Templates(directory="src/public/templates")
router = APIRouter()

@router.post('/', response_model=EnderecoSchema, status_code=201)
def create_endereco(endereco: EnderecoSchema, session: Session = Depends(get_session)):
    endereco = Endereco(
        cep=endereco.cep,
        cidade=endereco.cidade,
        logradouro=endereco.logradouro,
        bairro=endereco.bairro,
        numero=endereco.numero
    )
    session.add(endereco)
    session.commit()
    session.refresh(endereco)

    return endereco


def get_endereco(session: Session, endereco_id: int):
    return session.query(Endereco).filter(Endereco.id == endereco_id).first()

# Rota para mostrar o endereço
@router.get("/showendereco/{endereco_id}", response_class=HTMLResponse)
def show_endereco(request: Request, endereco_id: int, session: Session = Depends(get_session)):
    endereco = get_endereco(session, endereco_id)
    return templates.TemplateResponse("endereco.html", {"request": request, "endereco": endereco})

@router.get('/endereco/{id}', response_model=EnderecoTest)
def reader_endereco(id: int, session: Session = Depends(get_session)):
    endereco = session.query(Endereco).filter(Endereco.id == id).first()
    print(endereco)
    return endereco
