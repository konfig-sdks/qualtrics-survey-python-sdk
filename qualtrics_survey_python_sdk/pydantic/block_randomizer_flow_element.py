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

from qualtrics_survey_python_sdk.pydantic.flow import Flow
from qualtrics_survey_python_sdk.pydantic.flow_id import FlowID

class BlockRandomizerFlowElement(BaseModel):
    # Type of block randomizer.
    type: typing.Optional[Literal["BlockRandomizer"]] = Field(None, alias='Type')

    flow_i_d: typing.Optional[FlowID] = Field(None, alias='FlowID')

    # Subset number.
    sub_set: typing.Optional[int] = Field(None, alias='SubSet')

    # If true, provide even presentation.
    even_presentation: typing.Optional[bool] = Field(None, alias='EvenPresentation')

    flow: typing.Optional[Flow] = Field(None, alias='Flow')
    class Config:
        arbitrary_types_allowed = True
