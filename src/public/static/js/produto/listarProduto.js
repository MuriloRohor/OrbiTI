var paginaAtual = 1;

function getProdutos(pagina) {
    var nome = document.getElementById('inputNomeProduto').value;

    axios.post('http://localhost:8000/produto/listar/pornome/', {
        nome: nome,
        pagina: pagina
    })
        .then(function (response) {
            var tbody = document.querySelector('tbody');
            tbody.innerHTML = "";
            response.data.forEach(produto => {
                var row =
                    `<tr>
                        <td class="column1">${produto.id}</td>
                        <td class="column2">${produto.nome}</td>
                        <td class="column3">${produto.marca}</td>
                        <td class="column4">${produto.categoria.nome}</td>
                        <td class="column5">${produto.categoria.fornecedor}</td>
                        <td class="column5"><button class="btn-list" onclick="editarRegistro(${produto.id})"><img src="http://localhost:8000/static/img/forms/icon_edit.png" alt=""></button>
                        <button class="btn-list" onclick="excluirRegistro(${produto.id})"><img src="http://localhost:8000/static/img/forms/icon_lixeira.png"" alt=""></button>
                        </td>
                    </tr>`;
                tbody.innerHTML += row;
            });

            document.getElementById('infoPaginaListagemProduto').textContent = 'Página ' + pagina;
            document.getElementById('btnPaginaAnteriorListagemProduto').disabled = pagina === 1;
        })
        .catch(function (error) {
            console.error('Erro ao buscar Produtos: ', error);
        });
}

document.getElementById('formBuscarProduto').addEventListener('submit', function (e) {
    e.preventDefault();
    getProdutos(paginaAtual);
});

document.getElementById('btnProximaPaginaListagemProduto').addEventListener('click', function () {
    getProdutos(++paginaAtual);
});

document.getElementById('btnPaginaAnteriorListagemProduto').addEventListener('click', function () {
    if (paginaAtual > 1) {
        getProdutos(--paginaAtual);
    }
});

getProdutos(paginaAtual);


