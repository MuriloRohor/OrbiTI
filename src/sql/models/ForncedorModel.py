from sqlalchemy import ForeignKey
from .Base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship

class Fornecedor(Base):
    
    __tablename__ = 'fornecedors'

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    cnpj: Mapped[int]
    telefone: Mapped[int]
    diretorio_img: Mapped[str]
    endereco_id: Mapped[int] = mapped_column(ForeignKey('enderecos.id'))

    endereco = relationship("Endereco", back_populates="fornecedor", uselist=False)
    produto = relationship("Produto", back_populates="fornecedor", uselist=False)