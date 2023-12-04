from sqlalchemy import ForeignKey
from .Base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship
from .EnderecoModel import Endereco  

class Fornecedor(Base):
    __tablename__ = 'fornecedores'

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    cnpj: Mapped[int]
    telefone: Mapped[int]
    endereco_id: Mapped[int] = mapped_column(ForeignKey('enderecos.id'))
    endereco = relationship("Endereco", back_populates="fornecedor", uselist=False)