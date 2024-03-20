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

from qualtrics_survey_python_sdk.pydantic.action_info import ActionInfo
from qualtrics_survey_python_sdk.pydantic.block_id import BlockID
from qualtrics_survey_python_sdk.pydantic.cross_logic_def_entry import CrossLogicDefEntry
from qualtrics_survey_python_sdk.pydantic.end_survey_options import EndSurveyOptions
from qualtrics_survey_python_sdk.pydantic.logic_object import LogicObject
from qualtrics_survey_python_sdk.pydantic.question_id import QuestionID
from qualtrics_survey_python_sdk.pydantic.quota_action import QuotaAction
from qualtrics_survey_python_sdk.pydantic.quota_id import QuotaID
from qualtrics_survey_python_sdk.pydantic.quota_schedule import QuotaSchedule
from qualtrics_survey_python_sdk.pydantic.survey_id import SurveyID
from qualtrics_survey_python_sdk.pydantic.web_service_options import WebServiceOptions

class Quota(BaseModel):
    # Quota Name
    name: str = Field(alias='Name')

    # Quota Limit. Default: 100
    occurrences: int = Field(alias='Occurrences')

    # Logic of when to increment the quota
    logic: typing.Union[LogicObject, typing.List[LogicObject]] = Field(alias='Logic')

    quota_action: QuotaAction = Field(alias='QuotaAction')

    i_d: QuotaID = Field(alias='ID')

    # One of Survey or ResponseSet
    quota_realm: Literal["Survey", "ResponseSet"] = Field(alias='QuotaRealm')

    # Quota Count. Default: 0
    count: typing.Optional[int] = Field(None, alias='Count')

    # For restoring quota count
    count_for_undo: typing.Optional[int] = Field(None, alias='CountForUndo')

    # One of Simple or Cross Logic Quota
    logic_type: typing.Optional[typing.Union[str]] = Field(None, alias='LogicType')

    # The element corresponding to the `QuotaAction` when `QuotaAction` is one of `DontDisplaySurvey`, `DontDisplayQuestion`, or `DontDisplayBlock`. See `QuotaAction`
    action_element: typing.Optional[typing.Union[SurveyID, QuestionID, BlockID, str]] = Field(None, alias='ActionElement')

    action_info: typing.Optional[ActionInfo] = Field(None, alias='ActionInfo')

    action_logic: typing.Optional[ActionInfo] = Field(None, alias='ActionLogic')

    quota_schedule: typing.Optional[QuotaSchedule] = Field(None, alias='QuotaSchedule')

    end_survey_options: typing.Optional[EndSurveyOptions] = Field(None, alias='EndSurveyOptions')

    web_service_options: typing.Optional[WebServiceOptions] = Field(None, alias='WebServiceOptions')

    # Definition for the cross logic quota
    cross_logic_def: typing.Optional[typing.List[CrossLogicDefEntry]] = Field(None, alias='CrossLogicDef')

    perform_action_on_user: typing.Optional[bool] = Field(None, alias='PerformActionOnUser')
    class Config:
        arbitrary_types_allowed = True
