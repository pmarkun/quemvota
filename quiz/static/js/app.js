var utils = {
  score: function(vectorA, vectorB) {
    return vectorA.map(function(valueA, index){
      var valueB = vectorB[index];
      return valueA === valueB ? 1: 0;
    }).reduce(function(a,b){ return a+b; });
  }
};

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

$(document).ready(function(){
  if (annyang) {
    // Add our commands to annyang
    annyang.setLanguage('pt-BR');
    annyang.addCommands(commands);
    annyang.debug(true);
  }
});

angular.module('quizapp', []);

angular.module('quizapp').factory('quiz', [
  function(){
    return {
      started: false,
      propostas: propostas,
      parlamentares: parlamentares,
      current: 0,
      vote: function(index, value){
        this.propostas[index].uservote = value;
        this.current++;
      }
    };
  }
]);

angular.module('quizapp').
  controller('introCtrl', [
    '$scope', 'quiz',
    function($scope, quiz){
      $scope.quiz = quiz;
      $scope.start = function(){
        $scope.quiz.started = true;
        if (annyang) {
          annyang.start();
        } else {
          console.log('banana');
        }

        // $('html, body').animate({
        //   scrollTop: $('.quiz-ui').offset().top
        // }, 1000);
      };
    }
  ]);

angular.module('quizapp').
  controller('quizUICtrl', [
    '$scope', 'quiz',
    function($scope, quiz){
      $scope.quiz = quiz;
      $scope.readout = function(index){
          responsiveVoice.speak(
            $scope.quiz.propostas[$scope.quiz.current].ementa,
            'Brazilian Portuguese Female',
            {onend: function(){
              responsiveVoice.speak(simbolica, 'Brazilian Portuguese Female',
                {onend: function() {$('.quiz-question .btn-concordo').eq($scope.quiz.current).click();},
                rate :1.5});
            }, rate: 1.2}
          );
      };
      var simbolica = 'Favoráveis permaneçam como estão, contrários se mániféstem.';
      $scope.$watch('quiz.started', function(){
        if ($scope.quiz.started) {
          $scope.readout($scope.quiz.current);
        }
      });
      $scope.$watch('quiz.current', function(){
        if (($scope.quiz.current > 0) && ($scope.quiz.current+1 < $scope.quiz.propostas.length)) {
          $scope.readout($scope.quiz.current);
        }
      });
    }
  ]);

angular.module('quizapp').
  controller('resultsCtrl', [
  '$scope', 'quiz',
    function($scope, quiz){
      $scope.quiz = quiz;
      $scope.calculateScores = function(){
        var uservotes = $scope.quiz.propostas.map(function(proposta){ return proposta.uservote; });
        $scope.quiz.parlamentares.forEach(function(parlamentar){
          parlamentar.score = utils.score(uservotes, parlamentar.votos);
        });
      };
      $scope.$watch('quiz.current', function(){
        if ($scope.quiz.current === $scope.quiz.propostas.length){
          $scope.calculateScores();
          $scope.sorted = _.sortBy($scope.quiz.parlamentares, 'score').reverse().slice(0, 30);
        }
      });
    }
  ]);
