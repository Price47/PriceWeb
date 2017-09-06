/**
 * Created by rockstar645 on 9/5/17.
 */

function getTvData(){
        $.get('rest/get_bestbuy_data').then(successCallback, errorCallback)
}

function errorCallback(response){
    console.log(response)
}

function successCallback(response){
    console.log(response);
    var straightData = response['normal_hits'];
    var curvedData = response['curved_hits'];

    var totalHits = straightData['LG'] +
                    straightData['Samsung'] +
                    straightData['Sony'] +
                    straightData['Toshiba'];

    var totalCurvedHits = curvedData['LG'] +
                            curvedData['Samsung'] +
                            curvedData['Sony'] +
                            curvedData['Toshiba'];

    var searchResults = Highcharts.chart('tv_search_results', {
            chart: {
                type: 'bar'
            },
            title: {
                text: 'Best Buy TV search results'
            },
            xAxis: {
                categories: ['LG', 'Samsung', 'Sony', 'Toshiba']
            },
            yAxis: {
                title: {
                    text: 'Hits'
                }
            },
            series: [{
                name: 'Smart TV Results',
                data: [straightData['LG'], straightData['Samsung'], straightData['Sony'], straightData['Toshiba']]
            },
            {
                name: 'Curved Smart TV Results',
                data: [curvedData['LG'], curvedData['Samsung'], curvedData['Sony'], curvedData['Toshiba']]
            }]
    });

    var resultPercentage = Highcharts.chart('tv_search_results_percentage', {
            chart: {
                type: 'pie'
            },
            tooltip: {
                pointFormat: '<b>{point.percentage:.1f}%</b>'
            },
            series: [{
                data: [{
                    name: 'LG',
                    y: straightData['LG']
            }, {
                    name: 'Samsung',
                    y: straightData['Samsung']

            }, {
                    name: 'Sony',
                    y: straightData['Sony']
            }, {
                    name: 'Toshiba',
                    y: straightData['Toshiba']
                }]
            }]
    });

    var curvedResultPercentage = Highcharts.chart('curved_tv_search_results_percentage', {
            chart: {
                type: 'pie'
            },
            tooltip: {
                pointFormat: '<b>{point.percentage:.1f}%</b>'
            },
            series: [{
                data: [{
                    name: 'LG',
                    y: curvedData['LG']
            }, {
                    name: 'Samsung',
                    y: curvedData['Samsung']

            }, {
                    name: 'Sony',
                    y: curvedData['Sony']
            }, {
                    name: 'Toshiba',
                    y: curvedData['Toshiba']
                }]
            }]
    });

    var rateTrend = Highcharts.chart('rate_search_trend', {
            title: {
                text: 'Search results vs Rating trend'
            },
            yAxis: {
                title: {
                    text:'Rating'
                }
            },
            xAxis: {
                title:{
                    text:'Search Ranking'
                }
            },
            plotOptions:{
                series:{
                    pointStart:1
                }
            },
            series:[{
                name: 'Smart TV',
                data: response['rate_trends']
            }, {
                name: 'Curved Smart Tv',
                data: response['curved_rate_trends']
            }]
    });

    var reviewTrend = Highcharts.chart('review_search_trend', {
            title: {
                text: 'Search results vs Review trend'
            },
            yAxis: {
                title: {
                    text:'Number of Reviews'
                }
            },
            xAxis: {
                title:{
                    text:'Search Ranking'
                }
            },
            plotOptions:{
                series:{
                    pointStart:1
                }
            },
            series:[{
                name: 'Smart TV',
                data: response['review_trends']
            }, {
                name: 'Curved Smart Tv',
                data: response['curved_review_trends']
            }]
    });
}

$(function () {
    Highcharts.setOptions({
        colors:['#447fff', '#44ff91', '#ffab4c', '#c549ff']

    });




});