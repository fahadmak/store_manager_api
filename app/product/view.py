from flask import Blueprint, jsonify, request, json

from app.model import Product, products
from app.validate import validate
product = Blueprint("product", __name__)


@product.route("/api/v1/products", methods=["POST"])
def add_product():
    data = request.json
    name = data.get("name")
    price = data.get("price")
    if not all([name, price]):
        return jsonify({"message": "please fill missing fields"}), 400
    productId = max([product.productId for product in products]) + 1 if products else 1
    product = Product(productId, name, price)
    products.append(product)
    return jsonify({"message": str(product)}), 201

