import requests

try:
    r= requests.get('https://ipapi123.co/json')
except requests.exceptions.RequestException as err:
    print("Request exception found")
    #raise err
    
    
