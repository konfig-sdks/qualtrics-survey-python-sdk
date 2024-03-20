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

from qualtrics_survey_python_sdk.pydantic.scoring_definition_scoring_categories import ScoringDefinitionScoringCategories
from qualtrics_survey_python_sdk.pydantic.scoring_definition_scoring_category_groups import ScoringDefinitionScoringCategoryGroups
from qualtrics_survey_python_sdk.pydantic.scoring_id import ScoringID

class ScoringDefinition(BaseModel):
    scoring_categories: ScoringDefinitionScoringCategories = Field(alias='ScoringCategories')

    scoring_category_groups: ScoringDefinitionScoringCategoryGroups = Field(alias='ScoringCategoryGroups')

    scoring_summary_category: ScoringID = Field(alias='ScoringSummaryCategory')

    # If scoring summary is after questions.
    scoring_summary_after_questions: bool = Field(alias='ScoringSummaryAfterQuestions')

    # If scoring summary is after survey.
    scoring_summary_after_survey: bool = Field(alias='ScoringSummaryAfterSurvey')

    default_scoring_category: ScoringID = Field(alias='DefaultScoringCategory')

    # The automated scoring category.
    auto_scoring_category: str = Field(alias='AutoScoringCategory')
    class Config:
        arbitrary_types_allowed = True
