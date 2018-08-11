$(document).ready(function () {
    $('.do_something').click(function() {
        $.getJSON('JSONData.json', function(data) {
        console.log(data);
        });
    });
});
