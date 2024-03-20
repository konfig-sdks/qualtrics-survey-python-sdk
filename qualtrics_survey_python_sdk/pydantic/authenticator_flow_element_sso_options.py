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

from qualtrics_survey_python_sdk.pydantic.authenticator_flow_element_sso_options_cas import AuthenticatorFlowElementSsoOptionsCas
from qualtrics_survey_python_sdk.pydantic.authenticator_flow_element_sso_options_ldap import AuthenticatorFlowElementSsoOptionsLdap
from qualtrics_survey_python_sdk.pydantic.authenticator_flow_element_sso_options_respondent_map import AuthenticatorFlowElementSsoOptionsRespondentMap
from qualtrics_survey_python_sdk.pydantic.authenticator_flow_element_sso_options_token import AuthenticatorFlowElementSsoOptionsToken

class AuthenticatorFlowElementSsoOptions(BaseModel):
    # SSO option type.
    type: Literal["Token", "CAS", "LDAP", "LTI", "Shibboleth", "UseBrandSettings", "GoogleOpenID", "Facebook"] = Field(alias='Type')

    # Capture respondent info.
    capture_respondent_info: typing.Optional[Literal["true", "false"]] = Field(None, alias='CaptureRespondentInfo')

    cas: typing.Optional[AuthenticatorFlowElementSsoOptionsCas] = Field(None, alias='cas')

    ldap: typing.Optional[AuthenticatorFlowElementSsoOptionsLdap] = Field(None, alias='ldap')

    respondent_map: typing.Optional[AuthenticatorFlowElementSsoOptionsRespondentMap] = Field(None, alias='respondentMap')

    token: typing.Optional[AuthenticatorFlowElementSsoOptionsToken] = Field(None, alias='token')

    # Use Panel.
    use_panel: typing.Optional[Literal["true", "false"]] = Field(None, alias='UsePanel')

    # Use person.
    use_person: typing.Optional[Literal["true", "false"]] = Field(None, alias='UsePerson')

    # Use SSO.
    use_s_s_o: typing.Optional[Literal["true", "false"]] = Field(None, alias='UseSSO')
    class Config:
        arbitrary_types_allowed = True
