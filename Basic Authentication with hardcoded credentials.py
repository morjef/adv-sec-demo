# Example 6: Basic Authentication with hardcoded credentials
import requests
def access_protected_resource():
    auth = ('admin', 'reallybadpassword')
    response = requests.get('http://protected.example.com', auth=auth)
    return response.text