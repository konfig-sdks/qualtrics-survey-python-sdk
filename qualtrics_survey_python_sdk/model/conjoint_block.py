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


class ConjointBlock(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Experience blocks limit the editable fields on the block.
    """


    class MetaOapg:
        required = {
            "Type",
            "SubType",
        }
        
        class properties:
            
            
            class Type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "ExperienceBlock": "EXPERIENCE_BLOCK",
                    }
                
                @schemas.classproperty
                def EXPERIENCE_BLOCK(cls):
                    return cls("ExperienceBlock")
            
            
            class SubType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "CBConjoint": "CBCONJOINT",
                        "MaxDiff": "MAX_DIFF",
                    }
                
                @schemas.classproperty
                def CBCONJOINT(cls):
                    return cls("CBConjoint")
                
                @schemas.classproperty
                def MAX_DIFF(cls):
                    return cls("MaxDiff")
            __annotations__ = {
                "Type": Type,
                "SubType": SubType,
            }
        additional_properties = schemas.AnyTypeSchema
    
    Type: MetaOapg.properties.Type
    SubType: MetaOapg.properties.SubType
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Type"]) -> MetaOapg.properties.Type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SubType"]) -> MetaOapg.properties.SubType: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Type"], typing_extensions.Literal["SubType"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Type"]) -> MetaOapg.properties.Type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SubType"]) -> MetaOapg.properties.SubType: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Type"], typing_extensions.Literal["SubType"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Type: typing.Union[MetaOapg.properties.Type, str, ],
        SubType: typing.Union[MetaOapg.properties.SubType, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'ConjointBlock':
        return super().__new__(
            cls,
            *args,
            Type=Type,
            SubType=SubType,
            _configuration=_configuration,
            **kwargs,
        )
