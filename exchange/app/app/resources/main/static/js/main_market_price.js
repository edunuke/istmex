$(document).ready(function(){
    $.ajax({ 
        url: '/gdax/btcusd',
        type: 'price',
        success: function(data) {
            $('#lastprice').html('<span>'+data["data"]["result"]["price"] +" USD"+'</span>')
            var datapoint = [data["data"]["result"]["price"]]

            cardChart1 = new Chart($('#card-chart1'), {
                type: 'line',
                data: {
                  labels: datapoint,
                  datasets: [{
                    label: 'price:',
                    backgroundColor: getStyle('--info'),
                    borderColor: 'rgba(255,255,255,.55)',
                    data: datapoint
                  }]
                },
                options: {
                  maintainAspectRatio: false,
                  legend: {
                    display: false
                  },
                  scales: {
                    xAxes: [{
                      gridLines: {
                        color: 'transparent',
                        zeroLineColor: 'transparent'
                      },
                      ticks: {
                        fontSize: 2,
                        fontColor: 'transparent'
                      }
                    }],
                    yAxes: [{
                      display: false,
                      ticks: {
                        display: false,
                      }
                    }]
                  },
                  elements: {
                    line: {
                      tension: 0.00001,
                      borderWidth: 1
                    },
                    point: {
                      radius: 4,
                      hitRadius: 10,
                      hoverRadius: 4
                    }
                  }
                }
              }); // eslint-disable-next-line no-unused-vars
        }
    });
    setInterval(() => {
        $.ajax({ 
            url: '/gdax/btcusd',
            type: 'price',
            success: function(data) {
                datapoint = data["data"]["result"]["price"]
                $('#lastprice').html('<span>'+datapoint+" USD"+'</span>')

                var chart = $('#card-chart1')//.highcharts()
                
                

                    dataset : [{
                        label: datapoint,
                        backgroundColor: getStyle('--info'),
                        borderColor: 'rgba(255,255,255,.55)',
                        data: datapoint,
                    }]

                      //cardChart1.config.data.labels.push("month");
                      cardChart1.options.scales.yAxes[0].ticks.suggestedMax = parseFloat(datapoint)+.01
                      cardChart1.options.scales.yAxes[0].ticks.suggestedMin = parseFloat(datapoint)-.01
                      cardChart1.config.data.datasets.forEach(function(dataset) {
                      dataset.data.push(data["data"]["result"]["price"]);
                      });

                      if (cardChart1.config.data.datasets[0].data.length == 10) {
                        cardChart1.config.data.labels.shift();
                        cardChart1.config.data.datasets.forEach((dataset) => {
                        dataset.data.shift();
                        });    
                      }


                      cardChart1.update();

                    console.log(cardChart1.config.data.datasets)


            }
        });
        
    }, 1000*5);
});
