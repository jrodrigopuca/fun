import json
import requests

url= "https://jsonplaceholder.typicode.com/todos/1"

respuesta = requests.get(url)
data=json.loads(respuesta.content)
print(data) # {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
