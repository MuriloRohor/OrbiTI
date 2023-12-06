from sqlalchemy.orm import Session
from src.sql.models.models import Endereco, Local

class LocalRepo():

    def __init__(self, session: Session) -> None:
        self.session = session

    def Criar(
        self,
        cep: int, 
        cidade: str, 
        logradouro: str, 
        bairro : str,
        numero : int,
        nome: str,
        tipo: str      
    ):
        db_endereco = Endereco(
            cep=cep,
            cidade=cidade,
            logradouro=logradouro,
            bairro=bairro,
            numero=numero
        )
        self.session.add(db_endereco)
        self.session.commit()

        local_endereco_id = db_endereco.id

        db_local = Local(
            nome=nome,
            tipo=tipo,
            endereco_id=local_endereco_id
        )

        self.session.add(db_endereco)
        self.session.commit()

        return db_local
    
    def Listar(self):
        db_locais = self.session.query(Local).all()
        return db_locais

    def FiltrandoPorNome(self, filtro_nome: str):
        db_locais = self.session.query(Local).filter(Local.nome.contains(filtro_nome)).all()
        return db_locais
     
        