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

from qualtrics_survey_python_sdk.pydantic.embedded_data_flow_element_embedded_data_item_data_visibility import EmbeddedDataFlowElementEmbeddedDataItemDataVisibility

class EmbeddedDataFlowElementEmbeddedDataItem(BaseModel):
    # A user-provided description of the embedded data.
    description: str = Field(alias='Description')

    # The type of embedded data.
    type: Literal["Recipient", "Custom", "EmbeddedData"] = Field(alias='Type')

    # Field for embedded data.
    field: str = Field(alias='Field')

    # Variable type.
    variable_type: typing.Optional[Literal["Nominal", "MultiValueNominal", "Ordinal", "Scale", "String", "Date", "FilterOnly", "Filter Only"]] = Field(None, alias='VariableType')

    data_visibility: typing.Optional[EmbeddedDataFlowElementEmbeddedDataItemDataVisibility] = Field(None, alias='DataVisibility')

    # If true, analyze embedded data text.
    analyze_text: typing.Optional[bool] = Field(None, alias='AnalyzeText')

    # An attribute associated with `key`.
    value: typing.Optional[str] = Field(None, alias='Value')
    class Config:
        arbitrary_types_allowed = True
