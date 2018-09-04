$(document).ready(function(){

    $.ajax({ 
        url: '/gdax/btcusd',
        type: 'summary',
        success: function(resp) {
          
                resp = JSON.parse(resp)["data"]

                lastPrice = []
                highPrice = []
                lowPrice =  []
                changepct = []
                changeabs = []
                volume = []
                timesteps = []

                for (var i in resp) {
                  data = resp[i]["data"]["result"]
                  time = resp[i]["time"]
                  
                  lowPrice.push(data["price"]["low"])
                  lastPrice.push(data["price"]["last"])
                  highPrice.push(data["price"]["high"])
                  changepct.push(data["price"]["change"]["percentage"])
                  changeabs.push(data["price"]["change"]["absolute"])
                  volume.push(data["volume"])
                  timesteps.push(new Date(resp[i]["time"]*1000))


                }
            $('#lastprice').html('<span> 1 BTC = '+lastPrice[0] +" USD"+'</span>')
            $('#lastdate').html('<span>'+"Last Price: "+
                                timesteps[0].getHours()+":"+
                                timesteps[0].getMinutes()+":"+
                                timesteps[0].getSeconds()+'</span>')

            if (changepct[0] < 0) {
              $("#changecaret").html('<i class="fa fa-arrow-down fa-3x" style="color:red">')
              $("#lastchangepct").html('<span id="uppct" style="color:red">'+Math.round((changepct[0] + 0.00001) * 10000) / 10000+' %'+'</span>')
              $("#lastabsolute").html('<span id="upabs" style="color:red">'+Math.round((changeabs[0] + 0.00001) * 10000) / 10000+' USD'+'</span>')
            } else {
              $("#changecaret").html('<i class="fa fa-arrow-up fa-3x" style="color:green"></i>')
              $("#lastchangepct").html('<span id="uppct" style="color:green">'+'+ '+Math.round((changepct[0] + 0.00001) * 10000) / 10000+' %'+'</span>')
              $("#lastabsolute").html('<span id="upabs" style="color:green">'+'+ '+Math.round((changeabs[0] + 0.00001) * 10000) / 10000+' USD'+'</span>')
            }

            cardChart1 = new Chart($('#card-chart1'), {
                type: 'line',
                data: {
                  labels: timesteps,
                  datasets: [{
                    label: 'last:',
                    backgroundColor: getStyle('--info'),
                    borderColor: 'rgba(255,255,255,0.5)',
                    data: lastPrice
                  }]
                },
                options: {
                  maintainAspectRatio: false,
                  legend: {
                    display: false
                  },
                  scales: {
                    xAxes: [{
                      display: false
                    }],
                    yAxes: [{
                      display: false,
                      ticks: {
                        max: Math.max.apply(Math, lastPrice) + 0.1, 
                        display: false,
                      }
                    }]
                  },
                  elements: {
                    line: {
                      borderWidth: 2
                    },
                    point: {
                      radius: 3,
                      hitRadius: 10,
                      hoverRadius: 4
                    }
                  }
                },

              });    
        }
    });
    setInterval(() => {
        $.ajax({ 
            url: '/gdax/btcusd',
            type: 'summary',
            success: function(resp) {
              resp = JSON.parse(resp)["data"]

              lastPrice = []
              highPrice = []
              lowPrice =  []
              changepct = []
              changeabs = []
              volume = []
              timesteps = []

              for (var i in resp) {
                data = resp[i]["data"]["result"]
                time = resp[i]["time"]

                
                lastPrice.push(data["price"]["last"])
                timesteps.push(new Date(resp[i]["time"]*1000))
                changepct.push(data["price"]["change"]["percentage"])
                changeabs.push(data["price"]["change"]["absolute"])
                volume.push(data["volume"])

              }

          $('#lastprice').html('<span> 1 BTC = '+lastPrice[0] +" USD"+'</span>')
          $('#lastdate').html('<span>'+"Last Price: "+
                              timesteps[0].getHours()+":"+
                              timesteps[0].getMinutes()+":"+
                              timesteps[0].getSeconds()+'</span>')
          
        if (changepct[0] < 0) {
          $("#changecaret").html('<i class="fa fa-arrow-down fa-3x" style="color:red"></i>')
          $("#lastchangepct").html('<span id="uppct" style="color:red">'+Math.round((changepct[0] + 0.00001) * 10000) / 10000+' %'+'</span>')
          $("#lastabsolute").html('<span id="upabs" style="color:red">'+Math.round((changeabs[0] + 0.00001) * 10000) / 10000+' USD'+'</span>')
          
        } else {
          $("#changecaret").html('<i class="fa fa-arrow-up fa-3x" style="color:green"></i>')
          $("#lastchangepct").html('<span id="uppct" style="color:green">'+'+ '+Math.round((changepct[0] + 0.00001) * 10000) / 10000+' %'+'</span>')
          $("#lastabsolute").html('<span id="upabs" style="color:green">'+'+ '+Math.round((changeabs[0] + 0.00001) * 10000) / 10000+' USD'+'</span>')
        }


          cardChart1.data.labels =timesteps
          cardChart1.data.datasets[0].data = lastPrice
          cardChart1.options.scales.yAxes[0].ticks.suggestedMax =Math.max.apply(Math, cardChart1.config.data.datasets[0].data) + 0.01

          cardChart1.update()

            }
        });
        
    }, 1000*5);
});
