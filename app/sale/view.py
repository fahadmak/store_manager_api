from flask import Blueprint, jsonify, request, json

from app.model import Sale, sales
from app.utils import find_product
sale = Blueprint('sale', __name__)


@sale.route("/api/v1/sales", methods=["POST"])
def add_sale():
    if request.content_type != "application/json":
        return jsonify({"error": "Invalid content type"}), 400
    data = request.json
    cart = data.get('cart')
    if not cart:
        return jsonify({"error": "please fill missing fields"}), 400
    if not isinstance(cart, dict):
        return jsonify({"error": "please input correct format like {'corn': 6000, 'fish': 12300}"}), 400
    cart_products = [product for product in cart]
    unavailable = [cart_product for cart_product in cart_products if find_product(cart_product) is False]
    if not unavailable:
        sold_id = max([sold.saleId for sold in sales]) + 1 if sales else 1
        sold = Sale(sold_id, cart)
        sales.append(sold)
        return jsonify({"message": str(sold)}), 201
    return jsonify({"error": f"{unavailable} products can not be found"}), 404


@sale.route("/api/v1/sales", methods=["GET"])
def get_all_sales():
    if not sales:
        return jsonify({"error": "They are currently no sales"}), 404
    json_sales = []
    for sold in sales:
        json_sales.append(sold.to_json())
    return jsonify({"sales": json_sales})

