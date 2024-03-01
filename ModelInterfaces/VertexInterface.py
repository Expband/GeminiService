from Model.VertexModel import VertexModel


class VertexInterface:
    def __init__(self):
        self.v_model = VertexModel()
        self.chat = self.v_model.science_tutoring()
        self.parameters = None
        self.response = None


    def make_vertex_request(self, request: str):
        self.parameters = {
            "temperature": 0.7,  # Temperature controls the degree of randomness in token selection.
            "max_output_tokens": 256,  # Token limit determines the maximum amount of text output.
            "top_p": 0.95,
            # Tokens are selected from most probable to least until the sum of their probabilities equals the top_p value.
            "top_k": 40,  # A top_k of 1 means the selected token is the most probable among all tokens.
        }
        self.response = self.chat.send_message(request, **self.parameters)
        return self.response

