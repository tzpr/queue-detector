# detect change, predict queue


Components:

Redis (https://redis.io/topics/quickstart)
 - cache for queue state 

Node application server
 - integrates Slack channel to the system, receives messages from Slack
 - reads queue state from Redis cache
 - https://api.slack.com/tutorials/tunneling-with-ngrok
 - https://ngrok.com/
 
Python application
 - interprets queue state from images
 - updates queue state to Redis cache
 - http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html









 




