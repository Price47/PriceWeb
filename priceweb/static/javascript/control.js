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
    abstractMax = $('#abstract_max');
    abstractClose = $('#abstract_close');
    abstractFrame = $('#abstract_frame');
    developmentMax = $('#development_max');
    developmentClose = $('#development_close');
    developmentFrame = $('#dev_frame');
    resultMax = $('#results_max');
    resultsClose = $('#results_close');
    resultsFrame = $('#result_frame');

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

    abstractClose.click(function(){
        doriOverviewContent.slideUp();
    });

    developmentClose.click(function(){
        doriDevContent.slideUp();
    });

    resultsClose.click(function(){
        doriResultContent.slideUp();
    });

    abstractMax.click(function(){
        if(abstractFrame.css('height')=='250px'){
            $('#abstract_frame').animate({'height':'+=375px'})
        }
        if(abstractFrame.css('height')=='625px'){
            $('#abstract_frame').animate({'height':'-=375px'})
        }
    });

    developmentMax.click(function(){
        console.log(developmentFrame.css('height'));
        if(developmentFrame.css('height')=='250px'){
            $('#dev_frame').animate({'height':'+=550px'})
        }
        if(developmentFrame.css('height')=='800px'){
            $('#dev_frame').animate({'height':'-=550px'})
        }
    });

    resultMax.click(function(){
        if(resultsFrame.css('height')=='250px'){
            $('#result_frame').animate({'height':'+=100px'})
        }
        if(resultsFrame.css('height')=='350px'){
            $('#result_frame').animate({'height':'-=100px'})
        }
    });

    $.ajax(url)
        .done(function(){

        })
        .fail(function(){

        })




});



