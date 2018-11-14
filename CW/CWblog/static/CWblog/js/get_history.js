$(document).ready(function(){
    $.getJSON('http://localhost:8000/history', function(data){
        console.log(data);
        $.each(data, function (i, history) {
            $('#result').append( '<h4 class="article-font">' + history.title +"--" + history.year + '年</h4>' );
        });
    });
});

