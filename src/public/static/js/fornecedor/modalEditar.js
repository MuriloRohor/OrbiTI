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

            document.getElementById('confirmarEdicao').addEventListener('click', function () {

                const nome = document.getElementById('inputNome').value;
                const email = document.getElementById('inputEmail').value;
                const cnpj = document.getElementById('inputCnpj').value
                const telefone = document.getElementById('inputTelefone').value;
                const cep = document.getElementById('inputCep').value;
                const cidade = document.getElementById('inputCidade').value;
                const logradouro = document.getElementById('inputLogradouro').value;
                const bairro = document.getElementById('inputBairro').value;
                const numero = document.getElementById('inputNumero').value;

                // Criar um objeto com os dados
                const dadosDoFormulario = {
                    id: fornecedor.id,
                    nome: nome,
                    email: email,
                    cnpj: cnpj,
                    telefone: telefone,
                    endereco_id: fornecedor.endereco.id,
                    endereco: {
                        cep: cep,
                        cidade: cidade,
                        logradouro: logradouro,
                        bairro: bairro,
                        numero: numero
                    }
                };
                axios.put('http://localhost:8000/fornecedor/listar/editar', dadosDoFormulario)
                    .then(function (response) {
                        console.log('Resposta recebida:', response);

                        // Feche o modal aqui
                        // Feche o modal aqui
                        var modalEdit = document.getElementById('modalEditar');
                        modalEdit.style.display = "none";
                        document.getElementById('modal-content-edit').classList.remove('blur');
                    })
                    .catch(function (error) {
                        console.error('Erro ao enviar o formulário:', error);
                    });

            });

        } else {
            console.log("Fornecedor não encontrado.");
        }
    } catch (error) {
        console.error('Erro ao buscar fornecedor: ', error);
    }

    // Aplica o efeito de desfoque ao mainContent
    document.getElementById('modal-content-edit').classList.add('blur');

}


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