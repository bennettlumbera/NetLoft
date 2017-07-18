
//'use strict';

// var retail = angular.module("retail", []);

// angular.module('SampleApplication', [
// 	'appRoutes',
// 	'retail'
// ]);

var app = angular.module("app",["ngRoute"]);

app.config(["$routeProvider", function($routeProvider){
  $routeProvider
        .when("/retail", {
          templateUrl: "components/retail/partials/retail.html",
	        controller: "retail"
        });
		console.log("app.js: app.config was loaded")
}]);
