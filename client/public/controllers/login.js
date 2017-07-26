



app.controller("loginController", ['$scope', '$location', 'userFactory', function($scope, $location, userFactory){
  console.log("loginController here...")


  $scope.register = function(){
    console.log("first name = ", $scope.user.first_name);
    console.log("last name = ", $scope.user.last_name);
    console.log("email name = ", $scope.user.email);
    userFactory.register();
    $scope.msg = "message test"
    modal.style.display = "none"
    $location.url('/search')
  }


}]);
