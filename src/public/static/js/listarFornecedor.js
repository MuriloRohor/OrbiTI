const getFornecedores = async () => {
    try {
        const response = await axios.get('http://localhost:8000/fornecedor/listagem/todas');
        return response.data;
    } catch (error) {
        console.error('Erro ao obter fornecedores:', error);
        return [];
    }
};