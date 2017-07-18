retail
    .controller('RetailController', ['$scope','$http', function($scope, $http) {
        $scope.message = "Hello World";
        
        var config = {
            headers : {
                'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8;'
            }
        };

		$http.get('http://127.0.0.1:8000/chains/', config)
        .success(function (data, status, headers, config) {
        	console.log(data);
        })
        .error(function (data, status, header, config) {
        	console.log(data);
        });

}]);