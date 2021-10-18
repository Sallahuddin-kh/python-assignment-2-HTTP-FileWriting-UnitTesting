import json

def write_to_file(data)->bool:
    """
    :param data: json data
    :type data: list | dict | str

    :return: File writing success
    :rtype: bool
   

    Function Takes the data as dict or list and
    writes the data to a file. Raises exception in case
    of filing error. Does not allow to write in case
    data is not in dict or list.
    """
    try:
        if(type(data) is dict or type(data) is list):
            json_data = json.dumps(data,ensure_ascii=False)
            with open("file.txt", "w") as f:
                f.write(json_data)
                f.close()
            return True
        else:
            return False
    except OSError as except_text:
        print("A exception occured during file writing: ",except_text)
        return False
