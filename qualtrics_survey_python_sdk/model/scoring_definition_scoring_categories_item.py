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


class ScoringDefinitionScoringCategoriesItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Scoring categories.
    """


    class MetaOapg:
        required = {
            "Description",
            "ID",
            "Name",
        }
        
        class properties:
            Description = schemas.StrSchema
        
            @staticmethod
            def ID() -> typing.Type['ScoringID']:
                return ScoringID
            Name = schemas.StrSchema
            __annotations__ = {
                "Description": Description,
                "ID": ID,
                "Name": Name,
            }
        additional_properties = schemas.AnyTypeSchema
    
    Description: MetaOapg.properties.Description
    ID: 'ScoringID'
    Name: MetaOapg.properties.Name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Description"]) -> MetaOapg.properties.Description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ID"]) -> 'ScoringID': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Name"]) -> MetaOapg.properties.Name: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Description"], typing_extensions.Literal["ID"], typing_extensions.Literal["Name"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Description"]) -> MetaOapg.properties.Description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ID"]) -> 'ScoringID': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Name"]) -> MetaOapg.properties.Name: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Description"], typing_extensions.Literal["ID"], typing_extensions.Literal["Name"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Description: typing.Union[MetaOapg.properties.Description, str, ],
        ID: 'ScoringID',
        Name: typing.Union[MetaOapg.properties.Name, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'ScoringDefinitionScoringCategoriesItem':
        return super().__new__(
            cls,
            *args,
            Description=Description,
            ID=ID,
            Name=Name,
            _configuration=_configuration,
            **kwargs,
        )

from qualtrics_survey_python_sdk.model.scoring_id import ScoringID
