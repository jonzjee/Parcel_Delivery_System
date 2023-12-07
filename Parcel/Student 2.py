from tabulate import tabulate

# Initial table
table_price = [
    ['Zone A', 'RM8.00', 'RM16.00', 'RM18.00'],
    ['Zone B', 'RM9.00', 'RM18.00', 'RM20.00'],
    ['Zone C', 'RM10.00', 'RM20.00', 'RM22.00'],
    ['Zone D', 'RM11.00', 'RM22.00', 'RM24.00'],
    ['Zone E', 'RM12.00', 'RM24.00', 'RM26.00']
]


# Function to add a new destination and its prices
def add_price(destination, below_1kg_price, between_1kg_3kg_price, above_3kg_price):
    table_price.append([destination, below_1kg_price, between_1kg_3kg_price, above_3kg_price])


# Adding a new destination
add_price('Zone F', 'RM13.00', 'RM26.00', 'RM28.00')


# Function to modify the price of parcels above 3kg
def modify_price(destination, new_above_3kg_price):
    for row in table_price:
        if row[0] == destination:
            row[-1] = new_above_3kg_price


# Function to delete the price for parcels above 3kg
def delete_price(destination):
    for row in table_price:
        if row[0] == destination:
            row[-1] = ''


# Function to check the price based on weight and destination
def check_price(destination, weight):
    for row in table_price:
        if row[0] == destination:
            if weight < 1:
                return row[1]
            elif 1 <= weight <= 3:
                return row[2]
            else:
                return row[3]
    return None


# Displaying the pricing table using tabulate
print("Current Pricing Table:")
headers = ['Destination', 'Weight below 1kg', 'Weight in between 1kg to 3kg', 'Weight above 3kg']
print(tabulate(table_price, headers=headers, tablefmt="grid"))

# Input for the user to modify the price for the weight above 3kg
modify_destination = input("\nEnter the destination to modify the price for parcels above 3kg: ")
new_price = input(f"Enter the new price for {modify_destination} (above 3kg): ")

# Modify the price for the specified destination above 3kg
modify_price(modify_destination, new_price)

# Displaying the updated pricing table using tabulate
print("\nUpdated Pricing Table:")
print(tabulate(table_price, headers=headers, tablefmt="grid"))

# Input from the user to delete the price for a destination above 3kg
price_to_remove = input("\nEnter the destination to delete the price for parcels above 3kg: ")

# Delete the price for the specified destination above 3kg
delete_price(price_to_remove)

# Displaying the updated pricing table using tabulate
print("\nUpdated Pricing Table:")
print(tabulate(table_price, headers=headers, tablefmt="grid"))

# Input from the user to check the price for a parcel
destination_to_check = input("\nEnter the destination to check the price: ")
weight_to_check = float(input("Enter the weight of the parcel: "))

# Check the price for the specified destination and weight
price = check_price(destination_to_check, weight_to_check)
if price:
    print(f"The price for the parcel to {destination_to_check} weighing {weight_to_check}kg is: {price}")
else:
    print("Invalid destination or weight for pricing.")