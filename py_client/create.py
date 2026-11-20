import requests
import auth #local package/file


url= 'http://127.0.0.1:8000/api/products/create/'

args= {
    'title': 'Rara 1 bakas',
    'content': 'Rara 1 bakas',
    'price': 500.00
}

auth_response = auth.get_auth_token()

if auth_response.status_code == 200:
    token= auth_response.json()['token']
    headers= {
        'Authorization': f'Bearer {token}'
    }

    res= requests.post(url= url, json= args, headers= headers)

    print(res.json())

