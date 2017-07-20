/**
 * Created by rockstar645 on 4/27/17.
 */

$(document).ready(function(){
    var headContainer = $('#header_container');
    var doriDev = $('#dori_development');
    var doriOverview = $('#dori_overview');
    var doriResult = $('#dori_results');
    var doriDevContent = $('#dori_development_content');
    var doriOverviewContent = $('#dori_overview_content');
    var doriResultContent = $('#dori_results_content');
    var doriKinectView = $('#kinect_view');
    var doriVideo = $('#dori_video');
    var doriKinectViewContent = $('#kinect_view_content');
    var doriVideoContent = $('#dori_video_content');
    var abstractMax = $('#abstract_max');
    var abstractClose = $('#abstract_close');
    var abstractFrame = $('#abstract_frame');
    var developmentMax = $('#development_max');
    var developmentClose = $('#development_close');
    var developmentFrame = $('#dev_frame');
    var resultMax = $('#results_max');
    var resultsClose = $('#results_close');
    var resultsFrame = $('#result_frame');
    var topNav = $('#top_nav_links');
    var topNavAbout = $('#top_nav_about');
    var topNavDori = $('#top_nav_dori');
    var topNavLoading = $('#top_nav_loading');
    var topNavBrewer = $('#top_nav_brewer');
    var abvValue = $('#abv');
    var homeLinkGlyph = $('#home_link_glyph');

    var homeLinksVisible = false;



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

    function setElementHoverAttribute(elem, gradient, title){
        elem.hover(
            function(){
                $(this).addClass(gradient);
                setTitle(title);
            },function(){
                $(this).removeClass(gradient);
                resetTitle();
            });
    }

    // set the hover function for each link to highlight the top nav and output
    // the link path
    setElementHoverAttribute(topNavLoading, 'gradient1', 'Loading Screens');
    setElementHoverAttribute(topNavBrewer, 'gradient2', 'Brewer');
    setElementHoverAttribute(topNavDori, 'gradient3', 'DORi');
    setElementHoverAttribute( topNavAbout,'gradient4', 'About');



    $('.loadscreen-button').hover(
        function(){
            setTitle('Loading Screens');
            setHighlight('gradient1');
        },
        function(){
            resetTitle();
            removeHighlight();
        }
    );

    $('.brewer-button').hover(
        function(){
            setTitle('Brewer');
            setHighlight('gradient2');
        },
        function(){
            resetTitle();
            removeHighlight();
        }
    );

    $('.dori-link-button').hover(
        function(){
           setTitle('DORi Development Page');
           setHighlight('gradient3');
        },
        function(){
            resetTitle();
            removeHighlight();
        }
    );

    $('.about-button').hover(
        function(){
            setTitle('About This Page');
            setHighlight('gradient4')
        },
        function(){
           resetTitle();
           removeHighlight();

        }
    );


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

    $('#menu_button_down').click(function(){
        $(this).css({'display':'none'});
        $('#menu_wrapper').animate({'margin-top':'+=30px'});
        $('#menu_button_up').css({'display':'inline'});

    });

    $('#menu_button_up').click(function(){
        $(this).css({'display':'none'});

        $('#menu_wrapper').animate({'margin-top':'-=30px'});
        $('#menu_button_down').css({'display':'inline'});
    }) ;


    $('#home_link_open').click(function(){
        if(homeLinksVisible){
            homeLinkGlyph.removeClass('glyphicon glyphicon-resize-small');
            homeLinkGlyph.addClass('glyphicon glyphicon-resize-full');
            homeLinksVisible = false;
            $('#home_links_container').css({'display':'none'})
        }
        else{
            homeLinkGlyph.removeClass('glyphicon glyphicon-resize-full');
            homeLinkGlyph.addClass('glyphicon glyphicon-resize-small');
            homeLinksVisible = true;
            $('#home_links_container').css({'display':'inline'})
        }


    });




});



