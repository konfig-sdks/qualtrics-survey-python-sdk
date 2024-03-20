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

from qualtrics_survey_python_sdk.pydantic.quota_group_id import QuotaGroupID
from qualtrics_survey_python_sdk.pydantic.quota_id import QuotaID

class QuotaGroup(BaseModel):
    i_d: QuotaGroupID = Field(alias='ID')

    id: typing.Optional[QuotaGroupID] = Field(None, alias='Id')

    # Determines behavior when a single response matches multiple quotas within the group. One of `PlaceInAll`, `LeastFilled`, `MostFilled`, `LeastFilledPercent`, `MostFilledPercent`, `ReverseOrder`, or `CurrentDefinedOrder`
    multiple_match: typing.Optional[Literal["PlaceInAll", "LeastFilled", "MostFilled", "LeastFilledPercent", "MostFilledPercent", "ReverseOrder", "CurrentDefinedOrder"]] = Field(None, alias='MultipleMatch')

    # Name of the quota group
    name: typing.Optional[str] = Field(None, alias='Name')

    # `Public` refers to whether or not the Public Quota Dashboard is enabled. Enabling the Public Quota Dashboard will provide a public page where anyone can view the quotas in that group.
    public: typing.Optional[bool] = Field(None, alias='Public')

    # A list of all the quotas in the group
    quotas: typing.Optional[typing.List[QuotaID]] = Field(None, alias='Quotas')

    # Input will not be persisted. It is only used by the Quota Editor UI
    selected: typing.Optional[bool] = Field(None, alias='Selected')
    class Config:
        arbitrary_types_allowed = True
