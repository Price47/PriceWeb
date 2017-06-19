/**
 * Created by rockstar645 on 4/27/17.
 */

$(document).ready(function(){
    headContainer = $('#header_container');
    doriDev = $('#dori_development');
    doriOverview = $('#dori_overview');
    doriResult = $('#dori_results');
    doriDevContent = $('#dori_development_content');
    doriOverviewContent = $('#dori_overview_content');
    doriResultContent = $('#dori_results_content');
    doriKinectView = $('#kinect_view');
    doriVideo = $('#dori_video');
    doriKinectViewContent = $('#kinect_view_content');
    doriVideoContent = $('#dori_video_content');

    doriDevContent.slideUp();
    doriOverviewContent.slideUp();
    doriResultContent.slideUp();
    doriVideoContent.slideUp();
    doriKinectViewContent.slideUp();

    function setHighlight(gradient){
        headContainer.removeClass('wood-color-light');
        headContainer.addClass(gradient);
    }

    function removeHighlight(){
        headContainer.removeClass();
        headContainer.addClass('wood-color-light');
    }

    setTimeout( function(){
        $('.loader').css("display", "none")
    },1000 );

    function setTitle(text){
        $('#title_main').text(text);
    }

    function resetTitle(){
        $('#title_main').text('');
    }


    $('.home-logo a img').hover(
        function(){
            $(this).addClass('spin');
            setTitle('Home')
    },
        function(){
            $(this).removeClass('spin');
            resetTitle()
        }
    );


    $('#about_link, #about_button').hover(
        function(){
            setTitle('About This Page');
            setHighlight('gradient3')
        },
        function(){
           resetTitle();
           removeHighlight();

        }
    );

    $('#dori_link, #dori_button').hover(
        function(){
           setTitle('DORi Development Page');
           setHighlight('gradient1');
        },
        function(){
            resetTitle();
            removeHighlight();
        }
    );

    $('#loadscreen_button').hover(
        function(){
            setTitle('Loading Screens');
            setHighlight('gradient2');
        },
        function(){
            resetTitle();
            removeHighlight();
        }
    );

    $('#dori_button').click(function(){
        setHighlight('gradient1')
    });

    $('#carousel-slide-caption').html($('.active > .carousel-caption').html());
    $('.carousel').on('slid.bs.carousel', function () {
        $('#carousel-slide-caption').html($('.active > .carousel-caption').html());
        });

    doriDev.click(function(){
        doriDevContent.slideToggle();
    });

    doriOverview.click(function(){
        doriOverviewContent.slideToggle();
    });

    doriResult.click(function(){
        doriResultContent.slideToggle()
    });

    doriKinectView.click(function(){
        doriKinectViewContent.slideToggle();
    });

    doriVideo.click(function(){
        doriVideoContent.slideToggle();
    });

});



