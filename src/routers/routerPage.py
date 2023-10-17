from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

router_page = APIRouter()
templates = Jinja2Templates(directory="./src/public/templates")


@router_page.get("/", response_class=HTMLResponse)
def menu_page(request: Request):
    return RedirectResponse(url="/login")

@router_page.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router_page.get("/menu", response_class=HTMLResponse)
def menu_main(request: Request):
    return templates.TemplateResponse("menu/main.html", {"request": request})

@router_page.get("/adicionar-produto", response_class=HTMLResponse)
def menu_adicionar(request: Request):
    return templates.TemplateResponse("menu/adicionar-produto.html", {"request": request})

@router_page.get("/transferencia-estoque", response_class=HTMLResponse)
def menu_transferencia(request: Request):
    return templates.TemplateResponse("menu/transferencia-estoque.html", {"request": request})

@router_page.get("/usuario", response_class=HTMLResponse)
def menu_usuario(request: Request):
    return templates.TemplateResponse('menu/usuario.html', {"request": request})

@router_page.get("/produto", response_class=HTMLResponse)
def produto_main(request: Request):
    return templates.TemplateResponse("produto/main.html", {"request": request})

@router_page.get("/estoque", response_class=HTMLResponse)
def estoque_main(request:Request):
    return templates.TemplateResponse("estoque/main.html", {"request": request})