from typing import Annotated
import time
from fastapi import APIRouter, Depends, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from src.sql.models.UsuarioModel import Usuario
from src.util.security import obter_usuario_logado

templates = Jinja2Templates(directory="src/public/templates")

router = APIRouter()


@router.get("/", response_class=RedirectResponse)
def root(request: Request):
    return RedirectResponse(url="/login", status_code=302)

@router.get("/login", response_class=HTMLResponse)
def login_page(
    request: Request,
    usuario: Usuario = Depends(obter_usuario_logado)        
):
    return templates.TemplateResponse("login.html", {"request": request, "usuario": usuario})

@router.post("/login", response_class=RedirectResponse):







"""
@router.post("/", response_class=HTMLResponse)
def get_form(usuario: Annotated[str, Form()], senha: Annotated[str, Form()]):
    print(usuario, senha)
    if (usuario == "murilo" and senha == "123"):
        print(usuario, senha)
        time.sleep(5)
    return RedirectResponse(url="/menu/", status_code=status.HTTP_302_FOUND)

"""
"""
@router_page.get("/", response_class=HTMLResponse)
def menu_page(request: Request):
    return RedirectResponse(url="/login")

"""