from flask_restful import Resource, reqparse, abort
from flask import request

import redis
import time
import random


# connect to redis
# https://redis.io/topics/quickstart
# https://github.com/andymccurdy/redis-py
message_broker = redis.StrictRedis(host='localhost', port=6379, db=0)


class DetectChange(Resource):
    def get(self): 
        '''
        Analyze received image and update queue state to redis
        
        TODO: change to POST and handle the image payload

        ---
        responses:
          200:
            description: Message returned
        '''
        self.check_queue()
        return {'message': 'Hello from detector!'}

    def analyze_queue_picture(self):
        # just some fake values
        if (random.randint(0, 10)) % 2 == 0:
            return 'queue'
        else:
            return 'no-queue'

    def check_queue(self):
        queue_state = self.analyze_queue_picture()
        print('Current queue state: ', queue_state)

        if message_broker.get('queue_state') is not queue_state:
            message_broker.set('queue_state', queue_state)        