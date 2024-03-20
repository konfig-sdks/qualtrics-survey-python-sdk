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

from qualtrics_survey_python_sdk.pydantic.library_id import LibraryID
from qualtrics_survey_python_sdk.pydantic.message_id import MessageID

class CustomValidationMessage(BaseModel):
    library_i_d: LibraryID = Field(alias='libraryID')

    message_i_d: MessageID = Field(alias='messageID')

    # The unique identifier for the `subMessageID`.
    sub_message_i_d: Literal["VE_FORCE_RESPONSE", "VE_FORCE_RESPONSE_PLURAL", "VE_FORCE_RESPONSE_MORE", "VE_FORCE_RESPONSE_OTHER", "VE_MIN_CHOICES", "VE_MAX_CHOICES", "VE_MAX_CHOICES_PGR", "VE_MIN_CHOICES_MATRIX", "VE_MAX_CHOICES_MATRIX", "VE_MIN_CHOICES_HLText", "VE_MAX_CHOICES_HLText", "VE_INCORRECT_TOTAL", "VE_TOO_MANY_CHARACTERS", "VE_TOO_MANY_CHARACTERS_PLURAL", "VE_TOO_FEW_CHARACTERS", "VE_TOO_FEW_CHARACTERS_PLURAL", "VE_NOT_CONSECUTIVE", "VE_NOT_CONSECUTIVE_RANGE", "VE_VALIDATION_FAILED", "VE_VALIDUSSTATE", "VE_VALIDCAPHONE", "VE_VALIDUKPHONE", "VE_VALIDUKZIP", "VE_VALIDAUPHONE", "VE_VALIDNLPHONE", "VE_VALIDNZPHONE", "VE_VALIDAUZIP", "VE_VALIDNZZIP", "VE_VALIDNLZIP", "VE_VALIDUSZIP", "VE_VALIDCAZIP", "VE_VALIDDATE", "VE_VALIDALTDATE", "VE_VALIDINTLDATE", "VE_VALIDNUMBER", "VE_VALIDTEXTONLY", "VE_VALIDUSSTATE_PLURAL", "VE_VALIDEMAIL_PLURAL", "VE_VALIDUSPHONE_PLURAL", "VE_VALIDUSZIP_PLURAL", "VE_VALIDDATE_PLURAL", "VE_VALIDNUMBER_PLURAL", "VE_VALIDTEXTONLY_PLURAL", "VE_VALIDEXTENSIONS", "VE_VALIDPDF", "VE_VALIDDOCUMENT", "VE_VALIDEMAIL", "VE_VALIDSPREADSHEET", "VE_VALIDGRAPHIC", "VE_VALIDUPLOAD", "VE_VALIDSCREENCAPTURE", "VE_TEXT_ENTRY_HAS_VALUE_BUT_NOT_CHECKED", "VE_TEXT_ENTRY_HAS_VALUE_BUT_NOT_RANKED", "VE_SELECT_LEAST_MOST_PREFERRED", "VE_SELECT_LEAST_MOST_LEVEL", "VE_SELECT_MOST_VALUE_UPGRADE", "VE_SELECT_VALUABLE_LEVEL", "VE_IMPORTANCE_TOTAL", "VE_MIN_GROUP_CHOICES", "VE_MAX_GROUP_CHOICES", "VE_VALIDNUMBER_MIN", "VE_VALIDNUMBER_MAX", "VE_VALIDMIN_PLURAL", "VE_VALIDMAX_PLURAL", "VE_VALIDNUMBER_NUM_DECIMALS", "VE_FORCE_OTHER_RESPONSE", "VE_HEADER_VALIDATION_MESSAGE", "VE_CUSTOM_VALIDATION_NO_MESSAGE", "VE_CUSTOM_VALIDATION_NOT_APPLIED", "VE_QUESTION", "VE_ERROR", "VE_INCORRECT_CAPTCHA_RESPONSE", "VE_MULTIPLE_CHOICES"] = Field(alias='subMessageID')

    # A user-provided description of the custom validation.
    description: typing.Optional[str] = Field(None, alias='description')
    class Config:
        arbitrary_types_allowed = True
