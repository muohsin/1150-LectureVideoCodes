import requests


# try to get data from this website called (catfact.ninja/fact)
data = requests.get('https://catfact.ninja/fact').json()
print(data)

fact = data['fact']
print('A cat fact is: ' + fact)