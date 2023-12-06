from sqlalchemy import ForeignKey
from .Base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship

class Local(Base):
    __tablename__ = "locals"
    id_local: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    tipo: Mapped[str]
    endereco_id: Mapped[int] = mapped_column(ForeignKey('enderecos.id'))
    
    endereco = relationship("Endereco", back_populates="local", uselist=False)
