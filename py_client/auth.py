import requests
from getpass import getpass

def get_auth_token():
    endpoint = 'http://127.0.0.1:8000/auth/'

    username= input('Username: ')
    password= getpass()

    auth_response= requests.post(endpoint, json= {
        'username': 'sachet',
        'password': password
    })

    return auth_response

if __name__ == '__main__':
    print(get_auth_token().json()) 