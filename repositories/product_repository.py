from db.run_sql import run_sql

from models.manufacturer import Manufacturer
from models.product import Product

def save(product):
    sql = "INSERT INTO products (name, description, stock_quantity, buying_cost, selling_cost, manufacturer_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [product.name, product.description, product.stock_quantity, product.buying_cost, product.selling_cost, product.manufacturer.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id
    return product

def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)

def select_all():
    products = []
    sql = "SELECT * FROM products"
    results = run_sql(sql)
    for row in results:
        product = Product(row['name'], row['description'], row['stock_quantity'], row['buying_cost'], row['selling_cost'], row['manufacturer'], row['id'])
        products.append(product)
    return products

def delete(id):
    sql = "DELETE FROM products WHERE id = %s"
    values = [id]
    run_sql(sql)

def update(product):
    sql = "UPDATE products SET (name, description, stock_quantity, buying_cost, selling_cost, manufacturer) = (%s, %s, %s, %s, %s %s) WHERE id =%s"
    values = [product.name, product.description, product.stock_quantity, product.buying_cost, product.selling_cost, product.manufacturer, product.id]
    run_sql(sql, values)

def products(product):
    products = []

    sql = "SELECT * FROM products WHERE product_id = %s"
    values = [product.id]
    results = run_sql(sql, values)
    for row in results:
        product = Product(row['name'], row['description'], row['stock_quantity'], row['buying_cost'], row['selling_cost'], row['manufacturer'], row['id'])
        products.append(product)
    return products

