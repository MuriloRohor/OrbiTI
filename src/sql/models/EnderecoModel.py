from .Base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column



class Endereco(Base):
    __tablename__ = "enderecos"

    id: Mapped[int] = mapped_column(primary_key=True)
    cep: Mapped[int]
    cidade: Mapped[int]
    logradouro: Mapped[str]
    bairro: Mapped[str]
    numero: Mapped[int] 