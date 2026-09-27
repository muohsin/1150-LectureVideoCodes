secret_password = 'Kittens'

password = input('Enter your password: ')

if password == secret_password:
    print('welcome, authorized user!')

else:
    print('wrong password!')