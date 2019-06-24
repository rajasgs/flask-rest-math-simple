from . import api
from flask import current_app as app
from flask import request
from .response_utils import JSON_MIME_TYPE, success_, success_json

'''
    /placeholder/todos
    http://127.0.0.1:5000/placeholder/todos
'''
@api.route('/placeholder/todos')
def ph_temp():   

    object1 = {
        'userId' : 1,
        'id' : 1,
        'title' : 'Some one',
        'completed' : False
    }

    object2 = {
        'userId' : 1,
        'id' : 2,
        'title' : 'Some two',
        'completed' : False
    }

    app.logger.error('trap2.2 : ')
  
    result_json = [object1, object2]
    
    return success_json(result_json)

