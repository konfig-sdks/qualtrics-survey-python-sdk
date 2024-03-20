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


class EmbeddedDataFlowElementEmbeddedDataItemDataVisibility(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Visibility of data.
    """


    class MetaOapg:
        
        class properties:
            Private = schemas.BoolSchema
            Hidden = schemas.BoolSchema
            __annotations__ = {
                "Private": Private,
                "Hidden": Hidden,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Private"]) -> MetaOapg.properties.Private: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Hidden"]) -> MetaOapg.properties.Hidden: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Private", "Hidden", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Private"]) -> typing.Union[MetaOapg.properties.Private, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Hidden"]) -> typing.Union[MetaOapg.properties.Hidden, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Private", "Hidden", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Private: typing.Union[MetaOapg.properties.Private, bool, schemas.Unset] = schemas.unset,
        Hidden: typing.Union[MetaOapg.properties.Hidden, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmbeddedDataFlowElementEmbeddedDataItemDataVisibility':
        return super().__new__(
            cls,
            *args,
            Private=Private,
            Hidden=Hidden,
            _configuration=_configuration,
            **kwargs,
        )