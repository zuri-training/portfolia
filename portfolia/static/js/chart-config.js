const ctx = document.getElementById('myChart').getContext('2d');

const myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
        datasets: [{
            label: 'Website Visitors',
            data: [1, 6, 12, 18, 24,30,36,32,38,6,2,36],
            backgroundColor: [
                '#34C759',
            ],
            borderColor: [
                '#34C759',
            ],
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