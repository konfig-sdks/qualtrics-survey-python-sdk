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


class Labels(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Labels.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def NA() -> typing.Type['Selection']:
                return Selection
            __annotations__ = {
                "NA": NA,
            }
        
        @staticmethod
        def additional_properties() -> typing.Type['Selection']:
            return Selection
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["NA"]) -> 'Selection': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> 'Selection': ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["NA"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["NA"]) -> typing.Union['Selection', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union['Selection', schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["NA"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        NA: typing.Union['Selection', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: 'Selection',
    ) -> 'Labels':
        return super().__new__(
            cls,
            *args,
            NA=NA,
            _configuration=_configuration,
            **kwargs,
        )

from qualtrics_survey_python_sdk.model.selection import Selection
