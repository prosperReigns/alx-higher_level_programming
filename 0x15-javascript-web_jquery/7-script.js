$(function(){
	$.ajax({
		url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
		method: 'GET',
		success: function(data){
			const character = data.name;
			$("DIV#character").text(character);
		}
	});
});
