  $(function() {
    $( "#info" ).dialog({
      dialogClass: "no-close info-dialog",
      width: 550,
      height: 240,
      autoOpen: false,
      modal: true,
      show: {
        effect: "slide",
        duration: 500
      },
      hide: {
        effect: "clip",
        duration: 500
      },
      open: function(){
          jQuery('.ui-widget-overlay').bind('click',function(){
          jQuery('#info').dialog('close');
      })
      }
    });
 
    $( ".btn" ).click(function() {
      $(".ui-dialog").removeClass("ui-corner-all");
      $( "#info" ).dialog( "open" );
    });
  });
$(function() {
$('.slider').unslider({
  speed: 300,               //  The speed to animate each slide (in milliseconds)
  delay: 5000,              //  The delay between slide animations (in milliseconds)
  complete: function() {},  //  A function that gets called after every slide animation
  keys: true,               //  Enable keyboard (left, right) arrow shortcuts
  dots: true,               //  Display dot navigation
  fluid: false              //  Support responsive design. May break non-responsive designs
});
});
$(function(){
  $('.h label').mouseover(function(){
    $('.caption').fadeIn(400);
  });
  $('.h label').mouseout(function(){
    $('.h .caption').fadeOut(400);
  });
});


