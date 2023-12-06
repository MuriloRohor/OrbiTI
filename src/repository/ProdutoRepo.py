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
        categoria_id: int,
        fornecedor_id: int
        ):
        db_produto = Produto(
            nome=nome,
            marca=marca,
            descricao=descricao,
            categoria_id=categoria_id,
            fornecedor_id=fornecedor_id
        )
        self.session.add(db_produto)
        self.session.commit()
        return db_produto
    
    def Listar(self):
        db_produtos = self.session.query(Produto).all()
        return db_produtos
    
    def FiltrandoPorNome(self, filtro_nome: str):
        db_produtos = self.session.query(Produto).filter(Produto.nome.contains(filtro_nome)).all()
        return db_produtos
    