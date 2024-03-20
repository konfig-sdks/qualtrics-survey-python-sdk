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


class TableOfContentsFlowElementOptions(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Options for the table of contents flow element.
    """


    class MetaOapg:
        
        class properties:
            
            
            class ShowSidebar(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def TRUE(cls):
                    return cls("true")
                
                @schemas.classproperty
                def FALSE(cls):
                    return cls("false")
            
            
            class TocConclusion(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def TRUE(cls):
                    return cls("true")
                
                @schemas.classproperty
                def FALSE(cls):
                    return cls("false")
            __annotations__ = {
                "ShowSidebar": ShowSidebar,
                "TocConclusion": TocConclusion,
            }
        additional_properties = schemas.AnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ShowSidebar"]) -> MetaOapg.properties.ShowSidebar: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TocConclusion"]) -> MetaOapg.properties.TocConclusion: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ShowSidebar"], typing_extensions.Literal["TocConclusion"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ShowSidebar"]) -> typing.Union[MetaOapg.properties.ShowSidebar, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TocConclusion"]) -> typing.Union[MetaOapg.properties.TocConclusion, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ShowSidebar"], typing_extensions.Literal["TocConclusion"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        ShowSidebar: typing.Union[MetaOapg.properties.ShowSidebar, str, schemas.Unset] = schemas.unset,
        TocConclusion: typing.Union[MetaOapg.properties.TocConclusion, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'TableOfContentsFlowElementOptions':
        return super().__new__(
            cls,
            *args,
            ShowSidebar=ShowSidebar,
            TocConclusion=TocConclusion,
            _configuration=_configuration,
            **kwargs,
        )
