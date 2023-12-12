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
    email: Mapped[str]
    login: Mapped[str]
    senha: Mapped[str]
    token: Mapped[str]
    endereco_id: Mapped[int] = mapped_column(ForeignKey('enderecos.id'))
    permissao_id: Mapped[int] = mapped_column(ForeignKey('permisao_usuarios.id'))

    endereco = relationship("Endereco", back_populates="usuario", uselist=False)
    permissao_usuario = relationship("PermissaoUsuario", back_populates="usuario", uselist=False)

