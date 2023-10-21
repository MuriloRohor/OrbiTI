const ctx = document.getElementById('graph1');

new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['São Paulo', 'Rio de Janeiro', 'Espirito Santo', 'Minas Gerais', 'Bahia', 'Goías'],
    datasets: [{
      label: 'Valor total dos Itens de Estoque R$',
      backgroundColor: [
        'rgb(0, 0, 0)',
        'rgb(13, 13, 13)',
        'rgb(26, 26, 26)',
        'rgb(38, 38, 38)',
        'rgb(51, 51, 51)',
        'rgb(64, 64, 64)'
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
      label: 'Movimentação de Itens Estoque Espirito Santo',
      backgroundColor: 'rgb(0,0,0)',
      borderColor: 'rgb(0,0,0)',
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
      backgroundColor: 'rgb(0,0,0)',
      borderColor: 'rgb(0,0,0)',
      data: [120, 190, 30, 50, 200, 45, 80, 79, 17, 500, 400, 550],
      borderWidth: 1
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
        'rgb(0, 0, 0)',
        'rgb(13, 13, 13)',
        'rgb(26, 26, 26)',
        'rgb(38, 38, 38)',
        'rgb(51, 51, 51)',
        'rgb(64, 64, 64)'
      ],
      data: [12000, 19000, 9000, 11000, 8000, 30000],
    }]
  },
  options: {
    scales: {
  
    }
  }
});