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
			$("#q"+q).hide('slow');
			window.location.href = "/resultado/"+MEUS_VOTOS.join("");
			}
	});


	if (annyang) {
	          // Let's define our first command. First the text we expect, and then the function it should call
	          var commands = {
	            'pela família meu voto É sim': function() {
	              $('.btn-concordo:visible').click();
	            },
	            'pela família voto É sim': function() {
	              $('.btn-concordo:visible').click();
	            },
	            'meu voto é sim': function() {
	              $('.btn-concordo:visible').click();
	            },
	            'Meu voto é não': function() {
	              $('.btn-discordo:visible').click();
	            },
	            'é golpe': function() {
	              $('.btn-discordo:visible').click();
	            }
	          };

	          // Add our commands to annyang
	          annyang.setLanguage('pt-BR')
	          annyang.addCommands(commands);
	          annyang.debug(true);

	          // Start listening. You can call this here, or attach this call to an event, button, etc.
	          $("#bigredbtn").click(function (){
	          	annyang.start();
	          });
	          
	        }
});
