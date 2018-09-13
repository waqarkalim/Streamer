var output = "";

// output.promise().done(function( arg1 ) {

//   alert( this === output && arg1 === output );
// });

output += "<div class='panel-group' id='myList'>";


var jsonGet = $.getJSON("JSONData.json", function(data) {
    output += "<div class='panel panel-default'>";

    $.each(data, function(index, val) {
        var name = val.Name;
        var season = val.Season;
        var punctuationless = name.replace(/[.,\/#!$%\^&\*;:{}=\-_`~()']/g, "");
        var name = punctuationless.replace(/\s{2,}/g, " ");
        var nameId = name.replace(/\s+/g, '-').toLowerCase();


        output += "<div id='" + nameId + "' class ='panel-collapse collapse>'"
        output += "<ul class='list-group'>";
        output += "<li class='list-group-item'>";

        output += "<div class='panel panel-default panel-borderless'>";
        output += "<div class='panel-heading'>";

        output += "<h4 class='panel-title'>";

        output += "<a data-toggle='collapse' href='#" + nameId + "-" + index + "'>" + name + "</a>";

        output += "</h4>";

        output += "</div>";
        output += "<div id='" + nameId + "-" + index + "' class='panel-collapse collapse'>";
        output += "<ul class='list-group'>";

        $.each(season, function(key, value) {

            var seasonObj = this;
            var punctuationless = key.replace(/[.,\/#!$%\^&\*;:{}=\-_`~()']/g, "");
            var key = punctuationless.replace(/\s{2,}/g, " ");
            var seasonId = nameId + "-" + key.replace(/\s+/g, '-').toLowerCase();

            output += "<li class='list-group-item'>";

            output += "<div class='panel panel-default'>";
            output += "<div class='panel-heading'>";

            output += "<h4 class='panel-title'>";

            output += "<a data-toggle='collapse' href='#" + seasonId + "'>" + key + "</a>";

            output += "</h4>";

            output += "</div>";

            output += "<div id='" + seasonId + "' class='panel-collapse collapse'>";
            output += "<ul class='list-group'>";

            $.each(seasonObj, function(key, value) {

                var episodeId = seasonId + "-episode-" + (this.episodeId);
                var linkArray = this.episodeLink;

                var link = linkArray[0];

                output += "<li class='list-group-item'>";
                output += "<div class='panel panel-default'>";
                output += "<div class='panel-heading'>";

                output += "<h4 class='panel-title'>";

                output += "<a id='" + episodeId + "' data-toggle='collapse' href='" + link + "'>Episode " + this.episodeId + "</a>";

                output += "</h4>";

                output += "</div>";
                output += "<div class='iframeholder-" + episodeId + "'></div>";
                output += "</div>";

                output += "</li>";
            });
            output += "</ul>";
            output += "</div>";
            output += "</div>";
            output += "</li>";

        });
        output += "</ul>";
        output += "</div>";
        output += "</div>";
        output += "</li>";
        output += "</ul>";
        output += "</div>";

    });
    output += "</div>";
    output += "</div>";

    // $('span').html(output); // ACTUALLY WORKS but not on Mobile so change it, BUT best one so far

});

jsonGet.done(function() {
    $('span').html(output);

    /* SEEKER FUNCTION */
    var clicks = 0;
    $("a").click(function(event) {

        if ((event.target.id).includes("episode")) {
            /*
            alert(event.target.id);
            alert($("#" + event.target.id).attr("href") + " " + $('div.iframeholder-' + event.target.id).length);
*/
            if ($('div.iframeholder-' + event.target.id).length === 1) {

                if ((clicks % 2) == 0) {

                    $('div.iframeholder-' + event.target.id).html(function() {

                        var link = ($("#" + event.target.id).attr("href"));
                        return '<div class="embed-responsive embed-responsive-16by9"><iframe class="embed-responsive-item" sandbox="allow-scripts allow-forms allow-same-origin" src="' + link + '" allowfullscreen="true" webkitallowfullscreen="true" mozallowfullscreen="true" marginheight="0" marginwidth="0" scrolling="no" target="_blank" frameborder="0"></iframe></div>'

                    });
                } else {

                    $('div.iframeholder-' + event.target.id).html(function() {
                        var link = ($("#" + event.target.id).attr("href"));
                        return ''

                    });
                }
            }
        }
        clicks++;

    });

    $("#myInput").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $("#myList li").filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });

    $('.parent').on("click", function() {

        $(this).find(".sub-nav").toggle();
        $(this).siblings().find(".sub-nav").hide();

        if ($(".sub-nav:visible").length === 0) {
            $("#menu-overlay").hide();
        } else {
            $("#menu-overlay").show();
        }
    });

    $("#menu-overlay").on("click", function() {
        $(".sub-nav").hide();
        $(this).hide();
    });
});

// $(document).ready(function() {
// });


