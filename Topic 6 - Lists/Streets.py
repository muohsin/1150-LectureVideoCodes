
# Create a list containing three street names.
streets = ['Lake', 'Hennepin', 'Lyndale']

# Display the entire list.
print(streets)

# # Display the first street in the list.
# print(streets[0])
#
# # Display the second street in the list.
# print(streets[1])
#
# # Display the third street in the list.
# print(streets[2])
#
# # Change the first street name from Lake to Chicago.
# streets[0] = 'Chicago'
#
# # Display the list again to see the change.
# print(streets)
#
# # Change the second street name to a different name.
# streets[1] = 'Nicollet'
#
# # Display the updated list.
# print(streets)
#
# # Change the third street name to a different name.
# streets[2] = 'University'
#
# # Display the list one more time.
# print(streets)


# Create a list of streets where deliveries need to be made.
streets = ['Lake', 'Hennepin', 'Lyndale']

# Go through the list and print each street name.
for street in streets:
    print(street)

# Start a message that will contain all the delivery instructions.
delivery_instructions = 'Please deliver to these streets: '

# Add each street name to the delivery message.
# The '\n' moves the next street name onto a new line.
for street in streets:
    delivery_instructions = delivery_instructions + street + '\n'

# Display the complete delivery instructions.
print(delivery_instructions)



