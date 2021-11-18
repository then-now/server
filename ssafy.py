import requests
from pprint import pprint

response = requests.get('http://127.0.0.1:8000/movies/13/')
pprint(response.json())
