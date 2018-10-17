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
    valid = validate(name, price)
    if not valid:
        return jsonify({"message": "incorrect information"}), 400
    if name in [product.name for product in products]:
        return jsonify({"message": f"{name} already exists"}), 409
    productId = max([product.productId for product in products]) + 1 if products else 1
    product = Product(productId, name, price)
    products.append(product)
    return jsonify({"message": str(product)}), 201



@product.route("/api/v1/products", methods=["GET"])
def get_all_products():
    if products:
        all_products = json.dumps([product.to_json() for product in products])
        return jsonify({"products": all_products}), 200
    error = json.dumps({"message": "There currently no products"})
    return jsonify(error), 200

