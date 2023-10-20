const ctx = document.getElementById('graph1');

new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['São Paulo', 'Rio de Janeiro', 'Espirito Santo', 'Minas Gerais', 'Bahia', 'Goías'],
    datasets: [{
      label: 'Valor total dos Itens de Estoque R$',
      backgroundColor: [
        'rgba(90, 128, 185,1)',
        'rgba(38, 115, 170,1)',
        'rgba(52, 73, 94, 1)',
        'rgba(44, 62, 80, 1)',
        'rgba(149, 165, 166, 1)',
        'rgba(127, 140, 141, 1)'
      ],
      borderColor: [
        'rgba(90, 128, 185,1)',
        'rgba(38, 115, 170,1)',
        'rgba(52, 73, 94, 1)',
        'rgba(44, 62, 80, 1)',
        'rgba(149, 165, 166, 1)',
        'rgba(127, 140, 141, 1)'
      ],
      data: [12000, 19000, 9000, 11000, 8000, 30000],
    }]
  },
  options: {
    scales: {
      y: {
        beginAtZero: true
      }
    }
  }
});
