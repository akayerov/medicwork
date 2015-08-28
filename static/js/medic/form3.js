  function calCell (t, r, c) {
    
    switch (t) {
	  case '1000':
	    switch (c) {
		  case '1': case '2': case '3': case '4':
	        $('#t' + t + '_r' + r + '_c' + c).html(
		      (parseInt($('#t' + t + '_r' + r + '_c' + (parseInt(c) + 4)).val()) + parseInt($('#t' + t + '_r' + r + '_c' + (parseInt(c) + 8)).val()))||
              (parseInt($('#t' + t + '_r' + r + '_c' + (parseInt(c) + 4)).html()) + parseInt($('#t' + t + '_r' + r + '_c' + (parseInt(c) + 8)).html()))||
		      0)
	        break;
	      case '5': case '6': case '7': case '8':
		    $('#t' + t + '_r' + r + '_c' + (parseInt(c) - 4)).html(
		      (parseInt($('#t' + t + '_r' + r + '_c' + c).val()) + parseInt($('#t' + t + '_r' + r + '_c' + (parseInt(c) + 4)).val()))||
              (parseInt($('#t' + t + '_r' + r + '_c' + c).html()) + parseInt($('#t' + t + '_r' + r + '_c' + (parseInt(c) + 4)).html()))||
		      0);
			sumCell(t, parseInt(c) - 4);
		    break;
	      case '9': case '10': case '11': case '12':
		    $('#t' + t + '_r' + r + '_c' + (parseInt(c) - 8)).html(
		      (parseInt($('#t' + t + '_r' + r + '_c' + (parseInt(c) - 4)).val()) + parseInt($('#t' + t + '_r' + r + '_c' + c).val()))||
              (parseInt($('#t' + t + '_r' + r + '_c' + (parseInt(c) - 4)).html()) + parseInt($('#t' + t + '_r' + r + '_c' + c).html()))||
		      0);
			sumCell(t, parseInt(c) - 8);
		    break;
		}
	    break;
      case '4000': case '5000': case '5001': case '6000':
	  // суммирование происходит по строкам 
        switch (c) {
          // сумирование для столбца мужчины/всего 
          case '1': case '2': case '3': case '4':
            $('#t' + t + '_r' + r + '_c4').html(
		      (parseInt($('#t' + t + '_r' + r + '_c1').val()) + parseInt($('#t' + t + '_r' + r + '_c2').val()) + parseInt($('#t' + t + '_r' + r + '_c3').val()))||
              (parseInt($('#t' + t + '_r' + r + '_c1').html()) + parseInt($('#t' + t + '_r' + r + '_c2').html()) + parseInt($('#t' + t + '_r' + r + '_c3').html()))||
		      0);
            break;
          // сумирование для столбца женщины/всего
          case '5': case '6': case '7': case '8':
            $('#t' + t + '_r' + r + '_c8').html(
	          (parseInt($('#t' + t + '_r' + r + '_c5').val()) + parseInt($('#t' + t + '_r' + r + '_c6').val()) + parseInt($('#t' + t + '_r' + r + '_c7').val()))||
		      (parseInt($('#t' + t + '_r' + r + '_c5').html()) + parseInt($('#t' + t + '_r' + r + '_c6').html()) + parseInt($('#t' + t + '_r' + r + '_c7').html()))||
		      0);
            break;
	    } 
        switch (c) {
          // сумирование для столбца всего/21-36 лет
          case '1': case '5': case '9':
            $('#t' + t + '_r' + r + '_c9').html(
		      (parseInt($('#t' + t + '_r' + r + '_c1').val()) + parseInt($('#t' + t + '_r' + r + '_c5').val()))||
		      (parseInt($('#t' + t + '_r' + r + '_c1').html()) + parseInt($('#t' + t + '_r' + r + '_c5').html()))||
		      0);
            break;
          // сумирование для столбца всего/37-60 лет
          case '2': case '6': case '10':
            $('#t' + t + '_r' + r + '_c10').html(
		      (parseInt($('#t' + t + '_r' + r + '_c2').val()) + parseInt($('#t' + t + '_r' + r + '_c6').val()))||
		      (parseInt($('#t' + t + '_r' + r + '_c2').html()) + parseInt($('#t' + t + '_r' + r + '_c6').html()))||
              0);
            break;
          // сумирование для столбца всего/более 60 лет
          case '3': case '7': case '11':
            $('#t' + t + '_r' + r + '_c11').html(
		      (parseInt($('#t' + t + '_r' + r + '_c3').val()) + parseInt($('#t' + t + '_r' + r + '_c7').val()))||
		      (parseInt($('#t' + t + '_r' + r + '_c3').html()) + parseInt($('#t' + t + '_r' + r + '_c7').html()))||
		      0);
		    break;
        }
        // суммирование для столбца всего/всего
        $('#t' + t + '_r' + r + '_c12').html(parseInt($('#t' + t + '_r' + r + '_c9').html()) + parseInt($('#t' + t + '_r' + r + '_c10').html()) + parseInt($('#t' + t + '_r' + r + '_c11').html()));
	    break;
	}
  }
  function sumCell (t, c){ // Строка "Итого"
    sum = 0;
	s = parseInt($('#t' + t + '_S').html());
	f = parseInt($('#t' + t + '_F').html());
	if ((t == '5000') || ( t == '5001') || (t == '6000')) {
	  if (t == '5000') {
	    s = 0
		f = 0
	  }
	  else 
	    f = f + 1
		  sum = parseInt($('#t' + t + '_r' + (s) + '_c' + c).val()||$('#t' + t + '_r' + (s) + '_c' + c).html()||0)
		  + parseInt($('#t' + t + '_r' + (2 + s) + '_c' + c).val()||$('#t' + t + '_r'   + (2 + s) + '_c' + c).html()||0)
          + parseInt($('#t' + t + '_r' + (28 + s) + '_c' + c).val()||$('#t' + t + '_r'  + (2 + s) + '_c' + c).html()||0) 
		  + parseInt($('#t' + t + '_r' + (30 + s) + '_c' + c).val()||$('#t' + t + '_r' + (32 + s) + '_c' + c).html()||0)
		  + parseInt($('#t' + t + '_r' + (34 + s) + '_c' + c).val()||$('#t' + t + '_r' + (34 + s) + '_c' + c).html()||0)
		  + parseInt($('#t' + t + '_r' + (36 + s) + '_c' + c).val()||$('#t' + t + '_r' + (38 + s) + '_c' + c).html()||0)
		  + parseInt($('#t' + t + '_r' + (40 + s) + '_c' + c).val()||$('#t' + t + '_r' + (40 + s) + '_c' + c).html()||0)
		  + parseInt($('#t' + t + '_r' + (53 + s) + '_c' + c).val()||$('#t' + t + '_r' + (44 + s) + '_c' + c).html()||0)
		  + parseInt($('#t' + t + '_r' + (57 + s) + '_c' + c).val()||$('#t' + t + '_r' + (57 + s) + '_c' + c).html()||0)
		  + parseInt($('#t' + t + '_r' + (62 + s) + '_c' + c).val()||$('#t' + t + '_r' + (63 + s) + '_c' + c).html()||0)
		  + parseInt($('#t' + t + '_r' + (66 + s) + '_c' + c).val()||$('#t' + t + '_r' + (66 + s) + '_c' + c).html()||0)
	}
	else
	  for (var i = s; i <= f; i++) {
	    sum = sum + parseInt($('#t' + t + '_r' + i + '_c' + c).val()||$('#t' + t + '_r' + i + '_c' + c).html()||0);
	  }
	$('#t' + t + '_rS_c' + c).html(sum);
  }
  $('input').blur ( function () {
    pole = $(this).attr('name').split('_');
	if ((pole[0].slice(1) == 1000) || (pole[0].slice(1) == 4000) || (pole[0].slice(1) == 5000) || (pole[0].slice(1) == 5001) || (pole[0].slice(1) == 6000)) 
	  calCell(pole[0].slice(1), pole[1].slice(1), pole[2].slice(1)); 
	if ((pole[0].slice(1) == 1000) || (pole[0].slice(1) == 5000) || (pole[0].slice(1) == 5001) || (pole[0].slice(1) == 6000)) {
	  sumCell(pole[0].slice(1), pole[2].slice(1));
	  if ((pole[0].slice(1) == 5000) || (pole[0].slice(1) == 5001) || (pole[0].slice(1) == 6000)) 
	    calCell(pole[0].slice(1), 'S', pole[2].slice(1)); 
	}
  })


    function getSumCell (t, c){ // Строка "Итого"
    sum = 0;
	s = parseInt($('#t' + t + '_S').html());
	f = parseInt($('#t' + t + '_F').html());
	if ((t == '5000') || ( t == '5001') || (t == '6000')) {
	  if (t == '5000') {
	    s = 0
		f = 0
	  }
	  else 
	    f = f + 1
	  sum = parseInt($('#t' + t + '_r' + (s) + '_c' + c).val()||$('#t' + t + '_r' + (s) + '_c' + c).html()||0)
		  + parseInt($('#t' + t + '_r' + (2 + s) + '_c' + c).val()||$('#t' + t + '_r'   + (2 + s) + '_c' + c).html()||0)
          + parseInt($('#t' + t + '_r' + (28 + s) + '_c' + c).val()||$('#t' + t + '_r'  + (2 + s) + '_c' + c).html()||0) 
		  + parseInt($('#t' + t + '_r' + (30 + s) + '_c' + c).val()||$('#t' + t + '_r' + (32 + s) + '_c' + c).html()||0)
		  + parseInt($('#t' + t + '_r' + (34 + s) + '_c' + c).val()||$('#t' + t + '_r' + (34 + s) + '_c' + c).html()||0)
		  + parseInt($('#t' + t + '_r' + (36 + s) + '_c' + c).val()||$('#t' + t + '_r' + (38 + s) + '_c' + c).html()||0)
		  + parseInt($('#t' + t + '_r' + (40 + s) + '_c' + c).val()||$('#t' + t + '_r' + (40 + s) + '_c' + c).html()||0)
		  + parseInt($('#t' + t + '_r' + (53 + s) + '_c' + c).val()||$('#t' + t + '_r' + (44 + s) + '_c' + c).html()||0)
		  + parseInt($('#t' + t + '_r' + (57 + s) + '_c' + c).val()||$('#t' + t + '_r' + (57 + s) + '_c' + c).html()||0)
		  + parseInt($('#t' + t + '_r' + (62 + s) + '_c' + c).val()||$('#t' + t + '_r' + (63 + s) + '_c' + c).html()||0)
		  + parseInt($('#t' + t + '_r' + (66 + s) + '_c' + c).val()||$('#t' + t + '_r' + (66 + s) + '_c' + c).html()||0)
	}
	else
	  for (var i = s; i <= f; i++) {
	    sum = sum + parseInt($('#t' + t + '_r' + i + '_c' + c).val()||$('#t' + t + '_r' + i + '_c' + c).html()||0);
	  }
	return sum;
  }
  
  function valCell (t, r, c) {
	    val = parseInt($('#t' + t + '_r' + r + '_c' + c).val());
	    return val;
  } 
  function valCelld (cell) {
	    val = parseInt($('#' + cell).val());
	    return val;
  } 
  function valCellPrev (t, r, c) {
	    val = parseInt($('#p' + t + '_r' + r + '_c' + c).val()||$('#p' + t + '_r' + r + '_c' + c).html()||0)
	    return val;
  } 
  function valCelldPrev (cell) {
	    val = parseInt($('#p' + cell).val());
	    return val;
  } 

  
  function valCell_Sum  (tab, startrow, col, num, step) {
      var val = 0;
	  for(var i = 0; i< num; i++) {
    	  val += valCell(tab, startrow + step*i ,col )
      }
	  return val;
  } 

  function validSubStr(tab, startrow, namerow, col, num, namerow1) {
    s =  valCell(tab, startrow , col)
    s1 = 0
    for(var i = 0; i< num; i++) {
      s1 += valCell(tab, startrow + 1 + i ,col )
    }
    if( s < s1 ) {
       $("#errmess").html("Ошибка 105. Таблица " + tab + ". Значение в строке " + namerow + " колонка " + (parseInt(col)+3) + " (" + s + ") должно быть больше или равно значения в подстроках (" +
       		           s1 + ")" + namerow1);           
       return false;
    }
    return true; 
  }
  
  function validate_form ( hndl ) {
	   /* проверка на уровне onsubmit формы - не используется сейчас*/
	    var attrtype = $(hndl).attr('type')
	    var attrname = $(hadl).attr('name')
	    
	    
	    if(valCell("1000","1","7") >= valCell("1000","1","8")) {
	    	$("#errmess").html("Ошибок нет")
	    	return true;
	    }
	    else {
	    	$("#errmess").html("Ошибка 1. Значение 1 этапа должно быть больше чем 2-го")
	    	return false;
	    }
	  
  }


  function validTab5_6() {
	  if( !validTab5x("5000"))
		  return false;
	  if( !validTab5x("5001"))
		  return false;
	  if( !validTab5x("6000"))
		  return false;
      return true;
  }
  
  function validTab5x( tab) {
	  var arrcol = ["1", "2", "3","4","5","6","7","13"];  /* Excel col = - 3  для каждого столбца таблицы tab */
    
      
      for (var j = 0; j < arrcol.length; j++) {
    	 rowS = parseInt($('#t' + tab + '_S').html());
/*1 - 1.1*/
  	     if (!validSubStr(tab, rowS + 0, "1", arrcol[j], 1, ""))
  	  	    return false;
/*2 - 2.1*/
  	     if (!validSubStr(tab, rowS + 2, "2", arrcol[j], 1, ""))
  	  	    return false;
/*2.1 - 2.2:2.13*/
         r = rowS;
         row = parseInt(r)  + 3;
  	     s =  valCell(tab, row, arrcol[j])
  	     s1	 = valCell_Sum  (tab, row+1, arrcol[j],12,2)
         if( s < s1 ) {
  	        $("#errmess").html("Ошибка 101. Таблица " + tab + ". Значение в строке 2.1 колонка " + (parseInt(arrcol[j])+3) + " (" + s + ") должно быть больше или равно суммы подстрок 2.2-2.13  (" +
  	        		           s1 + ")");           
  	        return false;
         }   
/*2.2 - 2.2.1 */
  	     if (!validSubStr(tab, rowS + 4, "2.2", arrcol[j], 1, ""))
  	  	    return false;
/*2.3 - 2.3.1 */
  	     if (!validSubStr(tab, rowS + 6, "2.3", arrcol[j], 1, ""))
  	  	    return false;
/*2.4 - 2.4.1 */
  	     if (!validSubStr(tab, rowS + 8, "2.4", arrcol[j], 1, ""))
  	  	    return false;
/*2.5 - 2.5.1 */
  	     if (!validSubStr(tab, rowS + 10, "2.5", arrcol[j], 1, ""))
  	  	    return false;
/*2.6 - 2.6.1 */
  	     if (!validSubStr(tab, rowS + 12, "2.6", arrcol[j], 1, ""))
  	  	    return false;
/*2.7 - 2.7.1 */
  	     if (!validSubStr(tab,rowS + 14, "2.7", arrcol[j], 1, ""))
  	  	    return false;
/*2.8 - 2.8.1 */
  	     if (!validSubStr(tab, rowS + 16, "2.8", arrcol[j], 1, ""))
  	  	    return false;
/*2.9 - 2.9.1 */
  	     if (!validSubStr(tab, rowS + 18, "2.9", arrcol[j], 1, ""))
  	  	    return false;
/*2.10 - 2.10.1 */
  	     if (!validSubStr(tab,rowS + 20, "2.10", arrcol[j], 1, ""))
  	  	    return false;
/*2.11 - 2.11.1 */
  	  	  if (!validSubStr(tab, rowS + 22, "2.11", arrcol[j], 1, ""))
  	  	    return false;
/*2.12 - 2.12.1 */
  	  	  if (!validSubStr(tab, rowS + 24, "2.12", arrcol[j], 1, ""))
  	  	    return false;
/*2.13 - 2.13.1 */
 	  	  if (!validSubStr(tab, rowS + 26, "2.13", arrcol[j], 1, ""))
  	  	    return false;
/*3 - 3.1 */
 	  	  if (!validSubStr(tab, rowS + 28, "3", arrcol[j], 1, ""))
  	  	    return false;
/*4 - 4.1:4.3 */
 	  	  if (!validSubStr(tab, rowS + 30, "4", arrcol[j], 3, ""))
  	  	    return false;
/*5 - 5.1 */
 	  	  if (!validSubStr(tab, rowS + 34, "5", arrcol[j], 1, ""))
  	  	    return false;
/*6 - 6.1:6.3 */
 	  	  if (!validSubStr(tab, rowS + 36, "6", arrcol[j], 3, ""))
  	  	    return false;
/*7 - 7.1:7.4.4 нелогично*/
         row = rowS + 40;
  	     s =  valCell(tab, row, arrcol[j])
  	     s1	 = valCell_Sum(tab,row+1, arrcol[j],2,1) + valCell_Sum(tab,row+7, arrcol[j],2,1) + valCell(tab, row+12, arrcol[j])
         if( s < s1 ) {
  	        $("#errmess").html("Ошибка 111. Таблица " + tab + ". Значение в строке 7 колонка " + (parseInt(arrcol[j])+3) + " (" + s + ") должно быть больше или равно суммы подстрок 7.1-7.4 и 7.4.4  (" +
  	        		           s1 + ")");           
  	        return false;
         }   
/*7.2 - 7.2.1:7.2.3 нелогично*/
         if (!validSubStr(tab, rowS + 42, "7.2", arrcol[j], 3, "(исключая стр 7.2.4))"))
  	  	    return false;
/*7.2.3 - 7.2.4 нелогично */
         if (!validSubStr(tab, rowS + 45, "7.2.3", arrcol[j], 1, "(имеется ввиду стр 7.2.4))"))
  	  	    return false;
   	     
/*7.4 - 7.4.1 */
        if (!validSubStr(tab, rowS + 48, "7.4", arrcol[j], 3, "(исключая стр 7.4.4))"))
	      return false;
/*8 - 8.1:8.3 */
  	    if (!validSubStr(tab, rowS + 53, "8", arrcol[j], 3, ""))
  	      return false;
/*9 - 9.1:9.4 */
  	    if (!validSubStr(tab, rowS + 57, "9", arrcol[j], 4, ""))
  	      return false;
/*10 - 10.1:10.3 */
	    if (!validSubStr(tab, rowS + 62, "10", arrcol[j], 3, ""))
  	      return false;
/*10 - мужчины */
  	    s =  valCell(tab, rowS + 64, arrcol[j])
        if((arrcol[j] == "1" || arrcol[j] == "2" || arrcol[j] == "3" ) && s > 0) {
   	       $("#errmess").html("Ошибка 112. Таблица " + tab + ". Значение в строке 10.2 колонка " + (parseInt(arrcol[j])+3) + " (" + s + ") должно быть 0 ");
          return false;
        }
        s =  valCell(tab, rowS + 65, arrcol[j])
        if((arrcol[j] == "1" || arrcol[j] == "2" || arrcol[j] == "3" ) && s > 0) {
           $("#errmess").html("Ошибка 113. Таблица " + tab + ". Значение в строке 10.3 колонка " + (parseInt(arrcol[j])+3) + " (" + s + ") должно быть 0 ");           
           return false;
        }

/*10 - женщины */
  	    s =  valCell(tab, rowS + 63, arrcol[j])
        if((arrcol[j] == "4" || arrcol[j] == "5" || arrcol[j] == "6" ) && s > 0) {
  	      $("#errmess").html("Ошибка 114. Таблица " + tab + ". Значение в строке 10.1 колонка " + (parseInt(arrcol[j])+3) + " (" + s + ") должно быть 0 ");           
          return false;
        }
      }        	 
	  return true;
  }
  
  function validTab7000() {
	  var s6000 =  getSumCell ("6000", "13");
	  var s7000_r6 = valCell("7000","257","1") + valCell("7000","257","2") + valCell("7000","257","3") + 
      valCell("7000","257","4") + valCell("7000","257","5") + valCell("7000","257","6");
	  
	  if( s6000 != s7000_r6 ) {
	    	$("#errmess").html("Ошибка 700. Таблица 7000. Сумма по строке 6 таблицы 7000 (" + s7000_r6 + ") должна быть равна общей сумме в таблице 6000 колонка 16 (" + s6000 + ")");
	    	return false;
	  }  
	  var s7004_sub = valCelld("t7004_r1") + valCelld("t7004_r2") + valCelld("t7004_r3") + valCelld("t7004_r4") + valCelld("t7004_r5") +
	                  valCelld("t7004_r6") + valCelld("t7004_r7") + valCelld("t7004_r8") 
	  var s7004 = valCelld("t7004")
	  if(s7004_sub > s7004) {
      	  $("#errmess").html("Ошибка 7004. Таблица 7000. Значение в поле 7004 (" + s7004 + ") должно быть больше или равно суммы его подстрок  (" + s7004_sub + ")");
	      return false;
	  }
	  var v7005 = valCelld("t7005")
	  if( v7005 != 0) {
      	  $("#errmess").html("Ошибка 7005.Таблица 7000. Значение в поле 7005 должно быть равно 0");
	      return false;
	  }
	  var v7006 = valCelld("t7006")
	  if( v7006 != 1) {
      	  $("#errmess").html("Ошибка 7006. Таблица 7000. Значение в поле 7006 должно быть равно 1");
	      return false;
	  }

	  var v7007 = valCelld("t7007")
	  if( !(v7007 == 1 || v7007 == 0) ) {
      	  $("#errmess").html("Ошибка 7005. Таблица 7000. Значение в поле 7007 должно быть равно 0 или 1");
	      return false;
	  }

	  var v7009 = valCelld("t7009")
	  var sotkaz =  getSumCell ("2000", "3") + getSumCell ("3000", "4");
	  if(v7009 != sotkaz) {
      	  $("#errmess").html("Ошибка 7009. Таблица 7000. Значение в поле 7009 (" + v7009 + ") должна быть равно общей сумме отказов (" + sotkaz + ") в табл.2000 столбец 5  и табл.3000 столбец 6");
	      return false;
	  }
     return true;
  }

  function validGroup(tab,tab7,row,row7, col, col7){ 
    s = valCell(tab, row, col)
    s1 = valCell_Sum(tab7, row7, col7, 4, 1)
	if(s != s1) {
       $("#errmess").html("Ошибка 1001. Таблица " + tab + ". Значение в строке " + (parseInt(row)) + " в колонке " + (parseInt(col)+2) + " (" + s + ") должно быть равна сумме строк 1-4 колонки "  +
    		              (parseInt(col7)+2) + " в табл." + tab7 + " (" + s1 + ")");           
      return false;
	}  
    return true;
  } 

  function validTab1000 (){ 
	  tab = "1000";
  	  rowS = parseInt($('#t' + tab + '_S').html());
	  tab7 = "7000";
  	  rowS7 = parseInt($('#t' + tab7 + '_S').html());
  	  
  	  
  	  s = valCell_Sum(tab, rowS, "7", 3, 1) + valCell_Sum(tab, rowS, "11", 3, 1);
  	  s1 = valCelld("t7001") + valCelld("t7002");
  	  if(s != s1) {
	     $("#errmess").html("Ошибка 1000. Таблица " + tab + ". Сумма по колонке 5" + " (" + s + ") должно быть равна сумме стр. 7001 + 7002  (" +
   	          s1 + ")");           
         return false;
  	  } 
/* по группам наcеления */
  	  if (!validGroup(tab, tab7, rowS, rowS7,"7","1"))
	  	    return false;
  	  if (!validGroup(tab, tab7, rowS+1, rowS7,"7","2"))
	  	    return false;
  	  if (!validGroup(tab, tab7, rowS+2, rowS7,"7","3"))
	  	    return false;
  	  if (!validGroup(tab, tab7,  rowS, rowS7,"11","4"))
	  	    return false;
	  if (!validGroup(tab, tab7, rowS+1, rowS7,"11","5"))
	  	    return false;
	  if (!validGroup(tab, tab7, rowS+2, rowS7,"11","6"))
	  	    return false;
      return true;       
  }

  function valid2000_1 (tab,rowS,i,sum_all) {
  	  s =  valCell(tab, rowS + i, "1") + valCell(tab, rowS + i, "2") + valCell(tab, rowS + i, "3");
	  num = i + 1;
	  if( num == 2 || num == 3 || num == 4 || num == 14 || num == 10 || num == 12 || num == 13 || num == 15 || num == 20) {
		  if(s != sum_all) {
		      $("#errmess").html("Ошибка 2003. Таблица " + tab + ". Сумма колонок 3,4,5 в строке " + num +  "(" + s + ") должна быть равна сумме колонки 5 табл. 1000  (" +
			    		 sum_all + ")");           
			  return false;
		  }
			  
	  }
	  else {
		  if(s > sum_all) {
		      $("#errmess").html("Ошибка 2003. Таблица " + tab + ". Сумма колонок 3,4,5 в строке " + num +  "(" + s + ") должна быть меньше или равна сумме колонки 5 табл. 1000  (" +
			    		 sum_all + ")");           
			  return false;
		  }
	  }
	  return true;
  } 

  function validTab2000(){ 
	  tab = "2000";
  	  rowS = parseInt($('#t' + tab + '_S').html());
	  tab1 = "1000";
  	  rowS1 = parseInt($('#t' + tab1 + '_S').html());
  	  
  	  sum_all = valCell_Sum(tab1, rowS1, "7", 3, 1) + valCell_Sum(tab1, rowS1, "11", 3, 1)
  	  s =  valCell(tab, rowS, "1")
  	  if(s != sum_all) {
	     $("#errmess").html("Ошибка 2001. Таблица " + tab + ". Значение в строке 1 кол. 3 " + " (" + s + ") должно быть равна сумме колонки 5 табл. 1000  (" +
	    		 sum_all + ")");           
         return false;
  	  } 
  	  s =  valCell(tab, rowS+ 19, "1")
  	  if(s != sum_all) {
	     $("#errmess").html("Ошибка 2002. Таблица " + tab + ". Значение в строке 20 кол. 3 " + " (" + s + ") должно быть равна сумме колонки 5 табл. 1000  (" +
	    		 sum_all + ")");           
         return false;
  	  } 
      for(var i = 1; i<=18; i++) {
        if(!valid2000_1(tab,rowS,i,sum_all))
        	return false;
      }
      return true;       
  }

  function valid3000_1 (tab,rowS,i) {
  	  s =  valCell(tab, rowS + i, "1")
  	  s1 =  valCell(tab, rowS + i, "2") + valCell(tab, rowS + i, "3") + valCell(tab, rowS + i, "4")
	  num = i + 1;
	  if(s < s1) {
	      $("#errmess").html("Ошибка 3001. Таблица " + tab + ". Сумма колонок 4,5,6 в строке " + num +  "(" + s1 + ") должна быть меньше или равна  колонки 3 (" +
			    		 s + ")");           
		  return false;
	  }
			  
	  return true;
  } 

  function validTab3000(){ 
	  tab = "3000";
  	  rowS = parseInt($('#t' + tab + '_S').html());
	  tab1 = "1000";
  	  rowS1 = parseInt($('#t' + tab1 + '_S').html());
  	  
  	  sum_all = valCell_Sum(tab1, rowS1, "7", 3, 1) + valCell_Sum(tab1, rowS1, "11", 3, 1)
      for(var i = 0; i<16; i++) {
        if(!valid3000_1(tab,rowS,i))
        	return false;
      }
/* 20 %*/
      s = valCell(tab, rowS + 13, "1"); 	  
	  if(s < sum_all * 20 / 100) {
        $("#errmess").html("Ошибка 3002. Таблица " + tab + ". Значение в строке 14 кол. 3 " +  "(" + s + ") должно быть больше или равно 20% от суммы колонки 5 табл. 1000  (" +
        		sum_all + ")");
      	return false;
	  }    
      s = valCell(tab, rowS + 14, "1"); 	  
	  if(s < sum_all * 20 / 100) {
	     $("#errmess").html("Ошибка 3003. Таблица " + tab + ". Значение в строке 15 кол. 3 " +  "(" + s + ") должна быть больше или равно 20% от суммы колонки 5 табл. 1000  (" +
	    		 sum_all + ")");           
      	return false;
	  }    
 /* 30 %*/
	  s = valCell_Sum(tab, rowS, "1", 16, 1)
	  if(s < sum_all * 30 / 100) {
        $("#errmess").html("Ошибка 3002. Таблица " + tab + ". Сумма по колонке 3 " +  "(" + s + ") должна быть больше или равно 30% от суммы колонки 5 табл. 1000  (" +
        		sum_all + ")");
      	return false;
	  }    

      return true;       
  }

  function isPrev() {
	  t = "1000"
  	  rowS = parseInt($('#t' + t + '_S').html());
	  i = 0;
	  c = 5;
      col = c.toString(10);		  
      p = valCellPrev(t, rowS, col) + valCellPrev(t, rowS + 1, col) + valCellPrev(t, rowS + 2, col);
	  if( p > 0)
		  return true;
	  else
	      return false;	  
  }
  
  function validPrev1000() {
	  t = "1000"
  	  rowS = parseInt($('#t' + t + '_S').html());
	  for(i = 0; i <3; i++) {
  	    for(c = 5; c <13; c++) {
	      col = c.toString(10);		  
          s = valCell(t, rowS + i, col); 	  
	      p = valCellPrev(t, rowS + i, col);
	      name = $('#t' + t + '_r' + (rowS + i) + '_name').html()
          if( c == 5 || c == 6 || c == 9 || c == 10) {
		      if(s != p) {
			        $("#errmess").html("Ошибка 1010. Таблица " + t + ". Значение в ячейке строка " + name + " колонка " + (c+2) +  "(" + s + ") " +
			        		"           должно быть равно значению предыдущего периода  (" +	p + ")");
			      	return false;
			  }
        	  
          }
          else {
		      if(s < p) {
			        $("#errmess").html("Ошибка 1011. Таблица " + t + ". Значение в ячейке строка " + name + " колонка " + (c+2) +  "(" + s + ") " +
			        		"           должно быть больше или равно значению предыдущего периода  (" +	p + ")");
			      	return false;
			  }
          }    
  	    }  
	  }  
	  return true;
  }

  function showBorder(tab, row, col, mode) {
     if( !mode)
	     $('#t' + tab + '_r' + row + '_c' + col).addClass('errmess');
	 else   
	     $('#t' + tab + '_r' + row + '_c' + col).removeClass('errmess');
 	  
  }

  function validPrev2_7(t,num_row, cols) {
  	  rowS = parseInt($('#t' + t + '_S').html());
	  for(i = 0; i <=num_row; i++) {
	    for (var j = 0; j < cols.length; j++) {
	      c = cols[j];	
	      col = cols[j].toString(10);		  
          s = valCell(t, rowS + i, col); 	  
	      p = valCellPrev(t, rowS + i, col);
	      name = $('#t' + t + '_r' + (rowS + i) + '_name').html()
	      if(s < p) {
                showBorder(t, rowS + i, col,false)
	    	    $("#errmess").html("Ошибка 2011. Таблица " + t + ". Значение в ячейке строка " + name + " колонка " + (c+2) +  " (" + s + ") " +
		        		"           должно быть больше или равно значению предыдущего периода  (" +	p + ")");
		      	return false;
		  }
	      else 
              showBorder(t, rowS + i, col,true)
  	    }  
	  }  
	  return true;
  }
  
  
  
  function isValid (){ 
   /* alert("Hi there! val=" + valCell("1000","1","7"));*/
	   if( !validTab1000() ) return false;
	   if( !validTab2000() ) return false;
	   if( !validTab3000() ) return false;
	   if( !validTab2000() ) return false;
	   if( !validTab5_6() ) return false;
	   if( !validTab7000() ) return false;
  /* prev period по только 1000 и 2000 таблицы */
	   if(isPrev()) {
	     if( !validPrev1000() ) return false;
	     var cols = [1,2,3,4];
	     if( !validPrev2_7("2000", 20, cols) ) return false;
	   }
	   return true;       
  }
  
  
  $(document).ready ( function () {
    $('.cal',this).each ( function () {
	  pole = $(this).attr('id').split('_');
	  if (pole[1].slice(1) == 'S') sumCell(pole[0].slice(1), pole[2].slice(1));
	  else calCell(pole[0].slice(1), pole[1].slice(1), pole[2].slice(1));
	})
    $(document).ready ( function () { 
       $("#btnSend").bind("click",function(event){ 
 /*	   $("#btnTest").bind("click",function(event){ */
 		   return isValid(); 
 	   }); 
    })

  })
  
  $('.number').blur ( function() {
    if ($(this).val() == '') {$(this).val(0)} 
  })
 /*
  $('input^[type="number"]').blur ( function() {
    if ($(this).val() == '') {$(this).val(0)} 
  })
*/
 