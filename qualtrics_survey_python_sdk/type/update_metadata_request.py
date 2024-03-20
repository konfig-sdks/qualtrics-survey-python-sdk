# coding: utf-8

"""
    Qualtrics Survey API

    The Qualtrics Survey endpoints give you access to the structure of the surveys you create.   Surveys have a complex structure, and you are encouraged to become familiar with the structure using your brand's Qualtrics page to build surveys at first. Then you can query those surveys using these endpoints.   Once you are familiar, you can use this API to create surveys on the fly, or modify existing surveys in your library. 

    The version of the OpenAPI document: 3.0.0
    Created by: https://www.qualtrics.com/support/
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from qualtrics_survey_python_sdk.type.survey_status_put_metadata import SurveyStatusPutMetadata

class RequiredUpdateMetadataRequest(TypedDict):
    pass

class OptionalUpdateMetadataRequest(TypedDict, total=False):
    # The name of the survey.
    SurveyName: str

    # A user-provided description of the survey.
    SurveyDescription: typing.Optional[str]

    SurveyStatus: SurveyStatusPutMetadata

    # The start date of the survey expressed as a [MySQL datetime](https://dev.mysql.com/doc/refman/8.0/en/datetime.html) value.
    SurveyStartDate: str

    # The expiration date of the survey expressed as a [MySQL datetime](https://dev.mysql.com/doc/refman/8.0/en/datetime.html) value.
    SurveyExpirationDate: str

class UpdateMetadataRequest(RequiredUpdateMetadataRequest, OptionalUpdateMetadataRequest):
    pass
