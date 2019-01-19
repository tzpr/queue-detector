
from flask_restful import Resource, reqparse, abort
from flask import request


class HelloSpace(Resource):
    def get(self):
        '''
        Get a hello message
        ---
        responses:
          200:
            description: Message returned
        '''
        return {'message': 'Hello from space!'}