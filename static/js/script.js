/*
    jQuery for MaterializeCSS initialization
*/

$(document).ready(function () {
    $(".sidenav").sidenav({edge: "right"});
    $('select').formSelect();
    $('.modal').modal();
    $('.carousel.carousel-slider').carousel({
		fullWidth: true,
		indicators: true,
	});
	setInterval(function () {
		$('.carousel').carousel('next');
	}, 4000);
});





