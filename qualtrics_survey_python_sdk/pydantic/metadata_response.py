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

from qualtrics_survey_python_sdk.pydantic.successful_meta import SuccessfulMeta
from qualtrics_survey_python_sdk.pydantic.survey_metadata import SurveyMetadata

class MetadataResponse(BaseModel):
    meta: SuccessfulMeta = Field(alias='meta')

    result: SurveyMetadata = Field(alias='result')
    class Config:
        arbitrary_types_allowed = True
