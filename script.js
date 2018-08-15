output = "";

output += "<div class='panel-group' id='myList'>";
$.getJSON("JSONData.json", function(data) {
    output += "<div class='panel panel-default'>";

    $.each(data, function(index, val){
        var name = val.Name;
        var season = val.Season;
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

                var episodeId = seasonId + "-episode-" +  (this.episodeId);
                var linkArray = this.episodeLink;

                var link = linkArray[0];

                output += "<li class='list-group-item'>";
                output += "<div class='panel panel-default'>";
                output += "<div class='panel-heading'>";

                output += "<h4 class='panel-title'>";

                output += "<a id='" + episodeId + "' data-toggle='collapse' href='" + link + "'>Episode " + this.episodeId + "</a>";

                output += "</h4>";

                output += "</div>";
                output += "<div id='iframeholder-" + episodeId + "'></div>";
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
});

alert(output);
$(document).ready(function(){
    $('span').html(output);
});

/* SEEKER FUNCTION */

$(document).ready(function(){

    $("a").click(function(event) {

        if ((event.target.id).includes("episode")) {
            alert(event.target.id);
            alert($("#" + event.target.id).attr("href") + " " + $('#iframeholder-' + event.target.id).length);

            if($('#iframeholder-' + event.target.id).length === 1) {
                alert(('#iframeholder-' + event.target.id));
                var link = ($("#" + event.target.id).attr("href"));
                alert('<iframe id="iframe" src="'+ (link) + '" width="700" height="450"></iframe>');
                $('#iframeHolder-' + event.target.id).html('<iframe id="iframe" src="'+ (link) + '" width="700" height="450"></iframe>');
            }
        }

    });

    $("#myInput").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $("#myList li").filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });

  $('.parent').on("click",function(){

    $(this).find(".sub-nav").toggle();
    $(this).siblings().find(".sub-nav").hide();

    if($(".sub-nav:visible").length === 0 ){
      $("#menu-overlay").hide();
    }else {
      $("#menu-overlay").show();
    }
  });

   $("#menu-overlay").on("click",function(){
     $(".sub-nav").hide();
     $(this).hide();
   });
});
