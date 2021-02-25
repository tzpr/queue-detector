# detect change, predict queue

<img src="https://github.com/tzpr/queue-detector/blob/master/Screenshot-2.png" alt="Image of Coffee Assistant" width="650">


Components:

Redis
 - stores queue state 
 - https://redis.io/topics/quickstart

Node application server
 - integrates Slack channel to the system, receives messages from Slack
 - reads queue state from Redis cache
 - https://api.slack.com/tutorials/tunneling-with-ngrok
 - https://ngrok.com/
 
Python application
 - Running in Jetson Nano
 - predicts queue state from image
 - updates queue state to Redis cache

 
 
 
### Running on localhost

#### Prerequisites
- docker installed (https://www.docker.com/)
- redis installed `docker run -d -p 6060:6379 --name coffee-queue redis`
- ngrok installed (https://ngrok.com/download)
- Slack channel were app can be configured (https://api.slack.com/apps)

#### Running
1. start ngrok (provides tunneling to access localhost from the Internet) `ngrok http 4390`
2. start redis `docker start coffee-queue`
3. start slack-integration Node.js app `cd slack-integration && npm install && node app.js`
3. create and configure Slack app to communicate with node API \
(https://api.slack.com/tutorials/tunneling-with-ngrok)




