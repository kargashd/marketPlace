import pytest

from src.main import Product, Category

def test_prod_init(first_prod, second_prod):
    """Тест на определение наличия корректных атрибутов"""
    assert first_prod.name == "Микроволновка"
    assert first_prod.description == "Микроволновая печь, предназначенная для подогрева пищи"
    assert first_prod.price == 26000
    assert first_prod.quantity == 7

    assert second_prod.name == "Мультиварка"
    assert second_prod.description == "Мультиварка, предназначенная для приготовления пищи"


def test_category_init(first_category):
    """Тест категорий продуктов"""
    assert first_category.name == "Телевизоры"
    assert first_category.description == "Телевизоры - устройства для просмотра визуальной мультимедии"
    assert first_category.products == ["Samsung", "LG"]


def test_total_categories_counter():
    """Тест счётчика количества категорий"""
    Category.category_count = 0
    category = Category("Тест", "Описание", [])
    assert Category.category_count == 1


def test_unique_products_counter():
    """Тест счётчика уникальных товаров"""
    Category.product_count = 0
    test_product = Product("Телефон", "Смартфон", 50000, 10)
    category = Category("Электроника", "Техника", [test_product])
    assert Category.product_count == 1
