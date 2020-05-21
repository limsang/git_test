# -*- coding: utf-8 -*-
import os
from flask import Flask, jsonify, request, send_from_directory
import jsonify
import ssl

def get_test_api_server():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'hello world'

    @app.route("/test1")
    def test():
        return 'test1 page'


    @app.route('/test3')
    def environments():
        return jsonify({"language"})

    return app

def get_api_server():
    app = Flask(__name__, static_url_path='/static')
    # app = Flask(__name__)
    version = 'v1.0'

    info = {
        'name': 'eames test api',
        'version': version
    }

    @app.route("/info")
    def info():
        # return 'test1 page'
        return jsonify({'server info': info})

    @app.route('/')
    def root():
        return app.send_static_file('index.html')

    @app.route('/static/<path:path>')
    def send_static(path):
        return send_from_directory('static', path)

    @app.route('/recsys/api/', methods=['POST'])
    def get_personal_recommendation():
        try:
            """웹페이지에서 입력받은 UserId가 들어온다."""
            content = request.json
            userId = content['userId']
            print(userId)

            response = {
                'message': 'test is done perfectly'
            }

            return jsonify(response)
        except Exception as e:
            print("error", e)
    return app

def main():
    # apps = get_test_api_server()
    # apps.run(host='0.0.0.0', debug=False)
    #
    api_server = get_api_server()
    api_server.run(host='0.0.0.0', debug=True)

if __name__ == "__main__":
    main()