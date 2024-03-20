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

from qualtrics_survey_python_sdk.pydantic.block_elements import BlockElements
from qualtrics_survey_python_sdk.pydantic.block_id import BlockID
from qualtrics_survey_python_sdk.pydantic.block_options import BlockOptions
from qualtrics_survey_python_sdk.pydantic.library_id import LibraryID
from qualtrics_survey_python_sdk.pydantic.referenced_block_id import ReferencedBlockID

class ReferenceBlock(BaseModel):
    type: Literal["Standard"] = Field(alias='Type')

    sub_type: Literal["Reference"] = Field(alias='SubType')

    i_d: BlockID = Field(alias='ID')

    description: typing.Optional[str] = Field(alias='Description')

    library_i_d: LibraryID = Field(alias='LibraryID')

    referenced_block_i_d: ReferencedBlockID = Field(alias='ReferencedBlockID')

    block_elements: typing.Optional[typing.Optional[typing.List[BlockElements]]] = Field(None, alias='BlockElements')

    options: typing.Optional[BlockOptions] = Field(None, alias='Options')
    class Config:
        arbitrary_types_allowed = True
