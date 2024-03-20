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

from qualtrics_survey_python_sdk.type.scoring_definition_scoring_categories import ScoringDefinitionScoringCategories
from qualtrics_survey_python_sdk.type.scoring_definition_scoring_category_groups import ScoringDefinitionScoringCategoryGroups
from qualtrics_survey_python_sdk.type.scoring_id import ScoringID

class RequiredScoringDefinition(TypedDict):
    ScoringCategories: ScoringDefinitionScoringCategories

    ScoringCategoryGroups: ScoringDefinitionScoringCategoryGroups

    ScoringSummaryCategory: ScoringID

    # If scoring summary is after questions.
    ScoringSummaryAfterQuestions: bool

    # If scoring summary is after survey.
    ScoringSummaryAfterSurvey: bool

    DefaultScoringCategory: ScoringID

    # The automated scoring category.
    AutoScoringCategory: str

class OptionalScoringDefinition(TypedDict, total=False):
    pass

class ScoringDefinition(RequiredScoringDefinition, OptionalScoringDefinition):
    pass
