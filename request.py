import requests
from requests.exceptions import *
try:
    r = requests.get('https://api.ekomi.de/v3/getFeedback?auth=100809|3222cc91604a81845f8c3c0d7&type=json&range=6m')
    r.raise_for_status()
    return_list = r.text
    f = open("demofile2.txt", "w")
    f.write(return_list)
    f.close()
except ConnectionError as c:
    print("Connection Error Exception Occured")
except HTTPError as h:
    print("Bad Status Code")
except Timeout as t:
    print('Request timeout occured')
except TooManyRedirects as r:
    print('Too many redirects have occured')