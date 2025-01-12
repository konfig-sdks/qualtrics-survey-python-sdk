# coding: utf-8

"""
    Qualtrics Survey API

    The Qualtrics Survey endpoints give you access to the structure of the surveys you create.   Surveys have a complex structure, and you are encouraged to become familiar with the structure using your brand's Qualtrics page to build surveys at first. Then you can query those surveys using these endpoints.   Once you are familiar, you can use this API to create surveys on the fly, or modify existing surveys in your library. 

    The version of the OpenAPI document: 3.0.0
    Created by: https://www.qualtrics.com/support/
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from qualtrics_survey_python_sdk import schemas  # noqa: F401


class SurveyDefinition(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "LastActivated",
            "ResponseSets",
            "Blocks",
            "SurveyID",
            "CreatorID",
            "SurveyName",
            "Scoring",
            "BrandID",
            "BrandBaseURL",
            "SurveyOptions",
            "LastModified",
            "OwnerID",
            "SurveyStatus",
            "LastAccessed",
            "SurveyFlow",
            "ProjectInfo",
            "Questions",
        }
        
        class properties:
        
            @staticmethod
            def SurveyOptions() -> typing.Type['SurveyOptions']:
                return SurveyOptions
        
            @staticmethod
            def SurveyID() -> typing.Type['SurveyID']:
                return SurveyID
            SurveyName = schemas.StrSchema
        
            @staticmethod
            def SurveyStatus() -> typing.Type['SurveyStatus']:
                return SurveyStatus
            LastModified = schemas.DateTimeSchema
            BrandID = schemas.StrSchema
        
            @staticmethod
            def OwnerID() -> typing.Type['UserID']:
                return UserID
            LastAccessed = schemas.DateTimeSchema
        
            @staticmethod
            def CreatorID() -> typing.Type['UserID']:
                return UserID
            LastActivated = schemas.DateTimeSchema
        
            @staticmethod
            def Questions() -> typing.Type['SurveyDefinitionQuestions']:
                return SurveyDefinitionQuestions
        
            @staticmethod
            def Blocks() -> typing.Type['SurveyDefinitionBlocks']:
                return SurveyDefinitionBlocks
        
            @staticmethod
            def ResponseSets() -> typing.Type['SurveyDefinitionResponseSets']:
                return SurveyDefinitionResponseSets
        
            @staticmethod
            def SurveyFlow() -> typing.Type['FlowDefinition']:
                return FlowDefinition
        
            @staticmethod
            def Scoring() -> typing.Type['ScoringDefinition']:
                return ScoringDefinition
        
            @staticmethod
            def ProjectInfo() -> typing.Type['ProjectInfoDefinition']:
                return ProjectInfoDefinition
            BrandBaseURL = schemas.StrSchema
            QuestionCount = schemas.StrSchema
        
            @staticmethod
            def DivisionID() -> typing.Type['DivisionID']:
                return DivisionID
            __annotations__ = {
                "SurveyOptions": SurveyOptions,
                "SurveyID": SurveyID,
                "SurveyName": SurveyName,
                "SurveyStatus": SurveyStatus,
                "LastModified": LastModified,
                "BrandID": BrandID,
                "OwnerID": OwnerID,
                "LastAccessed": LastAccessed,
                "CreatorID": CreatorID,
                "LastActivated": LastActivated,
                "Questions": Questions,
                "Blocks": Blocks,
                "ResponseSets": ResponseSets,
                "SurveyFlow": SurveyFlow,
                "Scoring": Scoring,
                "ProjectInfo": ProjectInfo,
                "BrandBaseURL": BrandBaseURL,
                "QuestionCount": QuestionCount,
                "DivisionID": DivisionID,
            }
        additional_properties = schemas.AnyTypeSchema
    
    LastActivated: MetaOapg.properties.LastActivated
    ResponseSets: 'SurveyDefinitionResponseSets'
    Blocks: 'SurveyDefinitionBlocks'
    SurveyID: 'SurveyID'
    CreatorID: 'UserID'
    SurveyName: MetaOapg.properties.SurveyName
    Scoring: 'ScoringDefinition'
    BrandID: MetaOapg.properties.BrandID
    BrandBaseURL: MetaOapg.properties.BrandBaseURL
    SurveyOptions: 'SurveyOptions'
    LastModified: MetaOapg.properties.LastModified
    OwnerID: 'UserID'
    SurveyStatus: 'SurveyStatus'
    LastAccessed: MetaOapg.properties.LastAccessed
    SurveyFlow: 'FlowDefinition'
    ProjectInfo: 'ProjectInfoDefinition'
    Questions: 'SurveyDefinitionQuestions'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LastActivated"]) -> MetaOapg.properties.LastActivated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ResponseSets"]) -> 'SurveyDefinitionResponseSets': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Blocks"]) -> 'SurveyDefinitionBlocks': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SurveyID"]) -> 'SurveyID': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CreatorID"]) -> 'UserID': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SurveyName"]) -> MetaOapg.properties.SurveyName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Scoring"]) -> 'ScoringDefinition': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BrandID"]) -> MetaOapg.properties.BrandID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BrandBaseURL"]) -> MetaOapg.properties.BrandBaseURL: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SurveyOptions"]) -> 'SurveyOptions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LastModified"]) -> MetaOapg.properties.LastModified: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OwnerID"]) -> 'UserID': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SurveyStatus"]) -> 'SurveyStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LastAccessed"]) -> MetaOapg.properties.LastAccessed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SurveyFlow"]) -> 'FlowDefinition': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ProjectInfo"]) -> 'ProjectInfoDefinition': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Questions"]) -> 'SurveyDefinitionQuestions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["QuestionCount"]) -> MetaOapg.properties.QuestionCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DivisionID"]) -> 'DivisionID': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["LastActivated"], typing_extensions.Literal["ResponseSets"], typing_extensions.Literal["Blocks"], typing_extensions.Literal["SurveyID"], typing_extensions.Literal["CreatorID"], typing_extensions.Literal["SurveyName"], typing_extensions.Literal["Scoring"], typing_extensions.Literal["BrandID"], typing_extensions.Literal["BrandBaseURL"], typing_extensions.Literal["SurveyOptions"], typing_extensions.Literal["LastModified"], typing_extensions.Literal["OwnerID"], typing_extensions.Literal["SurveyStatus"], typing_extensions.Literal["LastAccessed"], typing_extensions.Literal["SurveyFlow"], typing_extensions.Literal["ProjectInfo"], typing_extensions.Literal["Questions"], typing_extensions.Literal["QuestionCount"], typing_extensions.Literal["DivisionID"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LastActivated"]) -> MetaOapg.properties.LastActivated: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ResponseSets"]) -> 'SurveyDefinitionResponseSets': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Blocks"]) -> 'SurveyDefinitionBlocks': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SurveyID"]) -> 'SurveyID': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CreatorID"]) -> 'UserID': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SurveyName"]) -> MetaOapg.properties.SurveyName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Scoring"]) -> 'ScoringDefinition': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BrandID"]) -> MetaOapg.properties.BrandID: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BrandBaseURL"]) -> MetaOapg.properties.BrandBaseURL: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SurveyOptions"]) -> 'SurveyOptions': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LastModified"]) -> MetaOapg.properties.LastModified: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OwnerID"]) -> 'UserID': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SurveyStatus"]) -> 'SurveyStatus': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LastAccessed"]) -> MetaOapg.properties.LastAccessed: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SurveyFlow"]) -> 'FlowDefinition': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ProjectInfo"]) -> 'ProjectInfoDefinition': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Questions"]) -> 'SurveyDefinitionQuestions': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["QuestionCount"]) -> typing.Union[MetaOapg.properties.QuestionCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DivisionID"]) -> typing.Union['DivisionID', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["LastActivated"], typing_extensions.Literal["ResponseSets"], typing_extensions.Literal["Blocks"], typing_extensions.Literal["SurveyID"], typing_extensions.Literal["CreatorID"], typing_extensions.Literal["SurveyName"], typing_extensions.Literal["Scoring"], typing_extensions.Literal["BrandID"], typing_extensions.Literal["BrandBaseURL"], typing_extensions.Literal["SurveyOptions"], typing_extensions.Literal["LastModified"], typing_extensions.Literal["OwnerID"], typing_extensions.Literal["SurveyStatus"], typing_extensions.Literal["LastAccessed"], typing_extensions.Literal["SurveyFlow"], typing_extensions.Literal["ProjectInfo"], typing_extensions.Literal["Questions"], typing_extensions.Literal["QuestionCount"], typing_extensions.Literal["DivisionID"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        LastActivated: typing.Union[MetaOapg.properties.LastActivated, str, datetime, ],
        ResponseSets: 'SurveyDefinitionResponseSets',
        Blocks: 'SurveyDefinitionBlocks',
        SurveyID: 'SurveyID',
        CreatorID: 'UserID',
        SurveyName: typing.Union[MetaOapg.properties.SurveyName, str, ],
        Scoring: 'ScoringDefinition',
        BrandID: typing.Union[MetaOapg.properties.BrandID, str, ],
        BrandBaseURL: typing.Union[MetaOapg.properties.BrandBaseURL, str, ],
        SurveyOptions: 'SurveyOptions',
        LastModified: typing.Union[MetaOapg.properties.LastModified, str, datetime, ],
        OwnerID: 'UserID',
        SurveyStatus: 'SurveyStatus',
        LastAccessed: typing.Union[MetaOapg.properties.LastAccessed, str, datetime, ],
        SurveyFlow: 'FlowDefinition',
        ProjectInfo: 'ProjectInfoDefinition',
        Questions: 'SurveyDefinitionQuestions',
        QuestionCount: typing.Union[MetaOapg.properties.QuestionCount, str, schemas.Unset] = schemas.unset,
        DivisionID: typing.Union['DivisionID', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'SurveyDefinition':
        return super().__new__(
            cls,
            *args,
            LastActivated=LastActivated,
            ResponseSets=ResponseSets,
            Blocks=Blocks,
            SurveyID=SurveyID,
            CreatorID=CreatorID,
            SurveyName=SurveyName,
            Scoring=Scoring,
            BrandID=BrandID,
            BrandBaseURL=BrandBaseURL,
            SurveyOptions=SurveyOptions,
            LastModified=LastModified,
            OwnerID=OwnerID,
            SurveyStatus=SurveyStatus,
            LastAccessed=LastAccessed,
            SurveyFlow=SurveyFlow,
            ProjectInfo=ProjectInfo,
            Questions=Questions,
            QuestionCount=QuestionCount,
            DivisionID=DivisionID,
            _configuration=_configuration,
            **kwargs,
        )

from qualtrics_survey_python_sdk.model.division_id import DivisionID
from qualtrics_survey_python_sdk.model.flow_definition import FlowDefinition
from qualtrics_survey_python_sdk.model.project_info_definition import ProjectInfoDefinition
from qualtrics_survey_python_sdk.model.scoring_definition import ScoringDefinition
from qualtrics_survey_python_sdk.model.survey_definition_blocks import SurveyDefinitionBlocks
from qualtrics_survey_python_sdk.model.survey_definition_questions import SurveyDefinitionQuestions
from qualtrics_survey_python_sdk.model.survey_definition_response_sets import SurveyDefinitionResponseSets
from qualtrics_survey_python_sdk.model.survey_id import SurveyID
from qualtrics_survey_python_sdk.model.survey_options import SurveyOptions
from qualtrics_survey_python_sdk.model.survey_status import SurveyStatus
from qualtrics_survey_python_sdk.model.user_id import UserID
