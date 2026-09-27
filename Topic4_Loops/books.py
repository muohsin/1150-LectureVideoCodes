# Ask the user how many books they need to buy for the semester.
number_of_books = int(input('How many books to buy? '))


# Start the total at 0 because we have not added any book prices yet.
total = 0


# Repeat the loop for each book the user said they need.
for book in range(number_of_books):

    # Ask the user for the price of each book.
    # float() allows the user to enter prices with decimals.
    book_price = float(input('Enter book price in $ '))


    # Check if the book is free.
    # If the price is 0, let the user know they got a free book.
    if book_price == 0:
        print('Yay! Free book!')


    # Add the current book's price to the total.
    total = total + book_price


# Display the final total price after all book prices have been entered.
# The f-string lets us put the total directly inside the message.
print(f'The total price for all books is {total}')