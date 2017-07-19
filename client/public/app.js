
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
				.when("/host", {
					templateUrl: "partials/host.html",
					controller: "hostController"
				})
				.when("/place", {
					templateUrl: "partials/place.html",
					controller: "placeController"
				})
				.when("/booking", {
					templateUrl: "partials/booking.html",
					controller: "bookingController"
				})
				;

}]);
