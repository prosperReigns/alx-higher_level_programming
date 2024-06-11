$(function(){
	$.ajax({
		url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
		method: 'GET',
		success: function(data){
		data.result.forEach(function(movie){
			let Title = movie.title;
			let list = $("<li></li>").text(Title);
			$("UL#list_movies").append(list);
		});
		}
	});
});
