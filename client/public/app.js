
//'use strict';

// var retail = angular.module("retail", []);

// angular.module('SampleApplication', [
// 	'appRoutes',
// 	'retail'
// ]);

var app = angular.module("app",["ngRoute"]);

app.config(["$routeProvider", "$locationProvider", function($routeProvider, $locationProvider){
  $routeProvider
        .when("/", {
          templateUrl: "partials/home.html",
	        controller: "homeController"
        })
        .when("/search", {
          templateUrl: "partials/search.html",
	        controller: "homeController"
        });

	$locationProvider.html5Mode(true);
}]);
