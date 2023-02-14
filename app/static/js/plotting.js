export function histogram(id, x, y) {
    new Chart(
        document.getElementById(id),
        {
            type: 'bar',
            data: {
                labels: x,
                datasets: [{
                    data: y,
                    label: "Distribution over xyz",
                    backgroundColor: "rgba(235, 22, 22, .6)",
                    borderColor: "rgba(235, 22, 22, .6)"
                }]
            },
            options: {
                responsive: true,
                scales: {
                    x: {ticks: {color: "rgba(235, 22, 22, .6)"}},
                    y: {ticks: {beginAtZero: true}}
                }
            }
        }
    );
}

export function doughnut(id) {
    new Chart(
        document.getElementById(id),
        {
            type: "doughnut",
            data: {
                labels: ["Italy", "France", "Spain", "USA", "Argentina"],
                datasets: [{
                    backgroundColor: [
                        "rgba(235, 22, 22, .7)",
                        "rgba(235, 22, 22, .6)",
                        "rgba(235, 22, 22, .5)",
                        "rgba(235, 22, 22, .4)",
                        "rgba(235, 22, 22, .3)"
                    ],
                    data: [55, 49, 44, 24, 15]
                }]
            },
            options: {
                responsive: true
            }
           }
    );
}