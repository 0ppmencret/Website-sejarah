from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()
app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET")

jwt = JWTManager(app)
limiter = Limiter(get_remote_address, app=app, default_limits=["100 per hour"])

@app.route("/token", methods=["POST"])
def get_token():
    username = request.json.get("username")
    if username == "leo":
        return jsonify(access_token=create_access_token(identity=username))
    return jsonify(msg="Unauthorized"), 401

@app.route("/secure", methods=["GET"])
@jwt_required()
@limiter.limit("10/minute")
def secure_data():
    return jsonify(data="Data rahasia sejarah terlindungi.")

if __name__ == "__main__":
    app.run(debug=True)
