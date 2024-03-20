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

from qualtrics_survey_python_sdk.pydantic.block_id import BlockID
from qualtrics_survey_python_sdk.pydantic.comparison_operators import ComparisonOperators

class LoopAndMergeExpression(BaseModel):
    # The logic type of the loop and merge expression.
    logic_type: Literal["LoopAndMerge"] = Field(alias='LogicType')

    # A user-provided description field.
    description: str = Field(alias='Description')

    # The type of loop and merge expression.
    type: Literal["Expression"] = Field(alias='Type')

    left_operand: typing.Optional[BlockID] = Field(None, alias='LeftOperand')

    operator: typing.Optional[ComparisonOperators] = Field(None, alias='Operator')

    # Operation.
    right_operand: typing.Optional[Literal["lm://CurrentLoop", "lm://CurrentLoopNumber", "lm://CurrentLoopById"]] = Field(None, alias='RightOperand')
    class Config:
        arbitrary_types_allowed = True
