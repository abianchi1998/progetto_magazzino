from flask import Flask, jsonify
from src.routes import products_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(products_bp)
    @app.route('/')
    def home():
        return jsonify({"Message": "Benvenuti nel magazzino dei videogiochi Nintendo!"}), 200

    return app