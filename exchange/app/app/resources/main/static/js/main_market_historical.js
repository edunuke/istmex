
$(document).ready(function(){

    $.ajax({ 
        url: '/gdax/btcusd',
        type: 'hist',
        success: function(resp) {

            data = JSON.parse(resp)["data"]["result"]["43200"]
            var ohlc = [],
            volume = [],
            dataLength = data.length
            i = 0;
    
            for (i; i < dataLength; i += 1) {
                ohlc.push([
                    data[i][0]*1000, // the date
                    data[i][1], // open
                    data[i][2], // high
                    data[i][3], // low
                    data[i][4] // close
                ]);
        
                volume.push([
                    data[i][0]*1000, // the date
                    data[i][5] // the volume
                ]);
            }
        
        
            // create the chart
            Highcharts.stockChart('main-chart', {

                rangeSelector: {    
                    enabled:true,
                    selected:1,
                    buttons: [{
                        type: 'week',
                        count: 1*2,
                        text: '1w',
                        dataGrouping: {
                            forced: true,
                            units: [['day', [1]]]
                        }
                    }, {
                        type: 'month',
                        count: 1*3,
                        text: '3m',
                        dataGrouping: {
                            forced: true,
                            units: [['day', [1]]]
                        }
                    }, {
                        type: 'all',
                        text: 'ytd',
                        count: 1,
                        dataGrouping: {
                            forced: true,
                            units: [['day', [1]]]
                        }
                    }],
                }, 
                yAxis: [{
                    labels: {
                        align: 'left',
                        x: 0
                    },

                    height: '60%',
                    lineWidth: 2,
                    resize: {
                        enabled: true
                    }
                }, {
                    labels: {
                        align: 'left',
                        x: 0
                    },

                    top: '65%',
                    height: '35%',
                    offset: 0,
                    lineWidth: 2
                }],
                inputEnabled: false,
                tooltip: {
                    split: true
                },
                scrollbar: {
                    liveRedraw: true
                },
                plotOptions: {
                    candlestick: {
                        color: "#EC7063",
                        upColor: "#82E0AA"
                    }
                },
                time: { useUTC: false },
                series: [{
                    type: 'candlestick',
                    name: 'BTCUSD',
                    data: ohlc,
                    //pointStart: Date.UTC(2018, 1, 1),
                    //pointInterval: 60 * 1000,
                }, {
                    type: 'column',
                    name: 'Volume',
                    data: volume,
                    yAxis: 1,
                    //pointStart: Date.UTC(2018, 1, 1),
                    //pointInterval: 60 * 1000,

                }]
            });
        },
        complete:function(){
            $(".highcharts-credits").hide()

        }
    })

    // set up the updating of the chart once per min
    $("#update-history").on("click", function(e){
        e.preventDefault()

        $.ajax({
            url: '/gdax/btcusd',
            type: 'hist',
            beforeSend:function(){
                $("#update-history i").addClass("fa-spin")
            },
            success: function(resp) {
                chart = $('#main-chart').highcharts()
                var data = JSON.parse(resp)["data"]["result"]["43200"]
                var ohlc = []
                var volume = []
                var dataLength = data.length,
                            
                i = 0;
                    
                for (i; i < dataLength; i += 1) {
                ohlc.push([data[i][0]*1000, // the date
                           data[i][1], // open
                           data[i][2], // high
                           data[i][3], // low
                           data[i][4] // close
                          ]);
                
                volume.push([
                            data[i][0]*1000, // the date
                            data[i][5] // the volume
                            ]);
                
                }

                new_serie = [{
                    type: 'candlestick',
                    name: 'BTCUSD',
                    data: ohlc,
                }, {
                    type: 'column',
                    name: 'Volume',
                    data: volume,


                }]

                chart.update({
                    series:new_serie
                })

            },
            complete: function(){
                setTimeout(function(){
                    $("#update-history i").removeClass("fa-spin")
                }, 2000);
                
            }
        });
    })



// set up the updating of the chart once per min




})
