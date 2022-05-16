#!/usr/bin/env python
"""
model tests
"""

import os
import unittest
import time
import test_functions


class LoggerTest(unittest.TestCase):
    """
    test the essential functionality
    """
        
    def test_01_train(self):
        """
        ensure log file is created
        """

        test_functions.train_model()
        file_name = time.strftime("%Y%m%d-%H%M%S")
        self.assertTrue(os.path.exists(os.path.join("../logs", file_name + '.txt')))


### Run the tests
if __name__ == '__main__':
    unittest.main()
      
