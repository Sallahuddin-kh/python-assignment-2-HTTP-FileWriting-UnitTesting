import pytest
import request

"""
This file contains unit tests for request module
"""

@pytest.mark.parametrize("param",[[1,2,3,4,5,6],{1:"q",2:"f",3:"f",4:"g",5:"g",6:"d"}])
def test_write_to_file1(param):
    """
    Tests the output of file writing function with correct input
    """
    assert request.write_to_file(param) == True

@pytest.mark.parametrize("param",["String",12,(1,2,3,4)])
def test_cwrite_to_file2(param):
    """
    Tests the output of file writing function with incorrect input
    """
    assert request.write_to_file(param) == False

@pytest.mark.parametrize("param",["https://api.ekomi.de/v3/getFeedback?auth=100809|3222cc91604a81845f8c3c0d7&type=json&range=6m"])
def test_fetch_from_HTTP_to_File1(param):
    """
    Tests the HTTP fetch function with correct input
    """
    assert type(request.fetch_from_HTTP_to_File(param)) == list

@pytest.mark.parametrize("param",["http://somebadurl.example/","Non url",123])
def test_fetch_from_HTTP_to_File2(param):
    """
    Tests the HTTP fetch function with incorrect input
    """
    response_data = request.fetch_from_HTTP_to_File(param)
    assert response_data["response"] == "error"
