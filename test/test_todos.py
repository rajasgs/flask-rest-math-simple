#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 
Course work: 
@author: raja
Source:
    https://realpython.com/testing-third-party-apis-with-mocks/
'''

# Standard library imports...
from unittest.mock import Mock, patch

# Third-party imports...
from nose.tools import assert_true
import requests

# Third-party imports...
from nose.tools import assert_is_not_none

# Local imports...
from services import get_todos


def test_request_response():
    
    # Send a request to the API server and store the response.
    response = requests.get('http://127.0.0.1:5000/placeholder/todos')

    # Confirm that the request-response cycle completed successfully.
    assert_true(response.ok)




def test_request_response_1():
    
    # Call the service, which will send a request to the server.
    response = get_todos()

    # If the request is sent successfully, then I expect a response to be returned.
    assert_is_not_none(response)



@patch('services.requests.get')
def test_getting_todos(mock_get):
    
    # Configure the mock to return a response with an OK status code.
    mock_get.return_value.ok = True

    # Call the service, which will send a request to the server.
    response = get_todos()

    # If the request is sent successfully, then I expect a response to be returned.
    assert_is_not_none(response)


def test_getting_todos_1():
    with patch('services.requests.get') as mock_get:
        # Configure the mock to return a response with an OK status code.
        mock_get.return_value.ok = True

        # Call the service, which will send a request to the server.
        response = get_todos()

    # If the request is sent successfully, then I expect a response to be returned.
    assert_is_not_none(response)


def test_getting_todos_2():
    mock_get_patcher = patch('services.requests.get')

    # Start patching `requests.get`.
    mock_get = mock_get_patcher.start()

    # Configure the mock to return a response with an OK status code.
    mock_get.return_value.ok = True

    # Call the service, which will send a request to the server.
    response = get_todos()

    # Stop patching `requests.get`.
    mock_get_patcher.stop()

    # If the request is sent successfully, then I expect a response to be returned.
    assert_is_not_none(response)