async function excluirRegistro(selectId) {

    document.getElementById('detalhesFornecedor').innerHTML = '';
    document.getElementById('detalhesEndereco').innerHTML = '';

    const fornecedores = await getFornecedores();
    console.log(fornecedores);

    let fornecedor = null;

    fornecedores.forEach(responseFornecedor => {
        if (selectId == responseFornecedor.id) {
            fornecedor = responseFornecedor
        }
    });

    if (fornecedor) {
        let detalhesFornecedor = `
            <p>Fornecedor</p>
            <span>Codigo: ${fornecedor.id}</span>
            <span>Nome: ${fornecedor.nome}</span>
            <span>CNPJ: ${fornecedor.cnpj}</span>
            <span>Telefone: ${fornecedor.telefone}</span>
            `;

        let detalhesEndereco = `
            <p>Endereço</p>
            <span>CEP: ${fornecedor.endereco.cep}</span>
            <span>Cidade: ${fornecedor.endereco.cidade}</span>
            <span>Logradouro: ${fornecedor.endereco.logradouro}</span>
            <span>Bairro: ${fornecedor.endereco.bairro}</span>
            <span>Numero: ${fornecedor.endereco.numero}</span>
            `;

        let img_profile = `<img src="/static${fornecedor.diretorio_img}" alt="" width=25% >`;

        // Exibe os detalhes no modal
        document.getElementById('detalhesFornecedor').innerHTML = detalhesFornecedor;
        document.getElementById('detalhesEndereco').innerHTML = detalhesEndereco;
        document.getElementById('img_profile').innerHTML = img_profile;

        // Exibe o modal
        var modal = document.getElementById('modalExcluir');
        modal.style.display = "block";

        // Aplica o efeito de desfoque ao mainContent
        document.getElementById('mainContent').classList.add('blur');

        
    } else {
        console.log("Fornecedor não encontrado.");
    }
}


// Fechar o modal
var span = document.getElementsByClassName("close")[0];
span.onclick = function () {
    var modal = document.getElementById('modalExcluir');
    modal.style.display = "none";
    document.getElementById('mainContent').classList.remove('blur');
}

// Fechar o modal quando clicar fora dele
window.onclick = function (event) {
    var modal = document.getElementById('modalExcluir');
    if (event.target == modal) {
        modal.style.display = "none";
        document.getElementById('mainContent').classList.remove('blur');
    }
}