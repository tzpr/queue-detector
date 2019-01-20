import os
import random

from flask_restful import Resource, reqparse, abort
from flask import request
from redis import Redis

# connect to redis
redis = Redis(host=os.environ['REDIS_HOST'], port=os.environ['REDIS_PORT'])


class InitBaseImage(Resource):
    def get(self):
        '''
        Get base image if available
        '''

        return {'message': 'Init base image',
                'base_image': redis.get('base_image'),
                'info': 'Resource: InitBaseImage GET)'}


    def post(self):
        '''
        Init base image
        '''
        # TODO get img from POST request
        img = 'IMG from POST'

        redis.set('base_image', img)

        return {'message': 'Init base image',
                'base_image': img,
                'info': 'Resource: InitBaseImage POST'}        



class AnalyseImage(Resource):
    def get(self): 
        '''
        Just a test GET method for the Resource
        
        '''
        state = self.check_queue()
        return {'message': 'Test message from AnalyseImage',
                'state': state,
                'info': 'Resource: AnalyseImage GET)'}


    def post(self):
        '''
        Post image to be analyzed
        '''
        # TODO get img from POST request
        
        state = self.check_queue()
        return {'message': 'AnalyseImage',
                'state': state,
                'info': 'Resource: AnalyseImage POST'}


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