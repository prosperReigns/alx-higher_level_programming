$(function(){
	$.ajax({
		url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
		method: 'GET',
		success: function(data){
			const greet = data.hello;
			$("DIV#hello").text(greet);
		}
	});
});
