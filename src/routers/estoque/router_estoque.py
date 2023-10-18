from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="./src/public/templates")

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def estoque_main(request:Request):
    return templates.TemplateResponse("estoque/main.html", {"request": request})