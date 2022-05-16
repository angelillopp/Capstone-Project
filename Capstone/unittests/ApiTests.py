#!/usr/bin/env python
"""
api tests

these tests use the requests package however similar requests can be made with curl

e.g.

data = '{"key":"value"}'
curl -X POST -H "Content-Type: application/json" -d "%s" http://localhost:8080/predict'%(data)
"""

import sys
import os
import unittest
import requests
import re
from ast import literal_eval
import numpy as np

port = 8080

try:
    requests.post('http://127.0.0.1:{}/predict'.format(port))
    server_available = True
except:
    server_available = False
    
## test class for the main window function
class ApiTest(unittest.TestCase):
    """
    test the essential functionality
    """

    @unittest.skipUnless(server_available, "local server is not running")
    def test_01_train(self):
        """
        test the train functionality
        """
      
        request_json = {'folder_name':'test'}
        r = requests.post('http://127.0.0.1:{}/train'.format(port), json=request_json)
        train_complete = re.sub("\W+", "", r.text)
        self.assertEqual(train_complete, 'Model trained succesfully.')
    
    @unittest.skipUnless(server_available,"local server is not running")
    def test_02_predict(self):
        """
        test the predict functionality
        """

        request_json = {'start_date': '2018-08-08',
                      'end_date': '2018-09-09'
        }

        r = requests.post('http://127.0.0.1:{}/predict'.format(port), json=request_json)
        response = literal_eval(r.text)

        self.assertTrue('The total revenue between' in response)

        
### Run the tests
if __name__ == '__main__':
    unittest.main()
