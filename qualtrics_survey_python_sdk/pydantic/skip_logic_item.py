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

from qualtrics_survey_python_sdk.pydantic.locator import Locator
from qualtrics_survey_python_sdk.pydantic.question_id import QuestionID
from qualtrics_survey_python_sdk.pydantic.survey_id import SurveyID

class SkipLogicItem(BaseModel):
    choice_locator: Locator = Field(alias='ChoiceLocator')

    # All the possible skip logic conditions
    condition: Literal["Selected", "NotSelected", "Displayed", "NotDisplayed", "GreaterThan", "LessThan", "GreaterThanOrEqual", "LessThanOrEqual", "EqualTo", "NotEqualTo", "Empty", "NotEmpty", "ClickedIn", "NotClickedIn", "Uploaded", "NotUploaded", "Contains", "DoesNotContain", "MatchesRegex"] = Field(alias='Condition')

    question_i_d: QuestionID = Field(alias='QuestionID')

    # The ID of the logic.
    skip_logic_i_d: typing.Optional[str] = Field(None, alias='SkipLogicID')

    # The ID of the choice.
    choice_i_d: typing.Optional[str] = Field(None, alias='ChoiceID')

    # a user-provided description field.
    description: typing.Optional[str] = Field(None, alias='Description')

    locator: typing.Optional[Locator] = Field(None, alias='Locator')

    # The text description of the skip condition
    skip_to_description: typing.Optional[str] = Field(None, alias='SkipToDescription')

    # Where to send respondents when the condition is satisfied
    skip_to_destination: typing.Optional[typing.Union[str, SurveyID]] = Field(None, alias='SkipToDestination')
    class Config:
        arbitrary_types_allowed = True
