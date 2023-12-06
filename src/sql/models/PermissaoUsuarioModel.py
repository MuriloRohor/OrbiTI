from .Base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship

class PermissaoUsuario(Base):
    __tablename__ = "permisao_usuarios"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    descricao: Mapped[str]

    usuario = relationship("Usuario", back_populates="permissao_usuario", uselist=False)


    

