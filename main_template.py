from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flasgger import Swagger # This package/library is responsible for building out the api docs utilized in this repo

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

class UppercaseText(Resource):

    def get(self):
        """
        This method responds to the GET request for this endpoint and returns the data in uppercase.
        ---
        tags:
        - Text Processing
        parameters:
            - name: text
              in: query
              type: string
              required: true
              description: The text to be converted to uppercase
        responses:
            200:
                description: A successful GET request
                content:
                    application/json:
                      schema:
                        type: object
                        properties:
                            text:
                                type: string
                                description: The text in uppercase
        """
        text = request.args.get('text')

        return jsonify({"text": text.upper()})

class ProcessText(Resource):
    def get(self):
        """
        This method responds to the GET request for this endpoint and processes the text based on parameters.
        ---
        tags:
        - Text Processing
        parameters:
            - name: text
              in: query
              type: string
              required: true
              description: The text to be processed
            - name: duplication_factor
              in: query
              type: integer
              required: false
              description: The number of times to repeat the text
            - name: capitalization
              in: query
              type: string
              required: false
              enum: [UPPER, LOWER, None]
              description: The capitalization style to apply (UPPER, LOWER, or None)
        responses:
            200:
                description: A successful GET request
                content:
                    application/json:
                      schema:
                        type: object
                        properties:
                            text:
                                type: string
                                description: The processed text
        """
        text = request.args.get('text')
        duplication_factor = request.args.get('duplication_factor', default=1, type=int)
        capitalization = request.args.get('capitalization', default=None, type=str)

        if not text:
            return jsonify({"error": "Text parameter is required"}), 400
        
        # Apply duplication
        text = text * duplication_factor
        
        # Apply capitalization
        if capitalization == "UPPER":
            text = text.upper()
        elif capitalization == "LOWER":
            text = text.lower()

        return jsonify({"text": text})

api.add_resource(ProcessText, "/process-text")
api.add_resource(UppercaseText, "/uppercase")

if __name__ == "__main__":
    app.run(debug=True)