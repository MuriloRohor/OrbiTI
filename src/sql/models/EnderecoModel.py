from .Base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship
class Endereco(Base):
    __tablename__ = "enderecos"

    id: Mapped[int] = mapped_column(primary_key=True)
    cep: Mapped[int]
    cidade: Mapped[str]
    logradouro: Mapped[str]
    bairro: Mapped[str]
    numero: Mapped[int]

    fornecedor = relationship("Fornecedor", back_populates="endereco", uselist=False)
    local = relationship("Local", back_populates="endereco", uselist=False)
    usuario = relationship("Usuario", back_populates="endereco", uselist=False)