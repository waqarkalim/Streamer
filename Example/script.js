
output = "";
$.getJSON("JSONData.json", function(data) {
    output += "<div id='menu-overlay'></div>";
    output += "<div id='menu'>";

    output += "<ul class='list-group' id='myList'>";
    $.each(data, function(key, val){
        var name = val.Name;
        var season = val.Season;


        output += "<li class='parent list-group-item'><b>" + name + "</b>";
        output += "<ul class='sub-nav'>";

        $.each(season, function(key, value) {

            var seasonObj = this;
            output += "<li>" + key ;
            output += "<ul>";
            $.each(seasonObj, function(key, value) {
                output += '<li>Episode ' + this.episodeId + '</li>';
            });
            output += "</ul>";
            output += "</li>";

        });

        output += "</ul>";
        output += "</li>";

    });
    output += "</ul>";
    output += "</div>";
});

alert(output);
$(document).ready(function(){
    $('span').html(output);
});

/* SEEKER FUNCTION */

$(document).ready(function(){
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
