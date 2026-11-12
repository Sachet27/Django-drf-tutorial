import requests

url= 'http://127.0.0.1:8000/api/products/'

result= requests.get(url= url)

print(result.json())