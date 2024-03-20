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

from qualtrics_survey_python_sdk.pydantic.response_set_id import ResponseSetID
from qualtrics_survey_python_sdk.pydantic.survey_id import SurveyID
from qualtrics_survey_python_sdk.pydantic.survey_status import SurveyStatus
from qualtrics_survey_python_sdk.pydantic.user_id import UserID

class SurveyMetadata(BaseModel):
    survey_i_d: SurveyID = Field(alias='SurveyID')

    # The name of the survey. 
    survey_name: str = Field(alias='SurveyName')

    # The description of the survey. 
    survey_description: typing.Optional[str] = Field(alias='SurveyDescription')

    survey_owner_i_d: UserID = Field(alias='SurveyOwnerID')

    # The brand ID associated with the survey. 
    survey_brand_i_d: str = Field(alias='SurveyBrandID')

    division_i_d: typing.Optional[str] = Field(alias='DivisionID')

    # The default language of the survey. 
    survey_language: str = Field(alias='SurveyLanguage')

    survey_active_response_set: ResponseSetID = Field(alias='SurveyActiveResponseSet')

    survey_status: SurveyStatus = Field(alias='SurveyStatus')

    # The date and time the survey starts. 
    survey_start_date: typing.Optional[datetime] = Field(alias='SurveyStartDate')

    # The date and time the survey ex 
    survey_expiration_date: typing.Optional[datetime] = Field(alias='SurveyExpirationDate')

    # The date and time the survey was created. 
    survey_creation_date: typing.Optional[datetime] = Field(alias='SurveyCreationDate')

    creator_i_d: UserID = Field(alias='CreatorID')

    # The date and time of the last survey modification.
    last_modified: datetime = Field(alias='LastModified')

    # The date and time the survey was last accessed. 
    last_accessed: typing.Optional[datetime] = Field(alias='LastAccessed')

    last_activated: typing.Optional[datetime] = Field(alias='LastActivated')

    deleted: typing.Optional[datetime] = Field(alias='Deleted')
    class Config:
        arbitrary_types_allowed = True
