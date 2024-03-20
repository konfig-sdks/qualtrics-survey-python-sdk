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

from qualtrics_survey_python_sdk.pydantic.block_options_looping_options_static import BlockOptionsLoopingOptionsStatic
from qualtrics_survey_python_sdk.pydantic.locator import Locator
from qualtrics_survey_python_sdk.pydantic.question_id import QuestionID

class BlockOptionsLoopingOptions(BaseModel):
    choice_group_locator: typing.Optional[Locator] = Field(None, alias='ChoiceGroupLocator')

    locator: typing.Optional[Locator] = Field(None, alias='Locator')

    q_i_d: typing.Optional[QuestionID] = Field(None, alias='QID')

    # Type of randomization to apply to the loop ordering
    randomization: typing.Optional[Literal["None", "Subset", "All"]] = Field(None, alias='Randomization')

    static: typing.Optional[BlockOptionsLoopingOptionsStatic] = Field(None, alias='Static')
    class Config:
        arbitrary_types_allowed = True
