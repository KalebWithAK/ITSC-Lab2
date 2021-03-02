from Invoice import Invoice

products = {}
total_amount = 0
repeat = ''

while True:
    product = input('What is your product: ')
    unit_price = Invoice().inputNumber('Please enter the unit price: ')
    qnt = Invoice().inputNumber('Please enter the quantity of the product: ')
    discount = Invoice().inputNumber('Discount percent (%): ')
    repeat = Invoice().inputAnswer('Another product? (y, n): ')
    result = Invoice().addProduct(qnt, unit_price, discount)
    products[product] = result
    if (repeat == 'n'):
        break

total_amount = Invoice().totalPurePrice(products)

print('Your total pure price is: %s' % total_amount)

#Invoice().displayProducts(products)
#Invoice().editProductName(products, input('Product to edit: '), input('New product name: '))
#Invoice().editQuantity(products, input('Product to edit: '), input('New quantity: '))

print(Invoice().editDiscount(products, 'Pen', 6))
