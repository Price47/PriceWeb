/**
 * Created by rockstar645 on 7/5/17.
 */
$(document).ready(function() {
    var rng = document.querySelector("#abv");
    var beerQueryInput = $('#beerquery_check');
    var beerNameQueryCheck = $('#name_query_check');
    var beerNameQueryDiv = $('#beer_name_div');
    var beerAbvQueryCheck = $('#abv_query_check');
    var beerAbvQueryDiv = $('#beer_abv_div');


    var abvRange = function () {
        window.requestAnimationFrame(function () {
            document.querySelector("#abv_value").innerHTML = rng.value;
        });
    };

    rng.addEventListener("mousedown", function () {
        abvRange();
        rng.addEventListener("mousemove", abvRange);
    });
    rng.addEventListener("mouseup", function () {
        rng.removeEventListener("mousemove", abvRange);
    });


    beerQueryInput.on('click', function () {
        if ($(this).is(':checked')) {
            $('#beer_query_div').show();
            $('#brew_submit').val('Search')
        }
        else {
            $('#brew_submit').val('Random');
            beerNameQueryCheck.prop('checked', false);
            beerAbvQueryCheck.prop('checked', false);
            $('#beer_query_div').hide();
            beerNameQueryDiv.hide();
            beerAbvQueryDiv.hide();
        }
    });

    beerNameQueryCheck.on('click', function () {
        if ($(this).is(':checked')) {
            beerNameQueryDiv.show()
        }
        else
            beerNameQueryDiv.hide()
    });

    beerAbvQueryCheck.on('click', function () {
        if ($(this).is(':checked')) {
            beerAbvQueryDiv.show();
        }
        else
            beerAbvQueryDiv.hide()
    });
});