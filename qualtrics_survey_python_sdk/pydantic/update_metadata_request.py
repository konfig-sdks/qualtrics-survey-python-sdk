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
from pydantic import BaseModel, Field, RootModel

from qualtrics_survey_python_sdk.pydantic.survey_status_put_metadata import SurveyStatusPutMetadata

class UpdateMetadataRequest(BaseModel):
    # The name of the survey.
    survey_name: typing.Optional[str] = Field(None, alias='SurveyName')

    # A user-provided description of the survey.
    survey_description: typing.Optional[typing.Optional[str]] = Field(None, alias='SurveyDescription')

    survey_status: typing.Optional[SurveyStatusPutMetadata] = Field(None, alias='SurveyStatus')

    # The start date of the survey expressed as a [MySQL datetime](https://dev.mysql.com/doc/refman/8.0/en/datetime.html) value.
    survey_start_date: typing.Optional[str] = Field(None, alias='SurveyStartDate')

    # The expiration date of the survey expressed as a [MySQL datetime](https://dev.mysql.com/doc/refman/8.0/en/datetime.html) value.
    survey_expiration_date: typing.Optional[str] = Field(None, alias='SurveyExpirationDate')
    class Config:
        arbitrary_types_allowed = True
