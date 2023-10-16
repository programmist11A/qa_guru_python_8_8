"""
Протестируйте классы из модуля models.py
"""
import pytest

from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture
def cart():
    return Cart()

class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(0) == True
        assert product.check_quantity(999) == True
        assert product.check_quantity(1000) == True
        assert product.check_quantity(1001) == False

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(1000)

        assert product.quantity == 0

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            assert product.buy(1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_add_in_cart(self, cart,  product):
        cart.add_product(product, 1)
        assert cart.products[product] == 1
        cart.add_product(product, 99)
        assert cart.products[product] == 100

    def test_remove_in_cart(self, cart, product):
        cart.add_product(product, 3)
        cart.remove_product(product, 3)

        assert product not in cart.products

        cart.add_product(product, 2)
        cart.remove_product(product, 5)

        assert product not in cart.products

    def test_clear(self, cart, product):
        cart.add_product(product, 1)
        cart.clear()

        assert product not in cart.products


    def test_get_total_price(self, cart, product):
        cart.add_product(product, 22)
        total_price = cart.get_total_price()

        assert total_price == 2200.0


    def test_buy(self, cart, product):
        product.quantity = 10
        cart.add_product(product, 5)
        cart.buy()

        assert product not in cart.products
        assert product.quantity == 5

        product.quantity = 3
        cart.add_product(product, 5)

        with pytest.raises(ValueError):
            cart.buy()
