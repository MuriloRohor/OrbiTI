import uuid
from fastapi import APIRouter, Depends, Form, HTTPException, Request, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from typing import List
from src.repository.ProdutoRepo import ProdutoRepo

from src.sql.config.database import get_session

templates = Jinja2Templates(directory="src/public/templates")
router = APIRouter()

IMAGES_DIR_PRODUTO='src/public/static/img/logo_produto/'

@router.get("/", response_class=HTMLResponse)
def produto_main(request: Request):
    titulo_page = "Produto"
    return templates.TemplateResponse("produto/main.html", {"request": request, "titulo": titulo_page})

@router.get('/cadastrar', response_class=HTMLResponse)
def produto_cadastrar(request: Request):
    titulo_page = "Cadastrar Produto"
    return templates.TemplateResponse("produto/cadastrar.html", {"request": request, "titulo": titulo_page})

@router.get('/editar', response_class=HTMLResponse)
def produto_editar(request: Request):
    titulo_page = "Editar Produto"
    return templates.TemplateResponse("produto/editar.html", {"request": request, "titulo": titulo_page})

@router.get('/excluir', response_class=HTMLResponse)
def produto_excluir(request: Request):
    titulo_page = "Excluir Produto"
    return templates.TemplateResponse("produto/excluir.html", {"request": request, "titulo": titulo_page})

@router.get('/listar', response_class=HTMLResponse)
def produto_listar(request: Request):
    titulo_page = "Listar Produto"
    return templates.TemplateResponse("produto/listar.html", {"request": request, "titulo": titulo_page})

@router.post('/cadastrar', response_class=RedirectResponse)
async def produto_cadastrar_post(
    request: Request,
    nome: str = Form(...),
    marca: str = Form(...),
    desc: str = Form(...),
    categoria: int = Form(...),
    fornecedor: int = Form(...),
    img: UploadFile = File(...),
    session: Session = Depends(get_session)
    ):

    img.filename = f"{uuid.uuid4()}.png"
    contents = await img.read()

    # salvando imagem
    with open(f"{IMAGES_DIR_PRODUTO}{img.filename}", "wb") as f:
        f.write(contents)

    db_IMAGES_DIR ="/img/logo_produto/"

    print(db_IMAGES_DIR)
    diretorio_img = db_IMAGES_DIR + img.filename
    
    try:
        ProdutoRepo(session)\
        .Criar(
            nome,
            marca,
            desc,
            diretorio_img,
            categoria,
            fornecedor
        )

        return RedirectResponse(url="/produto/cadastrar", status_code=302)
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=str(e))