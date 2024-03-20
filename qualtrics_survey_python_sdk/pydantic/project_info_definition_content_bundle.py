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

from qualtrics_survey_python_sdk.pydantic.project_info_definition_content_bundle_survey_input_variables import ProjectInfoDefinitionContentBundleSurveyInputVariables

class ProjectInfoDefinitionContentBundle(BaseModel):
    bundle_short_name: str = Field(alias='BundleShortName')

    registry_sha: str = Field(alias='RegistrySha')

    registry_version: str = Field(alias='RegistryVersion')

    survey_input_variables: ProjectInfoDefinitionContentBundleSurveyInputVariables = Field(alias='SurveyInputVariables')
    class Config:
        arbitrary_types_allowed = True
