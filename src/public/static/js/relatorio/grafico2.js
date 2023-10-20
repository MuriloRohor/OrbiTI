const ctx2 = document.getElementById('graph2');

new Chart(ctx2, {
  type: 'line',
  data: {
    labels: ['Estoq', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
    datasets: [{
      label: 'Serviços de Sla',
      data: [12, 19, 3, 5, 2, 3],
      borderWidth: 1
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


