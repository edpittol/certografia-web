$(function() {

	$(window).resize(resize);
	resize();

	function resize() {		
		$("textarea")
			.width($(window).width() - 46)
			.height($(window).height() - 75)
	}

	$('span').tooltip()

});