from flask_restful import Resource
from flask import request, make_response, jsonify
from BusinessLogicLayer.VertexService import VertexInterface
from PresentationLayer.Validator import Validator
from PresentationLayer.ResponseConfigurator import ResponseConfigurator


class VertexHandler(Resource):
    def __init__(self):
        self.__v_interface = VertexInterface()
        self.__validator = Validator()
        self.__request = None
        self.__response = None
        self.__prepared_response = None
        self.__response_configurator = ResponseConfigurator()

    def post(self):

        self.__request = request.get_json()
        print(self.__request)
        try:
            if not self.__validator.validate(request=self.__request)['validation_status']:
                self.__response = self.__v_interface.make_vertex_request(self.__request['request'])
                return self.__response_configurator.generate_response(self.__response.text, 200)
            else:
                return self.__response_configurator.generate_response(self.__validator.return_error_message(), 422)
        except Exception as ex:
            return self.__response_configurator.generate_response(ex, 400)
