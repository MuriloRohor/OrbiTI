from .Base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship

class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    sobrenome: Mapped[str]
    data_nascimento: Mapped[str]
    cpf: Mapped[int]
    cargo: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    login: Mapped[str]
    senha: Mapped[str]
    token: Mapped[str]
    admin: Mapped[bool]
    endereco_id: Mapped[int] = mapped_column(ForeignKey('enderecos.id'))
    endereco = relationship("Endereco", back_populates="usuario", uselist=False)

