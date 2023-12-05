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
    session.commit()

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
    session.add(new_endereco_for_fornecedor)     # Adiciona o objeto criado na sessão.
    session.commit()                             # Faz o commit dos dados para o banco.
    endereco_id = new_endereco_for_fornecedor.id # Recupera o Id do endereço criado.
    endereco = session.scalar(                   # Recupera o endereço se a condição for satisfeita.
        select(Endereco).where(
            Endereco.cidade == "joeba"
        )
    )


    new_fornecedor = Fornecedor(
        nome="pedro",
        cnpj=1234567891000,
        telefone=123456789,
        endereco_id=endereco_id                 # Informando o id do endereco recem criado
    )
    session.add(new_fornecedor)
    session.commit()
    fornecedor = session.scalar(                # Recupera o fornecedor se o id do endereço for igual ao endereço recem criado
        select(Fornecedor).where(
            Fornecedor.endereco_id == endereco_id
        )
    )
    assert fornecedor is not None
    assert fornecedor.endereco_id == endereco_id
    assert endereco.cidade == "joeba"
    