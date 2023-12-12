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
    document.getElementById('modal-content-edit').classList.add('blur');
}

async function confirmarEdit() {

    console.log("função chamada")
    const formulario = document.getElementById('formFornecedor');

    formulario.addEventListener('submit', function (e) {
        e.preventDefault();
        const dadosDoFormulario = new FormData(formulario);
        const fornecedor = Object.fromEntries(dadosDoFormulario.entries());

        axios.put('http://localhost:8000/fornecedor/listar/editar', fornecedor)
            .then(function (response) {
                console.log('Fornecedor Alterado:', response);
            })
            .catch(function (error) {
                console.error('Erro ao enviar o formulário:', error);
            });
    });
};

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