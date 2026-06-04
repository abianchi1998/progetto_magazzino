#app.py definisce e configura l'applicazione che vogliamo creare, in questo caso crea 
# l'istanza di flask e di blueprint (crea dei collegamenti)

from flask import Flask, jsonify #è un formato di testo usato per scambiare dati, linguaggio universale 
from src.routes import products_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(products_bp)
    @app.route('/')
    def home():
        return jsonify({"Message": "Benvenuti nel magazzino dei videogiochi Nintendo!"}), 200 #indica la tipologia di errore 

    return app