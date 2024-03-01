from flask_restful import Resource
from flask import request, make_response, jsonify
from ModelInterfaces.VertexInterface import VertexInterface


class VertexHandler(Resource):
    def __init__(self):
        self.__v_interface = VertexInterface()
        self.__request = None
        self.__response = None
        self.__prepared_response = None

    def post(self):
        self.__request = request.get_json()
        self.__response = self.__v_interface.make_vertex_request(self.__request['request'])
        self.__prepared_response = {'response': f'{self.__response.text}'}
        return make_response(jsonify(self.__prepared_response), 200)
