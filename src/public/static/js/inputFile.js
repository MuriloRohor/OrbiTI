document.addEventListener('DOMContentLoaded', (event) => {
    const realFileBtn = document.getElementById("real-file");
    const customBtn = document.getElementById("custom-button");
    const customTxt = document.getElementById("custom-text");
    const imagePreview = document.getElementById('image-preview'); // Obtenha a referência para o seu elemento de pré-visualização de imagem

    customBtn.addEventListener("click", function () {
        realFileBtn.click(); // Abre o diálogo de seleção de arquivo
    });

    realFileBtn.addEventListener("change", function () {
        if (realFileBtn.files[0]) {
            customTxt.innerHTML = realFileBtn.value.match(/[\/\\]([\w\d\s\.\-\(\)]+)$/)[1]; // Atualiza o texto para mostrar o nome do arquivo

            const reader = new FileReader();
            reader.addEventListener('load', function () {
                imagePreview.src = reader.result; // Define o src da imagem para a Data URL da imagem carregada
                imagePreview.style.display = 'block'; // Exibe a imagem
            });
            reader.readAsDataURL(realFileBtn.files[0]); // Inicia o processo de leitura do arquivo
        } else {
            customTxt.innerHTML = "Nenhum arquivo escolhido ainda."; // Atualiza o texto se nenhum arquivo for escolhido
            imagePreview.style.display = 'none'; // Esconde a imagem se nenhum arquivo foi selecionado
        }
    });
});
