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

from qualtrics_survey_python_sdk.type.division_id import DivisionID
from qualtrics_survey_python_sdk.type.flow_definition import FlowDefinition
from qualtrics_survey_python_sdk.type.project_info_definition import ProjectInfoDefinition
from qualtrics_survey_python_sdk.type.scoring_definition import ScoringDefinition
from qualtrics_survey_python_sdk.type.survey_definition_blocks import SurveyDefinitionBlocks
from qualtrics_survey_python_sdk.type.survey_definition_questions import SurveyDefinitionQuestions
from qualtrics_survey_python_sdk.type.survey_definition_response_sets import SurveyDefinitionResponseSets
from qualtrics_survey_python_sdk.type.survey_id import SurveyID
from qualtrics_survey_python_sdk.type.survey_options import SurveyOptions
from qualtrics_survey_python_sdk.type.survey_status import SurveyStatus
from qualtrics_survey_python_sdk.type.user_id import UserID

class RequiredSurveyDefinition(TypedDict):
    SurveyOptions: SurveyOptions

    SurveyID: SurveyID

    SurveyName: str

    SurveyStatus: SurveyStatus

    LastModified: datetime

    BrandID: str

    OwnerID: UserID

    # The date the survey was last accessed 
    LastAccessed: datetime

    CreatorID: UserID

    LastActivated: datetime

    Questions: SurveyDefinitionQuestions

    Blocks: SurveyDefinitionBlocks

    ResponseSets: SurveyDefinitionResponseSets

    SurveyFlow: FlowDefinition

    Scoring: ScoringDefinition

    ProjectInfo: ProjectInfoDefinition

    BrandBaseURL: str

class OptionalSurveyDefinition(TypedDict, total=False):
    # Number of questions in the survey
    QuestionCount: str

    DivisionID: DivisionID

class SurveyDefinition(RequiredSurveyDefinition, OptionalSurveyDefinition):
    pass
