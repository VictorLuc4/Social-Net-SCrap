// ----------------------------------------------
// Preferred Time for posts
// ----------------------------------------------
//categoryColors = getColorsForTab(explicitCountData.values, 0.35)

var prefposttime = document.getElementById("prefposttime").getContext("2d");
    Chart.defaults.global.responsive = false;

var prefposttimeChart = new Chart(prefposttime, {
    type: 'bubble',
    data: {
        datasets: [
            {
                label: 'Posts',
                data: videoData.bubble,
                backgroundColor: "rgba(134,196,236, 0.6)"
            },
        ]
    },
    options: {
        title: {
            display: true,
            text: "Posts posted times"
        },
        scales: {
            yAxes: [{
                ticks: {
                    max: 6,
                    min: 0,
                    stepSize: 1,
                    callback: function(value, index, values) {
                        days = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'};
                        return days[index]
                      }
                }
            }],
            xAxes: [{
                ticks: {
                    max: 24,
                    min: 0,
                    stepSize: 1,
                    callback: function(value, index, values) {
                        days = {0:'midnight', 1:'1am', 2:'2am', 3:'3am', 4:'4am', 5:'5am', 6:'6am', 
                        7:'7am', 8:'8am', 9:'9am', 10:'10am', 11:'11am', 12:'Lunch Time', 
                        13:'1pm', 14:'2pm', 15:'3pm', 16:'4pm', 17:'5pm', 18:'6pm', 19:'7pm', 
                        20:'8pm', 21:'9pm', 22:'10pm', 23:'11pm', 24:'midnight too'}

                        return days[index]
                      }
                }
            }]
        },
},
});

