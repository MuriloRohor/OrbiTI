
// Quando o usuário clica no botão "Excluir"
function excluirRegistro(id, nome, cnpj, telefone, diretorio_img, cep, cidade, logradouro, bairro, numero) {
    let detalhesFornecedor = `
            <p>Fornecedor</p>
            
            <span>Codigo - ${id}</span>
            <span>Nome - ${nome}</span>
            <span>CNPJ - ${cnpj}</span>
            <span>Telefone - ${telefone}</span>
            `;

    let detalhesEndereco = `
            <p>Endereço</p>
            <span>CEP - ${cep}</span>
            <span>Cidade - ${cidade}</span>
            <span>Logradouro - ${logradouro}</span>
            <span>Bairro - ${bairro}</span>
            <span>Numero - ${numero}</span>
            `;

    let img_profile = `<img src="/static${diretorio_img}" alt="" width=25% >`;


    // Exibe os detalhes no modal
    document.getElementById('detalhesFornecedor').innerHTML = detalhesFornecedor;
    document.getElementById('detalhesEndereco').innerHTML = detalhesEndereco;
    document.getElementById('img_profile').innerHTML = img_profile;


    // Exibe o modal
    var modal = document.getElementById('modalExcluir');
    modal.style.display = "block";

    // Aplica o efeito de desfoque ao mainContent
    document.getElementById('mainContent').classList.add('blur');
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

