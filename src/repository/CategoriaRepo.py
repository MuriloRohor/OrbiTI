from sqlalchemy.orm import Session

from src.sql.models.CategoriaModel import Categoria


class CategoriaRepo():
    def __init__(self, session: Session) -> None:
        self.session = session

    def ListarTodas(self):
        db_categoria = self.session.query(Categoria).all()
        return db_categoria
    
    def FiltrandoPorNome(self, filtro_nome: str, pagina_atual: int, itens_por_pagina=10):
        offset = (pagina_atual - 1) * itens_por_pagina

        db_categoria = self.session.query(Categoria)\
                                      .filter(Categoria.nome.contains(filtro_nome))\
                                      .limit(itens_por_pagina)\
                                      .offset(offset)\
                                      .all()

        return db_categoria
