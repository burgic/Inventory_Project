
from flask import Blueprint, Flask, redirect, render_template, request
from models.manufacturer import Manufacturer

from repositories import manufacturer_repository
from repositories import product_repository
from models.product import Product
from models.manufacturer import Manufacturer

product_blueprint = Blueprint("products", __name__)

@product_blueprint.route("/products")
def products():
    products = product_repository.select_all()
    return render_template("/products.html", all_products = products)

@product_blueprint.route("/new")
def new_task():
    products = product_repository.select_all()
    manufacturers = manufacturer_repository.select_all()

    return render_template("/new.html", title='New Product', manufacturers = manufacturers)

@product_blueprint.route("/new", methods=['POST'])
def create_product():
    name = request.form ['name']
    description = request.form['description']
    stock_quantity = request.form['stock_quantity']
    buying_cost = request.form['buying_cost']
    selling_cost = request.form['selling_cost']
    manufacturer_id = request.form['manufacturer_id']
    manufacturer = manufacturer_repository.select(manufacturer_id)
    product = Product(name, description, stock_quantity, buying_cost, selling_cost, manufacturer)
    product_repository.save(product)
    return redirect("/products")

@product_blueprint.route("/products/<id>", methods=['GET'])
def show_product(id):
    product = product_repository.select(id)
    return render_template('/products/<id>/show.html', product = product)

@product_blueprint.route("/products/<id>", methods=['POST'])
def update_product(id):
    name = request.form ['name']
    description = request.form['description']
    stock_quantity = request.form['stock_quantity']
    buying_cost = request.form['buying_cost']
    selling_cost = request.form['selling_cost']
    manufacturer_id = request.form['manufacturer_id']

    product = Product(name, description, stock_quantity, buying_cost, selling_cost, manufacturer_id)
    product_repository.update(product)
    return redirect('/products', product = product)

@product_blueprint.route("/manufacturers")
def manufacturers():
    manufacturers = manufacturer_repository.select_all()
    return render_template("/manufacturers.html", all_manufacturers = manufacturers)

@product_blueprint.route("/new_manufacturer")
def new_manufacturer():
    manufacturers = manufacturer_repository.select_all()
    products = product_repository.select_all()
    return render_template("/new_manufacturer.html", title="New Manufacturer", manufacturers = manufacturers)

@product_blueprint.route("/new_manufacturer")
def create_manufacturer():
    name = request.form.get['name']
    location = request.form.get['location']
    payment_days = request.form.get['payment_days']
    payment_code = request.form.get['payment_code']

    manufacturer = Manufacturer(name, location, payment_days, payment_code, id=None)
    manufacturer_repository.save(manufacturer)
    return redirect("/manufacturers")
