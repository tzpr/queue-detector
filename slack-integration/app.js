
const express = require('express');
const request = require('request');
require('dotenv').config() // read config data from .env

//Check https://api.slack.com/tutorials/tunneling-with-ngrok for more info

// Instantiates Express and assigns app variable to it
const app = express();

// Define a port we want to listen to
const PORT = 4390;

// Lets start server
app.listen(PORT, function () {
    //Callback triggered when server is successfully listening. Hurray!
    console.log("Example app listening on port " + PORT);
});

// This route handles GET requests to our root ngrok address and responds with the same "Ngrok is working message" we used before
app.get('/', function(req, res) { 
    res.send('Ngrok is working! Path Hit: ' + req.url);
});

// This route handles get request to a /oauth endpoint. We'll use this endpoint for handling the logic of the Slack oAuth process behind our app.
app.get('/oauth', function(req, res) {
    // When a user authorizes an app, a code query parameter is passed on the oAuth endpoint. If that code is not there, we respond with an error message
    if (!req.query.code) {
        res.status(500);
        res.send({"Error": "Looks like we're not getting code."});
        console.log("Looks like we're not getting code.");
    } else {
        // We'll do a GET call to Slack's `oauth.access` endpoint, passing our app's client ID, client secret, and the code we just got as query parameters.
        request({
            url: 'https://slack.com/api/oauth.access', //URL to hit
            qs: {  //Query string data
                code: req.query.code, 
                client_id: process.env.CLIENT_ID,
                client_secret: process.env.CLIENT_SECRET}, 
            method: 'GET', //Specify the method
        }, function (error, response, body) {
            if (error) {
                console.log(error);
            } else {
                res.json(body);

            }
        })
    }
});

// Route the endpoint that our slash command will point to and send back a simple response to indicate that ngrok is working
app.post('/command', function(req, res) {
     // TODO: call the python script
    res.send('Hello stranger! There might be some queue or then not...');
});