export function histogram(canvas_id, x, y, rating) {
    // Set bordercolor according to rating
    const backgroundcolor = [];
    const bordercolor = [];

    for(let i=0; i<x.length; i++){
        if (x[i] == rating){
            backgroundcolor.push("rgba(235, 22, 22)");
            bordercolor.push("white")}
        else {
            backgroundcolor.push("rgba(235, 22, 22)")};
            bordercolor.push("rgba(235, 22, 22)")
        }

    // styling
    const options = {
        responsive: true,
        scales: {
            x: {ticks: {color: "rgba(235, 22, 22)"}},
            y: {ticks: {beginAtZero: true}}
        },
        plugins: {
            legend: {
                display: false
            }
        }
    }

    // actually generate plot
    new Chart(
        document.getElementById(canvas_id),
        {
            type: 'bar',
            data: {
                labels: x,
                datasets: [{
                    data: y,
                    label: "Peer members",
                    backgroundColor: backgroundcolor,
                    borderColor: bordercolor,
                    borderWidth: 2
                }]
            },
            options: options
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

export function timeseries(canvas_id, t, y, y_peers, y_market) {
    const data = {
        labels: t,
        datasets: [{
            label: 'Time series',
            data: y,
            borderColor: 'white',
            tension: 0.1 // bezier property
        },
            {
            label: 'Peers',
            data: y_peers,
            borderColor: "rgba(235, 22, 22, 1)",
            tension: 0.1 // bezier property
        },
            {
            label: 'Market',
            data: y_market,
            borderColor: "rgba(235, 22, 22, 1)",
                borderDash: [10,10],
            tension: 0.1 // bezier property
        }
        ]
    };
    const options = {
        elements: {
            point:{
                radius: 0
            }
        }
    }

    new Chart(
        document.getElementById(canvas_id),
        {
            type: 'line',
            data: data,
            options: options
        }
    );

}