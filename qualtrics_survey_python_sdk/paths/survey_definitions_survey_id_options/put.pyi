# coding: utf-8

"""
    Qualtrics Survey API

    The Qualtrics Survey endpoints give you access to the structure of the surveys you create.   Surveys have a complex structure, and you are encouraged to become familiar with the structure using your brand's Qualtrics page to build surveys at first. Then you can query those surveys using these endpoints.   Once you are familiar, you can use this API to create surveys on the fly, or modify existing surveys in your library. 

    The version of the OpenAPI document: 3.0.0
    Created by: https://www.qualtrics.com/support/
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from qualtrics_survey_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from qualtrics_survey_python_sdk.api_response import AsyncGeneratorResponse
from qualtrics_survey_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from qualtrics_survey_python_sdk import schemas  # noqa: F401

from qualtrics_survey_python_sdk.model.page_transition import PageTransition as PageTransitionSchema
from qualtrics_survey_python_sdk.model.secure_response_files import SecureResponseFiles as SecureResponseFilesSchema
from qualtrics_survey_python_sdk.model.no_index import NoIndex as NoIndexSchema
from qualtrics_survey_python_sdk.model.partial_data_close_after import PartialDataCloseAfter as PartialDataCloseAfterSchema
from qualtrics_survey_python_sdk.model.previous_button_mid import PreviousButtonMid as PreviousButtonMidSchema
from qualtrics_survey_python_sdk.model.progress_bar_display import ProgressBarDisplay as ProgressBarDisplaySchema
from qualtrics_survey_python_sdk.model.survey_options import SurveyOptions as SurveyOptionsSchema
from qualtrics_survey_python_sdk.model.skin import Skin as SkinSchema
from qualtrics_survey_python_sdk.model.eos_message import EOSMessage as EOSMessageSchema
from qualtrics_survey_python_sdk.model.response_summary import ResponseSummary as ResponseSummarySchema
from qualtrics_survey_python_sdk.model.survey_meta_description import SurveyMetaDescription as SurveyMetaDescriptionSchema
from qualtrics_survey_python_sdk.model.survey_protection import SurveyProtection as SurveyProtectionSchema
from qualtrics_survey_python_sdk.model.internal_server_error_response import InternalServerErrorResponse as InternalServerErrorResponseSchema
from qualtrics_survey_python_sdk.model.header_mid import HeaderMid as HeaderMidSchema
from qualtrics_survey_python_sdk.model.validation_message_library import ValidationMessageLibrary as ValidationMessageLibrarySchema
from qualtrics_survey_python_sdk.model.unauthorized_request_error_response import UnauthorizedRequestErrorResponse as UnauthorizedRequestErrorResponseSchema
from qualtrics_survey_python_sdk.model.next_button_mid import NextButtonMid as NextButtonMidSchema
from qualtrics_survey_python_sdk.model.collect_geo_location import CollectGeoLocation as CollectGeoLocationSchema
from qualtrics_survey_python_sdk.model.ballot_box_stuffing_prevention_message_library import BallotBoxStuffingPreventionMessageLibrary as BallotBoxStuffingPreventionMessageLibrarySchema
from qualtrics_survey_python_sdk.model.password_protection import PasswordProtection as PasswordProtectionSchema
from qualtrics_survey_python_sdk.model.ballot_box_stuffing_prevention_message import BallotBoxStuffingPreventionMessage as BallotBoxStuffingPreventionMessageSchema
from qualtrics_survey_python_sdk.model.custom_languages import CustomLanguages as CustomLanguagesSchema
from qualtrics_survey_python_sdk.model.survey_expiration_date import SurveyExpirationDate as SurveyExpirationDateSchema
from qualtrics_survey_python_sdk.model.survey_title import SurveyTitle as SurveyTitleSchema
from qualtrics_survey_python_sdk.model.inactive_message import InactiveMessage as InactiveMessageSchema
from qualtrics_survey_python_sdk.model.request_successful_response import RequestSuccessfulResponse as RequestSuccessfulResponseSchema
from qualtrics_survey_python_sdk.model.recaptcha_v3 import RecaptchaV3 as RecaptchaV3Schema
from qualtrics_survey_python_sdk.model.questions_per_page import QuestionsPerPage as QuestionsPerPageSchema
from qualtrics_survey_python_sdk.model.inactive_message_library import InactiveMessageLibrary as InactiveMessageLibrarySchema
from qualtrics_survey_python_sdk.model.invalid_request_error_response import InvalidRequestErrorResponse as InvalidRequestErrorResponseSchema
from qualtrics_survey_python_sdk.model.survey_expiration import SurveyExpiration as SurveyExpirationSchema
from qualtrics_survey_python_sdk.model.available_languages import AvailableLanguages as AvailableLanguagesSchema
from qualtrics_survey_python_sdk.model.survey_id import SurveyID as SurveyIDSchema
from qualtrics_survey_python_sdk.model.thank_you_email_message_library import ThankYouEmailMessageLibrary as ThankYouEmailMessageLibrarySchema
from qualtrics_survey_python_sdk.model.partial_data import PartialData as PartialDataSchema
from qualtrics_survey_python_sdk.model.anonymize_response import AnonymizeResponse as AnonymizeResponseSchema
from qualtrics_survey_python_sdk.model.footer_mid import FooterMid as FooterMidSchema
from qualtrics_survey_python_sdk.model.inactive_survey import InactiveSurvey as InactiveSurveySchema
from qualtrics_survey_python_sdk.model.survey_termination import SurveyTermination as SurveyTerminationSchema
from qualtrics_survey_python_sdk.model.ballot_box_stuffing_prevention_behavior import BallotBoxStuffingPreventionBehavior as BallotBoxStuffingPreventionBehaviorSchema
from qualtrics_survey_python_sdk.model.survey_start_date import SurveyStartDate as SurveyStartDateSchema
from qualtrics_survey_python_sdk.model.referer_check import RefererCheck as RefererCheckSchema
from qualtrics_survey_python_sdk.model.forbidden_request_error_response import ForbiddenRequestErrorResponse as ForbiddenRequestErrorResponseSchema
from qualtrics_survey_python_sdk.model.validation_message import ValidationMessage as ValidationMessageSchema
from qualtrics_survey_python_sdk.model.thank_you_email_message import ThankYouEmailMessage as ThankYouEmailMessageSchema
from qualtrics_survey_python_sdk.model.language_code import LanguageCode as LanguageCodeSchema
from qualtrics_survey_python_sdk.model.email_thank_you import EmailThankYou as EmailThankYouSchema
from qualtrics_survey_python_sdk.model.validate_message import ValidateMessage as ValidateMessageSchema
from qualtrics_survey_python_sdk.model.survey_name import SurveyName as SurveyNameSchema

from qualtrics_survey_python_sdk.type.custom_languages import CustomLanguages
from qualtrics_survey_python_sdk.type.recaptcha_v3 import RecaptchaV3
from qualtrics_survey_python_sdk.type.secure_response_files import SecureResponseFiles
from qualtrics_survey_python_sdk.type.no_index import NoIndex
from qualtrics_survey_python_sdk.type.validation_message_library import ValidationMessageLibrary
from qualtrics_survey_python_sdk.type.header_mid import HeaderMid
from qualtrics_survey_python_sdk.type.survey_id import SurveyID
from qualtrics_survey_python_sdk.type.password_protection import PasswordProtection
from qualtrics_survey_python_sdk.type.survey_termination import SurveyTermination
from qualtrics_survey_python_sdk.type.response_summary import ResponseSummary
from qualtrics_survey_python_sdk.type.survey_expiration_date import SurveyExpirationDate
from qualtrics_survey_python_sdk.type.language_code import LanguageCode
from qualtrics_survey_python_sdk.type.ballot_box_stuffing_prevention_behavior import BallotBoxStuffingPreventionBehavior
from qualtrics_survey_python_sdk.type.survey_name import SurveyName
from qualtrics_survey_python_sdk.type.next_button_mid import NextButtonMid
from qualtrics_survey_python_sdk.type.previous_button_mid import PreviousButtonMid
from qualtrics_survey_python_sdk.type.internal_server_error_response import InternalServerErrorResponse
from qualtrics_survey_python_sdk.type.invalid_request_error_response import InvalidRequestErrorResponse
from qualtrics_survey_python_sdk.type.validate_message import ValidateMessage
from qualtrics_survey_python_sdk.type.email_thank_you import EmailThankYou
from qualtrics_survey_python_sdk.type.eos_message import EOSMessage
from qualtrics_survey_python_sdk.type.ballot_box_stuffing_prevention_message import BallotBoxStuffingPreventionMessage
from qualtrics_survey_python_sdk.type.validation_message import ValidationMessage
from qualtrics_survey_python_sdk.type.page_transition import PageTransition
from qualtrics_survey_python_sdk.type.forbidden_request_error_response import ForbiddenRequestErrorResponse
from qualtrics_survey_python_sdk.type.request_successful_response import RequestSuccessfulResponse
from qualtrics_survey_python_sdk.type.survey_meta_description import SurveyMetaDescription
from qualtrics_survey_python_sdk.type.available_languages import AvailableLanguages
from qualtrics_survey_python_sdk.type.unauthorized_request_error_response import UnauthorizedRequestErrorResponse
from qualtrics_survey_python_sdk.type.survey_title import SurveyTitle
from qualtrics_survey_python_sdk.type.inactive_message_library import InactiveMessageLibrary
from qualtrics_survey_python_sdk.type.thank_you_email_message import ThankYouEmailMessage
from qualtrics_survey_python_sdk.type.inactive_survey import InactiveSurvey
from qualtrics_survey_python_sdk.type.survey_protection import SurveyProtection
from qualtrics_survey_python_sdk.type.partial_data_close_after import PartialDataCloseAfter
from qualtrics_survey_python_sdk.type.progress_bar_display import ProgressBarDisplay
from qualtrics_survey_python_sdk.type.inactive_message import InactiveMessage
from qualtrics_survey_python_sdk.type.survey_expiration import SurveyExpiration
from qualtrics_survey_python_sdk.type.survey_options import SurveyOptions
from qualtrics_survey_python_sdk.type.ballot_box_stuffing_prevention_message_library import BallotBoxStuffingPreventionMessageLibrary
from qualtrics_survey_python_sdk.type.questions_per_page import QuestionsPerPage
from qualtrics_survey_python_sdk.type.thank_you_email_message_library import ThankYouEmailMessageLibrary
from qualtrics_survey_python_sdk.type.skin import Skin
from qualtrics_survey_python_sdk.type.survey_start_date import SurveyStartDate
from qualtrics_survey_python_sdk.type.anonymize_response import AnonymizeResponse
from qualtrics_survey_python_sdk.type.collect_geo_location import CollectGeoLocation
from qualtrics_survey_python_sdk.type.footer_mid import FooterMid
from qualtrics_survey_python_sdk.type.referer_check import RefererCheck
from qualtrics_survey_python_sdk.type.partial_data import PartialData

from ...api_client import Dictionary
from qualtrics_survey_python_sdk.pydantic.referer_check import RefererCheck as RefererCheckPydantic
from qualtrics_survey_python_sdk.pydantic.questions_per_page import QuestionsPerPage as QuestionsPerPagePydantic
from qualtrics_survey_python_sdk.pydantic.validate_message import ValidateMessage as ValidateMessagePydantic
from qualtrics_survey_python_sdk.pydantic.secure_response_files import SecureResponseFiles as SecureResponseFilesPydantic
from qualtrics_survey_python_sdk.pydantic.ballot_box_stuffing_prevention_behavior import BallotBoxStuffingPreventionBehavior as BallotBoxStuffingPreventionBehaviorPydantic
from qualtrics_survey_python_sdk.pydantic.partial_data import PartialData as PartialDataPydantic
from qualtrics_survey_python_sdk.pydantic.ballot_box_stuffing_prevention_message import BallotBoxStuffingPreventionMessage as BallotBoxStuffingPreventionMessagePydantic
from qualtrics_survey_python_sdk.pydantic.password_protection import PasswordProtection as PasswordProtectionPydantic
from qualtrics_survey_python_sdk.pydantic.inactive_survey import InactiveSurvey as InactiveSurveyPydantic
from qualtrics_survey_python_sdk.pydantic.custom_languages import CustomLanguages as CustomLanguagesPydantic
from qualtrics_survey_python_sdk.pydantic.survey_expiration import SurveyExpiration as SurveyExpirationPydantic
from qualtrics_survey_python_sdk.pydantic.ballot_box_stuffing_prevention_message_library import BallotBoxStuffingPreventionMessageLibrary as BallotBoxStuffingPreventionMessageLibraryPydantic
from qualtrics_survey_python_sdk.pydantic.progress_bar_display import ProgressBarDisplay as ProgressBarDisplayPydantic
from qualtrics_survey_python_sdk.pydantic.partial_data_close_after import PartialDataCloseAfter as PartialDataCloseAfterPydantic
from qualtrics_survey_python_sdk.pydantic.collect_geo_location import CollectGeoLocation as CollectGeoLocationPydantic
from qualtrics_survey_python_sdk.pydantic.survey_protection import SurveyProtection as SurveyProtectionPydantic
from qualtrics_survey_python_sdk.pydantic.no_index import NoIndex as NoIndexPydantic
from qualtrics_survey_python_sdk.pydantic.forbidden_request_error_response import ForbiddenRequestErrorResponse as ForbiddenRequestErrorResponsePydantic
from qualtrics_survey_python_sdk.pydantic.validation_message import ValidationMessage as ValidationMessagePydantic
from qualtrics_survey_python_sdk.pydantic.recaptcha_v3 import RecaptchaV3 as RecaptchaV3Pydantic
from qualtrics_survey_python_sdk.pydantic.email_thank_you import EmailThankYou as EmailThankYouPydantic
from qualtrics_survey_python_sdk.pydantic.survey_name import SurveyName as SurveyNamePydantic
from qualtrics_survey_python_sdk.pydantic.previous_button_mid import PreviousButtonMid as PreviousButtonMidPydantic
from qualtrics_survey_python_sdk.pydantic.language_code import LanguageCode as LanguageCodePydantic
from qualtrics_survey_python_sdk.pydantic.thank_you_email_message import ThankYouEmailMessage as ThankYouEmailMessagePydantic
from qualtrics_survey_python_sdk.pydantic.survey_id import SurveyID as SurveyIDPydantic
from qualtrics_survey_python_sdk.pydantic.survey_termination import SurveyTermination as SurveyTerminationPydantic
from qualtrics_survey_python_sdk.pydantic.survey_start_date import SurveyStartDate as SurveyStartDatePydantic
from qualtrics_survey_python_sdk.pydantic.footer_mid import FooterMid as FooterMidPydantic
from qualtrics_survey_python_sdk.pydantic.inactive_message_library import InactiveMessageLibrary as InactiveMessageLibraryPydantic
from qualtrics_survey_python_sdk.pydantic.unauthorized_request_error_response import UnauthorizedRequestErrorResponse as UnauthorizedRequestErrorResponsePydantic
from qualtrics_survey_python_sdk.pydantic.survey_title import SurveyTitle as SurveyTitlePydantic
from qualtrics_survey_python_sdk.pydantic.available_languages import AvailableLanguages as AvailableLanguagesPydantic
from qualtrics_survey_python_sdk.pydantic.inactive_message import InactiveMessage as InactiveMessagePydantic
from qualtrics_survey_python_sdk.pydantic.response_summary import ResponseSummary as ResponseSummaryPydantic
from qualtrics_survey_python_sdk.pydantic.next_button_mid import NextButtonMid as NextButtonMidPydantic
from qualtrics_survey_python_sdk.pydantic.internal_server_error_response import InternalServerErrorResponse as InternalServerErrorResponsePydantic
from qualtrics_survey_python_sdk.pydantic.anonymize_response import AnonymizeResponse as AnonymizeResponsePydantic
from qualtrics_survey_python_sdk.pydantic.survey_expiration_date import SurveyExpirationDate as SurveyExpirationDatePydantic
from qualtrics_survey_python_sdk.pydantic.validation_message_library import ValidationMessageLibrary as ValidationMessageLibraryPydantic
from qualtrics_survey_python_sdk.pydantic.page_transition import PageTransition as PageTransitionPydantic
from qualtrics_survey_python_sdk.pydantic.skin import Skin as SkinPydantic
from qualtrics_survey_python_sdk.pydantic.invalid_request_error_response import InvalidRequestErrorResponse as InvalidRequestErrorResponsePydantic
from qualtrics_survey_python_sdk.pydantic.eos_message import EOSMessage as EOSMessagePydantic
from qualtrics_survey_python_sdk.pydantic.request_successful_response import RequestSuccessfulResponse as RequestSuccessfulResponsePydantic
from qualtrics_survey_python_sdk.pydantic.header_mid import HeaderMid as HeaderMidPydantic
from qualtrics_survey_python_sdk.pydantic.thank_you_email_message_library import ThankYouEmailMessageLibrary as ThankYouEmailMessageLibraryPydantic
from qualtrics_survey_python_sdk.pydantic.survey_meta_description import SurveyMetaDescription as SurveyMetaDescriptionPydantic
from qualtrics_survey_python_sdk.pydantic.survey_options import SurveyOptions as SurveyOptionsPydantic

# Path params
SurveyIdSchema = schemas.Schema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'surveyId': typing.Union[SurveyIDSchema, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_survey_id = api_client.PathParameter(
    name="surveyId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=SurveyIDSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = SurveyOptionsSchema


request_body_survey_options = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = RequestSuccessfulResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: RequestSuccessfulResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: RequestSuccessfulResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = InvalidRequestErrorResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: InvalidRequestErrorResponse


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: InvalidRequestErrorResponse


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = UnauthorizedRequestErrorResponseSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: UnauthorizedRequestErrorResponse


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: UnauthorizedRequestErrorResponse


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationJson = ForbiddenRequestErrorResponseSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: ForbiddenRequestErrorResponse


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: ForbiddenRequestErrorResponse


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)
SchemaFor500ResponseBodyApplicationJson = InternalServerErrorResponseSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: InternalServerErrorResponse


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: InternalServerErrorResponse


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _update_options_mapped_args(
        self,
        back_button: bool,
        ballot_box_stuffing_prevention: bool,
        header: str,
        footer: str,
        no_index: NoIndex,
        next_button: str,
        partial_data: PartialData,
        previous_button: str,
        progress_bar_display: ProgressBarDisplay,
        save_and_continue: bool,
        secure_response_files: SecureResponseFiles,
        skin: Skin,
        survey_expiration: SurveyExpiration,
        survey_protection: SurveyProtection,
        survey_termination: SurveyTermination,
        validation_message: ValidationMessage,
        survey_id: SurveyID,
        anonymize_response: typing.Optional[AnonymizeResponse] = None,
        autofocus: typing.Optional[bool] = None,
        autoadvance: typing.Optional[bool] = None,
        autoadvance_pages: typing.Optional[bool] = None,
        available_languages: typing.Optional[AvailableLanguages] = None,
        ballot_box_stuffing_prevention_behavior: typing.Optional[BallotBoxStuffingPreventionBehavior] = None,
        ballot_box_stuffing_prevention_message: typing.Optional[BallotBoxStuffingPreventionMessage] = None,
        ballot_box_stuffing_prevention_message_library: typing.Optional[BallotBoxStuffingPreventionMessageLibrary] = None,
        ballot_box_stuffing_prevention_url: typing.Optional[str] = None,
        collect_geo_location: typing.Optional[CollectGeoLocation] = None,
        custom_styles: typing.Optional[str] = None,
        custom_languages: typing.Optional[CustomLanguages] = None,
        email_thank_you: typing.Optional[EmailThankYou] = None,
        eos_message: typing.Optional[EOSMessage] = None,
        eos_redirect_url: typing.Optional[str] = None,
        external_css: typing.Optional[str] = None,
        header_mid: typing.Optional[HeaderMid] = None,
        footer_mid: typing.Optional[FooterMid] = None,
        inactive_survey: typing.Optional[InactiveSurvey] = None,
        inactive_message: typing.Optional[InactiveMessage] = None,
        inactive_message_library: typing.Optional[InactiveMessageLibrary] = None,
        next_button_mid: typing.Optional[NextButtonMid] = None,
        page_transition: typing.Optional[PageTransition] = None,
        partial_data_close_after: typing.Optional[PartialDataCloseAfter] = None,
        password: typing.Optional[str] = None,
        password_protection: typing.Optional[PasswordProtection] = None,
        previous_button_mid: typing.Optional[PreviousButtonMid] = None,
        questions_per_page: typing.Optional[QuestionsPerPage] = None,
        recaptcha_v3: typing.Optional[RecaptchaV3] = None,
        referer_check: typing.Optional[RefererCheck] = None,
        referer_url: typing.Optional[str] = None,
        response_summary: typing.Optional[ResponseSummary] = None,
        survey_expiration_date: typing.Optional[SurveyExpirationDate] = None,
        survey_meta_description: typing.Optional[SurveyMetaDescription] = None,
        survey_language: typing.Optional[LanguageCode] = None,
        survey_name: typing.Optional[SurveyName] = None,
        survey_start_date: typing.Optional[SurveyStartDate] = None,
        survey_title: typing.Optional[SurveyTitle] = None,
        thank_you_email_message: typing.Optional[ThankYouEmailMessage] = None,
        thank_you_email_message_library: typing.Optional[ThankYouEmailMessageLibrary] = None,
        validate_message: typing.Optional[ValidateMessage] = None,
        validation_message_library: typing.Optional[ValidationMessageLibrary] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if anonymize_response is not None:
            _body["AnonymizeResponse"] = anonymize_response
        if autofocus is not None:
            _body["Autofocus"] = autofocus
        if autoadvance is not None:
            _body["Autoadvance"] = autoadvance
        if autoadvance_pages is not None:
            _body["AutoadvancePages"] = autoadvance_pages
        if available_languages is not None:
            _body["AvailableLanguages"] = available_languages
        if back_button is not None:
            _body["BackButton"] = back_button
        if ballot_box_stuffing_prevention is not None:
            _body["BallotBoxStuffingPrevention"] = ballot_box_stuffing_prevention
        if ballot_box_stuffing_prevention_behavior is not None:
            _body["BallotBoxStuffingPreventionBehavior"] = ballot_box_stuffing_prevention_behavior
        if ballot_box_stuffing_prevention_message is not None:
            _body["BallotBoxStuffingPreventionMessage"] = ballot_box_stuffing_prevention_message
        if ballot_box_stuffing_prevention_message_library is not None:
            _body["BallotBoxStuffingPreventionMessageLibrary"] = ballot_box_stuffing_prevention_message_library
        if ballot_box_stuffing_prevention_url is not None:
            _body["BallotBoxStuffingPreventionURL"] = ballot_box_stuffing_prevention_url
        if collect_geo_location is not None:
            _body["CollectGeoLocation"] = collect_geo_location
        if custom_styles is not None:
            _body["CustomStyles"] = custom_styles
        if custom_languages is not None:
            _body["CustomLanguages"] = custom_languages
        if email_thank_you is not None:
            _body["EmailThankYou"] = email_thank_you
        if eos_message is not None:
            _body["EOSMessage"] = eos_message
        if eos_redirect_url is not None:
            _body["EOSRedirectURL"] = eos_redirect_url
        if external_css is not None:
            _body["ExternalCSS"] = external_css
        if header_mid is not None:
            _body["headerMid"] = header_mid
        if header is not None:
            _body["Header"] = header
        if footer_mid is not None:
            _body["footerMid"] = footer_mid
        if footer is not None:
            _body["Footer"] = footer
        if inactive_survey is not None:
            _body["InactiveSurvey"] = inactive_survey
        if inactive_message is not None:
            _body["InactiveMessage"] = inactive_message
        if inactive_message_library is not None:
            _body["InactiveMessageLibrary"] = inactive_message_library
        if no_index is not None:
            _body["NoIndex"] = no_index
        if next_button_mid is not None:
            _body["nextButtonMid"] = next_button_mid
        if next_button is not None:
            _body["NextButton"] = next_button
        if page_transition is not None:
            _body["PageTransition"] = page_transition
        if partial_data is not None:
            _body["PartialData"] = partial_data
        if partial_data_close_after is not None:
            _body["PartialDataCloseAfter"] = partial_data_close_after
        if password is not None:
            _body["Password"] = password
        if password_protection is not None:
            _body["PasswordProtection"] = password_protection
        if previous_button_mid is not None:
            _body["previousButtonMid"] = previous_button_mid
        if previous_button is not None:
            _body["PreviousButton"] = previous_button
        if progress_bar_display is not None:
            _body["ProgressBarDisplay"] = progress_bar_display
        if questions_per_page is not None:
            _body["QuestionsPerPage"] = questions_per_page
        if recaptcha_v3 is not None:
            _body["RecaptchaV3"] = recaptcha_v3
        if referer_check is not None:
            _body["RefererCheck"] = referer_check
        if referer_url is not None:
            _body["RefererURL"] = referer_url
        if response_summary is not None:
            _body["ResponseSummary"] = response_summary
        if save_and_continue is not None:
            _body["SaveAndContinue"] = save_and_continue
        if secure_response_files is not None:
            _body["SecureResponseFiles"] = secure_response_files
        if skin is not None:
            _body["Skin"] = skin
        if survey_expiration is not None:
            _body["SurveyExpiration"] = survey_expiration
        if survey_expiration_date is not None:
            _body["SurveyExpirationDate"] = survey_expiration_date
        if survey_meta_description is not None:
            _body["SurveyMetaDescription"] = survey_meta_description
        if survey_language is not None:
            _body["SurveyLanguage"] = survey_language
        if survey_name is not None:
            _body["SurveyName"] = survey_name
        if survey_protection is not None:
            _body["SurveyProtection"] = survey_protection
        if survey_start_date is not None:
            _body["SurveyStartDate"] = survey_start_date
        if survey_termination is not None:
            _body["SurveyTermination"] = survey_termination
        if survey_title is not None:
            _body["SurveyTitle"] = survey_title
        if thank_you_email_message is not None:
            _body["ThankYouEmailMessage"] = thank_you_email_message
        if thank_you_email_message_library is not None:
            _body["ThankYouEmailMessageLibrary"] = thank_you_email_message_library
        if validate_message is not None:
            _body["ValidateMessage"] = validate_message
        if validation_message is not None:
            _body["ValidationMessage"] = validation_message
        if validation_message_library is not None:
            _body["ValidationMessageLibrary"] = validation_message_library
        args.body = _body
        if survey_id is not None:
            _path_params["surveyId"] = survey_id
        args.path = _path_params
        return args

    async def _aupdate_options_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Update Options
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_survey_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/survey-definitions/{surveyId}/options',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_survey_options.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _update_options_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Update Options
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_survey_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/survey-definitions/{surveyId}/options',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_survey_options.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class UpdateOptionsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_options(
        self,
        back_button: bool,
        ballot_box_stuffing_prevention: bool,
        header: str,
        footer: str,
        no_index: NoIndex,
        next_button: str,
        partial_data: PartialData,
        previous_button: str,
        progress_bar_display: ProgressBarDisplay,
        save_and_continue: bool,
        secure_response_files: SecureResponseFiles,
        skin: Skin,
        survey_expiration: SurveyExpiration,
        survey_protection: SurveyProtection,
        survey_termination: SurveyTermination,
        validation_message: ValidationMessage,
        survey_id: SurveyID,
        anonymize_response: typing.Optional[AnonymizeResponse] = None,
        autofocus: typing.Optional[bool] = None,
        autoadvance: typing.Optional[bool] = None,
        autoadvance_pages: typing.Optional[bool] = None,
        available_languages: typing.Optional[AvailableLanguages] = None,
        ballot_box_stuffing_prevention_behavior: typing.Optional[BallotBoxStuffingPreventionBehavior] = None,
        ballot_box_stuffing_prevention_message: typing.Optional[BallotBoxStuffingPreventionMessage] = None,
        ballot_box_stuffing_prevention_message_library: typing.Optional[BallotBoxStuffingPreventionMessageLibrary] = None,
        ballot_box_stuffing_prevention_url: typing.Optional[str] = None,
        collect_geo_location: typing.Optional[CollectGeoLocation] = None,
        custom_styles: typing.Optional[str] = None,
        custom_languages: typing.Optional[CustomLanguages] = None,
        email_thank_you: typing.Optional[EmailThankYou] = None,
        eos_message: typing.Optional[EOSMessage] = None,
        eos_redirect_url: typing.Optional[str] = None,
        external_css: typing.Optional[str] = None,
        header_mid: typing.Optional[HeaderMid] = None,
        footer_mid: typing.Optional[FooterMid] = None,
        inactive_survey: typing.Optional[InactiveSurvey] = None,
        inactive_message: typing.Optional[InactiveMessage] = None,
        inactive_message_library: typing.Optional[InactiveMessageLibrary] = None,
        next_button_mid: typing.Optional[NextButtonMid] = None,
        page_transition: typing.Optional[PageTransition] = None,
        partial_data_close_after: typing.Optional[PartialDataCloseAfter] = None,
        password: typing.Optional[str] = None,
        password_protection: typing.Optional[PasswordProtection] = None,
        previous_button_mid: typing.Optional[PreviousButtonMid] = None,
        questions_per_page: typing.Optional[QuestionsPerPage] = None,
        recaptcha_v3: typing.Optional[RecaptchaV3] = None,
        referer_check: typing.Optional[RefererCheck] = None,
        referer_url: typing.Optional[str] = None,
        response_summary: typing.Optional[ResponseSummary] = None,
        survey_expiration_date: typing.Optional[SurveyExpirationDate] = None,
        survey_meta_description: typing.Optional[SurveyMetaDescription] = None,
        survey_language: typing.Optional[LanguageCode] = None,
        survey_name: typing.Optional[SurveyName] = None,
        survey_start_date: typing.Optional[SurveyStartDate] = None,
        survey_title: typing.Optional[SurveyTitle] = None,
        thank_you_email_message: typing.Optional[ThankYouEmailMessage] = None,
        thank_you_email_message_library: typing.Optional[ThankYouEmailMessageLibrary] = None,
        validate_message: typing.Optional[ValidateMessage] = None,
        validation_message_library: typing.Optional[ValidationMessageLibrary] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_options_mapped_args(
            back_button=back_button,
            ballot_box_stuffing_prevention=ballot_box_stuffing_prevention,
            header=header,
            footer=footer,
            no_index=no_index,
            next_button=next_button,
            partial_data=partial_data,
            previous_button=previous_button,
            progress_bar_display=progress_bar_display,
            save_and_continue=save_and_continue,
            secure_response_files=secure_response_files,
            skin=skin,
            survey_expiration=survey_expiration,
            survey_protection=survey_protection,
            survey_termination=survey_termination,
            validation_message=validation_message,
            survey_id=survey_id,
            anonymize_response=anonymize_response,
            autofocus=autofocus,
            autoadvance=autoadvance,
            autoadvance_pages=autoadvance_pages,
            available_languages=available_languages,
            ballot_box_stuffing_prevention_behavior=ballot_box_stuffing_prevention_behavior,
            ballot_box_stuffing_prevention_message=ballot_box_stuffing_prevention_message,
            ballot_box_stuffing_prevention_message_library=ballot_box_stuffing_prevention_message_library,
            ballot_box_stuffing_prevention_url=ballot_box_stuffing_prevention_url,
            collect_geo_location=collect_geo_location,
            custom_styles=custom_styles,
            custom_languages=custom_languages,
            email_thank_you=email_thank_you,
            eos_message=eos_message,
            eos_redirect_url=eos_redirect_url,
            external_css=external_css,
            header_mid=header_mid,
            footer_mid=footer_mid,
            inactive_survey=inactive_survey,
            inactive_message=inactive_message,
            inactive_message_library=inactive_message_library,
            next_button_mid=next_button_mid,
            page_transition=page_transition,
            partial_data_close_after=partial_data_close_after,
            password=password,
            password_protection=password_protection,
            previous_button_mid=previous_button_mid,
            questions_per_page=questions_per_page,
            recaptcha_v3=recaptcha_v3,
            referer_check=referer_check,
            referer_url=referer_url,
            response_summary=response_summary,
            survey_expiration_date=survey_expiration_date,
            survey_meta_description=survey_meta_description,
            survey_language=survey_language,
            survey_name=survey_name,
            survey_start_date=survey_start_date,
            survey_title=survey_title,
            thank_you_email_message=thank_you_email_message,
            thank_you_email_message_library=thank_you_email_message_library,
            validate_message=validate_message,
            validation_message_library=validation_message_library,
        )
        return await self._aupdate_options_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_options(
        self,
        back_button: bool,
        ballot_box_stuffing_prevention: bool,
        header: str,
        footer: str,
        no_index: NoIndex,
        next_button: str,
        partial_data: PartialData,
        previous_button: str,
        progress_bar_display: ProgressBarDisplay,
        save_and_continue: bool,
        secure_response_files: SecureResponseFiles,
        skin: Skin,
        survey_expiration: SurveyExpiration,
        survey_protection: SurveyProtection,
        survey_termination: SurveyTermination,
        validation_message: ValidationMessage,
        survey_id: SurveyID,
        anonymize_response: typing.Optional[AnonymizeResponse] = None,
        autofocus: typing.Optional[bool] = None,
        autoadvance: typing.Optional[bool] = None,
        autoadvance_pages: typing.Optional[bool] = None,
        available_languages: typing.Optional[AvailableLanguages] = None,
        ballot_box_stuffing_prevention_behavior: typing.Optional[BallotBoxStuffingPreventionBehavior] = None,
        ballot_box_stuffing_prevention_message: typing.Optional[BallotBoxStuffingPreventionMessage] = None,
        ballot_box_stuffing_prevention_message_library: typing.Optional[BallotBoxStuffingPreventionMessageLibrary] = None,
        ballot_box_stuffing_prevention_url: typing.Optional[str] = None,
        collect_geo_location: typing.Optional[CollectGeoLocation] = None,
        custom_styles: typing.Optional[str] = None,
        custom_languages: typing.Optional[CustomLanguages] = None,
        email_thank_you: typing.Optional[EmailThankYou] = None,
        eos_message: typing.Optional[EOSMessage] = None,
        eos_redirect_url: typing.Optional[str] = None,
        external_css: typing.Optional[str] = None,
        header_mid: typing.Optional[HeaderMid] = None,
        footer_mid: typing.Optional[FooterMid] = None,
        inactive_survey: typing.Optional[InactiveSurvey] = None,
        inactive_message: typing.Optional[InactiveMessage] = None,
        inactive_message_library: typing.Optional[InactiveMessageLibrary] = None,
        next_button_mid: typing.Optional[NextButtonMid] = None,
        page_transition: typing.Optional[PageTransition] = None,
        partial_data_close_after: typing.Optional[PartialDataCloseAfter] = None,
        password: typing.Optional[str] = None,
        password_protection: typing.Optional[PasswordProtection] = None,
        previous_button_mid: typing.Optional[PreviousButtonMid] = None,
        questions_per_page: typing.Optional[QuestionsPerPage] = None,
        recaptcha_v3: typing.Optional[RecaptchaV3] = None,
        referer_check: typing.Optional[RefererCheck] = None,
        referer_url: typing.Optional[str] = None,
        response_summary: typing.Optional[ResponseSummary] = None,
        survey_expiration_date: typing.Optional[SurveyExpirationDate] = None,
        survey_meta_description: typing.Optional[SurveyMetaDescription] = None,
        survey_language: typing.Optional[LanguageCode] = None,
        survey_name: typing.Optional[SurveyName] = None,
        survey_start_date: typing.Optional[SurveyStartDate] = None,
        survey_title: typing.Optional[SurveyTitle] = None,
        thank_you_email_message: typing.Optional[ThankYouEmailMessage] = None,
        thank_you_email_message_library: typing.Optional[ThankYouEmailMessageLibrary] = None,
        validate_message: typing.Optional[ValidateMessage] = None,
        validation_message_library: typing.Optional[ValidationMessageLibrary] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_options_mapped_args(
            back_button=back_button,
            ballot_box_stuffing_prevention=ballot_box_stuffing_prevention,
            header=header,
            footer=footer,
            no_index=no_index,
            next_button=next_button,
            partial_data=partial_data,
            previous_button=previous_button,
            progress_bar_display=progress_bar_display,
            save_and_continue=save_and_continue,
            secure_response_files=secure_response_files,
            skin=skin,
            survey_expiration=survey_expiration,
            survey_protection=survey_protection,
            survey_termination=survey_termination,
            validation_message=validation_message,
            survey_id=survey_id,
            anonymize_response=anonymize_response,
            autofocus=autofocus,
            autoadvance=autoadvance,
            autoadvance_pages=autoadvance_pages,
            available_languages=available_languages,
            ballot_box_stuffing_prevention_behavior=ballot_box_stuffing_prevention_behavior,
            ballot_box_stuffing_prevention_message=ballot_box_stuffing_prevention_message,
            ballot_box_stuffing_prevention_message_library=ballot_box_stuffing_prevention_message_library,
            ballot_box_stuffing_prevention_url=ballot_box_stuffing_prevention_url,
            collect_geo_location=collect_geo_location,
            custom_styles=custom_styles,
            custom_languages=custom_languages,
            email_thank_you=email_thank_you,
            eos_message=eos_message,
            eos_redirect_url=eos_redirect_url,
            external_css=external_css,
            header_mid=header_mid,
            footer_mid=footer_mid,
            inactive_survey=inactive_survey,
            inactive_message=inactive_message,
            inactive_message_library=inactive_message_library,
            next_button_mid=next_button_mid,
            page_transition=page_transition,
            partial_data_close_after=partial_data_close_after,
            password=password,
            password_protection=password_protection,
            previous_button_mid=previous_button_mid,
            questions_per_page=questions_per_page,
            recaptcha_v3=recaptcha_v3,
            referer_check=referer_check,
            referer_url=referer_url,
            response_summary=response_summary,
            survey_expiration_date=survey_expiration_date,
            survey_meta_description=survey_meta_description,
            survey_language=survey_language,
            survey_name=survey_name,
            survey_start_date=survey_start_date,
            survey_title=survey_title,
            thank_you_email_message=thank_you_email_message,
            thank_you_email_message_library=thank_you_email_message_library,
            validate_message=validate_message,
            validation_message_library=validation_message_library,
        )
        return self._update_options_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdateOptions(BaseApi):

    async def aupdate_options(
        self,
        back_button: bool,
        ballot_box_stuffing_prevention: bool,
        header: str,
        footer: str,
        no_index: NoIndex,
        next_button: str,
        partial_data: PartialData,
        previous_button: str,
        progress_bar_display: ProgressBarDisplay,
        save_and_continue: bool,
        secure_response_files: SecureResponseFiles,
        skin: Skin,
        survey_expiration: SurveyExpiration,
        survey_protection: SurveyProtection,
        survey_termination: SurveyTermination,
        validation_message: ValidationMessage,
        survey_id: SurveyID,
        anonymize_response: typing.Optional[AnonymizeResponse] = None,
        autofocus: typing.Optional[bool] = None,
        autoadvance: typing.Optional[bool] = None,
        autoadvance_pages: typing.Optional[bool] = None,
        available_languages: typing.Optional[AvailableLanguages] = None,
        ballot_box_stuffing_prevention_behavior: typing.Optional[BallotBoxStuffingPreventionBehavior] = None,
        ballot_box_stuffing_prevention_message: typing.Optional[BallotBoxStuffingPreventionMessage] = None,
        ballot_box_stuffing_prevention_message_library: typing.Optional[BallotBoxStuffingPreventionMessageLibrary] = None,
        ballot_box_stuffing_prevention_url: typing.Optional[str] = None,
        collect_geo_location: typing.Optional[CollectGeoLocation] = None,
        custom_styles: typing.Optional[str] = None,
        custom_languages: typing.Optional[CustomLanguages] = None,
        email_thank_you: typing.Optional[EmailThankYou] = None,
        eos_message: typing.Optional[EOSMessage] = None,
        eos_redirect_url: typing.Optional[str] = None,
        external_css: typing.Optional[str] = None,
        header_mid: typing.Optional[HeaderMid] = None,
        footer_mid: typing.Optional[FooterMid] = None,
        inactive_survey: typing.Optional[InactiveSurvey] = None,
        inactive_message: typing.Optional[InactiveMessage] = None,
        inactive_message_library: typing.Optional[InactiveMessageLibrary] = None,
        next_button_mid: typing.Optional[NextButtonMid] = None,
        page_transition: typing.Optional[PageTransition] = None,
        partial_data_close_after: typing.Optional[PartialDataCloseAfter] = None,
        password: typing.Optional[str] = None,
        password_protection: typing.Optional[PasswordProtection] = None,
        previous_button_mid: typing.Optional[PreviousButtonMid] = None,
        questions_per_page: typing.Optional[QuestionsPerPage] = None,
        recaptcha_v3: typing.Optional[RecaptchaV3] = None,
        referer_check: typing.Optional[RefererCheck] = None,
        referer_url: typing.Optional[str] = None,
        response_summary: typing.Optional[ResponseSummary] = None,
        survey_expiration_date: typing.Optional[SurveyExpirationDate] = None,
        survey_meta_description: typing.Optional[SurveyMetaDescription] = None,
        survey_language: typing.Optional[LanguageCode] = None,
        survey_name: typing.Optional[SurveyName] = None,
        survey_start_date: typing.Optional[SurveyStartDate] = None,
        survey_title: typing.Optional[SurveyTitle] = None,
        thank_you_email_message: typing.Optional[ThankYouEmailMessage] = None,
        thank_you_email_message_library: typing.Optional[ThankYouEmailMessageLibrary] = None,
        validate_message: typing.Optional[ValidateMessage] = None,
        validation_message_library: typing.Optional[ValidationMessageLibrary] = None,
        validate: bool = False,
        **kwargs,
    ) -> RequestSuccessfulResponsePydantic:
        raw_response = await self.raw.aupdate_options(
            back_button=back_button,
            ballot_box_stuffing_prevention=ballot_box_stuffing_prevention,
            header=header,
            footer=footer,
            no_index=no_index,
            next_button=next_button,
            partial_data=partial_data,
            previous_button=previous_button,
            progress_bar_display=progress_bar_display,
            save_and_continue=save_and_continue,
            secure_response_files=secure_response_files,
            skin=skin,
            survey_expiration=survey_expiration,
            survey_protection=survey_protection,
            survey_termination=survey_termination,
            validation_message=validation_message,
            survey_id=survey_id,
            anonymize_response=anonymize_response,
            autofocus=autofocus,
            autoadvance=autoadvance,
            autoadvance_pages=autoadvance_pages,
            available_languages=available_languages,
            ballot_box_stuffing_prevention_behavior=ballot_box_stuffing_prevention_behavior,
            ballot_box_stuffing_prevention_message=ballot_box_stuffing_prevention_message,
            ballot_box_stuffing_prevention_message_library=ballot_box_stuffing_prevention_message_library,
            ballot_box_stuffing_prevention_url=ballot_box_stuffing_prevention_url,
            collect_geo_location=collect_geo_location,
            custom_styles=custom_styles,
            custom_languages=custom_languages,
            email_thank_you=email_thank_you,
            eos_message=eos_message,
            eos_redirect_url=eos_redirect_url,
            external_css=external_css,
            header_mid=header_mid,
            footer_mid=footer_mid,
            inactive_survey=inactive_survey,
            inactive_message=inactive_message,
            inactive_message_library=inactive_message_library,
            next_button_mid=next_button_mid,
            page_transition=page_transition,
            partial_data_close_after=partial_data_close_after,
            password=password,
            password_protection=password_protection,
            previous_button_mid=previous_button_mid,
            questions_per_page=questions_per_page,
            recaptcha_v3=recaptcha_v3,
            referer_check=referer_check,
            referer_url=referer_url,
            response_summary=response_summary,
            survey_expiration_date=survey_expiration_date,
            survey_meta_description=survey_meta_description,
            survey_language=survey_language,
            survey_name=survey_name,
            survey_start_date=survey_start_date,
            survey_title=survey_title,
            thank_you_email_message=thank_you_email_message,
            thank_you_email_message_library=thank_you_email_message_library,
            validate_message=validate_message,
            validation_message_library=validation_message_library,
            **kwargs,
        )
        if validate:
            return RequestSuccessfulResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(RequestSuccessfulResponsePydantic, raw_response.body)
    
    
    def update_options(
        self,
        back_button: bool,
        ballot_box_stuffing_prevention: bool,
        header: str,
        footer: str,
        no_index: NoIndex,
        next_button: str,
        partial_data: PartialData,
        previous_button: str,
        progress_bar_display: ProgressBarDisplay,
        save_and_continue: bool,
        secure_response_files: SecureResponseFiles,
        skin: Skin,
        survey_expiration: SurveyExpiration,
        survey_protection: SurveyProtection,
        survey_termination: SurveyTermination,
        validation_message: ValidationMessage,
        survey_id: SurveyID,
        anonymize_response: typing.Optional[AnonymizeResponse] = None,
        autofocus: typing.Optional[bool] = None,
        autoadvance: typing.Optional[bool] = None,
        autoadvance_pages: typing.Optional[bool] = None,
        available_languages: typing.Optional[AvailableLanguages] = None,
        ballot_box_stuffing_prevention_behavior: typing.Optional[BallotBoxStuffingPreventionBehavior] = None,
        ballot_box_stuffing_prevention_message: typing.Optional[BallotBoxStuffingPreventionMessage] = None,
        ballot_box_stuffing_prevention_message_library: typing.Optional[BallotBoxStuffingPreventionMessageLibrary] = None,
        ballot_box_stuffing_prevention_url: typing.Optional[str] = None,
        collect_geo_location: typing.Optional[CollectGeoLocation] = None,
        custom_styles: typing.Optional[str] = None,
        custom_languages: typing.Optional[CustomLanguages] = None,
        email_thank_you: typing.Optional[EmailThankYou] = None,
        eos_message: typing.Optional[EOSMessage] = None,
        eos_redirect_url: typing.Optional[str] = None,
        external_css: typing.Optional[str] = None,
        header_mid: typing.Optional[HeaderMid] = None,
        footer_mid: typing.Optional[FooterMid] = None,
        inactive_survey: typing.Optional[InactiveSurvey] = None,
        inactive_message: typing.Optional[InactiveMessage] = None,
        inactive_message_library: typing.Optional[InactiveMessageLibrary] = None,
        next_button_mid: typing.Optional[NextButtonMid] = None,
        page_transition: typing.Optional[PageTransition] = None,
        partial_data_close_after: typing.Optional[PartialDataCloseAfter] = None,
        password: typing.Optional[str] = None,
        password_protection: typing.Optional[PasswordProtection] = None,
        previous_button_mid: typing.Optional[PreviousButtonMid] = None,
        questions_per_page: typing.Optional[QuestionsPerPage] = None,
        recaptcha_v3: typing.Optional[RecaptchaV3] = None,
        referer_check: typing.Optional[RefererCheck] = None,
        referer_url: typing.Optional[str] = None,
        response_summary: typing.Optional[ResponseSummary] = None,
        survey_expiration_date: typing.Optional[SurveyExpirationDate] = None,
        survey_meta_description: typing.Optional[SurveyMetaDescription] = None,
        survey_language: typing.Optional[LanguageCode] = None,
        survey_name: typing.Optional[SurveyName] = None,
        survey_start_date: typing.Optional[SurveyStartDate] = None,
        survey_title: typing.Optional[SurveyTitle] = None,
        thank_you_email_message: typing.Optional[ThankYouEmailMessage] = None,
        thank_you_email_message_library: typing.Optional[ThankYouEmailMessageLibrary] = None,
        validate_message: typing.Optional[ValidateMessage] = None,
        validation_message_library: typing.Optional[ValidationMessageLibrary] = None,
        validate: bool = False,
    ) -> RequestSuccessfulResponsePydantic:
        raw_response = self.raw.update_options(
            back_button=back_button,
            ballot_box_stuffing_prevention=ballot_box_stuffing_prevention,
            header=header,
            footer=footer,
            no_index=no_index,
            next_button=next_button,
            partial_data=partial_data,
            previous_button=previous_button,
            progress_bar_display=progress_bar_display,
            save_and_continue=save_and_continue,
            secure_response_files=secure_response_files,
            skin=skin,
            survey_expiration=survey_expiration,
            survey_protection=survey_protection,
            survey_termination=survey_termination,
            validation_message=validation_message,
            survey_id=survey_id,
            anonymize_response=anonymize_response,
            autofocus=autofocus,
            autoadvance=autoadvance,
            autoadvance_pages=autoadvance_pages,
            available_languages=available_languages,
            ballot_box_stuffing_prevention_behavior=ballot_box_stuffing_prevention_behavior,
            ballot_box_stuffing_prevention_message=ballot_box_stuffing_prevention_message,
            ballot_box_stuffing_prevention_message_library=ballot_box_stuffing_prevention_message_library,
            ballot_box_stuffing_prevention_url=ballot_box_stuffing_prevention_url,
            collect_geo_location=collect_geo_location,
            custom_styles=custom_styles,
            custom_languages=custom_languages,
            email_thank_you=email_thank_you,
            eos_message=eos_message,
            eos_redirect_url=eos_redirect_url,
            external_css=external_css,
            header_mid=header_mid,
            footer_mid=footer_mid,
            inactive_survey=inactive_survey,
            inactive_message=inactive_message,
            inactive_message_library=inactive_message_library,
            next_button_mid=next_button_mid,
            page_transition=page_transition,
            partial_data_close_after=partial_data_close_after,
            password=password,
            password_protection=password_protection,
            previous_button_mid=previous_button_mid,
            questions_per_page=questions_per_page,
            recaptcha_v3=recaptcha_v3,
            referer_check=referer_check,
            referer_url=referer_url,
            response_summary=response_summary,
            survey_expiration_date=survey_expiration_date,
            survey_meta_description=survey_meta_description,
            survey_language=survey_language,
            survey_name=survey_name,
            survey_start_date=survey_start_date,
            survey_title=survey_title,
            thank_you_email_message=thank_you_email_message,
            thank_you_email_message_library=thank_you_email_message_library,
            validate_message=validate_message,
            validation_message_library=validation_message_library,
        )
        if validate:
            return RequestSuccessfulResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(RequestSuccessfulResponsePydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        back_button: bool,
        ballot_box_stuffing_prevention: bool,
        header: str,
        footer: str,
        no_index: NoIndex,
        next_button: str,
        partial_data: PartialData,
        previous_button: str,
        progress_bar_display: ProgressBarDisplay,
        save_and_continue: bool,
        secure_response_files: SecureResponseFiles,
        skin: Skin,
        survey_expiration: SurveyExpiration,
        survey_protection: SurveyProtection,
        survey_termination: SurveyTermination,
        validation_message: ValidationMessage,
        survey_id: SurveyID,
        anonymize_response: typing.Optional[AnonymizeResponse] = None,
        autofocus: typing.Optional[bool] = None,
        autoadvance: typing.Optional[bool] = None,
        autoadvance_pages: typing.Optional[bool] = None,
        available_languages: typing.Optional[AvailableLanguages] = None,
        ballot_box_stuffing_prevention_behavior: typing.Optional[BallotBoxStuffingPreventionBehavior] = None,
        ballot_box_stuffing_prevention_message: typing.Optional[BallotBoxStuffingPreventionMessage] = None,
        ballot_box_stuffing_prevention_message_library: typing.Optional[BallotBoxStuffingPreventionMessageLibrary] = None,
        ballot_box_stuffing_prevention_url: typing.Optional[str] = None,
        collect_geo_location: typing.Optional[CollectGeoLocation] = None,
        custom_styles: typing.Optional[str] = None,
        custom_languages: typing.Optional[CustomLanguages] = None,
        email_thank_you: typing.Optional[EmailThankYou] = None,
        eos_message: typing.Optional[EOSMessage] = None,
        eos_redirect_url: typing.Optional[str] = None,
        external_css: typing.Optional[str] = None,
        header_mid: typing.Optional[HeaderMid] = None,
        footer_mid: typing.Optional[FooterMid] = None,
        inactive_survey: typing.Optional[InactiveSurvey] = None,
        inactive_message: typing.Optional[InactiveMessage] = None,
        inactive_message_library: typing.Optional[InactiveMessageLibrary] = None,
        next_button_mid: typing.Optional[NextButtonMid] = None,
        page_transition: typing.Optional[PageTransition] = None,
        partial_data_close_after: typing.Optional[PartialDataCloseAfter] = None,
        password: typing.Optional[str] = None,
        password_protection: typing.Optional[PasswordProtection] = None,
        previous_button_mid: typing.Optional[PreviousButtonMid] = None,
        questions_per_page: typing.Optional[QuestionsPerPage] = None,
        recaptcha_v3: typing.Optional[RecaptchaV3] = None,
        referer_check: typing.Optional[RefererCheck] = None,
        referer_url: typing.Optional[str] = None,
        response_summary: typing.Optional[ResponseSummary] = None,
        survey_expiration_date: typing.Optional[SurveyExpirationDate] = None,
        survey_meta_description: typing.Optional[SurveyMetaDescription] = None,
        survey_language: typing.Optional[LanguageCode] = None,
        survey_name: typing.Optional[SurveyName] = None,
        survey_start_date: typing.Optional[SurveyStartDate] = None,
        survey_title: typing.Optional[SurveyTitle] = None,
        thank_you_email_message: typing.Optional[ThankYouEmailMessage] = None,
        thank_you_email_message_library: typing.Optional[ThankYouEmailMessageLibrary] = None,
        validate_message: typing.Optional[ValidateMessage] = None,
        validation_message_library: typing.Optional[ValidationMessageLibrary] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_options_mapped_args(
            back_button=back_button,
            ballot_box_stuffing_prevention=ballot_box_stuffing_prevention,
            header=header,
            footer=footer,
            no_index=no_index,
            next_button=next_button,
            partial_data=partial_data,
            previous_button=previous_button,
            progress_bar_display=progress_bar_display,
            save_and_continue=save_and_continue,
            secure_response_files=secure_response_files,
            skin=skin,
            survey_expiration=survey_expiration,
            survey_protection=survey_protection,
            survey_termination=survey_termination,
            validation_message=validation_message,
            survey_id=survey_id,
            anonymize_response=anonymize_response,
            autofocus=autofocus,
            autoadvance=autoadvance,
            autoadvance_pages=autoadvance_pages,
            available_languages=available_languages,
            ballot_box_stuffing_prevention_behavior=ballot_box_stuffing_prevention_behavior,
            ballot_box_stuffing_prevention_message=ballot_box_stuffing_prevention_message,
            ballot_box_stuffing_prevention_message_library=ballot_box_stuffing_prevention_message_library,
            ballot_box_stuffing_prevention_url=ballot_box_stuffing_prevention_url,
            collect_geo_location=collect_geo_location,
            custom_styles=custom_styles,
            custom_languages=custom_languages,
            email_thank_you=email_thank_you,
            eos_message=eos_message,
            eos_redirect_url=eos_redirect_url,
            external_css=external_css,
            header_mid=header_mid,
            footer_mid=footer_mid,
            inactive_survey=inactive_survey,
            inactive_message=inactive_message,
            inactive_message_library=inactive_message_library,
            next_button_mid=next_button_mid,
            page_transition=page_transition,
            partial_data_close_after=partial_data_close_after,
            password=password,
            password_protection=password_protection,
            previous_button_mid=previous_button_mid,
            questions_per_page=questions_per_page,
            recaptcha_v3=recaptcha_v3,
            referer_check=referer_check,
            referer_url=referer_url,
            response_summary=response_summary,
            survey_expiration_date=survey_expiration_date,
            survey_meta_description=survey_meta_description,
            survey_language=survey_language,
            survey_name=survey_name,
            survey_start_date=survey_start_date,
            survey_title=survey_title,
            thank_you_email_message=thank_you_email_message,
            thank_you_email_message_library=thank_you_email_message_library,
            validate_message=validate_message,
            validation_message_library=validation_message_library,
        )
        return await self._aupdate_options_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        back_button: bool,
        ballot_box_stuffing_prevention: bool,
        header: str,
        footer: str,
        no_index: NoIndex,
        next_button: str,
        partial_data: PartialData,
        previous_button: str,
        progress_bar_display: ProgressBarDisplay,
        save_and_continue: bool,
        secure_response_files: SecureResponseFiles,
        skin: Skin,
        survey_expiration: SurveyExpiration,
        survey_protection: SurveyProtection,
        survey_termination: SurveyTermination,
        validation_message: ValidationMessage,
        survey_id: SurveyID,
        anonymize_response: typing.Optional[AnonymizeResponse] = None,
        autofocus: typing.Optional[bool] = None,
        autoadvance: typing.Optional[bool] = None,
        autoadvance_pages: typing.Optional[bool] = None,
        available_languages: typing.Optional[AvailableLanguages] = None,
        ballot_box_stuffing_prevention_behavior: typing.Optional[BallotBoxStuffingPreventionBehavior] = None,
        ballot_box_stuffing_prevention_message: typing.Optional[BallotBoxStuffingPreventionMessage] = None,
        ballot_box_stuffing_prevention_message_library: typing.Optional[BallotBoxStuffingPreventionMessageLibrary] = None,
        ballot_box_stuffing_prevention_url: typing.Optional[str] = None,
        collect_geo_location: typing.Optional[CollectGeoLocation] = None,
        custom_styles: typing.Optional[str] = None,
        custom_languages: typing.Optional[CustomLanguages] = None,
        email_thank_you: typing.Optional[EmailThankYou] = None,
        eos_message: typing.Optional[EOSMessage] = None,
        eos_redirect_url: typing.Optional[str] = None,
        external_css: typing.Optional[str] = None,
        header_mid: typing.Optional[HeaderMid] = None,
        footer_mid: typing.Optional[FooterMid] = None,
        inactive_survey: typing.Optional[InactiveSurvey] = None,
        inactive_message: typing.Optional[InactiveMessage] = None,
        inactive_message_library: typing.Optional[InactiveMessageLibrary] = None,
        next_button_mid: typing.Optional[NextButtonMid] = None,
        page_transition: typing.Optional[PageTransition] = None,
        partial_data_close_after: typing.Optional[PartialDataCloseAfter] = None,
        password: typing.Optional[str] = None,
        password_protection: typing.Optional[PasswordProtection] = None,
        previous_button_mid: typing.Optional[PreviousButtonMid] = None,
        questions_per_page: typing.Optional[QuestionsPerPage] = None,
        recaptcha_v3: typing.Optional[RecaptchaV3] = None,
        referer_check: typing.Optional[RefererCheck] = None,
        referer_url: typing.Optional[str] = None,
        response_summary: typing.Optional[ResponseSummary] = None,
        survey_expiration_date: typing.Optional[SurveyExpirationDate] = None,
        survey_meta_description: typing.Optional[SurveyMetaDescription] = None,
        survey_language: typing.Optional[LanguageCode] = None,
        survey_name: typing.Optional[SurveyName] = None,
        survey_start_date: typing.Optional[SurveyStartDate] = None,
        survey_title: typing.Optional[SurveyTitle] = None,
        thank_you_email_message: typing.Optional[ThankYouEmailMessage] = None,
        thank_you_email_message_library: typing.Optional[ThankYouEmailMessageLibrary] = None,
        validate_message: typing.Optional[ValidateMessage] = None,
        validation_message_library: typing.Optional[ValidationMessageLibrary] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_options_mapped_args(
            back_button=back_button,
            ballot_box_stuffing_prevention=ballot_box_stuffing_prevention,
            header=header,
            footer=footer,
            no_index=no_index,
            next_button=next_button,
            partial_data=partial_data,
            previous_button=previous_button,
            progress_bar_display=progress_bar_display,
            save_and_continue=save_and_continue,
            secure_response_files=secure_response_files,
            skin=skin,
            survey_expiration=survey_expiration,
            survey_protection=survey_protection,
            survey_termination=survey_termination,
            validation_message=validation_message,
            survey_id=survey_id,
            anonymize_response=anonymize_response,
            autofocus=autofocus,
            autoadvance=autoadvance,
            autoadvance_pages=autoadvance_pages,
            available_languages=available_languages,
            ballot_box_stuffing_prevention_behavior=ballot_box_stuffing_prevention_behavior,
            ballot_box_stuffing_prevention_message=ballot_box_stuffing_prevention_message,
            ballot_box_stuffing_prevention_message_library=ballot_box_stuffing_prevention_message_library,
            ballot_box_stuffing_prevention_url=ballot_box_stuffing_prevention_url,
            collect_geo_location=collect_geo_location,
            custom_styles=custom_styles,
            custom_languages=custom_languages,
            email_thank_you=email_thank_you,
            eos_message=eos_message,
            eos_redirect_url=eos_redirect_url,
            external_css=external_css,
            header_mid=header_mid,
            footer_mid=footer_mid,
            inactive_survey=inactive_survey,
            inactive_message=inactive_message,
            inactive_message_library=inactive_message_library,
            next_button_mid=next_button_mid,
            page_transition=page_transition,
            partial_data_close_after=partial_data_close_after,
            password=password,
            password_protection=password_protection,
            previous_button_mid=previous_button_mid,
            questions_per_page=questions_per_page,
            recaptcha_v3=recaptcha_v3,
            referer_check=referer_check,
            referer_url=referer_url,
            response_summary=response_summary,
            survey_expiration_date=survey_expiration_date,
            survey_meta_description=survey_meta_description,
            survey_language=survey_language,
            survey_name=survey_name,
            survey_start_date=survey_start_date,
            survey_title=survey_title,
            thank_you_email_message=thank_you_email_message,
            thank_you_email_message_library=thank_you_email_message_library,
            validate_message=validate_message,
            validation_message_library=validation_message_library,
        )
        return self._update_options_oapg(
            body=args.body,
            path_params=args.path,
        )

