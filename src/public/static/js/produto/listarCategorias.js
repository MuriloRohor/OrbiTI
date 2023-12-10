document.addEventListener('DOMContentLoaded', function() {
    axios.get('http://localhost:8000/produto/listar/categoria')
        .then(function(response) {
            
            const categorias = response.data;
            const selectElement = document.getElementById('categoriaSelect');

            categorias.forEach(categoria => {
                const option = document.createElement('option');
                option.value = categoria.id; 
                option.textContent = `${categoria.id}`; 
                selectElement.appendChild(option);
            });
        })
        .catch(function(error) {
            console.error('Erro ao carregar categorias:', error);
        });
});
