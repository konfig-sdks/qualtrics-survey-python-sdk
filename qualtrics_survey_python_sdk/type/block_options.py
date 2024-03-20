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

from qualtrics_survey_python_sdk.type.block_options_looping_options import BlockOptionsLoopingOptions
from qualtrics_survey_python_sdk.type.library_id import LibraryID
from qualtrics_survey_python_sdk.type.message_id import MessageID
from qualtrics_survey_python_sdk.type.questions_per_page import QuestionsPerPage
from qualtrics_survey_python_sdk.type.randomization_element import RandomizationElement

class RequiredBlockOptions(TypedDict):
    pass

class OptionalBlockOptions(TypedDict, total=False):
    # Prevents modification of the block and its contents
    BlockLocking: str

    # Authorization to modify the block
    BlockPassword: str

    BlockVisiblity: str

    RandomizeQuestions: str

    # Loop & Merge type
    Looping: str

    LoopingOptions: BlockOptionsLoopingOptions

    # The configuration for the type of Randomization to apply. Many options based on 3 types of Randomization in RandomizeQuestions
    Randomization: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # The text on the next button at preview and runtime, or if nextButtonMID is set, the name of the message referred to there
    NextButton: str

    # The text on the previous button at preview and runtime, or if previousButtonMID is set, the name of the message referred to there
    PreviousButton: str

    nextButtonLibraryID: LibraryID

    nextButtonMID: MessageID

    previousButtonLibraryID: MessageID

class BlockOptions(RequiredBlockOptions, OptionalBlockOptions):
    pass
