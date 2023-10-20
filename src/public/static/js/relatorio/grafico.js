const ctx = document.getElementById('graph1');

new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['Estoque', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
    datasets: [{
      label: 'Serviços de Sla',
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
      data: [12, 19, 3, 5, 2, 3],
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
