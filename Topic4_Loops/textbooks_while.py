# while version textbook total program

total = 0
more_books = True

while more_books:
    book_price = float(input('Enter price of books $'))
    total = total + book_price
    any_more = input('Any more books? Enter "Y" for yes "N" for no. ')
    if any_more.upper()== 'N':
        more_books = False

print(f'The total of all the books is ${total}')
