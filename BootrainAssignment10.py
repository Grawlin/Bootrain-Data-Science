class item:
    def __init__(self, item_name, price):
        self.item_name = item_name
        self.price = price

class customer:
    def __init__(self, customer_id, phone_number):
        self.customer_id = customer_id
        self.phone_number = phone_number
    
    def purchase(self, amount, price):
        return amount * price

item_quantity = 2
sku1 = item('Coca-Cola', 2.00)
sku2 = item('Sandwich', 10.00)
person1 = customer(1234, 41029785)

print('')
print('The customer N°id:', person1.customer_id, 'bought', item_quantity, sku1.item_name, 'for a total of',
person1.purchase(item_quantity, sku1.price), '\n')