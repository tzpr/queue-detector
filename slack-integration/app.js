
const express = require('express'); // https://www.npmjs.com/package/express
const request = require('request'); // https://www.npmjs.com/package/request
const redis = require("redis");     // https://github.com/NodeRedis/node_redis

require('dotenv').config()          // https://www.npmjs.com/package/dotenv


const redisClient = redis.createClient(process.env.REDIS_PORT, 
    process.env.REDIS_HOST);

// https://nodejs.org/api/util.html#util_util_promisify_original
const {promisify} = require('util');
const redisGetAsync = promisify(redisClient.get).bind(redisClient);

//Check https://api.slack.com/tutorials/tunneling-with-ngrok

// Instantiates Express and assigns app variable to it
const app = express();

// Define a port we want to listen to
const PORT = process.env.SLACK_INTEGRATION_API_PORT;

function getQueueState() {
    return redisGetAsync('queue_state').then(function(res) {
        return res;
    });
}

redisClient.on("error", function (err) {
    console.log("Error " + err);
});

// Lets start server
app.listen(PORT, function () {
    //Callback triggered when server is successfully listening. Hurray!
    console.log("App listening on port " + PORT);
});

// This route handles GET requests to our root ngrok address and responds with the same "Ngrok is working message" we used before
app.get('/', function(req, res) { 
    console.log('Hello from space! Ngrok is working!');
    res.send('Hello from space! Ngrok is working! Path Hit: ' + req.url);
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

// Route the endpoint that our slash command will point to
app.post('/command', function(req, res) {
    // ask queue state from redis
    getQueueState().then(function(state) {
        console.log('queue state from redis: ' + state);
        res.send(state);
    });
});