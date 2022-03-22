from flask import Blueprint, Flask, render_template, request

from repositories import manufacturer_repository
from repositories import product_repository
from models.product import Product

product_blueprint = Blueprint("tasks", __name__)

@product_blueprint.route("/products")
def products():
    products = product_repository.select_all()
    return render_template("product/index.html", all_products = products)

@product_blueprint.route("/")