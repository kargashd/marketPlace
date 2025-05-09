import pytest
from pycodestyle import update_counts
from unicodedata import category

from src.main import Category, Product


class TestProduct:
    """Тесты для класса Product"""

    def test_create_new_product(self):
        """Тест создания корректного товара через класс-метод"""
        test_data = {
            "name": "Телевизор",
            "description": "4K Screen",
            "price": "100000",
            "quantity": "5",
        }
        product = Product.new_product(test_data)

        assert product.name == "Телевизор"
        assert product.description == "4K Screen"
        assert product.price == 100000.0
        assert product.quantity == 5

    def test_new_product_missing_field(self):
        """Тест для проверки обязательного поля"""
        test_data = {
            "name": "Телевизор",
            "description": "4K Screen",
            "price": "100000",
            # Нет quantity
        }
        with pytest.raises(ValueError, match="Отсутствует обязательное поле: quantity"):
            Product.new_product(test_data)

    def test_new_product_invalid_type(self):
        """Тест на некорреткный тип данных"""
        test_data = {
            "name": "Телевизор",
            "description": "4K Screen",
            "price": "строка",
            "quantity": "5",
        }
        with pytest.raises(ValueError, match="Некорректный тип данных"):
            Product.new_product(test_data)

    def test_price_getter(self):
        """Тест геттера цены"""
        product = Product("Ноутбук", "Игровой", 50000, 7)
        assert product.price == 50000.0

    def test_quantity_getter(self):
        """Тест геттера количества товара"""
        product = Product("Ноутбук", "Игровой", 50000, 7)
        assert product.quantity == 7.0

    def test_price_setter(self):
        """Тест сеттера цены с корреткным значением"""
        product = Product("Ноутбук", "Игровой", 50000, 7)
        product.price = 50000
        assert product.price == 50000

    def test_price_setter_invalid(self):
        """Тест сеттера цены с некорректным значением"""
        product = Product("Ноутбук", "Игровой", 50000, 7)
        with pytest.raises(
            ValueError, match="Цена не должна быть нулевая или отрицательная"
        ):
            product.price = -20000


class TestCategory:
    """Тесты для класса Category"""

    @pytest.fixture
    def sample_products(self):
        """Фикстура с тестовыми товарами"""
        return [
            Product("Samsung", "4K Screen", 100000, 5),
            Product("LG", "4K HDR", 80000, 7),
        ]

    def test_products_getter(self, sample_products):
        """Тест геттера products"""
        category = Category("Телевизоры", "Современные модели", sample_products)
        products_str = category.products

        assert "Samsung,100000 руб, Остаток: 5" in products_str
        assert "LG,80000 руб, Остаток: 7" in products_str

    def test_add_products_valid(self, sample_products):
        """Тест добавления корректного товара"""
        category = Category("Телевизоры", "Современные модели", sample_products)
        new_product = Product("Xiaomi", "Smart TV", 30000, 8)

        initial_count = (
            len(category.products.split("\n")) - 1
        )  # Учитываем последнюю пустую строку
        category.add_products(new_product)
        updated_count = len(category.products.split("\n")) - 1

        assert updated_count == initial_count + 1
        assert "Xiaomi,30000 руб, Остаток: 8" in category.products

    def test_add_products_invalid(self, sample_products):
        """Тест на добавление неверного типа"""
        category = Category("Телевизоры", "Современные модели", sample_products)

        with pytest.raises(
            TypeError, match="Можно добавлять только объекты из Product"
        ):
            category.add_products("Не товар")

    def test_category_counter(self):
        """Тест счётчик категорий"""
        initial_count = Category.category_count
        category = Category("Новая", "Категория", [])
        assert Category.category_count == initial_count + 1

    def test_product_counter(self, sample_products):
        """Тест счётчика товаров"""
        initial_count = Category.product_count
        category = Category("Телевизоры", "Современные модели", sample_products)
        assert Category.product_count == initial_count + len(sample_products)
