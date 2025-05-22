from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy login route
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if data['username'] == 'admin' and data['password'] == 'admin':
        return jsonify({"message": "Login successful", "token": "dummy-jwt-token"})
    else:
        return jsonify({"message": "Invalid credentials"}), 401

@app.route('/health', methods=['GET'])
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
