class Category:
    def __init__(self, name):
        self.name = name

    def show_category(self):
        print(f"Category: {self.name}")


class Product:
    def __init__(self, name, brand, price, quantity, category):
        self.name = name
        self.brand = brand
        self.price = price
        self.quantity = quantity
        self.category = category

    def show_info(self):
        print(f"Product: {self.name}")
        print(f"Brand: {self.brand}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")
        print(f"Category: {self.category.name}")

    def update_price(self, new_price):
        self.price = new_price
        print(f"New price for {self.name}: {self.price}")

    def sell_product(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
            print(f"Sold {amount} items of {self.name}")
            print(f"Remaining quantity: {self.quantity}")
        else:
            print("Not enough products in stock")


skincare = Category("Skincare")

cream = Product(
    "Face Cream",
    "Nivea",
    350,
    10,
    skincare
)

cream.show_info()

cream.update_price(400)

cream.sell_product(3)