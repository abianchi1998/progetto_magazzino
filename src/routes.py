from flask import Blueprint, jsonify, request
from src.handlers.product_handler import (
    get_all_products_handler,
    create_product_handler,
    update_product_handler,
    delete_product_handler
)

products_bp = Blueprint("products", __name__, url_prefix="/products")

# 1. GET
@products_bp.route('/read', methods=['GET'])
def get_products():
    prodotti = get_all_products_handler()
    return jsonify(prodotti), 200

# 2. POST
@products_bp.route('/create', methods=['POST'])
def create_product():
    data = request.get_json()
    risultato, status_code = create_product_handler(data)
    return jsonify(risultato), status_code

# 3. PUT
@products_bp.route('/update/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    risultato, status_code = update_product_handler(product_id, data)
    return jsonify(risultato), status_code

# 4. DELETE
@products_bp.route('/delete/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    risultato, status_code = delete_product_handler(product_id)
    return jsonify(risultato), status_code