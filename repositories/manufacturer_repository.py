from db.run_sql import run_sql

from models.manufacturer import Manufacturer
from models.product import Product

import repositories.product_repository as product_repository

def save(manufacturer):
    sql = "INSERT INTO manufacturers (name, location, payment_days, payment_code) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [manufacturer.name, manufacturer.location, manufacturer.payment_days, manufacturer.payment_code]
    results = run_sql(sql, values)
    id = results[0]['id']
    manufacturer.id = id
    return manufacturer

def select_all():
    manufactuers = []

    sql = "SELECT * FROM manufacturers"
    results = run_sql(sql)
    for row in results:
        product = product_repository.select(row['product_id'])
        manufactuer = Manufacturer(row['name'], row['location'], row['payment_days'], row['completed'], row['id'])
        manufactuers.append(manufactuers)
    return manufactuers