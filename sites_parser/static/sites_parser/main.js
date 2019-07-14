$("#button_1").on("click", function(e) {
    e.preventDefault();
    $.ajax({url: "/start_parsing"});
    var intervalId = null;
    var varName = function(){
    $.ajax({
        type: 'GET',
        url: '/get_new_info/',
          datatype: "json",
        success: function(data, textStatus, jqXHR) {
          if (jqXHR.status == "200"){
            for (var i = 0; i < data.length; i++) {
                var id_for_win1 = "#1_"+ data[i]['id'];
                $(id_for_win1).html(
                    '<дата '+data[i]['data']['parsing_time']+'>: '+
                    'url: '+data[i]['data']['site_url']+' / '+
                    'статус: '+data[i]['data']['parsing_complete']);
                var id_for_win2 = "#2_"+ data[i]['id'];
                $(id_for_win2).html(
                    'заголовок: '+data[i]['data']['site_title']+' / '+
                    'кодировка: '+data[i]['data']['site_encoding']+' / '+
                    'тег h1: '+data[i]['data']['site_header']);
            }};
            if (jqXHR.status == "204"){
                clearInterval(intervalId);
                $('.alert').show();
            };
          },
    });
    };
    $(document).ready(function(){
         intervalId = setInterval(varName, 2000);
    });
});
