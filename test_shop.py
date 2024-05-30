"""
Протестируйте классы из модуля homework/models.py
"""
import pytest
from models import Product, Cart
from pytest import raises


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        product.buy(50)
        assert product.quantity == 950

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        with pytest.raises(ValueError):
            product.buy(1001)
        assert product.quantity == 1000

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1100)
        assert product.quantity == 1000


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    @pytest.fixture
    def cart(self):
        return Cart()

    def test_add_product(self, cart):
        # Добавления продукта в корзину, когда продукт еще не в корзине
        product = Product("book", 100, "This is a book", 1000)
        cart.add_product(product, 50)
        assert cart.products[product] == 50

        # Добавления продукта в корзину, когда продукт уже в корзине
        product = Product("book", 100, "This is a book", 1000)
        cart.add_product(product, 50)
        assert cart.products[product] == 50

    def test_clear(self, cart):
        # очистка корзины, когда корзина не пуста
        cart.add_product(Product("book", 100, "This is a book", 1000), 50)
        cart.clear()
        assert cart.products == {}

        # очистка корзины, когда корзина пуста
        cart.clear()
        assert cart.products == {}

    def test_remove_product(self, cart):
        # Удаления продукта из корзины, когда remove_count не указан
        product = Product("book", 100, "This is a book", 1000)
        cart.add_product(product, 50)
        assert cart.products[product] == 50

        # Удаления продукта из корзины, когда remove_count меньше количества продукта
        cart.remove_product(product)
        assert product not in cart.products

    def test_del_product(self, cart):
        # Удаление продукта из корзины, когда remove_count больше количества продукта
        product = Product("book", 100, "This is a book", 1000)
        cart.add_product(product, 50)
        assert cart.products[product] == 50

        # Удаление продукта из корзины, когда remove_count больше количества продукта
        cart.remove_product(product, 10)
        assert cart.products[product] == 40

    def test_clear_cart(self, cart):
        # очистка корзины, когда корзина не пуста
        product1 = Product("book", 100, "This is a book", 1000)
        cart.add_product(product1, 50)
        assert cart.products[product1] == 50

        # очистка корзины, когда корзина пуста
        cart.clear()
        assert cart.products == {}

    def test_get_total_price(self, cart):
        # получения общей стоимости корзины, когда корзина пуста
        assert cart.get_total_price() == 0

        # получения общей стоимости корзины, когда корзина содержит продукты
        cart.add_product(Product("book", 100, "This is a book", 1000), 50)
        assert cart.get_total_price() == 5000

        # общая стоимость корзины, когда корзина содержит несколько продуктов
        cart.add_product(Product("pen", 50, "This is a pen", 100), 2)
        assert cart.get_total_price() == 5100

    def test_buy(self, cart):
        # покупки продуктов из корзины, когда в корзине достаточно продуктов
        cart.add_product(Product("book", 100, "This is a book", 1000), 50)
        cart.buy()
        assert len(cart.products) == 1

    def test_buy_cart_value_error(self, cart, product):
        # покупки продуктов из корзины, когда в корзине недостаточно продуктов
        cart.add_product(product, 10001)
        with pytest.raises(ValueError):
            cart.buy()