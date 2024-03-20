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

from qualtrics_survey_python_sdk.pydantic.quota_id import QuotaID

class QuotaExpression(BaseModel):
    # The logic type of the quota expression.
    logic_type: Literal["Quota"] = Field(alias='LogicType')

    # A user-provided description field.
    description: str = Field(alias='Description')

    # Operator.
    left_operand: str = Field(alias='LeftOperand')

    quota_i_d: QuotaID = Field(alias='QuotaID')

    # The type of quota.
    quota_type: Literal["Simple", "Cross", "NoLogic"] = Field(alias='QuotaType')

    # The type of quota expression.
    type: Literal["Expression"] = Field(alias='Type')

    # Operator.
    operator: typing.Optional[Literal["QuotaMet", "QuotaNotMet", "GreaterThan", "GreaterThanOrEqual", "LessThan", "LessThanOrEqual", "EqualTo", "NotEqualTo"]] = Field(None, alias='Operator')

    # The name of the quota.
    quota_name: typing.Optional[str] = Field(None, alias='QuotaName')

    # A unique identifier for the `SubQuotaID`.
    sub_quota_i_d: typing.Optional[str] = Field(None, alias='SubQuotaID')
    class Config:
        arbitrary_types_allowed = True
