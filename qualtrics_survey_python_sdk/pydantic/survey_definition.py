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

from qualtrics_survey_python_sdk.pydantic.division_id import DivisionID
from qualtrics_survey_python_sdk.pydantic.flow_definition import FlowDefinition
from qualtrics_survey_python_sdk.pydantic.project_info_definition import ProjectInfoDefinition
from qualtrics_survey_python_sdk.pydantic.scoring_definition import ScoringDefinition
from qualtrics_survey_python_sdk.pydantic.survey_definition_blocks import SurveyDefinitionBlocks
from qualtrics_survey_python_sdk.pydantic.survey_definition_questions import SurveyDefinitionQuestions
from qualtrics_survey_python_sdk.pydantic.survey_definition_response_sets import SurveyDefinitionResponseSets
from qualtrics_survey_python_sdk.pydantic.survey_id import SurveyID
from qualtrics_survey_python_sdk.pydantic.survey_options import SurveyOptions
from qualtrics_survey_python_sdk.pydantic.survey_status import SurveyStatus
from qualtrics_survey_python_sdk.pydantic.user_id import UserID

class SurveyDefinition(BaseModel):
    survey_options: SurveyOptions = Field(alias='SurveyOptions')

    survey_i_d: SurveyID = Field(alias='SurveyID')

    survey_name: str = Field(alias='SurveyName')

    survey_status: SurveyStatus = Field(alias='SurveyStatus')

    last_modified: datetime = Field(alias='LastModified')

    brand_i_d: str = Field(alias='BrandID')

    owner_i_d: UserID = Field(alias='OwnerID')

    # The date the survey was last accessed 
    last_accessed: datetime = Field(alias='LastAccessed')

    creator_i_d: UserID = Field(alias='CreatorID')

    last_activated: datetime = Field(alias='LastActivated')

    questions: SurveyDefinitionQuestions = Field(alias='Questions')

    blocks: SurveyDefinitionBlocks = Field(alias='Blocks')

    response_sets: SurveyDefinitionResponseSets = Field(alias='ResponseSets')

    survey_flow: FlowDefinition = Field(alias='SurveyFlow')

    scoring: ScoringDefinition = Field(alias='Scoring')

    project_info: ProjectInfoDefinition = Field(alias='ProjectInfo')

    brand_base_u_r_l: str = Field(alias='BrandBaseURL')

    # Number of questions in the survey
    question_count: typing.Optional[str] = Field(None, alias='QuestionCount')

    division_i_d: typing.Optional[DivisionID] = Field(None, alias='DivisionID')
    class Config:
        arbitrary_types_allowed = True
