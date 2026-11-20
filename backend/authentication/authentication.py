from rest_framework.authentication import TokenAuthentication as BaseTokenAuth 

class MyTokenAuthentication(BaseTokenAuth):
    keyword= 'Bearer'