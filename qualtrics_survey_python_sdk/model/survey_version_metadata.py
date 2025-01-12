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


class SurveyVersionMetadata(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "publishEvents",
            "surveyID",
            "versionID",
            "wasPublished",
            "description",
            "published",
            "creationDate",
            "userID",
            "versionNumber",
        }
        
        class properties:
            description = schemas.StrSchema
        
            @staticmethod
            def surveyID() -> typing.Type['SurveyID']:
                return SurveyID
            versionID = schemas.StrSchema
            versionNumber = schemas.IntSchema
        
            @staticmethod
            def userID() -> typing.Type['UserID']:
                return UserID
            creationDate = schemas.DateTimeSchema
            published = schemas.BoolSchema
            wasPublished = schemas.BoolSchema
        
            @staticmethod
            def publishEvents() -> typing.Type['SurveyVersionMetadataPublishEvents']:
                return SurveyVersionMetadataPublishEvents
            __annotations__ = {
                "description": description,
                "surveyID": surveyID,
                "versionID": versionID,
                "versionNumber": versionNumber,
                "userID": userID,
                "creationDate": creationDate,
                "published": published,
                "wasPublished": wasPublished,
                "publishEvents": publishEvents,
            }
    
    publishEvents: 'SurveyVersionMetadataPublishEvents'
    surveyID: 'SurveyID'
    versionID: MetaOapg.properties.versionID
    wasPublished: MetaOapg.properties.wasPublished
    description: MetaOapg.properties.description
    published: MetaOapg.properties.published
    creationDate: MetaOapg.properties.creationDate
    userID: 'UserID'
    versionNumber: MetaOapg.properties.versionNumber
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["surveyID"]) -> 'SurveyID': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["versionID"]) -> MetaOapg.properties.versionID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["versionNumber"]) -> MetaOapg.properties.versionNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userID"]) -> 'UserID': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["creationDate"]) -> MetaOapg.properties.creationDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["published"]) -> MetaOapg.properties.published: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wasPublished"]) -> MetaOapg.properties.wasPublished: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["publishEvents"]) -> 'SurveyVersionMetadataPublishEvents': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "surveyID", "versionID", "versionNumber", "userID", "creationDate", "published", "wasPublished", "publishEvents", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["surveyID"]) -> 'SurveyID': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["versionID"]) -> MetaOapg.properties.versionID: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["versionNumber"]) -> MetaOapg.properties.versionNumber: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userID"]) -> 'UserID': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["creationDate"]) -> MetaOapg.properties.creationDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["published"]) -> MetaOapg.properties.published: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wasPublished"]) -> MetaOapg.properties.wasPublished: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["publishEvents"]) -> 'SurveyVersionMetadataPublishEvents': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "surveyID", "versionID", "versionNumber", "userID", "creationDate", "published", "wasPublished", "publishEvents", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        publishEvents: 'SurveyVersionMetadataPublishEvents',
        surveyID: 'SurveyID',
        versionID: typing.Union[MetaOapg.properties.versionID, str, ],
        wasPublished: typing.Union[MetaOapg.properties.wasPublished, bool, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        published: typing.Union[MetaOapg.properties.published, bool, ],
        creationDate: typing.Union[MetaOapg.properties.creationDate, str, datetime, ],
        userID: 'UserID',
        versionNumber: typing.Union[MetaOapg.properties.versionNumber, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SurveyVersionMetadata':
        return super().__new__(
            cls,
            *args,
            publishEvents=publishEvents,
            surveyID=surveyID,
            versionID=versionID,
            wasPublished=wasPublished,
            description=description,
            published=published,
            creationDate=creationDate,
            userID=userID,
            versionNumber=versionNumber,
            _configuration=_configuration,
            **kwargs,
        )

from qualtrics_survey_python_sdk.model.survey_id import SurveyID
from qualtrics_survey_python_sdk.model.survey_version_metadata_publish_events import SurveyVersionMetadataPublishEvents
from qualtrics_survey_python_sdk.model.user_id import UserID
