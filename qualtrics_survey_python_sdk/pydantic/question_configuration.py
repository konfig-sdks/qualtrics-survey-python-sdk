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


class QuestionConfiguration(BaseModel):
    # An optional user-provided field for question descriptions.
    question_description_option: typing.Optional[Literal["UseText", "SpecifyLabel"]] = Field(None, alias='QuestionDescriptionOption')

    # Text position.
    text_position: typing.Optional[Literal["inline"]] = Field(None, alias='TextPosition')

    # Value of column width.
    choice_column_width: typing.Optional[Literal[25]] = Field(None, alias='ChoiceColumnWidth')

    # Repeating of headers.
    repeat_headers: typing.Optional[Literal["none"]] = Field(None, alias='RepeatHeaders')

    # If white space is allowed.
    white_space: typing.Optional[Literal["true", "false"]] = Field(None, alias='WhiteSpace')

    # Position of label.
    label_position: typing.Optional[Literal["BELOW", "SIDE"]] = Field(None, alias='LabelPosition')

    # Number of columns.
    num_columns: typing.Optional[int] = Field(None, alias='NumColumns')

    # If questions should be formatted for use on a mobile device.
    mobile_first: typing.Optional[bool] = Field(None, alias='MobileFirst')
    class Config:
        arbitrary_types_allowed = True
