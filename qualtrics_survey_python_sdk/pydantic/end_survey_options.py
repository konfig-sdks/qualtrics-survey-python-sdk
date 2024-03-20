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

from qualtrics_survey_python_sdk.pydantic.email_thank_you import EmailThankYou
from qualtrics_survey_python_sdk.pydantic.eos_message import EOSMessage
from qualtrics_survey_python_sdk.pydantic.message_id import MessageID
from qualtrics_survey_python_sdk.pydantic.message_library_id import MessageLibraryID
from qualtrics_survey_python_sdk.pydantic.response_summary import ResponseSummary
from qualtrics_survey_python_sdk.pydantic.survey_termination import SurveyTermination
from qualtrics_survey_python_sdk.pydantic.thank_you_email_message import ThankYouEmailMessage
from qualtrics_survey_python_sdk.pydantic.thank_you_email_message_library import ThankYouEmailMessageLibrary
from qualtrics_survey_python_sdk.pydantic.yes_no_empty_string import YesNoEmptyString

class EndSurveyOptions(BaseModel):
    # Whether to use the default ending options or advanced (custom)
    ending_type: Literal["Default", "Advanced"] = Field(alias='EndingType')

    # How to mark the response. Default `QuotaMet`
    response_flag: typing.Optional[Literal["QuotaMet"]] = Field(None, alias='ResponseFlag')

    survey_termination: typing.Optional[SurveyTermination] = Field(None, alias='SurveyTermination')

    # The URL to redirect respondents to at the end of the survey used when `SurveyTermination` is set to `Redirect`.
    e_o_s_redirect_u_r_l: typing.Optional[str] = Field(None, alias='EOSRedirectURL')

    # End of survey message library used when `SurveyTermination` is set to `DisplayMessage`. See `SurveyTermination` and `EOSMessage`.
    e_o_s_message_library: typing.Optional[str] = Field(None, alias='EOSMessageLibrary')

    e_o_s_message: typing.Optional[EOSMessage] = Field(None, alias='EOSMessage')

    email_thank_you: typing.Optional[EmailThankYou] = Field(None, alias='EmailThankYou')

    thank_you_email_message_library: typing.Optional[ThankYouEmailMessageLibrary] = Field(None, alias='ThankYouEmailMessageLibrary')

    thank_you_email_message: typing.Optional[ThankYouEmailMessage] = Field(None, alias='ThankYouEmailMessage')

    response_summary: typing.Optional[ResponseSummary] = Field(None, alias='ResponseSummary')

    # Show response summary before completing the survey
    confirm_response_summary: typing.Optional[Literal["true", ""]] = Field(None, alias='ConfirmResponseSummary')

    confirm_message_library: typing.Optional[MessageLibraryID] = Field(None, alias='ConfirmMessageLibrary')

    confirm_message: typing.Optional[MessageID] = Field(None, alias='ConfirmMessage')

    count_quotas: typing.Optional[YesNoEmptyString] = Field(None, alias='CountQuotas')

    screenout: typing.Optional[YesNoEmptyString] = Field(None, alias='Screenout')

    screen_out_name: typing.Optional[str] = Field(None, alias='ScreenOutName')

    anonymize_response: typing.Optional[YesNoEmptyString] = Field(None, alias='AnonymizeResponse')

    ignore_response: typing.Optional[YesNoEmptyString] = Field(None, alias='IgnoreResponse')
    class Config:
        arbitrary_types_allowed = True
