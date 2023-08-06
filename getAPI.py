import requests
import logging
logging.basicConfig(filename="APIfetcherror.log", format='%(asctime)s %(message)s',encoding='utf-8',level=logging.ERROR)

def get_api():
    try:
        response = requests.get('https://ipapi.co/json')
        response=response.json()
        location_data = {
        "ip": response.get("ip"),
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name"),
        "time zone": response.get("timezone")
        }
        
        return location_data
    except requests.exceptions.RequestException as err:
        print("Request exception found")
        logging.error(err)
        return 0
        
        
        
    

print(get_api())
                