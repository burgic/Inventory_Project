import pdb
from models.manufacturer import Manufacturer
from models.product import Product

import repositories.manufacturer_repository as manufacturer_repository
import repositories.product_repository as product_repository

product_repository.delete_all()
manufacturer_repository.delete_all()

manufacturer1 = Manufacturer("Jones' Cheese", "Cornwall", 30, "JCC")
manufacturer_repository.save(manufacturer1)
manufacturer2 = Manufacturer("Marvins Cheese Farm", "Restaurant at the Edge of the Universe", 42, "MTPA")
manufacturer_repository.save(manufacturer2)

print(manufacturer1.__dict__)
print(manufacturer2.__dict__)

print(manufacturer_repository.select_all())

product1 = Product("Guacamole Manchago", "Manchago made from Guacamole", 10, 15, 30, manufacturer1)
product_repository.save(product1)

product2 = Product("Zaphod's Brie", "Danger Sensing Cheese", 10, 20, 30, manufacturer2)
product_repository.save(product2)
