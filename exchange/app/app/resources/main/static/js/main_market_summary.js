$(document).ready(function(){

    var pusher = new Pusher('de504dc5763aeef9ff52');

    var channel = pusher.subscribe('live_trades');
    channel.bind('trade', function(data) {
        console.log(JSON.stringify(data));
    });
    
});
