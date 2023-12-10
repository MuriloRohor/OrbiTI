from sqlalchemy.orm import Session

from src.sql.models.CategoriaModel import Categoria


class CategoriaRepo():
    def __init__(self, session: Session) -> None:
        self.session = session

    def ListarTodas(self):
        db_categoria = self.session.query(Categoria).all()
        return db_categoria
