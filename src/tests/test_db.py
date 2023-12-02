from sqlalchemy import select

from src.sql.models.EnderecoModel import Endereco

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