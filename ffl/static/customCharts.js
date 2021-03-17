

// ----------------------------------------------
// explicit Count By Category
// ----------------------------------------------
categoryColors = getColorsForTab(explicitCountData.values, 0.35)

var explicitCountByCategory = document.getElementById("explicitCountByCategory").getContext("2d");
    //Chart.defaults.global.responsive = false;

var explicitCountByCategoryChart = new Chart(explicitCountByCategory, {
    type: 'doughnut',
    data: {
        labels : explicitCountData.labels,
        datasets: [{
            label: explicitCountData.legend,
            fill: true,
            lineTension: 0.1,
            backgroundColor: categoryColors,
            borderColor: categoryColors,
            data : explicitCountData.values,
        }]
    },
    options: {
        title: {
            display: true,
            text: explicitCountData.title
        },
},
});

// ----------------------------------------------
// Top 10 users by video number :
// ----------------------------------------------
top10colors = getColorsForTab(top10User.values, 0.16)

var top10UsersByVideoCount = document.getElementById("top10UsersByVideoCount").getContext("2d");
    //Chart.defaults.global.responsive = false;

var top10UsersByVideoCountChart = new Chart(top10UsersByVideoCount, {
    type: 'bar',
    data: {
            labels : top10User.labels,
            datasets: [{
                label: top10User.legend,
                fill: true,
                lineTension: 0.1,
                backgroundColor: top10colors,
                borderColor: top10colors,
                borderCapStyle: 'butt',
                borderDash: [],
                borderDashOffset: 0.0,
                borderJoinStyle: 'miter',
                pointBorderColor: top10colors,
                pointBackgroundColor: "#fff",
                pointBorderWidth: 1,
                pointHoverRadius: 5,
                pointHoverBackgroundColor: top10colors,
                pointHoverBorderColor: "rgba(220,220,220,1)",
                pointHoverBorderWidth: 2,
                pointRadius: 1,
                pointHitRadius: 10,
                data : top10User.values,
                spanGaps: false
            }]
        },
        options: {
            title: {
                display: true,
                text: top10User.title
            },
    },
});
// ----------------------------------------------

// ----------------------------------------------
// Top 10 users by video number :
// ----------------------------------------------
top10colors = getColorsForTab(top10Brand.values, 0.16)

var top10BrandByCount = document.getElementById("top10BrandByCount").getContext("2d");
    //Chart.defaults.global.responsive = false;

var top10BrandByCountChart = new Chart(top10BrandByCount, {
    type: 'bar',
    data: {
            labels : top10Brand.labels,
            datasets: [{
                label: top10Brand.legend,
                fill: true,
                lineTension: 0.1,
                backgroundColor: top10colors,
                borderColor: top10colors,
                borderCapStyle: 'butt',
                borderDash: [],
                borderDashOffset: 0.0,
                borderJoinStyle: 'miter',
                pointBorderColor: top10colors,
                pointBackgroundColor: "#fff",
                pointBorderWidth: 1,
                pointHoverRadius: 5,
                pointHoverBackgroundColor: top10colors,
                pointHoverBorderColor: "rgba(220,220,220,1)",
                pointHoverBorderWidth: 2,
                pointRadius: 1,
                pointHitRadius: 10,
                data : top10Brand.values,
                spanGaps: false
            }]
        },
        options: {
            title: {
                display: true,
                text: top10Brand.title
            },
    },
});
// ----------------------------------------------