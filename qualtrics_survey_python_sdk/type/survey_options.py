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

from qualtrics_survey_python_sdk.type.anonymize_response import AnonymizeResponse
from qualtrics_survey_python_sdk.type.available_languages import AvailableLanguages
from qualtrics_survey_python_sdk.type.ballot_box_stuffing_prevention_behavior import BallotBoxStuffingPreventionBehavior
from qualtrics_survey_python_sdk.type.ballot_box_stuffing_prevention_message import BallotBoxStuffingPreventionMessage
from qualtrics_survey_python_sdk.type.ballot_box_stuffing_prevention_message_library import BallotBoxStuffingPreventionMessageLibrary
from qualtrics_survey_python_sdk.type.collect_geo_location import CollectGeoLocation
from qualtrics_survey_python_sdk.type.custom_languages import CustomLanguages
from qualtrics_survey_python_sdk.type.email_thank_you import EmailThankYou
from qualtrics_survey_python_sdk.type.eos_message import EOSMessage
from qualtrics_survey_python_sdk.type.footer_mid import FooterMid
from qualtrics_survey_python_sdk.type.header_mid import HeaderMid
from qualtrics_survey_python_sdk.type.inactive_message import InactiveMessage
from qualtrics_survey_python_sdk.type.inactive_message_library import InactiveMessageLibrary
from qualtrics_survey_python_sdk.type.inactive_survey import InactiveSurvey
from qualtrics_survey_python_sdk.type.language_code import LanguageCode
from qualtrics_survey_python_sdk.type.next_button_mid import NextButtonMid
from qualtrics_survey_python_sdk.type.no_index import NoIndex
from qualtrics_survey_python_sdk.type.page_transition import PageTransition
from qualtrics_survey_python_sdk.type.partial_data import PartialData
from qualtrics_survey_python_sdk.type.partial_data_close_after import PartialDataCloseAfter
from qualtrics_survey_python_sdk.type.password_protection import PasswordProtection
from qualtrics_survey_python_sdk.type.previous_button_mid import PreviousButtonMid
from qualtrics_survey_python_sdk.type.progress_bar_display import ProgressBarDisplay
from qualtrics_survey_python_sdk.type.questions_per_page import QuestionsPerPage
from qualtrics_survey_python_sdk.type.recaptcha_v3 import RecaptchaV3
from qualtrics_survey_python_sdk.type.referer_check import RefererCheck
from qualtrics_survey_python_sdk.type.response_summary import ResponseSummary
from qualtrics_survey_python_sdk.type.secure_response_files import SecureResponseFiles
from qualtrics_survey_python_sdk.type.skin import Skin
from qualtrics_survey_python_sdk.type.survey_expiration import SurveyExpiration
from qualtrics_survey_python_sdk.type.survey_expiration_date import SurveyExpirationDate
from qualtrics_survey_python_sdk.type.survey_meta_description import SurveyMetaDescription
from qualtrics_survey_python_sdk.type.survey_name import SurveyName
from qualtrics_survey_python_sdk.type.survey_protection import SurveyProtection
from qualtrics_survey_python_sdk.type.survey_start_date import SurveyStartDate
from qualtrics_survey_python_sdk.type.survey_termination import SurveyTermination
from qualtrics_survey_python_sdk.type.survey_title import SurveyTitle
from qualtrics_survey_python_sdk.type.thank_you_email_message import ThankYouEmailMessage
from qualtrics_survey_python_sdk.type.thank_you_email_message_library import ThankYouEmailMessageLibrary
from qualtrics_survey_python_sdk.type.validate_message import ValidateMessage
from qualtrics_survey_python_sdk.type.validation_message import ValidationMessage
from qualtrics_survey_python_sdk.type.validation_message_library import ValidationMessageLibrary

class RequiredSurveyOptions(TypedDict):
    # If true, display the back button
    BackButton: bool

    # If true, prevent respondents from taking the survey multiple times.
    BallotBoxStuffingPrevention: bool

    # Header to display on each page such as a logo. Do not use in conjunction with `headerMid`.
    Header: str

    # Footer to display on each page such as a logo. Do not use in conjunction with `footerMid`.
    Footer: str

    NoIndex: NoIndex

    # The text to use as the \"next\" Button. Note that `BackButton` should be enabled for this property to be used. See `nextButtonMid` and `BackButton`.
    NextButton: str

    PartialData: PartialData

    # The text to use as the \"previous\" Button. Note that `BackButton` should be enabled for this property to be used. See `previousButtonMid` and `BackButton`.
    PreviousButton: str

    ProgressBarDisplay: ProgressBarDisplay

    # If true, allow respondents to save and continue later.
    SaveAndContinue: bool

    SecureResponseFiles: SecureResponseFiles

    Skin: Skin

    SurveyExpiration: SurveyExpiration

    SurveyProtection: SurveyProtection

    SurveyTermination: SurveyTermination

    ValidationMessage: ValidationMessage

class OptionalSurveyOptions(TypedDict, total=False):
    AnonymizeResponse: AnonymizeResponse

    # If true, provide autofocus for questions.
    Autofocus: bool

    # Enables autoadvance on questions
    Autoadvance: bool

    # Enables autoadvance on pages. This requires `Autoadvance` to be anbled as well
    AutoadvancePages: bool

    AvailableLanguages: AvailableLanguages

    BallotBoxStuffingPreventionBehavior: BallotBoxStuffingPreventionBehavior

    BallotBoxStuffingPreventionMessage: BallotBoxStuffingPreventionMessage

    BallotBoxStuffingPreventionMessageLibrary: BallotBoxStuffingPreventionMessageLibrary

    # Ballot Box stuffing prevention URL.
    BallotBoxStuffingPreventionURL: str

    CollectGeoLocation: CollectGeoLocation

    # Custom CSS to load when survey taking. See also `ExternalCSS`.
    CustomStyles: str

    CustomLanguages: CustomLanguages

    EmailThankYou: EmailThankYou

    EOSMessage: EOSMessage

    # The URL to redirect respondents to at the end of the survey used when `SurveyTermination` is set to `Redirect`.
    EOSRedirectURL: str

    # CSS URL to load when survey taking. See also `CustomStyles`.
    ExternalCSS: str

    headerMid: HeaderMid

    footerMid: FooterMid

    InactiveSurvey: InactiveSurvey

    InactiveMessage: InactiveMessage

    InactiveMessageLibrary: InactiveMessageLibrary

    nextButtonMid: NextButtonMid

    PageTransition: PageTransition

    PartialDataCloseAfter: PartialDataCloseAfter

    # The password to take the survey. See `PasswordProtection`.
    Password: str

    PasswordProtection: PasswordProtection

    previousButtonMid: PreviousButtonMid

    QuestionsPerPage: QuestionsPerPage

    RecaptchaV3: RecaptchaV3

    RefererCheck: RefererCheck

    # The URL respondents must come from to access the survey. See `RefererCheck`.
    RefererURL: str

    ResponseSummary: ResponseSummary

    SurveyExpirationDate: SurveyExpirationDate

    SurveyMetaDescription: SurveyMetaDescription

    SurveyLanguage: LanguageCode

    SurveyName: SurveyName

    SurveyStartDate: SurveyStartDate

    SurveyTitle: SurveyTitle

    ThankYouEmailMessage: ThankYouEmailMessage

    ThankYouEmailMessageLibrary: ThankYouEmailMessageLibrary

    ValidateMessage: ValidateMessage

    ValidationMessageLibrary: ValidationMessageLibrary

class SurveyOptions(RequiredSurveyOptions, OptionalSurveyOptions):
    pass
