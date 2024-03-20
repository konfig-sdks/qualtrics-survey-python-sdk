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

from qualtrics_survey_python_sdk.type.flow_id import FlowID
from qualtrics_survey_python_sdk.type.key_value_pair_array import KeyValuePairArray

class RequiredWebServiceFlowElement(TypedDict):
    pass

class OptionalWebServiceFlowElement(TypedDict, total=False):
    # The type of web service flow element.
    Type: str

    FlowID: FlowID

    # The URL of the web service flow element.
    URL: str

    # The method of the web service flow element.
    Method: str

    RequestParams: KeyValuePairArray

    EditBodyParams: KeyValuePairArray

    Body: KeyValuePairArray

    # The content type of the web service flow element.
    ContentType: str

    Headers: KeyValuePairArray

    ResponseMap: KeyValuePairArray

    # If true, \"fire and forget.\"
    FireAndForget: bool

    # If true, stringify values.
    StringifyValues: bool

class WebServiceFlowElement(RequiredWebServiceFlowElement, OptionalWebServiceFlowElement):
    pass
