star_id = input('Please enter your starId:')

star_id_length = len(star_id)

if star_id:
    print('You have entered a starid')
else:
    print('You have not entered star id')

if star_id_length == 8:
    print('Your starId is the correct length')

elif star_id_length > 8:
    print('Your starID is too long')
else:
    print('Your starID is too short. ')