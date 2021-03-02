class Invoice:

    def __init__(self):
        self.items = {}


    def addProduct(self, qnt, price, discount):
        self.items['qnt'] = qnt
        self.items['unit_price'] = price
        self.items['discount'] = discount

        return self.items


    def totalImpurePrice(self, products):
        total_impure_price = 0
        for k, v in products.items():
            total_impure_price += float(v['unit_price']) * int(v['qnt'])
        total_impure_price = round(total_impure_price, 2)
        return total_impure_price


    def totalDiscount(self, products):
        total_discount = 0
        for k, v in products.items():
            total_discount += (int(v['qnt']) * float(v['unit_price']) * float(v['discount'])) / 100
        total_discount = round(total_discount, 2)
        self.total_discount = total_discount
        return total_discount


    def totalPurePrice(self, products):
        total_pure_price = self.totalImpurePrice(products) - self.totalDiscount(products)
        return total_pure_price


    def inputAnswer(self, input_value):
        while True:
            userInput = input(input_value)
            if (userInput in ['y', 'n']):
                return userInput
            print('y or n! Try again.')


    def inputNumber(self, input_value):
        while True:
            try:
                userInput = float(input(input_value))
            except ValueError:
                print('Not a number! Try again.')
            else:
                return userInput


    def displayProducts(self, products):
        result = ''
        for k, v in products.items():
            result += 'Name: %s, Quantity: %s, Unit Price: %s, Discount: %s \n' % (k, v['qnt'], v['unit_price'], v['discount'])
        print(result)
        return result


    def editQuantity(self, products, product_name, new_qnt):
        if product_name in products.keys():
            products[product_name]['qnt'] = new_qnt
        print('Product {%s} quantity changed to %s' % (product_name, new_qnt))
        return products[product_name]['qnt']


    def editUnitPrice(self, products, product_name, new_price):
        if product_name in products.keys():
            products[product_name]['unit_price'] = new_price
        print('Product {%s} unit price changed to %s' % (product_name, new_price))
        return products[product_name]['unit_price']


    def editDiscount(self, products, product_name, new_discount):
        if product_name in products.keys():
            products[product_name]['discount'] = new_discount
        print('Product {%s} discount changed to %s' % (product_name, new_discount))
        return products[product_name]['discount']
