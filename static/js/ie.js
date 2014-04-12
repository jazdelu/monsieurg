  $(function() {
    $( "#ie" ).dialog({
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
 
    $(document).ready(function() {
      $(".ui-dialog").removeClass("ui-corner-all");
      $( "#ie" ).dialog( "open" );
    });
  });