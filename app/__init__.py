from flask import Flask, jsonify
from flask_cors import CORS
from .routes.routes import bp
from .services.load_model import load_model
from .exceptions.client_error import ClientError
from .exceptions.input_error import InputError
from asgiref.sync import async_to_sync
from pymongo import MongoClient
import os

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Koneksi ke MongoDB
    client = MongoClient(os.getenv("MONGODB_URI"))
    app.db = client["batikmadura"]["predictions"]

    # Load model langsung saat app dibuat
    app.model = async_to_sync(load_model)()

    app.register_blueprint(bp)

    # Error handling
    @app.errorhandler(ClientError)
    @app.errorhandler(InputError)
    def handle_input_related_errors(error):
        response = jsonify({
            "status": "fail",
            "message": error.message
        })
        response.status_code = error.status_code
        return response

    @app.errorhandler(Exception)
    def handle_generic_error(error):
        response = jsonify({
            "status": "fail",
            "message": str(error)
        })
        response.status_code = 500
        return response

    return app
