import requests
from requests.exceptions import *
import json

def write_to_file(data)->bool:
    try:
        if(type(data) is dict or type(data) is list):
            writer = json.dumps(data,ensure_ascii=False)
            f = open("demofile2.txt", "w")
            f.write(writer)
            f.close()
            return True
        else:
            raise ValueError
    except Exception as e:
        print(e)
        return False

def fetch_from_HTTP_to_File(url:str = 'https://api.ekomi.de/v3/getFeedback?auth=100809|3222cc91604a81845f8c3c0d7&type=json&range=6m'):
    try:
        r = requests.get(url)
        r.raise_for_status()
        return_list = r.json()
        if(write_to_file(return_list) == False):
            raise ValueError
        return return_list
    except ConnectionError as c:
        print(c)
        error_data = {"response": "error", "message": "An exception occured"}
        return json.dumps(error_data)