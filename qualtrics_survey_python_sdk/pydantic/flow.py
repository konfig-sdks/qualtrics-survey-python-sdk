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

from qualtrics_survey_python_sdk.pydantic.authenticator_flow_element import AuthenticatorFlowElement
from qualtrics_survey_python_sdk.pydantic.block_randomizer_flow_element import BlockRandomizerFlowElement
from qualtrics_survey_python_sdk.pydantic.block_standard_flow_element import BlockStandardFlowElement
from qualtrics_survey_python_sdk.pydantic.branch_flow_element import BranchFlowElement
from qualtrics_survey_python_sdk.pydantic.embedded_data_flow_element import EmbeddedDataFlowElement
from qualtrics_survey_python_sdk.pydantic.end_survey_flow_element import EndSurveyFlowElement
from qualtrics_survey_python_sdk.pydantic.group_flow_element import GroupFlowElement
from qualtrics_survey_python_sdk.pydantic.reference_survey_flow_element import ReferenceSurveyFlowElement
from qualtrics_survey_python_sdk.pydantic.table_of_contents_flow_element import TableOfContentsFlowElement
from qualtrics_survey_python_sdk.pydantic.web_service_flow_element import WebServiceFlowElement

Flow = typing.List[typing.Union[typing.List[AuthenticatorFlowElement], typing.List[BlockStandardFlowElement], typing.List[BlockRandomizerFlowElement], typing.List[BranchFlowElement], typing.List[EmbeddedDataFlowElement], typing.List[EndSurveyFlowElement], typing.List[GroupFlowElement], typing.List[ReferenceSurveyFlowElement], typing.List[TableOfContentsFlowElement], typing.List[WebServiceFlowElement]]]
