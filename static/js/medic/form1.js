
  function valCell (r, c, p) {
    var p = p || false;
	(p) ? val = parseInt($('#prev_r' + r + '_c' + c).html()) : val = parseInt($('#r' + r + '_c' + c).val());
    return val;
  }
  
  function validCol4_6(row, col) {
    if (valCell(row, col) > valCell(row, col - 1))
	  $('#errmess').append('<p>Ошибка ' + row + '01. В строке ' + row + ' значение в колонке ' + (col - 1) + ' (' + valCell(row, col - 1) + ') должно быть больше либо равно значению колонки ' + col + ' (' + valCell(row, col) + ')</p>');
  }
  function validSum(row) {
    if (valCell(row, 3) < (valCell(row,4) + valCell(row,6)))
	  $('#errmess').append('<p>Ошибка ' + row + '02. В строке ' + row + ' сумма значений в колонках 4 и 6 (' + (valCell(row,4) + valCell(row,6)) + ') должно быть больше значения колонки 3 (' + valCell(row, 3) + ')</p>');
    if (valCell(row, 3) < (valCell(row, 8) + valCell(row, 9) + valCell(row, 10)))
	  $('#errmess').append('<p>Ошибка ' + row + '03. В строке ' + row + ' сумма значений в колонках 8, 9 и 10 (' + (valCell(row, 8) + valCell(row, 9) + valCell(row, 10)) + ') должно быть больше значения колонки 3 (' + valCell(row, 3) + ')</p>');
  }
  
  function validAug4_6(row, col) {  
  if ((valCell(row, col) - valCell(row, col, true)) > (valCell(row, col - 1) - valCell(row, col - 1, true)))
	  $('#errmess').append('<p>Ошибка ' + row + '11. В строке ' + row + ' прирост в колонке ' + (col - 1) + ' (' + (valCell(row, col - 1) - valCell(row, col - 1, true)) + ') меньше прироста в колонке ' + (col - 1) + ' (' + (valCell(row, col) - valCell(row, col, true)) + ')</p>');
  }
  function validAugSum(row) {
    if ((valCell(row, 3) - valCell(row, 3, true)) < (valCell(row, 4) + valCell(row, 6) - valCell(row, 4, true) - valCell(row, 6, true)))
	  $('#errmess').append('<p>Ошибка ' + row + '12. В строке ' + row + ' прирост в колонке 3 (' + (valCell(row, 3) - valCell(row, 3, true)) + ') меньше суммы прироста колонок 4 и 6 (' + (valCell(row, 4) + valCell(row, 6) - valCell(row, 4, true) - valCell(row, 6, true)) + ')</p>');
    if ((valCell(row, 3) - valCell(row, 3, true)) < (valCell(row, 8) + valCell(row, 9) + valCell(row, 10) - valCell(row, 8, true) - valCell(row, 9, true) - valCell(row, 10, true)))
	  $('#errmess').append('<p>Ошибка ' + row + '13. В строке ' + row + ' прирост в колонке 3 (' + (valCell(row, 3) - valCell(row, 3, true)) + ') меньше суммы прироста колонок 8, 9 и 10 (' + (valCell(row, 8) + valCell(row, 9) + valCell(row, 10) - valCell(row, 8, true) - valCell(row, 9, true) - valCell(row, 10, true)) + ')</p>');
  }
  
  function validPrev() {
    err = false;
    for (i = 1; i <= 4; i++) {
	  for (j = 3; j <= 10; j++)
	    if (valCell(i, j, true) > valCell(i,j)) {
		  err = true;
		  break;
		}
	  if (err) break;
	  }
	if (err) $('#errmess').append('<p>Ошибка 10. Значения текуще периода должны быть больше предыдущего (в строке ' + i + ' колонка ' + j + ')</p>')
	else 
	  for (i = 1; i <= 4; i++) 
	    if (i != 2) {
	      validAug4_6(i, 5);
	      validAug4_6(i, 7);
		  validAugSum(i);
	    }
  }
  
  function isValid() {
    $('#errmess').html('');
	validPrev();
	for (i = 1; i <= 4; i++) 
	  if (i != 2) {
	    validCol4_6(i, 5);
	    validCol4_6(i, 7);
		validSum(i);
	  }
	if ($('#errmess').html() != '') return false
  }
  
  
  