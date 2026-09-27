# Get the name of the item from the user
item_name = input('Enter name of item: ')

# Get the unit price and convert it to a decimal number
unit_price = float(input('Enter unit price of ' + item_name + ': '))

# Get the quantity of items sold and convert it to an integer
quantity = int(input('Enter quantity of ' + item_name + ' sold: '))

# Get the total of the price
total = unit_price * quantity

# Students receive 50% discount, so divide the total by 2
student_total = total / 2

# Calculate the number of letters in the item name
number_of_letters = len(item_name)

#display the sales information

print()
print(item_name + ' sales ')
print('Quantity sold: ' + str(quantity))
print('Unit price: $' + str(unit_price))
print('Total: $' + str(total))
print('Total price for a student: $' + str(student_total))
print(item_name + ' has', number_of_letters, 'letters')


