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

from qualtrics_survey_python_sdk.pydantic.org_hierarchy_id import OrgHierarchyID
from qualtrics_survey_python_sdk.pydantic.org_hierarchy_metadata_expression_org_hierarchy_def import OrgHierarchyMetadataExpressionOrgHierarchyDef

class OrgHierarchyMetadataExpression(BaseModel):
    # A user-provided description field.
    description: str = Field(alias='Description')

    # The logic type of the Org Hierarchy Metadata type.
    logic_type: Literal["OrgHierarchyMetadata"] = Field(alias='LogicType')

    # The type of org hierarchy metadata expression.
    type: Literal["Expression"] = Field(alias='Type')

    # Text field for the Org Hierarchy Metadata type.
    field: typing.Optional[str] = Field(None, alias='Field')

    # Operator for the Org Hierarchy Metadata type.
    operator: typing.Optional[Literal["ArrayContains"]] = Field(None, alias='Operator')

    org_hierarchy_def: typing.Optional[OrgHierarchyMetadataExpressionOrgHierarchyDef] = Field(None, alias='OrgHierarchyDef')

    org_hierarchy_i_d: typing.Optional[OrgHierarchyID] = Field(None, alias='OrgHierarchyID')

    # An attribute associated with `key`.
    value: typing.Optional[str] = Field(None, alias='Value')
    class Config:
        arbitrary_types_allowed = True
