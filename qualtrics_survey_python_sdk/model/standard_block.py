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


class StandardBlock(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A logical grouping of questions, split by pages, with configuration on how to control the flow and visibility of each question. The original block's type is "Default"
    """


    class MetaOapg:
        required = {
            "Type",
            "Description",
        }
        
        class properties:
            
            
            class Type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "Standard": "STANDARD",
                        "Default": "DEFAULT",
                    }
                
                @schemas.classproperty
                def STANDARD(cls):
                    return cls("Standard")
                
                @schemas.classproperty
                def DEFAULT(cls):
                    return cls("Default")
            
            
            class Description(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 100
        
            @staticmethod
            def BlockElements() -> typing.Type['BlockElements']:
                return BlockElements
        
            @staticmethod
            def ID() -> typing.Type['BlockID']:
                return BlockID
            __annotations__ = {
                "Type": Type,
                "Description": Description,
                "BlockElements": BlockElements,
                "ID": ID,
            }
        additional_properties = schemas.AnyTypeSchema
    
    Type: MetaOapg.properties.Type
    Description: MetaOapg.properties.Description
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Type"]) -> MetaOapg.properties.Type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Description"]) -> MetaOapg.properties.Description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BlockElements"]) -> 'BlockElements': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ID"]) -> 'BlockID': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Type"], typing_extensions.Literal["Description"], typing_extensions.Literal["BlockElements"], typing_extensions.Literal["ID"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Type"]) -> MetaOapg.properties.Type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Description"]) -> MetaOapg.properties.Description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BlockElements"]) -> typing.Union['BlockElements', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ID"]) -> typing.Union['BlockID', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Type"], typing_extensions.Literal["Description"], typing_extensions.Literal["BlockElements"], typing_extensions.Literal["ID"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Type: typing.Union[MetaOapg.properties.Type, str, ],
        Description: typing.Union[MetaOapg.properties.Description, str, ],
        BlockElements: typing.Union['BlockElements', schemas.Unset] = schemas.unset,
        ID: typing.Union['BlockID', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'StandardBlock':
        return super().__new__(
            cls,
            *args,
            Type=Type,
            Description=Description,
            BlockElements=BlockElements,
            ID=ID,
            _configuration=_configuration,
            **kwargs,
        )

from qualtrics_survey_python_sdk.model.block_elements import BlockElements
from qualtrics_survey_python_sdk.model.block_id import BlockID
