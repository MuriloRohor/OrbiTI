from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="src/public/templates")

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def estoque_main(request:Request):
    titulo_page = "Estoque"
    return templates.TemplateResponse("estoque/main.html", {"request": request, "titulo": titulo_page})

@router.get("/cadastrar", response_class=HTMLResponse)
def estoque_main(request:Request):
    titulo_page = "Cadastro de Estoque"
    return templates.TemplateResponse("estoque/cadastrar.html", {"request": request, "titulo": titulo_page})

@router.get("/editar", response_class=HTMLResponse)
def estoque_main(request:Request):
    titulo_page = "Editar Estoque"
    return templates.TemplateResponse("estoque/editar.html", {"request": request, "titulo": titulo_page})

@router.get("/excluir", response_class=HTMLResponse)
def estoque_main(request:Request):
    titulo_page = "Exclusão de Estoque"
    return templates.TemplateResponse("estoque/excluir.html", {"request": request, "titulo": titulo_page})

@router.get("/listar", response_class=HTMLResponse)
def estoque_main(request:Request):
    titulo_page = "Listagem de Estoques"
    return templates.TemplateResponse("estoque/listar.html", {"request": request, "titulo": titulo_page})

