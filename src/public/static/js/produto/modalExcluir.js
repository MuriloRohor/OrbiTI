async function excluirRegistro(selectId) {

    document.getElementById('detalhesProduto').innerHTML = '';
    try {
        const response = await axios.post('http://localhost:8000/produto/listar/obter-por-id', {
            id: selectId
        });

        const produto = response.data;

        if (produto) {
            let detalhesProduto = `
            <p>Fornecedor</p>
            <span>Codigo: ${produto.id}</span>
            <span>Nome: ${produto.nome}</span>
            <span>Marca: ${produto.marca}</span>
            <span>Categoria: ${produto.categoria.nome}</span>
            <span>Fornecedor: ${produto.fornecedor.nome}</span>
            `;
            let img_profile = `<img src="/static${produto.diretorio_img}" alt="" width=25% >`;

            // Exibe os detalhes no modal
            document.getElementById('detalhesProduto').innerHTML = detalhesProduto;
            document.getElementById('img_profile').innerHTML = img_profile;

            // Exibe o modal
            var modal = document.getElementById('modalExcluir');
            modal.style.display = "block";

        } else {
            console.log("Fornecedor não encontrado.");
        }
    } catch (error) {
        console.error('Erro ao buscar fornecedor: ', error);
    }   

    // Aplica o efeito de desfoque ao mainContent
    document.getElementById('modal-content-produto').classList.add('blur');
}

document.getElementById('confirmarExclusao').addEventListener('click', async function () {
    // Obtenha o ID do fornecedor e o ID do endereço
    const produtoId = produto.id;

    const data = {
        id: fornecedorId,
    };

    const url = 'http://localhost:8000/produto/listar/delete';

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
    document.getElementById('modal-content-produto').classList.remove('blur');
}

// Fechar o modal quando clicar fora dele
window.onclick = function (event) {
    var modal = document.getElementById('modalExcluir');
    if (event.target == modal) {
        modal.style.display = "none";
        document.getElementById('modal-content-produto').classList.remove('blur');
    }
}