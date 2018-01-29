$(document).ready(function(){

  $('#stars li').on('mouseover', function(){
    var onStar = parseInt($(this).data('value'), 10); // The star currently mouse on

    $(this).parent().children('li.star').each(function(e){
      if (e < onStar) {
        $(this).addClass('hover');
      }
      else {
        $(this).removeClass('hover');
      }
    });

  }).on('mouseout', function(){
    $(this).parent().children('li.star').each(function(e){
      $(this).removeClass('hover');
    });
  });


  $('#stars li').on('click', function(){
    var onStar = parseInt($(this).data('value'), 10);
    var stars = $(this).parent().children('li.star');

    for (i = 0; i < stars.length; i++) {
      $(stars[i]).removeClass('selected');
    }

    for (i = 0; i < onStar; i++) {
      $(stars[i]).addClass('selected');
    }

    // JUST RESPONSE (Not needed)
    var ratingValue = parseInt($('#stars li.selected').last().data('value'), 10);
    var msg = "";
    if (ratingValue > 1) {
        $('.success-box').show();
        msg = "Thanks! You rated this " + ratingValue + " stars.";
        $('#rating_value').val(ratingValue);
        $('.rating-form').submit();
    }
    else {
        msg = "We will improve ourselves. You rated this " + ratingValue + " stars.";
    }
    responseMessage(msg);

  });

});


function responseMessage(msg) {
  $('.success-box').fadeIn(200);
  $('.success-box div.text-message').html("<span>" + msg + "</span>");
}