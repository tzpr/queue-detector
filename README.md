# detect change, predict queue


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
- Node.js installed (https://nodejs.org/en/)
- Python 3.x installed (https://www.python.org/downloads/)
- ngrok installed (https://ngrok.com/download)
- redis installed (https://redis.io/download)

#### Running
1. start ngrok (tunneling to access localhost from the Internet)

2. start redis (queue state cache)

3. start node app (API for slack)

4. start python app (image processing and queue prediction)

5. configure Slack app to communicate with node API 



 




