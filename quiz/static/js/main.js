var MEUS_VOTOS = [];
var s = 0;
$(document).ready(function () {
	$(".seta").click(function (){
		$('html, body').animate({
    		scrollTop: $("#main").offset().top
		}, 1000);
	});

	$(".controle .btn").click(function (e){
		var q = Number($(e.currentTarget).data('questao'));
		var voto = $(e.currentTarget).data('voto')
		MEUS_VOTOS.push(voto);
		if (q < $(".questao").length) {
			$("#q"+(q+1)).show('slow', function ()
				{
					$("#q"+q).hide('slow');		
				});
			}
		else {
			window.location.href = "/resultado/"+MEUS_VOTOS.join("");
			}
	});
});
