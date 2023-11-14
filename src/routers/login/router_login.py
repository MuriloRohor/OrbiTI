from typing import Annotated
import time
from fastapi import APIRouter, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="public/templates")

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/", response_class=HTMLResponse)
def get_form(usuario: Annotated[str, Form()], senha: Annotated[str, Form()]):
    print(usuario, senha)
    if (usuario == "murilo" and senha == "123"):
        print(usuario, senha)
        time.sleep(5)
    return RedirectResponse(url="/menu/", status_code=status.HTTP_302_FOUND)






"""
@router_page.get("/", response_class=HTMLResponse)
def menu_page(request: Request):
    return RedirectResponse(url="/login")

"""