const ctx = document.getElementById('graph1');

new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['São Paulo', 'Rio de Janeiro', 'Espirito Santo', 'Minas Gerais', 'Bahia', 'Goías'],
    datasets: [{
      label: 'Valor total dos Itens por Estoque R$',
      backgroundColor: [
        '#7D35B8',
        '#8B16EB',
        '#664185',
        '#463852',
        '#333146',
        '#424045'      
      ],
      data: [12000, 19000, 9000, 11000, 8000, 30000],
    }]
  },
  options: {
    scales: {
  
    }
  }
});

const ctx2 = document.getElementById('graph2');

new Chart(ctx2, {
  type: 'line',
  data: {
    labels: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
    datasets: [{
      label: 'Movimentação de entradas em estoques',
      backgroundColor: '#8B16EB',
      borderColor: '#8B16EB',
      data: [120, 190, 30, 50, 200, 45, 80, 79, 17, 500, 400, 550],
      borderWidth: 1
    }]
  },
  options: {
    scales: {
     
    }
  }
});

const ctx3 = document.getElementById('graph3');

new Chart(ctx3, {
  type: 'polarArea',
  data: {
    labels: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
    datasets: [{
      label: 'Movimentação de Itens Estoque Espirito Santo',
      backgroundColor: [
        'rgba(144,56,255,0.5)',  // Roxo
        'rgba(32,178,170,0.5)',  // Turquesa
        'rgba(255,99,132,0.5)',  // Vermelho
        'rgba(54,162,235,0.5)',  // Azul
        'rgba(255,206,86,0.5)',  // Amarelo
        'rgba(102,205,170,0.5)', // Verde Menta
        'rgba(153,102,255,0.5)', // Lilás
        'rgba(255,159,64,0.5)',  // Laranja
        'rgba(199,199,199,0.5)', // Cinza
        'rgba(83,102,113,0.5)',  // Azul Petróleo
        'rgba(255,99,71,0.5)',   // Coral
        'rgba(128,0,128,0.5)',   // Magenta
    ],
      borderColor: 'white',
      data: [50, 80, 60, 50, 30, 40, 80, 70, 30, 50, 40, 50],
      borderWidth: 3
    }]
  },
  options: {
    scales: {
    
    }
  }
});
const ctx4 = document.getElementById('graph4');

new Chart(ctx4, {
  type: 'pie',
  data: {
    labels: ['São Paulo', 'Rio de Janeiro', 'Espirito Santo', 'Minas Gerais', 'Bahia', 'Goías'],
    datasets: [{
      label: 'Valor total dos Itens de Estoque R$',
      backgroundColor: [
        'rgba(144,56,255,0.5)',  // Roxo
        'rgba(32,178,170,0.5)',  // Turquesa
        'rgba(255,99,132,0.5)',  // Vermelho
        'rgba(54,162,235,0.5)',  // Azul
        'rgba(255,206,86,0.5)',  // Amarelo
        'rgba(102,205,170,0.5)', // Verde Menta
        'rgba(153,102,255,0.5)', // Lilás
        'rgba(255,159,64,0.5)',  // Laranja
        'rgba(199,199,199,0.5)', // Cinza
        'rgba(83,102,113,0.5)',  // Azul Petróleo
        'rgba(255,99,71,0.5)',   // Coral
        'rgba(128,0,128,0.5)',   // Magenta
    ],
      data: [12000, 19000, 9000, 11000, 8000, 30000],
    }]
  },
  options: {
    scales: {
  
    }
  }
});