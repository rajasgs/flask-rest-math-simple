from . import api
from flask import current_app as app
from flask import request
from .response_utils import JSON_MIME_TYPE, success_, success_json




'''
    /template/add?a=2&b=2
    http://127.0.0.1:5000/template/add?a=2&b=2
'''
@api.route('/template/add')
def add1():   
    
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)    
    
    '''
    a = request.form.get('a', type=int)
    b = request.form.get('b', type=int)
    '''
    
    c = a + b

    result_json = {
        'result': c,
        
        'api_error': 0
    }
    
    return success_json(result_json)


'''
App Config:
    https://stackoverflow.com/questions/18214612/how-to-access-app-config-in-a-blueprint
'''