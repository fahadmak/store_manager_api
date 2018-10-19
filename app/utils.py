from app.models.model import products


def find_product(product_name):
    for product in products:
        if product.name == product_name:
            return True
    return False
