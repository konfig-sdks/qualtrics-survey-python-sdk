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

from qualtrics_survey_python_sdk.pydantic.answer_randomization import AnswerRandomization
from qualtrics_survey_python_sdk.pydantic.choice_order import ChoiceOrder
from qualtrics_survey_python_sdk.pydantic.image_id import ImageID
from qualtrics_survey_python_sdk.pydantic.language import Language
from qualtrics_survey_python_sdk.pydantic.question_choices import QuestionChoices
from qualtrics_survey_python_sdk.pydantic.question_configuration import QuestionConfiguration
from qualtrics_survey_python_sdk.pydantic.question_id import QuestionID
from qualtrics_survey_python_sdk.pydantic.question_sub_selector import QuestionSubSelector
from qualtrics_survey_python_sdk.pydantic.question_text import QuestionText
from qualtrics_survey_python_sdk.pydantic.question_type import QuestionType
from qualtrics_survey_python_sdk.pydantic.randomization import Randomization
from qualtrics_survey_python_sdk.pydantic.recode_values import RecodeValues
from qualtrics_survey_python_sdk.pydantic.selection import Selection
from qualtrics_survey_python_sdk.pydantic.validation import Validation

QuestionDefinition = typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]],typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]],typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]],typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]],typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]],typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
QuestionDefinition = object
