import os
import random

from flask_restful import Resource, reqparse, abort
from flask import request
from redis import Redis

# connect to redis
redis = Redis(host=os.environ['REDIS_HOST'], port=os.environ['REDIS_PORT'])


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
        state = self.check_queue()
        return {'message': 'Hello from detector! ' + state}

    def analyze_queue_picture(self):
        # just some fake values
        if (random.randint(0, 10)) % 2 == 0:
            return 'queue'
        else:
            return 'no-queue'

    def check_queue(self):
        queue_state = self.analyze_queue_picture()
        print('Current queue state: ', queue_state)

        if redis.get('queue_state') is not queue_state:
            redis.set('queue_state', queue_state)
        return queue_state        