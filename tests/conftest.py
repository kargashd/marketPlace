import pytest

from src.main import Product, Category

@pytest.fixture
def first_prod():
    """Фикстура для тестов класса первого продукта"""
    return Product(
        name = "Микроволновка",
        description = "Микроволновая печь, предназначенная для подогрева пищи",
        price = 26000,
        quantity = 7,
    )


@pytest.fixture
def second_prod():
    """Фикстура для теста класса второго продукта"""
    return Product(
        name = "Мультиварка",
        description = "Мультиварка, предназначенная для приготовления пищи",
        price = 23500,
        quantity = 4,
    )


@pytest.fixture
def first_category():
    """Фикстура для теста категории продуктов"""
    return Category(
        name = "Телевизоры",
        description = "Телевизоры - устройства для просмотра визуальной мультимедии",
        products = ["Samsung", "LG"]
    )
