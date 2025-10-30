from flask import Flask, request, jsonify
import csv
from pathlib import Path
from datetime import datetime

app = Flask(__name__)

BASE = Path(__file__).resolve().parent
DATA_DIR = BASE / "data"
DATA_DIR.mkdir(exist_ok=True)
CSV_PATH = DATA_DIR / "sensor_data.csv"

if not CSV_PATH.exists():
    with CSV_PATH.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ts_iso", "device", "sound_raw", "sound_adj", "ts_ms_device"])

@app.route("/ingest", methods=["POST"])
def ingest():
    data = request.get_json(force=True, silent=True)
    if not data:
        return jsonify({"ok": False, "error": "no json"}), 400

    device = data.get("device", "unknown")
    sound_raw = data.get("sound_raw")
    sound_adj = data.get("sound_adj")
    ts_ms_device = data.get("ts_ms")

    ts_iso = datetime.utcnow().isoformat()

    with CSV_PATH.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([ts_iso, device, sound_raw, sound_adj, ts_ms_device])

    return jsonify({"ok": True}), 200

@app.route("/")
def index():
    return "ESP32 ingest API alive", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
