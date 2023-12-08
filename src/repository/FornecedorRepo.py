from sqlalchemy import delete
from sqlalchemy.orm import Session
from src.sql.models.models import Endereco, Fornecedor
from src.schemas.FornecedorSchema import FornecedorSchema, FornecedorSchemaDelete


class FornecedorRepo():
    def __init__(self, session: Session) -> None:
        self.session = session


    def Criar(
        self, 
        cep: int, 
        cidade: str, 
        logradouro: str, 
        bairro : str,
        numero : int,
        nome : str,
        email: str,
        cnpj: int,
        telefone: int,
        diretorio_img: str
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

        fornecedor_endereco_id = db_endereco.id

        db_fornecedor = Fornecedor(
            nome=nome, 
            email=email,
            cnpj=cnpj, 
            telefone=telefone,
            diretorio_img=diretorio_img,
            endereco_id=fornecedor_endereco_id
        )
        self.session.add(db_fornecedor)
        self.session.commit()
        
        return db_fornecedor
    
    def Listar(self): 
        db_fornecedores = self.session.query(Fornecedor).all()
        return db_fornecedores
    
    def FiltrandoPorNome(self, filtro_nome: str):
        db_fornecedores = self.session.query(Fornecedor).filter(Fornecedor.nome.contains(filtro_nome)).all()
        return db_fornecedores
    
    def DeletarPorID(self, fornecedor: FornecedorSchemaDelete):
        try:
            db_fornecedor = delete(Fornecedor).where(Fornecedor.id == fornecedor.id)
            db_endereco = delete(Endereco).where(Endereco.id == fornecedor.endereco_id)

            self.session.execute(db_fornecedor)
            self.session.execute(db_endereco)

            self.session.commit()
            return "Forncedor Deletado"
        except Exception as e:
            print("Erro ao deletar", e)
        


