
output = "";

$.getJSON("JSONData.json", function(data) {
    $.each(data, function(key, val){
        var name = val.Name;
        var season = val.Season;

        output += "<div class='values'>";
        output += '<h5 class="value-id">' + name + '</h5>';


        $.each(season, function() {

            output += '<p>' + this.episodeId + '</p>';
        });


        output += '<p class="value-name">' + season + '</p>';
        output += "</div>";
    });
});

alert(output);
$(document).ready(function(){
    $('span').html(output);
});

/* SEEKER FUNCTION */

jQuery(function(){
  var $rows = $('.values');
  $('#seeker').keyup(function () {
    var regex =  new RegExp(RegExp.escape($.trim(this.value).replace(/\s+/g, ' ')), 'i')
    $rows.hide().filter(function () {
      var text = $(this).children(".value-name").text().replace(/\s+/g, ' ');
      return regex.test(text)
    }).show();
  });
});
