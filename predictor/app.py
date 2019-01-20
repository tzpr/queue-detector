import os

from flask import Flask       # http://flask.pocoo.org/docs/1.0/quickstart/#quickstart
from flask import jsonify, render_template
from flask_restful import Api # https://flask-restful.readthedocs.io/en/latest/

from resources.hello import HelloSpace
from resources.detect import AnalyseImage, InitBaseImage

bind_port = int(os.environ['BIND_PORT'])


app = Flask(__name__)
api = Api(app)

# activate/register paths
api.add_resource(HelloSpace, '/hello')
api.add_resource(AnalyseImage, '/predict')
api.add_resource(InitBaseImage, '/init')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=bind_port)