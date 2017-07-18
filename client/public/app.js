
'use strict';

var retail = angular.module("retail", []);

// angular.module('SampleApplication', [
// 	'appRoutes',
// 	'retail'
// ]);

var app = angular.module("app",["ngRoute"]);

app.config(["$routeProvider", function($routeProvider){
  $routeProvider
        .when("/",{
          templateUrl:"retail/templates/retail.template"
        })
        .otherwise({
          redirect_to: "/"
        });

}]);
