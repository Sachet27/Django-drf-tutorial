import requests

url= 'http://127.0.0.1:8000/api/products/create/'

args= {
    'title': 'Fanta lite',
    'content': 'can i confirm 1 fanta lite please brev?',
    'price': 150.00
}

res= requests.post(url= url, json= args)

print(res.json())