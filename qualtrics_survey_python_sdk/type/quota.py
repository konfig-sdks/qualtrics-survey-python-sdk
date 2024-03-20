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

from qualtrics_survey_python_sdk.type.action_info import ActionInfo
from qualtrics_survey_python_sdk.type.block_id import BlockID
from qualtrics_survey_python_sdk.type.cross_logic_def_entry import CrossLogicDefEntry
from qualtrics_survey_python_sdk.type.end_survey_options import EndSurveyOptions
from qualtrics_survey_python_sdk.type.logic_object import LogicObject
from qualtrics_survey_python_sdk.type.question_id import QuestionID
from qualtrics_survey_python_sdk.type.quota_action import QuotaAction
from qualtrics_survey_python_sdk.type.quota_id import QuotaID
from qualtrics_survey_python_sdk.type.quota_schedule import QuotaSchedule
from qualtrics_survey_python_sdk.type.survey_id import SurveyID
from qualtrics_survey_python_sdk.type.web_service_options import WebServiceOptions

class RequiredQuota(TypedDict):
    # Quota Name
    Name: str

    # Quota Limit. Default: 100
    Occurrences: int

    # Logic of when to increment the quota
    Logic: typing.Union[LogicObject, typing.List[LogicObject]]

    QuotaAction: QuotaAction

    ID: QuotaID

    # One of Survey or ResponseSet
    QuotaRealm: str

class OptionalQuota(TypedDict, total=False):
    # Quota Count. Default: 0
    Count: int

    # For restoring quota count
    CountForUndo: int

    # One of Simple or Cross Logic Quota
    LogicType: typing.Union[str]

    # The element corresponding to the `QuotaAction` when `QuotaAction` is one of `DontDisplaySurvey`, `DontDisplayQuestion`, or `DontDisplayBlock`. See `QuotaAction`
    ActionElement: typing.Union[SurveyID, QuestionID, BlockID, str]

    ActionInfo: ActionInfo

    ActionLogic: ActionInfo

    QuotaSchedule: QuotaSchedule

    EndSurveyOptions: EndSurveyOptions

    WebServiceOptions: WebServiceOptions

    # Definition for the cross logic quota
    CrossLogicDef: typing.List[CrossLogicDefEntry]

    PerformActionOnUser: bool

class Quota(RequiredQuota, OptionalQuota):
    pass
