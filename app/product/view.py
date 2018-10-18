from flask import Blueprint, jsonify, request, json

from app.model import Product, products
from app.validate import validate
from app.utils import find_product

product = Blueprint("product", __name__)


@product.route("/api/v1/products", methods=["POST"])
def add_product():
    """A method adds product instance to products list"""
    if request.content_type != "application/json":
        return jsonify({'message': "Invalid content type"}), 400
    data = request.json
    name = data.get("name")
    price = data.get("price")
    if not all([name, price]):
        return jsonify({"message": "please fill missing fields"}), 400
    valid = validate(name, price)
    if not valid:
        return jsonify({"message": "incorrect information"}), 400
    found_product = find_product(name)
    if found_product:
        return jsonify({"message": f"{name} already exists"}), 400
    productId = max([product.productId for product in products]) + 1 if products else 1     # create productId
    product = Product(productId, name, price)
    products.append(product)
    return jsonify({"message": str(product)}), 201


@product.route("/api/v1/products", methods=["GET"])
def get_all_products():
    """A method returns a products dictionary"""
    if request.content_type != "application/json":
        return jsonify({'message': "Invalid content type"}), 400
    if not products:
        return jsonify({"message": "There currently no products"}), 200
    all_products = [product.to_json() for product in products]
    return jsonify({"products": all_products}), 200


@product.route("/api/v1/products/<int:productId>", methods=["GET"])
def get_product_by_id(productId):
    """A method returns a product whose id is passed as an argument"""
    if request.content_type != "application/json":
        return jsonify({'message': "Invalid content type"}), 400
    product = [product.to_json() for product in products if product.productId == productId] if products else False
    if not product:
        error = {"message": f"product of ID {productId} does not exist"}
        return jsonify({"product": error}), 404
    product = product[0]
    return jsonify({"product": product}), 200

