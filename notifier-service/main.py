from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route('/notify', methods=['GET'])
def notify():
    # Simulate sending reminder
    return jsonify({"message": "Reminder sent!"})

@app.route('/health', methods=['GET'])
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)
