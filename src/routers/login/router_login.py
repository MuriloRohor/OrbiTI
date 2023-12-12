from typing import Annotated
import time
from src.sql.config.database import get_session
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Form, Query, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from src.sql.models.UsuarioModel import Usuario
from src.repository.UsuarioRepo import UsuarioRepo

from src.util.mensagem import adicionar_cookie_mensagem, redirecionar_com_mensagem
from src.util.security import adicionar_cookie_autenticacao, conferir_senha, gerar_token, obter_usuario_logado

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

@router.post("/login", response_class=RedirectResponse)
async def login_post(
    email: str = Form(...),
    senha: str = Form(...),
    return_url: str = Query("/menu"),
    session: Session = Depends(get_session)
    ):

    hash_senha_bd = UsuarioRepo(session).ObterSenhaPorEmail(email)
    if conferir_senha(senha, hash_senha_bd):
        token = gerar_token()
        print("gerou o tokern", token)
        UsuarioRepo(session).AlterarTokenPorEmail(token, email)
        print("alterou o token no banco do usuario")
        response = RedirectResponse(return_url, status.HTTP_302_FOUND)
        print("Redirect para a pagina /menu")
        adicionar_cookie_autenticacao(response, token)
        print("criou coockie de autenticação")
        adicionar_cookie_mensagem(response, "Login realizado com sucesso")
        return RedirectResponse(return_url, status.HTTP_302_FOUND)
    else:
        response = redirecionar_com_mensagem(
            "/login",
            "credenciais inválidas. Tente novamente",
        )
        return response







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