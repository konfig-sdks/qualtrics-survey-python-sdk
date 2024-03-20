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

from qualtrics_survey_python_sdk.type.survey_id import SurveyID
from qualtrics_survey_python_sdk.type.survey_version_metadata_publish_events import SurveyVersionMetadataPublishEvents
from qualtrics_survey_python_sdk.type.user_id import UserID

class RequiredSurveyVersionMetadata(TypedDict):
    # A user-provided description of the survey version.
    description: str

    surveyID: SurveyID

    # The unique identifier for this survey version.
    versionID: str

    # The version number of this survey.
    versionNumber: int

    userID: UserID

    # The creation date of survey version expressed as an [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) value.
    creationDate: datetime

    # When true, publish the new version.
    published: bool

    # Filter surveys by the publication status.
    wasPublished: bool

    publishEvents: SurveyVersionMetadataPublishEvents

class OptionalSurveyVersionMetadata(TypedDict, total=False):
    pass

class SurveyVersionMetadata(RequiredSurveyVersionMetadata, OptionalSurveyVersionMetadata):
    pass
