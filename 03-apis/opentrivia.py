import json
import requests
import html

url = 'https://opentdb.com/api.php?amount=10&type=multiple'

response = requests.get(url)
data = json.loads(response.text)
quiz = data['results']

for item in quiz:
    print(html.unescape(item['question']))


