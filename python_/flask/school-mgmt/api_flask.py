from flask import Flask, Response
import json

class ApiFlask(Flask):

    def make_response(self, result):
        # return Flask.make_response(self, result)
        result['message'] = "Flask working always"
        return Response(
            json.dumps(result),
            200,
            mimetype='application/json'
        )

