import requests

url= 'http://127.0.0.1:8000/api/products/create/'

result= requests.post(url= url, json= {'title': 'Kungfu Panda Sticker', 'content': 'Exactly as it says', 'price': 10.00})

print(result.json())