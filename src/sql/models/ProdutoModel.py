from sqlalchemy import ForeignKey
from .Base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship

class Produto(Base):
    __tablename__ = "produtos"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    marca: Mapped[str]
    descricao: Mapped[str]
    categoria_id: Mapped[int] = mapped_column(ForeignKey('categorias.id'))
    fornecedor_id: Mapped[int] = mapped_column(ForeignKey("fornecedors.id"))

    categoria = relationship("Categoria", back_populates="produto", uselist=False)
    fornecedor = relationship("Fornecedor", back_populates="produto", uselist=False)