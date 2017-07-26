

app.factory("userFactory", function ($http, $location) {

  var factory = {};

  factory.register = function(){
      console.log("hit userFactory")
  };

  return factory;
});
