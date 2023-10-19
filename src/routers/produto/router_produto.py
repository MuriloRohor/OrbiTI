from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="./src/public/templates")

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def produto_main(request: Request):
    return templates.TemplateResponse("produto/main.html", {"request": request})

@router.get('/cadastrar', response_class=HTMLResponse)
def produto_cadastrar(request: Request):
    return templates.TemplateResponse("produto/cadastrar.html", {"request": request})

@router.get('/editar', response_class=HTMLResponse)
def produto_editar(request: Request):
    return templates.TemplateResponse("produto/editar.html", {"request": request})

@router.get('/excluir', response_class=HTMLResponse)
def produto_excluir(request: Request):
    return templates.TemplateResponse("produto/excluir.html", {"request": request})

@router.get('/listar', response_class=HTMLResponse)
def produto_listar(request: Request):
    return templates.TemplateResponse("produto/listar.html", {"request": request})