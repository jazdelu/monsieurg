$(document).ready(function(){
  //initial theme selecte
  selected = $("#id_product").val();
  $.ajax({
    type: 'GET',
    url: "/ajax/product?pid="+$("#id_theme").val(),
    dataType:"json",
    success:function(data,textStatus){
      var s = $("#id_product");
    }
  });
});