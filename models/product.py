class Product:

    def __init__(self, name, description, stock_quantity, buying_cost, selling_cost, manufacturer, id = None):
        self.name = name
        self.description = description
        self.stock_quantity = stock_quantity
        self.buying_cost = buying_cost
        self.selling_cost = selling_cost
        self.manufacturer = manufacturer
        self.id = id