import requests
from requests.exceptions import *
import json
def fetch_from_HTTP_to_File():
    try:
        r = requests.get('https://dsdsdsfdsfdsfdsfdsf.cdcd')
        r.raise_for_status()
        return_list = r.text
        f = open("demofile2.txt", "w")
        f.write(return_list)
        f.close()
        return r.json()
    except ConnectionError as c:
        print("Connection Error Exception Occured")
        error_data = {"response": "error", "message": "Connection Not Established"}
        return json.dumps(error_data)
    except HTTPError as h:
        print("Bad Status Code")
        error_data = {"response": "error", "message": "Bad Status Code"}
        return json.dumps(error_data)
    except Timeout as t:
        print('Request timeout occured')
        error_data = {"response": "error", "message": "Request timeout occured"}
        return json.dumps(error_data)
    except TooManyRedirects as r:
        print('Too many redirects have occured')
        error_data = {"response": "error", "message": "Too many redirects have occured"}
        return json.dumps(error_data)


print(type(fetch_from_HTTP_to_File()))