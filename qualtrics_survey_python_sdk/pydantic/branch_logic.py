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

from qualtrics_survey_python_sdk.pydantic.device_type_expression import DeviceTypeExpression
from qualtrics_survey_python_sdk.pydantic.embedded_data_expression import EmbeddedDataExpression
from qualtrics_survey_python_sdk.pydantic.evaluator_metadata_expression import EvaluatorMetadataExpression
from qualtrics_survey_python_sdk.pydantic.geo_ip_expression import GeoIPExpression
from qualtrics_survey_python_sdk.pydantic.loop_and_merge_expression import LoopAndMergeExpression
from qualtrics_survey_python_sdk.pydantic.org_hierarchy_metadata_expression import OrgHierarchyMetadataExpression
from qualtrics_survey_python_sdk.pydantic.org_hierarchy_units_expression import OrgHierarchyUnitsExpression
from qualtrics_survey_python_sdk.pydantic.panel_data_expression import PanelDataExpression
from qualtrics_survey_python_sdk.pydantic.question_expression import QuestionExpression
from qualtrics_survey_python_sdk.pydantic.quota_expression import QuotaExpression
from qualtrics_survey_python_sdk.pydantic.relationship_expression import RelationshipExpression
from qualtrics_survey_python_sdk.pydantic.subject_metadata_expression import SubjectMetadataExpression

class BranchLogic(BaseModel):
    # Type of branch logic.
    type: Literal["BooleanExpression"] = Field(alias='Type')
    class Config:
        arbitrary_types_allowed = True
