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

from qualtrics_survey_python_sdk.pydantic.survey_id import SurveyID
from qualtrics_survey_python_sdk.pydantic.survey_version_metadata_publish_events import SurveyVersionMetadataPublishEvents
from qualtrics_survey_python_sdk.pydantic.user_id import UserID

class SurveyVersionMetadata(BaseModel):
    # A user-provided description of the survey version.
    description: str = Field(alias='description')

    survey_i_d: SurveyID = Field(alias='surveyID')

    # The unique identifier for this survey version.
    version_i_d: str = Field(alias='versionID')

    # The version number of this survey.
    version_number: int = Field(alias='versionNumber')

    user_i_d: UserID = Field(alias='userID')

    # The creation date of survey version expressed as an [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) value.
    creation_date: datetime = Field(alias='creationDate')

    # When true, publish the new version.
    published: bool = Field(alias='published')

    # Filter surveys by the publication status.
    was_published: bool = Field(alias='wasPublished')

    publish_events: SurveyVersionMetadataPublishEvents = Field(alias='publishEvents')
    class Config:
        arbitrary_types_allowed = True
