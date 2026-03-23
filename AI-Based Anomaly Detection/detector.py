from ai.model import predict

def detect_anomaly(features):
    result = predict([features])
    return "ANOMALY" if result[0] == -1 else "NORMAL"
