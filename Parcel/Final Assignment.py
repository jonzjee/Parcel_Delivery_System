from tabulate import tabulate

table_price = [
    ['Zone A', 'RM8.00', 'RM16.00'],
    ['Zone B', 'RM9.00', 'RM18.00'],
    ['Zone C', 'RM10.00', 'RM20.00'],
    ['Zone D', 'RM11.00', 'RM22.00'],
    ['Zone E', 'RM12.00', 'RM24.00']
]

def add_price(destination, below_1kg_price, between_1kg_3kg_price):
    table_price.append([destination, below_1kg_price, between_1kg_3kg_price])

add_price('Zone F', 'RM13.00', 'RM26.00')

print("Pricing Table:")
headers = ['Destination', 'Weight below 1kg', 'Weight in between 1kg to 3kg']
print(tabulate(table_price, headers=headers, tablefmt="grid"))
