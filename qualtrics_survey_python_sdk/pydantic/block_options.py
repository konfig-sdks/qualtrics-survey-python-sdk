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

from qualtrics_survey_python_sdk.pydantic.block_options_looping_options import BlockOptionsLoopingOptions
from qualtrics_survey_python_sdk.pydantic.library_id import LibraryID
from qualtrics_survey_python_sdk.pydantic.message_id import MessageID
from qualtrics_survey_python_sdk.pydantic.questions_per_page import QuestionsPerPage
from qualtrics_survey_python_sdk.pydantic.randomization_element import RandomizationElement

class BlockOptions(BaseModel):
    # Prevents modification of the block and its contents
    block_locking: typing.Optional[Literal["true", "false"]] = Field(None, alias='BlockLocking')

    # Authorization to modify the block
    block_password: typing.Optional[str] = Field(None, alias='BlockPassword')

    block_visiblity: typing.Optional[Literal["Collapsed", "Expanded"]] = Field(None, alias='BlockVisiblity')

    randomize_questions: typing.Optional[Literal["false", "RandomWithXPerPage", "RandomWithOnlyX", "Advanced"]] = Field(None, alias='RandomizeQuestions')

    # Loop & Merge type
    looping: typing.Optional[Literal["None", "Static", "Question"]] = Field(None, alias='Looping')

    looping_options: typing.Optional[BlockOptionsLoopingOptions] = Field(None, alias='LoopingOptions')

    # The configuration for the type of Randomization to apply. Many options based on 3 types of Randomization in RandomizeQuestions
    randomization: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='Randomization')

    # The text on the next button at preview and runtime, or if nextButtonMID is set, the name of the message referred to there
    next_button: typing.Optional[str] = Field(None, alias='NextButton')

    # The text on the previous button at preview and runtime, or if previousButtonMID is set, the name of the message referred to there
    previous_button: typing.Optional[str] = Field(None, alias='PreviousButton')

    next_button_library_i_d: typing.Optional[LibraryID] = Field(None, alias='nextButtonLibraryID')

    next_button_m_i_d: typing.Optional[MessageID] = Field(None, alias='nextButtonMID')

    previous_button_library_i_d: typing.Optional[MessageID] = Field(None, alias='previousButtonLibraryID')
    class Config:
        arbitrary_types_allowed = True
