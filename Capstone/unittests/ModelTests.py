#!/usr/bin/env python
"""
model tests
"""

import sys, os
import unittest
import numpy as np
import pandas as pd

## import model specific functions and variables
import test_functions

class ModelTest(unittest.TestCase):
    """
    test the essential functionality
    """
        
    def test_01_train(self):
        """
        test the train functionality
        """

        ## train the model
        test_functions.train_model()
        self.assertTrue(os.path.exists(os.path.join("../models", "model.joblib")))

    def test_02_load(self):
        """
        test the train functionality
        """
                        
        ## train the model
        model = test_functions.get_model()
        self.assertTrue('predict' in dir(model))

       
    def test_03_predict(self):
        """
        test the predict function input
        """

        result = test_functions.model_predict(start_date='2018-08-08', end_date='2018-09-09')
        self.assertTrue(type(result) == pd.Series)
    
### Run the tests
if __name__ == '__main__':
    unittest.main()
