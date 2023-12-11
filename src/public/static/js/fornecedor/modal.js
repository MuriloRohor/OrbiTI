async function excluirRegistro(selectId) {

    document.getElementById('detalhesFornecedor').innerHTML = '';
    document.getElementById('detalhesEndereco').innerHTML = '';


    if (fornecedor) {
        let detalhesFornecedor = `
            <p>Fornecedor</p>
            <span>Codigo: ${fornecedor.id}</span>
            <span>Nome: ${fornecedor.nome}</span>
            <span>Email: ${fornecedor.email}</span>
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

    } else {
        console.log("Fornecedor não encontrado.");
    }

    // Aplica o efeito de desfoque ao mainContent
    document.getElementById('modal-content').classList.add('blur');
}

document.getElementById('confirmarExclusao').addEventListener('click', async function () {
    // Obtenha o ID do fornecedor e o ID do endereço
    const fornecedorId = fornecedor.id;
    const enderecoId = fornecedor.endereco.id;

    const data = {
        id: fornecedorId,
        endereco_id: enderecoId
    };

    const url = 'http://localhost:8000/fornecedor/listar/delete';

    try {
        // Envie a solicitação HTTP para excluir o fornecedor usando o Axios
        const response = await axios.delete(url, { data });

        if (response.status === 200) {
            // A exclusão foi bem-sucedida
            alert('Fornecedor excluído com sucesso.');
            // Feche o modal
            var modal = document.getElementById('modalExcluir');
            modal.style.display = "none";
            document.getElementById('modal-content').classList.remove('blur');
            // Recarregue ou atualize a lista de fornecedores, se necessário
        } else {
            // Algo deu errado ao excluir
            alert('Erro ao excluir o fornecedor.');
        }
    } catch (error) {
        alert('Erro ao processar a solicitação:', error);
    }
});

// Fechar o modal
var span = document.getElementsByClassName("close")[0];
span.onclick = function () {
    var modal = document.getElementById('modalExcluir');
    modal.style.display = "none";
    document.getElementById('modal-content').classList.remove('blur');
}

// Fechar o modal quando clicar fora dele
window.onclick = function (event) {
    var modal = document.getElementById('modalExcluir');
    if (event.target == modal) {
        modal.style.display = "none";
        document.getElementById('modal-content').classList.remove('blur');
    }
}