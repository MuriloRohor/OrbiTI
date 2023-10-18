from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="./src/public/templates")

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})





"""
@router_page.get("/", response_class=HTMLResponse)
def menu_page(request: Request):
    return RedirectResponse(url="/login")

"""