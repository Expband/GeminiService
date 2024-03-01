from flask import Flask
from flask_restful import Api
from PresentationLayer.VertexHandler import VertexHandler

app = Flask(__name__)
api = Api(app)

api.add_resource(VertexHandler, '/vertex')

if __name__ == "__main__":
    app.run()
