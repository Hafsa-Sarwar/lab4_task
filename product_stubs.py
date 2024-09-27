class Product:
  def __init__(self, name, amount, price):
      self.name = name
      self.amount = amount
      self.price = price

  def get_price(self, quantity):
      pass

  def make_purchase(self, quantity):
      pass


product = Product("Laptop", 20, 50000)

product.make_purchase(100)
product.make_purchase(-5)
product.make_purchase(0)

product1 = Product("Watch", 10, 2000)

product1.make_purchase(100)
product1.make_purchase(-5)
product1.make_purchase(0)
