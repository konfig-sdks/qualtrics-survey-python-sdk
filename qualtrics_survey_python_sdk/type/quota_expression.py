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

from qualtrics_survey_python_sdk.type.quota_id import QuotaID

class RequiredQuotaExpression(TypedDict):
    # The logic type of the quota expression.
    LogicType: str

    # A user-provided description field.
    Description: str

    # Operator.
    LeftOperand: str

    QuotaID: QuotaID

    # The type of quota.
    QuotaType: str

    # The type of quota expression.
    Type: str

class OptionalQuotaExpression(TypedDict, total=False):
    # Operator.
    Operator: str

    # The name of the quota.
    QuotaName: str

    # A unique identifier for the `SubQuotaID`.
    SubQuotaID: str

class QuotaExpression(RequiredQuotaExpression, OptionalQuotaExpression):
    pass
