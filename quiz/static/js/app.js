angular.module('quizapp', []);

angular.module('quizapp').factory('quiz', [
  function(){
    return {
      started: false,
      propostas: propostas,
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
            $scope.quiz.propostas[$scope.quiz.current].ementa + '. ' + simbolica,
            'Brazilian Portuguese Female',
            {onend: function(){$('.quiz-question .btn-concordo').eq($scope.quiz.current).click(); }, rate: 1.5}
          );
      };
      var simbolica = 'Favoráveis permaneçam como estão, contrários se mániféstem.';
      $scope.$watch('quiz.started', function(){
        if ($scope.quiz.started) {
          $scope.readout($scope.quiz.current);
        }
      });
      $scope.$watch('quiz.current', function(){
        if ($scope.quiz.current > 0) {
          $scope.readout($scope.quiz.current);
        }
      });
    }
  ]);
