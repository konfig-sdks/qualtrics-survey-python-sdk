# coding: utf-8

# flake8: noqa

"""
    Qualtrics Survey API

    The Qualtrics Survey endpoints give you access to the structure of the surveys you create.   Surveys have a complex structure, and you are encouraged to become familiar with the structure using your brand's Qualtrics page to build surveys at first. Then you can query those surveys using these endpoints.   Once you are familiar, you can use this API to create surveys on the fly, or modify existing surveys in your library. 

    The version of the OpenAPI document: 3.0.0
    Created by: https://www.qualtrics.com/support/
"""

__version__ = "3.0.0"

# import ApiClient
from qualtrics_survey_python_sdk.api_client import ApiClient

# import Configuration
from qualtrics_survey_python_sdk.configuration import Configuration

# import exceptions
from qualtrics_survey_python_sdk.exceptions import OpenApiException
from qualtrics_survey_python_sdk.exceptions import ApiAttributeError
from qualtrics_survey_python_sdk.exceptions import ApiTypeError
from qualtrics_survey_python_sdk.exceptions import ApiValueError
from qualtrics_survey_python_sdk.exceptions import ApiKeyError
from qualtrics_survey_python_sdk.exceptions import ApiException

from qualtrics_survey_python_sdk.client import Qualtrics
