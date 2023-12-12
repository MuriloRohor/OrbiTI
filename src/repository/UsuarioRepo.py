from sqlalchemy.orm import Session
from src.sql.models.models import PermissaoUsuario, Endereco, Usuario

class UsuarioRepo():
    
    def __init__(self, session) -> None:
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
        login: str,
        senha: str,
        token: str,
        permissao_id: int
        ):
        
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
            login=login,
            senha=senha,
            endereco_id=usuario_endereco_id,
            permissao_id=permissao_id
        )

        self.session.add(db_usuario)
        self.session.commit()

        return db_usuario
    
    def Listar(self): 
        db_usuarios = self.session.query(Usuario).all()
        return db_usuarios
    
    def FiltrandoPorNome(self, filtro_nome: str):
        db_usuarios = self.session.query(Usuario).filter(Usuario.nome.contains(filtro_nome)).all()
        return db_usuarios
    
    def ObterUsuarioPorToken(self, token):
        db_usuario = self.session.query(Usuario)\
                                 .filter(Usuario.token == token)\
                                 .all()
        return db_usuario

