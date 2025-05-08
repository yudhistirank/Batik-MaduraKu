from flask import Blueprint, request
from ..handlers.handlers import predict_handler, get_predictions_handler

bp = Blueprint("batik", __name__)

@bp.route("/", methods=["GET"])
def home():
    return "Batik MaduraKu API sudah ready!"

@bp.route("/predict", methods=["POST"])
def predict():
    return predict_handler(request)

@bp.route("/predicts", methods=["GET"])
def get_predictions():
    return get_predictions_handler()
