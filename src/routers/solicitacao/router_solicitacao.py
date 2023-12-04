from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="src/public/templates")

router = APIRouter()

@router.get('/', response_class=HTMLResponse)
def solicitacao_main(request: Request):
    titulo_page = "Solicitações"
    return templates.TemplateResponse('solicitacao/main.html', {"request": request, "titulo": titulo_page})

@router.get('/criar', response_class=HTMLResponse)
def solicitacao_main(request: Request):
    titulo_page = "Criar Solicitação"
    return templates.TemplateResponse('solicitacao/criar.html', {"request": request, "titulo": titulo_page})

@router.get('/visualizar', response_class=HTMLResponse)
def solicitacao_main(request: Request):
    titulo_page = "Solicitações"
    return templates.TemplateResponse('solicitacao/visualizar.html', {"request": request, "titulo": titulo_page})