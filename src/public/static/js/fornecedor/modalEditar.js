async function editarRegistro(selectId) {

    document.getElementById('detalhesFornecedor').innerHTML = '';
    document.getElementById('detalhesEndereco').innerHTML = '';
    try {
        const response = await axios.post('http://localhost:8000/fornecedor/listar/obter-por-id', {
            id: selectId
        });

        const fornecedor = response.data;

        if (fornecedor) {
            document.getElementById('inputNome').value = fornecedor.nome;
            document.getElementById('inputEmail').value = fornecedor.email;
            document.getElementById('inputCnpj').value = fornecedor.cnpj;
            document.getElementById('inputTelefone').value = fornecedor.telefone;
            document.getElementById('inputCep').value = fornecedor.endereco.cep;
            document.getElementById('inputCidade').value = fornecedor.endereco.cidade;
            document.getElementById('inputLogradouro').value = fornecedor.endereco.logradouro;
            document.getElementById('inputBairro').value = fornecedor.endereco.bairro;
            document.getElementById('inputNumero').value = fornecedor.endereco.numero;


            let img_profile_edit = `<img src="/static${fornecedor.diretorio_img}" alt="" width=25% >`;
            document.getElementById('img_profile_edit').innerHTML = img_profile_edit;

            // Exibe o modal
            var modal = document.getElementById('modalEditar');
            modal.style.display = "block";

        } else {
            console.log("Fornecedor não encontrado.");
        }
    } catch (error) {
        console.error('Erro ao buscar fornecedor: ', error);
    }   

    // Aplica o efeito de desfoque ao mainContent
    document.getElementById('modal-content').classList.add('blur');
}

document.getElementById('confirmarEdicao').addEventListener('click', async function () {
    // Obtenha o ID do fornecedor e o ID do endereço
    const fornecedorId = fornecedor.id;
    const enderecoId = fornecedor.endereco.id;

    const data = {
        id: fornecedorId,

        endereco_id: enderecoId
    };

    const url = 'http://localhost:8000/fornecedor/listar/editar';

    try {
        // Envie a solicitação HTTP para editar o fornecedor usando o Axios
        const response = await axios.delete(url, { data });

        if (response.status === 200) {
            // A exclusão foi bem-sucedida
            alert('Fornecedor excluído com sucesso.');
            // Feche o modal
            var modalEdit = document.getElementById('modalEditar');
            modalEdit.style.display = "none";
            document.getElementById('modal-content-edit').classList.remove('blur');
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
var spanEdit = document.getElementsByClassName("closeEdit")[0];
spanEdit.onclick = function () {
    var modalEdit = document.getElementById('modalEditar');
    modalEdit.style.display = "none";
    document.getElementById('modal-content-edit').classList.remove('blur');
}

// Fechar o modal quando clicar fora dele
window.onclick = function (event) {
    var modalEdit = document.getElementById('modalEditar');
    if (event.target == modalEdit) {
        modalEdit.style.display = "none";
        document.getElementById('modal-content-edit').classList.remove('blur');
    }
}