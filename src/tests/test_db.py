from sqlalchemy import select

from src.sql.models.models import Endereco, Fornecedor, Local, Categoria, Produto, PermissaoUsuario, Usuario

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
    assert endereco is not None
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
        email="fornecedor@email.com",
        cnpj=1234567891000,
        telefone=123456789,
        diretorio_img="/img/logo_fornecedor/teste.png",
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
    assert fornecedor.diretorio_img == "/img/logo_fornecedor/teste.png"
    assert endereco.cidade == "joeba"


def test_create_local(session):
    new_endereco_for_local = Endereco(
        cep=29280000,
        cidade="jaracatia",
        logradouro="teste",
        bairro="teste",
        numero=1
    )
    session.add(new_endereco_for_local)     
    session.commit()
    endereco_id = new_endereco_for_local.id
    endereco = session.scalar(                   
        select(Endereco).where(
            Endereco.cidade == "jaracatia"
        )
    )

    new_local = Local(
        nome="Estoque A",
        tipo="Estoque",
        endereco_id=endereco_id
    )
    session.add(new_local)     
    session.commit()
    local = session.scalar(
        select(Local).where(
            Local.endereco_id == endereco_id
        )
    )

    assert local is not None
    assert endereco.cidade == "jaracatia"
    assert local.nome == "Estoque A"

def teste_create_Produto(session):
    new_endereco_for_fornecedor = Endereco(
        cep=29280000,
        cidade="piuma",
        logradouro="teste",
        bairro="teste",
        numero=1
    )
    session.add(new_endereco_for_fornecedor)     
    session.commit()
    endereco_id = new_endereco_for_fornecedor.id
    endereco = session.scalar(                   
        select(Endereco).where(
            Endereco.cidade == "piuma"
        )
    )

    new_fornecedor_for_produto = Fornecedor(
        nome="marcos",
        email="fornecedor@email.com",
        cnpj=1234567891000,
        telefone=123456789,
        diretorio_img="/img/logo_fornecedor/teste.png",
        endereco_id=endereco_id                 
    )
    session.add(new_fornecedor_for_produto)
    session.commit()
    fornecedor_id = new_fornecedor_for_produto.id
    fornecedor = session.scalar(                
        select(Fornecedor).where(
            Fornecedor.endereco_id == endereco_id
        )
    )
    

    new_categoria_for_produto = Categoria(
        nome="Monitor"
    )
    session.add(new_categoria_for_produto)
    session.commit()
    categoria_id = new_categoria_for_produto.id
    categoria = session.scalar(
        select(Categoria).where(
            Categoria.nome == "Monitor"
        )
    )
    

    new_produto = Produto(
        nome="Hero",
        marca="AOC",
        descricao="Monitor Gamer 144hz 1ms",
        diretorio_img="/img/logo_fornecedor/teste.png",
        categoria_id=categoria_id,
        fornecedor_id=fornecedor_id
    )
    session.add(new_produto)
    session.commit()
    produto_check_cat = session.scalar(
        select(Produto).where(
            Produto.categoria_id == categoria_id
        )
    )
    produto_check_forn = session.scalar(
        select(Produto).where(
            Produto.fornecedor_id == fornecedor_id
        )
    )
    assert endereco.cidade == "piuma"
    assert fornecedor.endereco_id == endereco_id
    assert categoria.nome == "Monitor"
    assert produto_check_cat is not None
    assert produto_check_forn is not None


def test_create_user(session):
    new_endereco_for_usuario = Endereco(
        cep=29280000,
        cidade="Alto Pongal",
        logradouro="teste",
        bairro="teste",
        numero=1
    )
    session.add(new_endereco_for_usuario)     
    session.commit()
    endereco_id = new_endereco_for_usuario.id
    endereco = session.scalar(                   
        select(Endereco).where(
            Endereco.cidade == "Alto Pongal"
        )
    )

    new_permissao_for_usuario = PermissaoUsuario(
        nome="Administrador",
        descricao="teste",
        
    )
    session.add(new_permissao_for_usuario)     
    session.commit()
    permissao_id = new_permissao_for_usuario.id
    permissao = session.scalar(                   
        select(PermissaoUsuario).where(
            PermissaoUsuario.nome == "Administrador"
        )
    )

    new_user = Usuario(
        nome="joao",
        sobrenome="teste",
        data_nascimento="02/02/2002",
        cpf=1,
        cargo="teste",
        email="user@email.com",
        login="user",
        senha="secret",
        endereco_id=endereco_id,
        permissao_id=permissao_id
    )
    session.add(new_user)     
    session.commit()
    usuario_check_ende = session.scalar(
        select(Usuario).where(
            Usuario.endereco_id == endereco_id
        )
    )
    usuario_check_perm = session.scalar(
        select(Usuario).where(
            Usuario.permissao_id == permissao_id
        )
    )
    
    assert endereco.cidade == "Alto Pongal"
    assert permissao.nome == "Administrador"
    assert usuario_check_ende.endereco_id == endereco_id
    assert usuario_check_perm.permissao_id == permissao_id

    
