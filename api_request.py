import requests # Package allows you to send HTTP requests

base_url = 'http://127.0.0.1:5000/uppercase'

params = {'text': 'hello worlddddddd'}

response = requests.get(base_url, params=params)


print(response.json())
print(response.status_code)