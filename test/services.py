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
#from flask import current_app as app

try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

# Third-party imports...
import requests

# Local imports...
from constants import BASE_URL

#TODOS_URL = urljoin(BASE_URL, 'todos')
TODOS_URL = 'https://webhook.site/b414e959-0bea-4cdd-aaff-684779ad320a'
TODOS_URL = 'http://127.0.0.1:5000/placeholder/todos'

def get_todos():
    response = requests.get(TODOS_URL)

    print('response : ', response)

    #app.logger.error('response : ', response)

    if response.ok:
        return response
        #return None
    else:
        return None