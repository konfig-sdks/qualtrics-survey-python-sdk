# coding: utf-8

"""
    Qualtrics Survey API

    The Qualtrics Survey endpoints give you access to the structure of the surveys you create.   Surveys have a complex structure, and you are encouraged to become familiar with the structure using your brand's Qualtrics page to build surveys at first. Then you can query those surveys using these endpoints.   Once you are familiar, you can use this API to create surveys on the fly, or modify existing surveys in your library. 

    The version of the OpenAPI document: 3.0.0
    Created by: https://www.qualtrics.com/support/
"""

import unittest
from unittest.mock import patch

import urllib3

import qualtrics_survey_python_sdk
from qualtrics_survey_python_sdk.paths.survey_definitions_survey_id_versions import post
from qualtrics_survey_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestSurveyDefinitionsSurveyIdVersions(ApiTestMixin, unittest.TestCase):
    """
    SurveyDefinitionsSurveyIdVersions unit test stubs
        Create Survey Version
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
