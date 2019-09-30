/**
 * http://usejsdoc.org/
 */
$(function() {
	$('.form-group label').addClass('col-sm-2');
	$('.form-group input, .form-group textarea, .form-group select').addClass('form-control');
});

$(document).ready(function() {
    $("#datepicker").datepicker({
        minDate: 2,
        maxDate: "+10D",
        isRTL: true
    });

});