class Product:
    """Класс, содержащий в себе информацию о товаре"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса. Задаем значение атрибутам экземпляра товара"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс, содержащий в себе информацию о категориях товара"""

    name: str
    description: str
    __products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """Метод для инициализации категории, задаем значение атрибутам категории товара"""
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)



    def add_products(self, product: Product):
        """Добавляет товар Product в приватный список __product"""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты из Product")
        self.__products.append(product)
        Category.product_count += 1






