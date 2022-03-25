from cProfile import run
from db.run_sql import run_sql

from models.manufacturer import Manufacturer
from models.product import Product

import repositories.product_repository as product_repository

def save(manufacturer):
    sql = "INSERT INTO manufacturers (name, location, payment_days, payment_code) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [manufacturer.name, manufacturer.location, manufacturer.payment_days, manufacturer.payment_code]
    results = run_sql(sql, values)
    # print(results)
    id = results[0]['id']
    manufacturer.id = id
    return manufacturer

def select_all():
    manufacturers = []

    sql = "SELECT * FROM manufacturers"
    results = run_sql(sql)
    for row in results:
        manufactuer = Manufacturer(row['name'], row['location'], row['payment_days'], row['payment_code'], row['id'])
        manufacturers.append(manufactuer)
    return manufacturers

def delete_all():
    sql = "DELETE FROM manufacturers"
    run_sql(sql)

def select(id):
    manufacturer = None
    sql = "SELECT * FROM manufacturers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)
    print(result)
    # if result:
    item = result[0]
    
    manufacturer = Manufacturer(item['name'], item['location'], item['payment_days'], item['payment_code'], item['id'])
    return manufacturer