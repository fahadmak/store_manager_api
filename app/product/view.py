from flask import Blueprint, jsonify, request

from app.models.model import Product, products
from app.models.error_model import InvalidUsage, InternalServerError
from app.validate import validate
from app.utils import find_product


product = Blueprint("product", __name__)


@product.route("/api/v1/products", methods=["POST"])
def add_product():
    """A method adds product instance to products list"""
    if request.content_type != "application/json":
        raise InvalidUsage("Invalid content type", 400)
    data = request.json
    name = data.get("name")
    price = data.get("price")
    try:
        if not all([name, price]):
            raise InvalidUsage("please fill missing fields", 400)
        valid = validate(name, price)
        if not valid:
            raise InvalidUsage("incorrect information", 400)
        found_product = find_product(name)
        if found_product:
            raise InvalidUsage(f"{name} already exists", 400)
        item_id = max([item.productId for item in products]) + 1 if products else 1     # create productId
        item = Product(item_id, name, price)
        products.append(item)
        return jsonify({"message": str(item)}), 201
    except InternalServerError:
        raise InternalServerError


@product.route("/api/v1/products", methods=["GET"])
def get_all_products():
    """A method returns a products dictionary"""
    try:
        if not products:
            raise InvalidUsage("There currently no products", 200)
        all_products = [item.to_json() for item in products]
        return jsonify({"products": all_products}), 200
    except InternalServerError:
        raise InternalServerError


@product.route("/api/v1/products/<int:product_id>", methods=["GET"])
def get_product_by_id(product_id):
    """A method returns a product whose id is passed as an argument"""
    try:
        found_product = [item.to_json() for item in products if item.productId == product_id] if products else False
        if not found_product:
            raise InvalidUsage(f"product of ID {product_id} does not exist", 404)
        found_product = found_product[0]
        return jsonify({"product": found_product}), 200
    except InternalServerError:
        raise InternalServerError


@product.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@product.errorhandler(InternalServerError)
def internal_server_error():
    response = jsonify({"message": InternalServerError.message})
    response.status_code = InternalServerError.status_code
    return response

