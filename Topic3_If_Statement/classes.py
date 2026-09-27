# USING NESTED IF

csharp = input('Have you taken the c# programming class? Type "yes" if so: ')
java = input('Have you taken the java programming class? Type "yes" if so: ')

if csharp == 'yes' or java == 'yes':
    print('You can take IOS programming!')
else:
    print('Sorry, you are not eligible')
