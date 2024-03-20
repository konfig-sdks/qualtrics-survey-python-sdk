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

from qualtrics_survey_python_sdk.type.locator import Locator
from qualtrics_survey_python_sdk.type.question_id import QuestionID
from qualtrics_survey_python_sdk.type.survey_id import SurveyID

class RequiredSkipLogicItem(TypedDict):
    ChoiceLocator: Locator

    # All the possible skip logic conditions
    Condition: str

    QuestionID: QuestionID

class OptionalSkipLogicItem(TypedDict, total=False):
    # The ID of the logic.
    SkipLogicID: str

    # The ID of the choice.
    ChoiceID: str

    # a user-provided description field.
    Description: str

    Locator: Locator

    # The text description of the skip condition
    SkipToDescription: str

    # Where to send respondents when the condition is satisfied
    SkipToDestination: typing.Union[str, SurveyID]

class SkipLogicItem(RequiredSkipLogicItem, OptionalSkipLogicItem):
    pass
