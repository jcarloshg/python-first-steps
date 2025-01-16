class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product: {self.name} - Price: {self.price}"


class CategoryProducts:

    def __init__(self, name, products):
        self.name = name
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    def print_products(self):
        for product in self.products:
            print(product)


laptop = Product("Laptop", 25000)
mouse = Product("Mouse", 1000)
smartPhone = Product("smartPhone", 6000)

office_category = CategoryProducts("Office", [laptop, mouse])
office_category.add_product(smartPhone)

office_category.print_products()
