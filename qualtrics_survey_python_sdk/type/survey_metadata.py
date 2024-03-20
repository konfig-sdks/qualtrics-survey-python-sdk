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

from qualtrics_survey_python_sdk.type.response_set_id import ResponseSetID
from qualtrics_survey_python_sdk.type.survey_id import SurveyID
from qualtrics_survey_python_sdk.type.survey_status import SurveyStatus
from qualtrics_survey_python_sdk.type.user_id import UserID

class RequiredSurveyMetadata(TypedDict):
    SurveyID: SurveyID

    # The name of the survey. 
    SurveyName: str

    # The description of the survey. 
    SurveyDescription: typing.Optional[str]

    SurveyOwnerID: UserID

    # The brand ID associated with the survey. 
    SurveyBrandID: str

    DivisionID: typing.Optional[str]

    # The default language of the survey. 
    SurveyLanguage: str

    SurveyActiveResponseSet: ResponseSetID

    SurveyStatus: SurveyStatus

    # The date and time the survey starts. 
    SurveyStartDate: typing.Optional[datetime]

    # The date and time the survey ex 
    SurveyExpirationDate: typing.Optional[datetime]

    # The date and time the survey was created. 
    SurveyCreationDate: typing.Optional[datetime]

    CreatorID: UserID

    # The date and time of the last survey modification.
    LastModified: datetime

    # The date and time the survey was last accessed. 
    LastAccessed: typing.Optional[datetime]

    LastActivated: typing.Optional[datetime]

    Deleted: typing.Optional[datetime]

class OptionalSurveyMetadata(TypedDict, total=False):
    pass

class SurveyMetadata(RequiredSurveyMetadata, OptionalSurveyMetadata):
    pass
