from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from typing import List

from src.sql.config.database import get_session

templates = Jinja2Templates(directory="src/public/templates")

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def produto_main(request: Request):
    titulo_page = "Produto"
    return templates.TemplateResponse("produto/main.html", {"request": request, "titulo": titulo_page})

@router.get('/cadastrar', response_class=HTMLResponse)
def produto_cadastrar(request: Request):
    titulo_page = "Cadastrar Produto"
    return templates.TemplateResponse("produto/cadastrar.html", {"request": request, "titulo": titulo_page})

@router.get('/editar', response_class=HTMLResponse)
def produto_editar(request: Request):
    titulo_page = "Editar Produto"
    return templates.TemplateResponse("produto/editar.html", {"request": request, "titulo": titulo_page})

@router.get('/excluir', response_class=HTMLResponse)
def produto_excluir(request: Request):
    titulo_page = "Excluir Produto"
    return templates.TemplateResponse("produto/excluir.html", {"request": request, "titulo": titulo_page})

@router.get('/listar', response_class=HTMLResponse)
def produto_listar(request: Request):
    titulo_page = "Listar Produto"
    return templates.TemplateResponse("produto/listar.html", {"request": request, "titulo": titulo_page})