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

from qualtrics_survey_python_sdk.type.authenticator_flow_element_options import AuthenticatorFlowElementOptions
from qualtrics_survey_python_sdk.type.authenticator_flow_element_panel_data import AuthenticatorFlowElementPanelData
from qualtrics_survey_python_sdk.type.authenticator_flow_element_sso_options import AuthenticatorFlowElementSsoOptions
from qualtrics_survey_python_sdk.type.branch_logic import BranchLogic
from qualtrics_survey_python_sdk.type.flow import Flow
from qualtrics_survey_python_sdk.type.flow_id import FlowID

class RequiredAuthenticatorFlowElement(TypedDict):
    Type: str

    PanelData: AuthenticatorFlowElementPanelData

    FieldData: BranchLogic

    # If true, filter data fields.
    FilterDataFields: bool

    SSOOptions: AuthenticatorFlowElementSsoOptions

    Options: AuthenticatorFlowElementOptions

class OptionalAuthenticatorFlowElement(TypedDict, total=False):
    FlowID: FlowID

    Flow: Flow

class AuthenticatorFlowElement(RequiredAuthenticatorFlowElement, OptionalAuthenticatorFlowElement):
    pass
