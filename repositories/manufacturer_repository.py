from db.run_sql import run_sql

from models.manufacturer import Manufacturer
from models.product import Product

import repositories.manufacturer_repository as manufacturer_repository

def save(manufacturer):
    sql = "INSERT INTO manufacturers (name, location, payment_days, payment_code) VALUES (%s, %s, %s, %s) RETURNING *"
    

# def save(manufacturer):

name, location, payment_days, payment_code