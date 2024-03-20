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

from qualtrics_survey_python_sdk.type.email_thank_you import EmailThankYou
from qualtrics_survey_python_sdk.type.eos_message import EOSMessage
from qualtrics_survey_python_sdk.type.message_id import MessageID
from qualtrics_survey_python_sdk.type.message_library_id import MessageLibraryID
from qualtrics_survey_python_sdk.type.response_summary import ResponseSummary
from qualtrics_survey_python_sdk.type.survey_termination import SurveyTermination
from qualtrics_survey_python_sdk.type.thank_you_email_message import ThankYouEmailMessage
from qualtrics_survey_python_sdk.type.thank_you_email_message_library import ThankYouEmailMessageLibrary
from qualtrics_survey_python_sdk.type.yes_no_empty_string import YesNoEmptyString

class RequiredEndSurveyOptions(TypedDict):
    # Whether to use the default ending options or advanced (custom)
    EndingType: str

class OptionalEndSurveyOptions(TypedDict, total=False):
    # How to mark the response. Default `QuotaMet`
    ResponseFlag: str

    SurveyTermination: SurveyTermination

    # The URL to redirect respondents to at the end of the survey used when `SurveyTermination` is set to `Redirect`.
    EOSRedirectURL: str

    # End of survey message library used when `SurveyTermination` is set to `DisplayMessage`. See `SurveyTermination` and `EOSMessage`.
    EOSMessageLibrary: str

    EOSMessage: EOSMessage

    EmailThankYou: EmailThankYou

    ThankYouEmailMessageLibrary: ThankYouEmailMessageLibrary

    ThankYouEmailMessage: ThankYouEmailMessage

    ResponseSummary: ResponseSummary

    # Show response summary before completing the survey
    ConfirmResponseSummary: str

    ConfirmMessageLibrary: MessageLibraryID

    ConfirmMessage: MessageID

    CountQuotas: YesNoEmptyString

    Screenout: YesNoEmptyString

    ScreenOutName: str

    AnonymizeResponse: YesNoEmptyString

    IgnoreResponse: YesNoEmptyString

class EndSurveyOptions(RequiredEndSurveyOptions, OptionalEndSurveyOptions):
    pass
