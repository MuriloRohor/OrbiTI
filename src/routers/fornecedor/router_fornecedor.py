import uuid
from fastapi import File, Form, Depends, APIRouter, HTTPException, Request, UploadFile
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from src.sql.config.database import get_session
from sqlalchemy.orm import Session
from typing import List, Optional

from src.schemas.FornecedorSchema import FornecedorSchema, FornecedorSchemaDelete, FornecedorSchemaFilterName, FornecedorSchemaId, FornecedorSchemaUpdate

from src.repository.FornecedorRepo import FornecedorRepo

templates = Jinja2Templates(directory="src/public/templates")
router = APIRouter()

IMAGES_DIR_FORNECEDOR='src/public/static/img/logo_fornecedor/'

@router.get("/")
def get_fornecedor(request: Request):
    titulo_pagina = "Fornecedor"
    return templates.TemplateResponse("fornecedor/main.html", {"request": request, "titulo": titulo_pagina})

@router.get("/cadastrar")
def get_cadastro_fornecedores(request: Request):
    titulo_pagina = "Cadastro Fornecedor"
    return templates.TemplateResponse("fornecedor/cadastrar.html", {"request": request, "titulo": titulo_pagina})

@router.get("/listar")
def exibir_form(request: Request):
    titulo_pagina = "Listagem Fornecedor"
    return templates.TemplateResponse("fornecedor/listagem.html", {"request": request, "titulo": titulo_pagina})


@router.post('/listar/obter-por-id', response_model=FornecedorSchema)
def get_all_fornecedores(request: Request, fornecedor_id: FornecedorSchemaId ,session: Session = Depends(get_session)):
    fornecedores = FornecedorRepo(session).ObterPorID(fornecedor_id)
    return fornecedores

@router.post('/listar/pornome', response_model=List[FornecedorSchema])
def get_filterbyname_fornecedores(requst: Request, filtro: FornecedorSchemaFilterName, session: Session = Depends(get_session)):
    fornecedores = FornecedorRepo(session).FiltrandoPorNome(filtro.nome, filtro.pagina)
    return fornecedores

@router.delete('/listar/delete')
def delete_for_id_fornecedor(request: Request, fornecedor: FornecedorSchemaDelete, session: Session = Depends(get_session)):
    FornecedorRepo(session).DeletarPorID(fornecedor)
    return "Fornecedor Deletado"

@router.put('/listar/editar')
def edit_for_id_fornecedor(request: Request, fornecedor: FornecedorSchemaUpdate, session: Session = Depends(get_session)):
    FornecedorRepo(session).UpdatePorID(fornecedor)
    return "Fornecedor Alterado"

@router.post("/criar")
async def create_fornecedor(
    request: Request, 
    cep: int = Form(...), 
    cidade: str = Form(...), 
    logradouro: str = Form(...), 
    bairro: str = Form(...), 
    numero: int = Form(...), 
    nome: str = Form(...),
    email: str = Form(...), 
    cnpj: int = Form(...), 
    telefone: int = Form(...),
    img: UploadFile = File(...),
    session: Session = Depends(get_session)
    ):
    
    img.filename = f"{uuid.uuid4()}.png"
    
    contents = await img.read()

    # salvando imagem

    with open(f"{IMAGES_DIR_FORNECEDOR}{img.filename}", "wb") as f:
        f.write(contents)

    db_IMAGES_DIR ="/img/logo_fornecedor/"

    print(db_IMAGES_DIR)
    diretorio_img = db_IMAGES_DIR + img.filename
    
    try:
        fornecedor = FornecedorRepo(session)
        fornecedor.Criar(
            cep,
            cidade,
            logradouro,
            bairro,
            numero,
            nome,
            email,
            cnpj,
            telefone,
            diretorio_img
        )

        return RedirectResponse(url="/fornecedor/cadastrar", status_code=302)
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=str(e))


    



    

    





    
    
    

#@router.get('/endereco/{id}', response_model=EnderecoTest)
#def reader_endereco(id: int, session: Session = Depends(get_session)):
    #endereco = session.query(Endereco).filter(Endereco.id == id).first()
    #print(endereco)
    #return endereco
