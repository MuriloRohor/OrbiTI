from typing import List, Optional
from sqlalchemy import update
from sqlalchemy.orm import Session
from src.sql.models.models import Endereco, Usuario

class UsuarioRepo():
    
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
        sobrenome: str,
        data_nascimento: str,
        cpf: int,
        cargo: str,
        email: str,
        login: str,
        senha: str,
        token: str,
        admin: bool
        )  -> Optional[Usuario]:
        
        db_endereco = Endereco(
            cep=cep, 
            cidade=cidade, 
            logradouro=logradouro, 
            bairro=bairro, 
            numero=numero, 
        )
        self.session.add(db_endereco)
        self.session.commit()

        usuario_endereco_id = db_endereco.id

        db_usuario = Usuario(
            nome=nome,
            sobrenome=sobrenome,
            data_nascimento=data_nascimento,
            cpf=cpf,
            cargo=cargo,
            email=email,
            login=login,
            senha=senha,
            token=token,
            endereco_id=usuario_endereco_id,
            admin=admin
        )

        self.session.add(db_usuario)
        self.session.commit()

        return db_usuario
    
    
    def Listar(self) -> Optional[List[Usuario]]: 
        db_usuarios = self.session.query(Usuario).all()
        return db_usuarios
    
    
    def FiltrandoPorNome(self, filtro_nome: str) -> Optional[List[Usuario]]:
        db_usuarios = self.session.query(Usuario).filter(Usuario.nome.contains(filtro_nome)).all()
        return db_usuarios
    
    
    def ObterPorToken(self, token: str) -> Optional[Usuario]:
        db_usuario = self.session.query(Usuario)\
                                 .filter(Usuario.token == token)\
                                 .first()
        return db_usuario
    

    def ObterPorEmail(self, email: str) -> Optional[Usuario]:
        db_usuario = self.session.query(Usuario)\
                                 .filter(Usuario.email == email)\
                                 .first()
        return db_usuario
    
    def ObterSenhaPorEmail(self, email: str) -> Optional[str]:
        db_usuario = self.session.query(Usuario)\
                                 .filter(Usuario.email == email)\
                                 .first()
        return db_usuario.senha
    
    def AlterarTokenPorEmail(self, token: str, email: str):
        db_usuario = update(Usuario)\
                     .where(Usuario.email == email)\
                     .values(
                        token=token
                        )
        self.session.execute(db_usuario)
        self.session.commit()
    
    def VerificarExisteEmail(self, email: str) -> bool or False:
        db_usuario = self.session.query(Usuario)\
                                 .filter(Usuario.email == email)\
                                 .first()
        return db_usuario is not None

