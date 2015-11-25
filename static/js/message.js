
$(document).ready ( function () {
  isValid();
  $('#errcount').html(parseInt($('#errmess > p').length));
  if (parseInt($('#errmess > p').length) == 0) $('#message').html('<p>Ошибок нет</p>')
  else  $('#message').html('')
//в ячейках нет пустых значений
  $('.number').blur ( function() {
    if ($(this).val() == '') {$(this).val(0)} 
  })
  $('input').click ( function() {
    $(this).select();
  })
	
  $('#showing').click ( function () {    
    if ($('#mess').hasClass("vMess")) {
      $('#mess').removeClass("vMess");
	  $(this).attr("src", "/static/img/showT.png");
	  $(this).attr("alt", "Показать");
	}
	else {
	  $('#mess').addClass("vMess");
	  $(this).attr("src", "/static/img/showF.png");
	  $(this).attr("alt", "Скрыть");
	}
  })
  $('#valid').click ( function () {
    isValid();
	$('#errcount').html(parseInt($('#errmess > p').length));
	if (parseInt($('#errmess > p').length) == 0) $('#message').html('<p>Ошибок нет</p>')
    else  $('#message').html('')
  })
  
  $("#btnSend").click ( function(){ 
	isValid()
	$('#errcount').html(parseInt($('#errmess > p').length));
    if ($('#errmess > p').length > 0) return false; 
  });
})