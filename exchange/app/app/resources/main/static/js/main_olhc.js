
$(document).ready(function(){
    $.ajax({

        url: '/kraken/btcusd/ohlc',
        type: 'GET',
//        contentType: "application/json",
        success: function(data) {
            data = data["data"]["result"]["300"]
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
                    selected:1,
                    buttons: [{
                        type: 'hour',
                        count: 24,
                        text: '1d',
                        dataGrouping: {
                            forced: true,
                            units: [['hour', [1]]]
                        }
                    }, {
                        type: 'hour',
                        count: 24*3,
                        text: '3d',
                        dataGrouping: {
                            forced: true,
                            units: [['hour', [1]]]
                        }
                    }, {
                        type: 'hour',
                        text: '1w',
                        count: 24*7,
                        dataGrouping: {
                            forced: true,
                            units: [['hour', [1]]]
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
                            maxWidth: 500
                        },
                        chartOptions: {
                            chart: {
                                height: 500
                            },
                            rangeSelector: {
                                enabled: false
                            },
                            navigator: {
                                enabled: true
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
                    pointInterval: 300 * 1000,
                }, {
                    type: 'column',
                    name: 'Volume',
                    data: volume,
                    yAxis: 1,
                    pointStart: Date.UTC(2018, 1, 1),
                    pointInterval: 300 * 1000,

                }]
            });
        },
        complete:function(){
            $(".highcharts-credits").hide()
            setInterval(function () {
                var chart = $('#main-chart').highcharts();
                var series = chart.series;
                var x = Date.now()+30000000;
                series[0].addPoint([x, Math.round(Math.random() * 10000),
                                        Math.round(Math.random() * 10000),
                                        Math.round(Math.random() * 10000),
                                        Math.round(Math.random() * 10000)], true, true);
                                     
                series[1].addPoint([x, Math.round(Math.random() * 50),
                                        Math.round(Math.random() * 50),
                                        Math.round(Math.random() * 50),
                                        Math.round(Math.random() * 50)], true, true);                                


            }, 1000*2);
        }
    })

                // set up the updating of the chart each second
                
                



})
