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

from qualtrics_survey_python_sdk.type.embedded_data_flow_element_embedded_data_item_data_visibility import EmbeddedDataFlowElementEmbeddedDataItemDataVisibility

class RequiredEmbeddedDataFlowElementEmbeddedDataItem(TypedDict):
    # A user-provided description of the embedded data.
    Description: str

    # The type of embedded data.
    Type: str

    # Field for embedded data.
    Field: str

class OptionalEmbeddedDataFlowElementEmbeddedDataItem(TypedDict, total=False):
    # Variable type.
    VariableType: str

    DataVisibility: EmbeddedDataFlowElementEmbeddedDataItemDataVisibility

    # If true, analyze embedded data text.
    AnalyzeText: bool

    # An attribute associated with `key`.
    Value: str

class EmbeddedDataFlowElementEmbeddedDataItem(RequiredEmbeddedDataFlowElementEmbeddedDataItem, OptionalEmbeddedDataFlowElementEmbeddedDataItem):
    pass
