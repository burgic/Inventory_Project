
from flask import Blueprint, Flask, redirect, render_template, request
from models.manufacturer import Manufacturer

from repositories import manufacturer_repository
from repositories import product_repository
from models.product import Product

product_blueprint = Blueprint("tasks", __name__)

@product_blueprint.route("/products")
def products():
    products = product_repository.select_all()
    return render_template("/products.html", all_products = products)

@product_blueprint.route("/new")
def new_task():
    # products = product_repository.select_all()
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
    return redirect('/products.html', product = product)

@product_blueprint.route("/manufacturers")
def manufacturers():
    manufacturers = manufacturer_repository.select_all()
    return render_template("/manufacturers.html", all_manufacturers = manufacturers)