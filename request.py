import requests
from requests.exceptions import ConnectionError,HTTPError,Timeout,TooManyRedirects
import json

def fetch_from_HTTP(url:str):
    """
    :return: json data
    :rtype: List | Dict | None


    Fetches data from url and calls the file writing function.
    Raises exception if HTTP error or file writing error occurs.
    """
    try:
        response_data = requests.get(url)
        response_data.raise_for_status()
        return_list = response_data.json()
        if(response_data.status_code == 204):
            return None
        return return_list
    except (ConnectionError,HTTPError,Timeout,TooManyRedirects) as except_text:
        print("HTTP exception occurred: ",except_text)
        error_data = '{"response": "error", "message": "An HTTP request exception occured"}'
        return json.loads(error_data)
    except ValueError:
        print("Unable to write data to the file. Incorrect format")
        error_data = '{"response": "error", "message": "Value data exception occured"}'
        return json.loads(error_data)
