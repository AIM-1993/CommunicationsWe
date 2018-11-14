$.ajax(
    $.getJSON('CWblog/', function(data){ 
        var famous_data = jQuery.parseJSON(data); 
        console.log(famous_data);
        $('#mrmy-body').html( '<p>' + famous_data.famous_saying + '</p>' ); 
        $('#mrmy-footer').html( '<p>By--' + famous_data.famous_name + '</p>' )
    })
)
