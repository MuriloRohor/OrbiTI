from sqlalchemy.orm import Session
from src.sql.models.models import Categoria, Fornecedor, Produto

class ProdutoRepo():

    def __init__(self, session) -> None:
        self.session = session

    def Criar(
        self,
        nome: str,
        marca: str,
        descricao: str,
        diretorio_img: str,
        categoria_id: int,
        fornecedor_id: int
        ):
        db_produto = Produto(
            nome=nome,
            marca=marca,
            descricao=descricao,
            diretorio_img=diretorio_img,
            categoria_id=categoria_id,
            fornecedor_id=fornecedor_id
        )
        self.session.add(db_produto)
        self.session.commit()
        return db_produto
    
    def Listar(self):
        db_produtos = self.session.query(Produto).all()
        return db_produtos
    
    def FiltrandoPorNome(self, filtro_nome: str, pagina_atual: int, itens_por_pagina=10):
        offset = (pagina_atual - 1) * itens_por_pagina
        db_produtos = self.session.query(Produto)\
                                      .filter(Produto.nome.contains(filtro_nome))\
                                      .limit(itens_por_pagina)\
                                      .offset(offset)\
                                      .all()
        return db_produtos
    