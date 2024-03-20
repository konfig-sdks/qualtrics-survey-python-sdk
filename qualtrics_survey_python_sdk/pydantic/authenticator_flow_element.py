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

from qualtrics_survey_python_sdk.pydantic.authenticator_flow_element_options import AuthenticatorFlowElementOptions
from qualtrics_survey_python_sdk.pydantic.authenticator_flow_element_panel_data import AuthenticatorFlowElementPanelData
from qualtrics_survey_python_sdk.pydantic.authenticator_flow_element_sso_options import AuthenticatorFlowElementSsoOptions
from qualtrics_survey_python_sdk.pydantic.branch_logic import BranchLogic
from qualtrics_survey_python_sdk.pydantic.flow import Flow
from qualtrics_survey_python_sdk.pydantic.flow_id import FlowID

class AuthenticatorFlowElement(BaseModel):
    type: Literal["Authenticator"] = Field(alias='Type')

    panel_data: AuthenticatorFlowElementPanelData = Field(alias='PanelData')

    field_data: BranchLogic = Field(alias='FieldData')

    # If true, filter data fields.
    filter_data_fields: bool = Field(alias='FilterDataFields')

    s_s_o_options: AuthenticatorFlowElementSsoOptions = Field(alias='SSOOptions')

    options: AuthenticatorFlowElementOptions = Field(alias='Options')

    flow_i_d: typing.Optional[FlowID] = Field(None, alias='FlowID')

    flow: typing.Optional[Flow] = Field(None, alias='Flow')
    class Config:
        arbitrary_types_allowed = True
