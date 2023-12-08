import uuid
from fastapi import File, Form, Depends, APIRouter, HTTPException, Request, UploadFile
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from src.sql.config.database import get_session
from sqlalchemy.orm import Session
from typing import List, Optional

from src.schemas.FornecedorSchema import FornecedorSchema

from src.repository.FornecedorRepo import FornecedorRepo

templates = Jinja2Templates(directory="src/public/templates")
router = APIRouter()

IMAGES_DIR='src/public/static/img/logo_fornecedor/'

@router.get("/")
def exibir_form(request: Request):
    titulo_pagina = "Listagem Fornecedor"
    return templates.TemplateResponse("fornecedor/main.html", {"request": request, "titulo": titulo_pagina})

@router.get("/listar")
def exibir_form(request: Request, filtro_nome: Optional[str]= None, session: Session = Depends(get_session)):
    titulo_pagina = "Listagem Fornecedor"
    fornecedor = FornecedorRepo(session)
    if filtro_nome:
        db_fornecedores = fornecedor.FiltrandoPorNome(filtro_nome)
        fornecedores = [FornecedorSchema.from_orm(fornecedor) for fornecedor in db_fornecedores]
    else:
        db_fornecedores = fornecedor.Listar()
        fornecedores = [FornecedorSchema.from_orm(fornecedor) for fornecedor in db_fornecedores]

    return templates.TemplateResponse("fornecedor/listagem.html", {"request": request, "titulo": titulo_pagina, "fornecedores": fornecedores})


@router.get('/listagem/todas', response_model=List[FornecedorSchema])
def get_fornecedores(request: Request, session: Session = Depends(get_session)):
    fornecedores = FornecedorRepo(session).Listar()
    return fornecedores

@router.delete('/listar/delete/{id}')
def delete_for_id_fornecedor(request: Request,id: int ,session: Session = Depends(get_session)):
    pass




@router.post("/fornecedor", response_model=FornecedorSchema)
async def create_fornecedor(
    request: Request, 
    cep: int = Form(...), 
    cidade: str = Form(...), 
    logradouro: str = Form(...), 
    bairro: str = Form(...), 
    numero: int = Form(...), 
    nome: str = Form(...), 
    cnpj: int = Form(...), 
    telefone: int = Form(...),
    img: UploadFile = File(...),
    session: Session = Depends(get_session)
    ):
    
    img.filename = f"{uuid.uuid4()}.png"
    
    contents = await img.read()

    # salvando imagem

    with open(f"{IMAGES_DIR}{img.filename}", "wb") as f:
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
            cnpj,
            telefone,
            diretorio_img
        )

        return RedirectResponse(url="/fornecedor", status_code=302)
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    

@router.delete('/fornecedor')
def delete_fornecedor():
    pass

    



    

    





    
    
    

#@router.get('/endereco/{id}', response_model=EnderecoTest)
#def reader_endereco(id: int, session: Session = Depends(get_session)):
    #endereco = session.query(Endereco).filter(Endereco.id == id).first()
    #print(endereco)
    #return endereco
