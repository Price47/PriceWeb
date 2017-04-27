/**
 * Created by rockstar645 on 4/27/17.
 */

$(document).ready(function(){

    $('#home-logo a img').hover(
        function(){
            $(this).addClass('spin')
    },
        function(){
            $(this).removeClass('spin')
        })

});

