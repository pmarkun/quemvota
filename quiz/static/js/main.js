var COMPARA = [1,1,1,1,1,1,1,1,1,1]
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
		if (q < $(".questao").length) 
		{
			$(".questao").hide('slow');
			$("#q"+(q+1)).show('slow');
		}
		else {
			for (i=0;i<MEUS_VOTOS.length;i++) {
				if (MEUS_VOTOS[i] == COMPARA[i]) {
					s += 1;
				}
			}
			var semelhanca = s/MEUS_VOTOS.length;
			alert(semelhanca.toPrecision(2)*100 + "% de semelhança");
		}
	});
});
