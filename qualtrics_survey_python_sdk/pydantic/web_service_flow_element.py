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

from qualtrics_survey_python_sdk.pydantic.flow_id import FlowID
from qualtrics_survey_python_sdk.pydantic.key_value_pair_array import KeyValuePairArray

class WebServiceFlowElement(BaseModel):
    # The type of web service flow element.
    type: typing.Optional[Literal["WebService"]] = Field(None, alias='Type')

    flow_i_d: typing.Optional[FlowID] = Field(None, alias='FlowID')

    # The URL of the web service flow element.
    u_r_l: typing.Optional[str] = Field(None, alias='URL')

    # The method of the web service flow element.
    method: typing.Optional[Literal["GET", "POST", "PUT", "PATCH", "DELETE"]] = Field(None, alias='Method')

    request_params: typing.Optional[KeyValuePairArray] = Field(None, alias='RequestParams')

    edit_body_params: typing.Optional[KeyValuePairArray] = Field(None, alias='EditBodyParams')

    body: typing.Optional[KeyValuePairArray] = Field(None, alias='Body')

    # The content type of the web service flow element.
    content_type: typing.Optional[Literal["application/x-www-form-urlencoded", "application/json"]] = Field(None, alias='ContentType')

    headers: typing.Optional[KeyValuePairArray] = Field(None, alias='Headers')

    response_map: typing.Optional[KeyValuePairArray] = Field(None, alias='ResponseMap')

    # If true, \"fire and forget.\"
    fire_and_forget: typing.Optional[bool] = Field(None, alias='FireAndForget')

    # If true, stringify values.
    stringify_values: typing.Optional[bool] = Field(None, alias='StringifyValues')
    class Config:
        arbitrary_types_allowed = True
