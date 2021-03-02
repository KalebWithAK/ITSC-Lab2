import pytest
from Invoice import Invoice

@pytest.fixture()
def products():
    products = {
        'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5},
        'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10}
    }

    return products


@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice


def test_CanCalculateTotalImpurePrice(invoice, products):
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75


def test_CanCalculateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62


def test_CanCalculateTotalPurePrice(invoice, products):
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38


def test_CanDisplayProducts(invoice, products):
    invoice.displayProducts(products)
    assert invoice.displayProducts(products) == 'Name: Pen, Quantity: 10, Unit Price: 3.75, Discount: 5 \nName: Notebook, Quantity: 5, Unit Price: 7.5, Discount: 10 \n'


def test_CanEditQuantity(invoice, products):
    invoice.editQuantity(products, 'Pen', 11)
    assert invoice.editQuantity(products, 'Pen', 11) == 11


def test_CanEditUnitPrice(invoice, products):
    invoice.editUnitPrice(products, 'Pen', 4)
    assert invoice.editUnitPrice(products, 'Pen', 4) == 4


def test_CanEditDiscount(invoice, products):
    invoice.editDiscount(products, 'Pen', 6)
    assert invoice.editDiscount(products, 'Pen', 6) == 6