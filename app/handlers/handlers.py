from flask import jsonify, current_app
from ..services.inference_service import predict_image
from ..services.get_history import get_prediction_history
from werkzeug.datastructures import FileStorage
from bson import ObjectId
import datetime
import pytz

def format_timestamp_indonesia(dt_utc):
    bulan = [
        "Januari", "Februari", "Maret", "April", "Mei", "Juni",
        "Juli", "Agustus", "September", "Oktober", "November", "Desember"
    ]
    wib = pytz.timezone("Asia/Jakarta")
    dt_wib = dt_utc.replace(tzinfo=pytz.utc).astimezone(wib)
    return f"{dt_wib.day:02d} {bulan[dt_wib.month - 1]} {dt_wib.year} {dt_wib.strftime('%H:%M')} WIB"

def predict_handler(request):
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file: FileStorage = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    model = current_app.model
    result, confidence, suggestion = predict_image(model, file)

    timestamp = datetime.datetime.utcnow()
    db = current_app.db
    record = {
        "filename": file.filename,
        "result": result,
        "confidence": confidence,
        "suggestion": suggestion,
        "timestamp": timestamp
    }
    saved = db.insert_one(record)

    return jsonify({
        "id": str(saved.inserted_id),
        "timestamp": format_timestamp_indonesia(timestamp),
        "prediction": result,
        "confidence": confidence,
        "suggestion": suggestion
    }), 200

def get_predictions_handler():
    db = current_app.db
    history = get_prediction_history(db)

    result = []
    for pred in history:
        result.append({
            "id": str(pred["_id"]),
            "filename": pred.get("filename", ""),
            "result": pred.get("result", ""),
            "confidence": pred.get("confidence", 0.0),
            "suggestion": pred.get("suggestion", ""),
            "timestamp": format_timestamp_indonesia(pred.get("timestamp")) if pred.get("timestamp") else ""
        })

    return jsonify(result), 200
