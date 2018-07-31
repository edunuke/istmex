
$(document).ready(function(){
    $.ajax({ 
        url: '/gdax/btcusd/1514764800',
        type: 'ohlc',
        success: function(data) {
            data = data["data"]["result"]["60"]
            var ohlc = [],
            volume = [],
            dataLength = data.length,
            
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
                    selected:0,
                    buttons: [{
                        type: 'minute',
                        count: 30,
                        text: '30m',
                        dataGrouping: {
                            forced: true,
                            units: [['minute', [1]]]
                        }
                    }, {
                        type: 'hour',
                        count: 24*2,
                        text: '2d',
                        dataGrouping: {
                            forced: true,
                            units: [['hour', [1]]]
                        }
                    }, {
                        type: 'all',
                        text: 'all',
                        count: 1,
                        dataGrouping: {
                            forced: true,
                            units: [['minute', [1]]]
                        }
                    }],
                }, 
                yAxis: [{
                    labels: {
                        align: 'right',
                        x: -3
                    },

                    height: '60%',
                    lineWidth: 2,
                    resize: {
                        enabled: true
                    }
                }, {
                    labels: {
                        align: 'right',
                        x: -3
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
                responsive: {
                    rules: [{
                        condition: {
                            maxWidth: 500,
                            minHeight: 
                        },
                        chartOptions: {
                            chart: {
                                height: 500
                            },
                            rangeSelector: {
                                enabled: false
                            },
                            navigator: {
                                enabled: false
                            }
                        }
                    }]
                },
                exporting: { enabled: false },
                time: { useUTC: false },
                series: [{
                    type: 'candlestick',
                    name: 'BTCUSD',
                    data: ohlc,
                    pointStart: Date.UTC(2018, 1, 1),
                    pointInterval: 60 * 1000,
                }, {
                    type: 'column',
                    name: 'Volume',
                    data: volume,
                    yAxis: 1,
                    pointStart: Date.UTC(2018, 1, 1),
                    pointInterval: 60 * 1000,

                }]
            });
        },
        complete:function(){
            $(".highcharts-credits").hide()

        }
    })

    // set up the updating of the chart once per min
                
    setInterval(function () {
        var chart = $('#main-chart').highcharts()
        var series = chart.series
        var lastTime =Math.floor((new Date()).getTime()/1000)

        $.ajax({
            url: '/gdax/btcusd/'+lastTime,
            type: 'ohlc',
            success: function(data) {
                data = data["data"]["result"]["60"]
                var ohlc = [],
                volume = [],
                dataLength = data.length,
                            
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
                series[0].addPoint(ohlc[i], true, true)
                series[1].addPoint(volume[i], true, true)
                
                }
            }
        });
    }, 1000*60);






})
