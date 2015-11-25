
$(document).ready ( function () {
//проверка на ошибки при открытии документа
/*  isValid();
  $('#errcount').html(parseInt($('#errmess > p').length));
  if (parseInt($('#errmess > p').length) == 0) $('#message').html('<p>Ошибок нет</p>')
  else  $('#message').html('');*/
//в ячейках нет пустых значений
  $('.number, input[type="number"]').blur ( function() {
    if ($(this).val() == '') {$(this).val(0)} 
  })
//выделение всего перед внесением
  $('input').click ( function() {
    $(this).select();
  })
//показать/скрыть коментарии	
  $('#showingL').click ( function () {   
    if ($('#Comments').hasClass("vComments")) {
      $('#Comments').removeClass("vComments");
	  $(this).attr("alt", "Показать");
	  $(this).attr("title", "Показать");
	}
	else {
	  $('#Comments').addClass("vComments");
	  $(this).attr("alt", "Скрыть");
	  $(this).attr("title", "Скрыть");
	}
  })
//показать/скрыть сообщения (ошибки, уведомления и т.п)
  $('#showingR').click ( function () {   
    if ($('#mess').hasClass("vMess")) {
      $('#mess').removeClass("vMess");
	  $(this).attr("src", "/static/img/showT.png");
	  $(this).attr("alt", "Показать");
	  $(this).attr("title", "Показать");
	}
	else {
	  $('#mess').addClass("vMess");
	  $(this).attr("src", "/static/img/showF.png");
	  $(this).attr("alt", "Скрыть");
	  $(this).attr("title", "Скрыть");
	}
  })

  
  
	  
	// тест Ajax  
    $("#btnAjax").click ( function(){ 

    	$('<div id="messwait" class="waitpopup"><img src="/static/img/ajax-loader.gif"> Загрузка, ждите..</div>').appendTo('body');
    			
	    $.ajax("/test1/1").then(function(data) {
	      $("#messwait").remove();
	      obj= JSON.parse(data)
	      $('#errmess').html('<p>' + 'id=' + obj.id + ' name=' + obj.name + '</p>')
     	  
        });
    });
  
  
//кнопка проверки на ошибки
  $('#valid').click ( function () {
    isValid();
	$('#errcount').html(parseInt($('#errmess > p').length));
	if (parseInt($('#errmess > p').length) == 0) $('#message').html('<p>Ошибок нет</p>')
    else  $('#message').html('')
  })
//проверка на ошибки перед отправкой на согласование  
  $("#btnSend").click ( function(){ 
	isValid()
	$('#errcount').html(parseInt($('#errmess > p').length));
    if ($('#errmess > p').length > 0) return false; 
  });
  
//блокировка повторного отправления запроса
  $('#btnBar button, #btnBar .button').click ( function () {
    if (!$('btnBar').attr('hidden')) 
	  if (!($(this).attr('id')=="btnSend")||($('#errmess > p').length == 0)){
	    $('#DocLoad').removeAttr('hidden');
        $('#btnBar').attr('hidden', 'hidden');
        $('#btnExp').attr('hidden', 'hidden');
	  }
	  else
	  {}
	else {
	  $('#btnBar button, #btnBar .button').attr('disabled', 'disabled');
      $('#btnExp').attr('disabled', 'disabled');
	}
  })
})