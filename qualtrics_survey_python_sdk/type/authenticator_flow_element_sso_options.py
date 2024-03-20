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

from qualtrics_survey_python_sdk.type.authenticator_flow_element_sso_options_cas import AuthenticatorFlowElementSsoOptionsCas
from qualtrics_survey_python_sdk.type.authenticator_flow_element_sso_options_ldap import AuthenticatorFlowElementSsoOptionsLdap
from qualtrics_survey_python_sdk.type.authenticator_flow_element_sso_options_respondent_map import AuthenticatorFlowElementSsoOptionsRespondentMap
from qualtrics_survey_python_sdk.type.authenticator_flow_element_sso_options_token import AuthenticatorFlowElementSsoOptionsToken

class RequiredAuthenticatorFlowElementSsoOptions(TypedDict):
    # SSO option type.
    Type: str

class OptionalAuthenticatorFlowElementSsoOptions(TypedDict, total=False):
    # Capture respondent info.
    CaptureRespondentInfo: str

    cas: AuthenticatorFlowElementSsoOptionsCas

    ldap: AuthenticatorFlowElementSsoOptionsLdap

    respondentMap: AuthenticatorFlowElementSsoOptionsRespondentMap

    token: AuthenticatorFlowElementSsoOptionsToken

    # Use Panel.
    UsePanel: str

    # Use person.
    UsePerson: str

    # Use SSO.
    UseSSO: str

class AuthenticatorFlowElementSsoOptions(RequiredAuthenticatorFlowElementSsoOptions, OptionalAuthenticatorFlowElementSsoOptions):
    pass
