/**
 * Created by rockstar645 on 4/27/17.
 */

$(document).ready(function(){
    $('#carousel').carousel();

    var loaderExample = 1;

    setTimeout( function(){
        $('.loader').css("display", "none")
    },1000 );


    function highlight(selector){
        selector.removeClass('home-links-still');
        selector.addClass('gradient1');
    }

    function delight(selector){
        selector.removeClass('gradient1');
        selector.addClass('home-links-still');
    }

    $('.home-logo a img').hover(
        function(){
            $(this).addClass('spin');
            $('#title_main').text('Home')
    },
        function(){
            $(this).removeClass('spin');
            $('#title_main').text('')
        }
    );

    $('#about_link, #about_button').hover(
        function(){
            $('#title_main').text('About This Page');
        },
        function(){
            $('#title_main').text('')

        }
    );

    $('#dori_link, #dori_button').hover(
        function(){
            $('#title_main').text('DORi Development Page');
        },
        function(){
            $('#title_main').text('');
        }
    );

    $('#loadscreen_button').hover(
        function(){
            $('#title_main').text('Loading Screens');
        },
        function(){
            $('#title_main').text('');
        }
    );

    $('#carousel-slide-caption').html($('.active > .carousel-caption').html());
    $('.carousel').on('slid.bs.carousel', function () {
        $('#carousel-slide-caption').html($('.active > .carousel-caption').html());
        });

});



