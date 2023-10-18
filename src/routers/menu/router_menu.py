from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="./src/public/templates")


@router.get("/", response_class=HTMLResponse)
def menu_main(request: Request):
    return templates.TemplateResponse("menu/main.html", {"request": request})

@router.get("/adicionar-produto", response_class=HTMLResponse)
def menu_adicionar(request: Request):
    return templates.TemplateResponse("/menu/adicionar-produto.html", {"request": request})

@router.get("/transferencia-estoque", response_class=HTMLResponse)
def menu_transferencia(request: Request):
    return templates.TemplateResponse("menu/transferencia-estoque.html", {"request": request})

@router.get("/usuario", response_class=HTMLResponse)
def menu_usuario(request: Request):
    return templates.TemplateResponse('menu/usuario.html', {"request": request})