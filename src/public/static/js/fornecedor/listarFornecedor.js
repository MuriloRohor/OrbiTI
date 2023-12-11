var paginaAtual = 1;

function getFornecedores(pagina) {
    var nome = document.getElementById('inputNomeFornecedor').value;

    axios.post('http://localhost:8000/fornecedor/listar/pornome/', {
        nome: nome,
        pagina: pagina
    })
        .then(function (response) {
            var tbody = document.querySelector('tbody');
            tbody.innerHTML = "";
            response.data.forEach(fornecedor => {
                var row =
                    `<tr>
                        <td class="column1">${fornecedor.id}</td>
                        <td class="column2">${fornecedor.nome}</td>
                        <td class="column3">${fornecedor.cnpj}</td>
                        <td class="column4">${fornecedor.telefone}</td>
                        <td class="column5">${fornecedor.endereco.cep}</td>
                        <td class="column5"><button class="btn-list" onclick="editarRegistro(${fornecedor.id})"><img src="http://localhost:8000/static/img/forms/icon_edit.png" alt=""></button>
                        <button class="btn-list" onclick="excluirRegistro(${fornecedor.id})"><img src="http://localhost:8000/static/img/forms/icon_lixeira.png"" alt=""></button>
                        </td>
                    </tr>`;
                tbody.innerHTML += row;
            });

            document.getElementById('infoPaginaListagemFornecedor').textContent = 'Página ' + pagina;
            document.getElementById('btnPaginaAnteriorListagemFornecedor').disabled = pagina === 1;
        })
        .catch(function (error) {
            console.error('Erro ao buscar fornecedores: ', error);
        });
}

document.getElementById('formBuscarFornecedor').addEventListener('submit', function (e) {
    e.preventDefault();
    getFornecedores(paginaAtual);
});

document.getElementById('btnProximaPaginaListagemFornecedor').addEventListener('click', function () {
    getFornecedores(++paginaAtual);
});

document.getElementById('btnPaginaAnteriorListagemFornecedor').addEventListener('click', function () {
    if (paginaAtual > 1) {
        getFornecedores(--paginaAtual);
    }
});

getFornecedores(paginaAtual);


