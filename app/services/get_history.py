def get_prediction_history(db):
    return list(db.find().sort("timestamp", -1))
