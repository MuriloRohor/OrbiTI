from sqlalchemy import select

from src.sql.models.models import Endereco, Fornecedor

# Teste da criação da tabela Endereços
def test_create_endereco(session):
    new_endereco = Endereco(
        cep=29280000,
        cidade="iconha",
        logradouro="teste",
        bairro="teste",
        numero=1
    )
    session.add(new_endereco)

    endereco = session.scalar(
        select(Endereco).where(
            Endereco.cidade == "iconha"
        )
                              )
    assert endereco.cidade == "iconha"

# Teste da criação da tabela fornecedor atribuindo um endereço a tabela
def test_create_fornecedor(session):
    new_endereco_for_fornecedor = Endereco(
        cep=29280000,
        cidade="joeba",
        logradouro="teste",
        bairro="teste",
        numero=1
    )
    session.add(new_endereco_for_fornecedor)
    endereco = session.scalar(
        select(Endereco).where(
            Endereco.cidade == "joeba"
        )
    )

    new_fornecedor = Fornecedor(
        nome="pedro",
        cnpj=1234567891000,
        telefone=123456789,
        endereco_id=1
    )
    session.add(new_fornecedor)
    fornecedor = session.scalar(
        select(Fornecedor).where(
            Fornecedor.endereco_id == 1
        )
    )
    assert fornecedor.id == 1
    assert endereco.cidade == "joeba"
    