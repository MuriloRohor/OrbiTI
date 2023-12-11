from sqlalchemy import delete, select
from sqlalchemy.orm import Session
from src.sql.models.models import Endereco, Fornecedor
from src.schemas.FornecedorSchema import FornecedorSchema, FornecedorSchemaDelete, FornecedorSchemaId


class FornecedorRepo():
    def __init__(self, session: Session) -> None:
        self.session = session


    def Criar(
        self, 
        cep: int, 
        cidade: str, 
        logradouro: str, 
        bairro : str,
        numero : int,
        nome : str,
        email: str,
        cnpj: int,
        telefone: int,
        diretorio_img: str
        ):
        db_endereco = Endereco(
            cep=cep, 
            cidade=cidade, 
            logradouro=logradouro, 
            bairro=bairro, 
            numero=numero, 
        )
        self.session.add(db_endereco)
        self.session.commit()

        fornecedor_endereco_id = db_endereco.id

        db_fornecedor = Fornecedor(
            nome=nome, 
            email=email,
            cnpj=cnpj, 
            telefone=telefone,
            diretorio_img=diretorio_img,
            endereco_id=fornecedor_endereco_id
        )
        self.session.add(db_fornecedor)
        self.session.commit()
        
        return db_fornecedor
    
    def Listar(self, pagina_atual: int, itens_por_pagina=10):
        offset = (pagina_atual -1) * itens_por_pagina

        db_fornecedores = self.session.query(Fornecedor)\
                                      .limit(itens_por_pagina)\
                                      .offset(offset)\
                                      .all()
        return db_fornecedores
    
    def FiltrandoPorNome(self, filtro_nome: str, pagina_atual: int, itens_por_pagina=10):
        # Calcula o Deslocamentoo
        offset = (pagina_atual - 1) * itens_por_pagina

        db_fornecedores = self.session.query(Fornecedor)\
                                      .filter(Fornecedor.nome.contains(filtro_nome))\
                                      .limit(itens_por_pagina)\
                                      .offset(offset)\
                                      .all()

        return db_fornecedores
    
    def ObterPorID(self, fornecedor: FornecedorSchemaId):
        db_fornecedor = self.session.query(Fornecedor)\
                                    .filter(Fornecedor.id == fornecedor.id)\
                                    .first()
        return db_fornecedor
    
    def DeletarPorID(self, fornecedor: FornecedorSchemaDelete):
        try:
            db_fornecedor = delete(Fornecedor).where(Fornecedor.id == fornecedor.id)
            db_endereco = delete(Endereco).where(Endereco.id == fornecedor.endereco_id)

            self.session.execute(db_fornecedor)
            self.session.execute(db_endereco)

            self.session.commit()
            return "Forncedor Deletado"
        except Exception as e:
            print("Erro ao deletar", e)
        


