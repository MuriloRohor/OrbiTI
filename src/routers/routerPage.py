from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

router_page = APIRouter()
templates = Jinja2Templates(directory="public/templates")


@router_page.get("/", response_class=HTMLResponse)
def menu_page(request: Request):
    return RedirectResponse(url="/login")

@router_page.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router_page.get('/menu', response_class=HTMLResponse)
def menu_page(request: Request):
    return templates.TemplateResponse("menu-main.html", {"request": request})