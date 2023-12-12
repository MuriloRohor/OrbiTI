from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from src.sql.config.database import engine
from src.repository.UsuarioRepo import UsuarioRepo
from src.sql.config.database import get_session


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

def criar_user_admin_padrao(session):

    if UsuarioRepo(session).VerificarExisteEmail("administrador@orbiti.com.br"):
        print("Usuário Padrão já está criado")
    
    else:
        UsuarioRepo(session).Criar(
            cep=0,
            cidade="",
            logradouro="",
            bairro="",
            numero=0,
            nome="TesteAdmin",
            sobrenome="",
            data_nascimento="",
            cpf=0,
            cargo="TI",
            email="administrador@orbiti.com.br",
            login="AdministradorTeste",
            senha="$2b$12$0tvgwOm.9kkI4ghpNtVBoejr6l3qAuslklJWIVw5XrDqXwv1cS4Bu",
            token="",
            admin=True
        )
        print("Usuário Padrão Criado")

def init_user():
    criar_user_admin_padrao(session)
