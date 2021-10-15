import requests
from requests.exceptions import *
import json

def write_to_file(data)->bool:
    """
    Function Takes the data as dict or list and
    writes the data to a file. Raises exception in case
    of filing error. Does not allow to write in case
    data is not in dict or list.
    """
    try:
        if(type(data) is dict or type(data) is list):
            writer = json.dumps(data,ensure_ascii=False)
            with open("file.txt", "w") as f:
                f.write(writer)
                f.close()
            return True
        else:
            return False
    except OSError as e:
        print("A exception occured during file writing: ",e)
        return False

def fetch_from_HTTP_to_File(url:str = "https://api.ekomi.de/v3/getFeedback?auth=100809|3222cc91604a81845f8c3c0d7&type=json&range=6m"):
    """
    Fetches data from url and calls the file writing function.
    Raises exception if HTTP error or file writing error occurs.
    """
    try:
        r = requests.get(url)
        r.raise_for_status()
        return_list = r.json()
        if(r.status_code == 204):
            return None
        if not write_to_file(return_list):
            raise ValueError
        return return_list
    except (ConnectionError,HTTPError,Timeout,TooManyRedirects) as c:
        print("HTTP exception occurred: ",c)
        error_data = '{"response": "error", "message": "An exception occured"}'
        return json.loads(error_data)
    except ValueError:
        print("Unable to write data to the file. Incorrect format")
        error_data = '{"response": "error", "message": "An exception occured"}'
        return json.loads(error_data)

a = fetch_from_HTTP_to_File(123)
print(a["response"])