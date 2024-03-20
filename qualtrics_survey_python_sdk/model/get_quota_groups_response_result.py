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


class GetQuotaGroupsResponseResult(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "elements",
        }
        
        class properties:
            
            
            class elements(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['QuotaGroup']:
                        return QuotaGroup
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['QuotaGroup'], typing.List['QuotaGroup']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'elements':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'QuotaGroup':
                    return super().__getitem__(i)
            nextPage = schemas.StrSchema
            __annotations__ = {
                "elements": elements,
                "nextPage": nextPage,
            }
    
    elements: MetaOapg.properties.elements
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["elements"]) -> MetaOapg.properties.elements: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nextPage"]) -> MetaOapg.properties.nextPage: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["elements", "nextPage", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["elements"]) -> MetaOapg.properties.elements: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nextPage"]) -> typing.Union[MetaOapg.properties.nextPage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["elements", "nextPage", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        elements: typing.Union[MetaOapg.properties.elements, list, tuple, ],
        nextPage: typing.Union[MetaOapg.properties.nextPage, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GetQuotaGroupsResponseResult':
        return super().__new__(
            cls,
            *args,
            elements=elements,
            nextPage=nextPage,
            _configuration=_configuration,
            **kwargs,
        )

from qualtrics_survey_python_sdk.model.quota_group import QuotaGroup
