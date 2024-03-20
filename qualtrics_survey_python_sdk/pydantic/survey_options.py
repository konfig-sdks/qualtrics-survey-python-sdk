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

from qualtrics_survey_python_sdk.pydantic.anonymize_response import AnonymizeResponse
from qualtrics_survey_python_sdk.pydantic.available_languages import AvailableLanguages
from qualtrics_survey_python_sdk.pydantic.ballot_box_stuffing_prevention_behavior import BallotBoxStuffingPreventionBehavior
from qualtrics_survey_python_sdk.pydantic.ballot_box_stuffing_prevention_message import BallotBoxStuffingPreventionMessage
from qualtrics_survey_python_sdk.pydantic.ballot_box_stuffing_prevention_message_library import BallotBoxStuffingPreventionMessageLibrary
from qualtrics_survey_python_sdk.pydantic.collect_geo_location import CollectGeoLocation
from qualtrics_survey_python_sdk.pydantic.custom_languages import CustomLanguages
from qualtrics_survey_python_sdk.pydantic.email_thank_you import EmailThankYou
from qualtrics_survey_python_sdk.pydantic.eos_message import EOSMessage
from qualtrics_survey_python_sdk.pydantic.footer_mid import FooterMid
from qualtrics_survey_python_sdk.pydantic.header_mid import HeaderMid
from qualtrics_survey_python_sdk.pydantic.inactive_message import InactiveMessage
from qualtrics_survey_python_sdk.pydantic.inactive_message_library import InactiveMessageLibrary
from qualtrics_survey_python_sdk.pydantic.inactive_survey import InactiveSurvey
from qualtrics_survey_python_sdk.pydantic.language_code import LanguageCode
from qualtrics_survey_python_sdk.pydantic.next_button_mid import NextButtonMid
from qualtrics_survey_python_sdk.pydantic.no_index import NoIndex
from qualtrics_survey_python_sdk.pydantic.page_transition import PageTransition
from qualtrics_survey_python_sdk.pydantic.partial_data import PartialData
from qualtrics_survey_python_sdk.pydantic.partial_data_close_after import PartialDataCloseAfter
from qualtrics_survey_python_sdk.pydantic.password_protection import PasswordProtection
from qualtrics_survey_python_sdk.pydantic.previous_button_mid import PreviousButtonMid
from qualtrics_survey_python_sdk.pydantic.progress_bar_display import ProgressBarDisplay
from qualtrics_survey_python_sdk.pydantic.questions_per_page import QuestionsPerPage
from qualtrics_survey_python_sdk.pydantic.recaptcha_v3 import RecaptchaV3
from qualtrics_survey_python_sdk.pydantic.referer_check import RefererCheck
from qualtrics_survey_python_sdk.pydantic.response_summary import ResponseSummary
from qualtrics_survey_python_sdk.pydantic.secure_response_files import SecureResponseFiles
from qualtrics_survey_python_sdk.pydantic.skin import Skin
from qualtrics_survey_python_sdk.pydantic.survey_expiration import SurveyExpiration
from qualtrics_survey_python_sdk.pydantic.survey_expiration_date import SurveyExpirationDate
from qualtrics_survey_python_sdk.pydantic.survey_meta_description import SurveyMetaDescription
from qualtrics_survey_python_sdk.pydantic.survey_name import SurveyName
from qualtrics_survey_python_sdk.pydantic.survey_protection import SurveyProtection
from qualtrics_survey_python_sdk.pydantic.survey_start_date import SurveyStartDate
from qualtrics_survey_python_sdk.pydantic.survey_termination import SurveyTermination
from qualtrics_survey_python_sdk.pydantic.survey_title import SurveyTitle
from qualtrics_survey_python_sdk.pydantic.thank_you_email_message import ThankYouEmailMessage
from qualtrics_survey_python_sdk.pydantic.thank_you_email_message_library import ThankYouEmailMessageLibrary
from qualtrics_survey_python_sdk.pydantic.validate_message import ValidateMessage
from qualtrics_survey_python_sdk.pydantic.validation_message import ValidationMessage
from qualtrics_survey_python_sdk.pydantic.validation_message_library import ValidationMessageLibrary

class SurveyOptions(BaseModel):
    # If true, display the back button
    back_button: bool = Field(alias='BackButton')

    # If true, prevent respondents from taking the survey multiple times.
    ballot_box_stuffing_prevention: bool = Field(alias='BallotBoxStuffingPrevention')

    # Header to display on each page such as a logo. Do not use in conjunction with `headerMid`.
    header: str = Field(alias='Header')

    # Footer to display on each page such as a logo. Do not use in conjunction with `footerMid`.
    footer: str = Field(alias='Footer')

    no_index: NoIndex = Field(alias='NoIndex')

    # The text to use as the \"next\" Button. Note that `BackButton` should be enabled for this property to be used. See `nextButtonMid` and `BackButton`.
    next_button: str = Field(alias='NextButton')

    partial_data: PartialData = Field(alias='PartialData')

    # The text to use as the \"previous\" Button. Note that `BackButton` should be enabled for this property to be used. See `previousButtonMid` and `BackButton`.
    previous_button: str = Field(alias='PreviousButton')

    progress_bar_display: ProgressBarDisplay = Field(alias='ProgressBarDisplay')

    # If true, allow respondents to save and continue later.
    save_and_continue: bool = Field(alias='SaveAndContinue')

    secure_response_files: SecureResponseFiles = Field(alias='SecureResponseFiles')

    skin: Skin = Field(alias='Skin')

    survey_expiration: SurveyExpiration = Field(alias='SurveyExpiration')

    survey_protection: SurveyProtection = Field(alias='SurveyProtection')

    survey_termination: SurveyTermination = Field(alias='SurveyTermination')

    validation_message: ValidationMessage = Field(alias='ValidationMessage')

    anonymize_response: typing.Optional[AnonymizeResponse] = Field(None, alias='AnonymizeResponse')

    # If true, provide autofocus for questions.
    autofocus: typing.Optional[bool] = Field(None, alias='Autofocus')

    # Enables autoadvance on questions
    autoadvance: typing.Optional[bool] = Field(None, alias='Autoadvance')

    # Enables autoadvance on pages. This requires `Autoadvance` to be anbled as well
    autoadvance_pages: typing.Optional[bool] = Field(None, alias='AutoadvancePages')

    available_languages: typing.Optional[AvailableLanguages] = Field(None, alias='AvailableLanguages')

    ballot_box_stuffing_prevention_behavior: typing.Optional[BallotBoxStuffingPreventionBehavior] = Field(None, alias='BallotBoxStuffingPreventionBehavior')

    ballot_box_stuffing_prevention_message: typing.Optional[BallotBoxStuffingPreventionMessage] = Field(None, alias='BallotBoxStuffingPreventionMessage')

    ballot_box_stuffing_prevention_message_library: typing.Optional[BallotBoxStuffingPreventionMessageLibrary] = Field(None, alias='BallotBoxStuffingPreventionMessageLibrary')

    # Ballot Box stuffing prevention URL.
    ballot_box_stuffing_prevention_u_r_l: typing.Optional[str] = Field(None, alias='BallotBoxStuffingPreventionURL')

    collect_geo_location: typing.Optional[CollectGeoLocation] = Field(None, alias='CollectGeoLocation')

    # Custom CSS to load when survey taking. See also `ExternalCSS`.
    custom_styles: typing.Optional[str] = Field(None, alias='CustomStyles')

    custom_languages: typing.Optional[CustomLanguages] = Field(None, alias='CustomLanguages')

    email_thank_you: typing.Optional[EmailThankYou] = Field(None, alias='EmailThankYou')

    e_o_s_message: typing.Optional[EOSMessage] = Field(None, alias='EOSMessage')

    # The URL to redirect respondents to at the end of the survey used when `SurveyTermination` is set to `Redirect`.
    e_o_s_redirect_u_r_l: typing.Optional[str] = Field(None, alias='EOSRedirectURL')

    # CSS URL to load when survey taking. See also `CustomStyles`.
    external_c_s_s: typing.Optional[str] = Field(None, alias='ExternalCSS')

    header_mid: typing.Optional[HeaderMid] = Field(None, alias='headerMid')

    footer_mid: typing.Optional[FooterMid] = Field(None, alias='footerMid')

    inactive_survey: typing.Optional[InactiveSurvey] = Field(None, alias='InactiveSurvey')

    inactive_message: typing.Optional[InactiveMessage] = Field(None, alias='InactiveMessage')

    inactive_message_library: typing.Optional[InactiveMessageLibrary] = Field(None, alias='InactiveMessageLibrary')

    next_button_mid: typing.Optional[NextButtonMid] = Field(None, alias='nextButtonMid')

    page_transition: typing.Optional[PageTransition] = Field(None, alias='PageTransition')

    partial_data_close_after: typing.Optional[PartialDataCloseAfter] = Field(None, alias='PartialDataCloseAfter')

    # The password to take the survey. See `PasswordProtection`.
    password: typing.Optional[str] = Field(None, alias='Password')

    password_protection: typing.Optional[PasswordProtection] = Field(None, alias='PasswordProtection')

    previous_button_mid: typing.Optional[PreviousButtonMid] = Field(None, alias='previousButtonMid')

    questions_per_page: typing.Optional[QuestionsPerPage] = Field(None, alias='QuestionsPerPage')

    recaptcha_v3: typing.Optional[RecaptchaV3] = Field(None, alias='RecaptchaV3')

    referer_check: typing.Optional[RefererCheck] = Field(None, alias='RefererCheck')

    # The URL respondents must come from to access the survey. See `RefererCheck`.
    referer_u_r_l: typing.Optional[str] = Field(None, alias='RefererURL')

    response_summary: typing.Optional[ResponseSummary] = Field(None, alias='ResponseSummary')

    survey_expiration_date: typing.Optional[SurveyExpirationDate] = Field(None, alias='SurveyExpirationDate')

    survey_meta_description: typing.Optional[SurveyMetaDescription] = Field(None, alias='SurveyMetaDescription')

    survey_language: typing.Optional[LanguageCode] = Field(None, alias='SurveyLanguage')

    survey_name: typing.Optional[SurveyName] = Field(None, alias='SurveyName')

    survey_start_date: typing.Optional[SurveyStartDate] = Field(None, alias='SurveyStartDate')

    survey_title: typing.Optional[SurveyTitle] = Field(None, alias='SurveyTitle')

    thank_you_email_message: typing.Optional[ThankYouEmailMessage] = Field(None, alias='ThankYouEmailMessage')

    thank_you_email_message_library: typing.Optional[ThankYouEmailMessageLibrary] = Field(None, alias='ThankYouEmailMessageLibrary')

    validate_message: typing.Optional[ValidateMessage] = Field(None, alias='ValidateMessage')

    validation_message_library: typing.Optional[ValidationMessageLibrary] = Field(None, alias='ValidationMessageLibrary')
    class Config:
        arbitrary_types_allowed = True
