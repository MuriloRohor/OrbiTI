
var paginaAtual = 1;

function buscarCategoria(pagina) {
    var nome = document.getElementById('inputNomeCategoria').value;

    axios.post('http://localhost:8000/categoria/listar/pornome', {
        nome: nome,
        pagina: pagina
    })
        .then(function (response) {
            // Atualiza a tabela
            var tbody = document.querySelector('#detalhesCategoria tbody');
            tbody.innerHTML = '';
            response.data.forEach(categoria => {
                var row = `<tr onclick="selecionarCategoria(${categoria.id})">
                             <td>${categoria.id}</td>
                             <td>${categoria.nome}</td>
                           </tr>`;
                tbody.innerHTML += row;
            });

            // Atualiza a informação da página
            document.getElementById('infoPagina').textContent = 'Página ' + pagina;
            document.getElementById('btnPaginaAnterior').disabled = pagina === 1;
        })
        .catch(function (error) {
            console.error('Erro ao buscar categorias:', error);
        });
}

document.getElementById('formBuscarCategoria').addEventListener('submit', function (e) {
    e.preventDefault();
    buscarCategoria(paginaAtual);
});

document.getElementById('btnProximaPaginaCategoria').addEventListener('click', function () {
    buscarCategoria(++paginaAtual);
});

document.getElementById('btnPaginaAnteriorCategoria').addEventListener('click', function () {
    if (paginaAtual > 1) {
        buscarCategoria(--paginaAtual);
    }
});


document.getElementById('btn-buscarCategoria').addEventListener('click', function () {
    var modal = document.getElementById('modalBuscarCategoria');
    modal.style.display = 'block';
});


function selecionarCategoria(categoriaId) {
    // Atualiza o valor do input no formulário
    document.getElementById('inputCategoria').value = categoriaId;

    // Fecha o modal (se necessário)
    var modal = document.getElementById('modalBuscarCategoria');
    modal.style.display = 'none';
}

// Fechar o modal ao clicar no botão de fechar
var span = document.querySelector('#modalBuscarCategoria .close');
span.onclick = function () {
    var modal = document.getElementById('modalBuscarCategoria');
    modal.style.display = "none";
}

// Fechar o modal ao clicar fora dele
window.onclick = function (event) {
    var modal = document.getElementById('modalBuscarCategoria');
    if (event.target == modal) {
        modal.style.display = "none";
    }
}