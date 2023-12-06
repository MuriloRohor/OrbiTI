from .Base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship

class Categoria(Base):
    __tablename__ = "categorias"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]

    produto = relationship("Produto", back_populates="categoria", uselist=False)
