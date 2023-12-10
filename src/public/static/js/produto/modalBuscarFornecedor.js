
var paginaAtual = 1;

function buscarFornecedores(pagina) {
    var nome = document.getElementById('inputNomeFornecedor').value;

    axios.post('http://localhost:8000/fornecedor/listagem/pornome', {
        nome: nome,
        pagina: pagina
    })
        .then(function (response) {
            // Atualiza a tabela
            var tbody = document.querySelector('#detalhesFornecedor tbody');
            tbody.innerHTML = '';
            response.data.forEach(fornecedor => {
                var row = `<tr>
                            <td>${fornecedor.codigo}</td>
                            <td>${fornecedor.nome}</td>
                            <td>${fornecedor.cnpj}</td>
                           </tr>`;
                tbody.innerHTML += row;
            });

            // Atualiza a informação da página
            document.getElementById('infoPagina').textContent = 'Página ' + pagina;
            document.getElementById('btnPaginaAnterior').disabled = pagina === 1;
        })
        .catch(function (error) {
            console.error('Erro ao buscar fornecedores:', error);
        });
}

document.getElementById('formBuscaFornecedor').addEventListener('submit', function (e) {
    e.preventDefault();
    buscarFornecedores(paginaAtual);
});

document.getElementById('btnProximaPagina').addEventListener('click', function () {
    buscarFornecedores(++paginaAtual);
});

document.getElementById('btnPaginaAnterior').addEventListener('click', function () {
    if (paginaAtual > 1) {
        buscarFornecedores(--paginaAtual);
    }
});


document.getElementById('btn-buscarFornecedor').addEventListener('click', function() {
    var modal = document.getElementById('modalBuscar');
    modal.style.display = 'block';
});

// Fechar o modal ao clicar no botão de fechar
var span = document.querySelector('#modalBuscar .close');
span.onclick = function () {
    var modal = document.getElementById('modalBuscar');
    modal.style.display = "none";
}

// Fechar o modal ao clicar fora dele
window.onclick = function (event) {
    var modal = document.getElementById('modalBuscar');
    if (event.target == modal) {
        modal.style.display = "none";
    }
}




// Inicializa a primeira busca
buscarFornecedores(paginaAtual);
