app.controller("homeController", ['$scope', '$location', function($scope, $location){
  console.log("homeController here...")


  $scope.register = function(){
    console.log("first name = ", $scope.user.first_name)
    console.log("last name = ", $scope.user.last_name)
    console.log("email name = ", $scope.user.email)
    $location.url('/')
  }

}]);
