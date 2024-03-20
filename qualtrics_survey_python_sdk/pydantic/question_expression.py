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

class QuestionExpression(BaseModel):
    choice_locator: Locator = Field(alias='ChoiceLocator')

    # The logic type of a question expression.
    logic_type: Literal["Question"] = Field(alias='LogicType')

    # Operator.
    operator: Literal["Selected", "NotSelected", "EqualTo", "NotEqualTo", "Empty", "NotEmpty", "Displayed", "NotDisplayed", "GreaterThan", "GreaterThanOrEqual", "LessThan", "LessThanOrEqual", "Contains", "DoesNotContain", "MatchesRegex", "IsNot", "Uploaded", "NotUploaded", "PDF", "Document", "ClickedIn", "NotClickedIn", "Extensions", "Graphic", "Spreadsheet"] = Field(alias='Operator')

    question_i_d: QuestionID = Field(alias='QuestionID')

    # If yes, question is in loop.
    question_is_in_loop: Literal["true", "false"] = Field(alias='QuestionIsInLoop')

    # The type of question expression.
    type: Literal["Expression"] = Field(alias='Type')
    class Config:
        arbitrary_types_allowed = True
