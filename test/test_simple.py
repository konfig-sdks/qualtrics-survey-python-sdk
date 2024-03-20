# coding: utf-8

"""
    Qualtrics Survey API

    The Qualtrics Survey endpoints give you access to the structure of the surveys you create.   Surveys have a complex structure, and you are encouraged to become familiar with the structure using your brand's Qualtrics page to build surveys at first. Then you can query those surveys using these endpoints.   Once you are familiar, you can use this API to create surveys on the fly, or modify existing surveys in your library. 

    The version of the OpenAPI document: 3.0.0
    Created by: https://www.qualtrics.com/support/
"""

import unittest

import os
from pprint import pprint
from qualtrics_survey_python_sdk import Qualtrics

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        qualtrics = Qualtrics(
        
                        api_token = 'YOUR_API_KEY',
        
            client_id = 'YOUR_CLIENT_ID',
            client_secret = 'YOUR_CLIENT_SECRET',,
        
            client_id = 'YOUR_CLIENT_ID',
            client_secret = 'YOUR_CLIENT_SECRET',
        )
        self.assertIsNotNone(qualtrics)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
