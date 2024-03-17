from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from PresentationLayer.VertexHandler import VertexHandler

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)

api.add_resource(VertexHandler, '/vertex')

if __name__ == "__main__":
    app.run(port=5001)
