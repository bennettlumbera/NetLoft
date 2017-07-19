
//'use strict';

// var retail = angular.module("retail", []);

// angular.module('SampleApplication', [
// 	'appRoutes',
// 	'retail'
// ]);

var app = angular.module("app",["ngRoute", "ui.bootstrap"])

app.config(["$routeProvider", function($routeProvider){
	$routeProvider
        .when("/", {
          templateUrl: "partials/home.html",
	        controller: "homeController"
        })
        .when("/search", {
          templateUrl: "partials/search.html",
	        controller: "homeController"
        })
				.when("/login", {
					templateUrl: "partials/home.html",
					controller: "loginController"
				});

}]);
