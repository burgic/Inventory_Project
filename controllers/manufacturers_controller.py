from flask import Blueprint, Flask, redirect, render_template, request
from models.manufacturer import Manufacturer

from repositories import manufacturer_repository
from repositories import product_repository
from models.product import Product
from models.manufacturer import Manufacturer

# manufacturer_blueprint = Blueprint("tasks", __name__)


# @manufacturer_blueprint.route("/new_manufacturer.html")
# def new_manufacturer():
#     manufacturers = manufacturer_repository.select_all()
#     products = product_repository.select_all()
#     return render_template("/new_manufacturer.html", title="New Manufacturer", manufacturers = manufacturers)

# @manufacturer_blueprint.route("/new_manufacturer")
# def create_manufacturer():
#     name = request.form['name']
#     location = request.form['location']
#     payment_days = request.form['payment_days']
#     payment_code = request.form['payment_code']

#     manufacturer = Manufacturer(name, location, payment_days, payment_code, id=None)
#     manufacturer_repository.save(manufacturer)
#     return redirect("/manufacturers")

