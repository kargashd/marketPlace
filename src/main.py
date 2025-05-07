from colorama.ansi import clear_screen


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
        self.__price = price
        self.quantity = quantity


    @classmethod
    def new_product(cls, product_store: dict) -> 'Product':
        """Класс-метод для создания товара из словаря с параметрами класса Product"""
        try:
            return cls(
                name=str(product_store['name']),
                description=str(product_store['description']),
                price=float(product_store['price']),
                quantity=int(product_store['quantity'])
            )
        except KeyError as e:
            raise ValueError(f"Отсутсвует обязательное поле: {e.args[0]}")
        except (TypeError, ValueError) as e:
            raise ValueError(f"Некорректный тип данных: {e}")


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


    @property
    def products(self):
        """Геттер для вывода списка товаров"""
        prod_str = ''
        for prod in self.__products:
            prod_str += f'{prod.name},{prod.price} руб, Остаток: {prod.quantity}\n'
        return prod_str
