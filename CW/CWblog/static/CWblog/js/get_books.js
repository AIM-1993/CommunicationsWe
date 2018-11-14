$(document).ready(function(){
    $.getJSON('http://localhost:8000/weather', function(data){
        console.log(data);
        $.each(data, function (i, history) {
            $('#result').append( '<p>' + history.title + '</p>' );
        })

    })

});

