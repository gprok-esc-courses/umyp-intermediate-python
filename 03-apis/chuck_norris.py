import json
import requests

url = 'https://api.chucknorris.io/jokes/random'

response = requests.get(url)

print(response.text)

data = json.loads(response.text)

print(data)

print(data['value'])