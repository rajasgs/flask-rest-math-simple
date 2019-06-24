import os
import unittest
from Main import app
import json
 

'''
class BasicTests(unittest.TestCase):
 
    ############################
    #### setup and teardown ####
    ############################
 
    # executed prior to each test
    def setUp(self):
        #print('setup reached')
        self.app = app.test_client()
        print('self.app : ', self.app)
        
        
 
    # executed after each test
    def tearDown(self):
        print('tear down reached')
        
 
 
    ###############
    #### tests ####
    ###############
 
    def test_main_page(self):
        
        #print('test main page reached')
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_math_2_4(self):
        
        #print('test math 2 and 4')
        response = self.app.get('/math/add?a=2&b=4', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        #print('response : ', response.data)

        json_data = json.loads(response.data)

        #print('json_data : ', json_data['result'])

        result = json_data['result']

        int_result = int(result)

        print(int_result)

        self.assertEqual(int_result, 6)
 
 
if __name__ == "__main__":
    unittest.main()

'''