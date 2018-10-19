from flask import Blueprint, jsonify, request

from app.models.model import Sale, sales, products
from app.models.error_model import InvalidUsage, InternalServerError

from app.utils import find_product


sale = Blueprint('sale', __name__)


@sale.route("/api/v1/sales", methods=["POST"])
def add_sale():
    if request.content_type != "application/json":
        raise InvalidUsage("Invalid content type", 400)
    data = request.json
    cart = data.get('cart')
    try:
        if not cart:
            raise InvalidUsage("please fill missing fields", 400)
        if not isinstance(cart, dict):
            raise InvalidUsage("please input correct format like {'corn': 6000, 'fish': 12300}", 400)
        unavailable = [item for item in cart if item not in [product.name for product in products]]
        if not unavailable:
            sold_id = max([sold.saleId for sold in sales]) + 1 if sales else 1
            sold = Sale(sold_id, cart)
            sales.append(sold)
            return jsonify({"message": str(sold)}), 201
        raise InvalidUsage(f"{unavailable} products can not be found", 404)
    except InternalServerError:
        raise InternalServerError


@sale.route("/api/v1/sales", methods=["GET"])
def get_all_sales():
    try:
        if not sales:
            raise InvalidUsage("They are currently no sales", 404)
        json_sales = []
        for sold in sales:
            json_sales.append(sold.to_json())
        return jsonify({"sales": json_sales}), 200
    except InternalServerError:
        raise InternalServerError


@sale.route("/api/v1/sales/<int:sale_id>", methods=["GET"])
def get_sale_by_id(sale_id):
    try:
        for sold in sales:
            if sold.saleId == sale_id:
                return jsonify({"sale": sold.to_json()}), 200
        else:
            return jsonify({"error": f"Sale Record of ID {sale_id} does not exist"}), 404
    except InternalServerError:
        raise InternalServerError


@sale.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@sale.errorhandler(InternalServerError)
def internal_server_error():
    response = jsonify({"message": InternalServerError.message})
    response.status_code = InternalServerError.status_code
    return response
