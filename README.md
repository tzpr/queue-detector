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
 - interprets queue state from images
 - updates queue state to Redis cache
 - http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html
 
 
 
### Running on localhost

#### Prerequisites
- docker installed (https://www.docker.com/)
- ngrok installed (https://ngrok.com/download)
- Slack channel were app can be configured (https://api.slack.com/apps)

#### Running
1. start ngrok (provides tunneling to access localhost from the Internet)

2. execute in root folder `docker-compose up`

3. create and configure Slack app to communicate with node API

 




