console.log("Loaded /server/config/routes.js");

// var QuestionController = require("../controllers/questions");

module.exports = function (app) {

//mock api structure, factory.js --> --> Python

    app.get("localhost:8000/api/" /*controller*/)  // Controller get questions
    app.post("localhost:8000/api/login")  // Controller create questions
    app.get("localhost:8000/api/register") //get one question object from db
    app.post("localhost:8000/api/newPlace")  // Controller create questions
    app.post("localhost:8000/api/newTrip") //update like count
};
