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


class SurveyQSF(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "SurveyEntry",
            "SurveyElements",
        }
        
        class properties:
        
            @staticmethod
            def SurveyEntry() -> typing.Type['SurveyMetadata']:
                return SurveyMetadata
            
            
            class SurveyElements(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['SurveyElement']:
                        return SurveyElement
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['SurveyElement'], typing.List['SurveyElement']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'SurveyElements':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'SurveyElement':
                    return super().__getitem__(i)
            __annotations__ = {
                "SurveyEntry": SurveyEntry,
                "SurveyElements": SurveyElements,
            }
    
    SurveyEntry: 'SurveyMetadata'
    SurveyElements: MetaOapg.properties.SurveyElements
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SurveyEntry"]) -> 'SurveyMetadata': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SurveyElements"]) -> MetaOapg.properties.SurveyElements: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["SurveyEntry", "SurveyElements", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SurveyEntry"]) -> 'SurveyMetadata': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SurveyElements"]) -> MetaOapg.properties.SurveyElements: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["SurveyEntry", "SurveyElements", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        SurveyEntry: 'SurveyMetadata',
        SurveyElements: typing.Union[MetaOapg.properties.SurveyElements, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SurveyQSF':
        return super().__new__(
            cls,
            *args,
            SurveyEntry=SurveyEntry,
            SurveyElements=SurveyElements,
            _configuration=_configuration,
            **kwargs,
        )

from qualtrics_survey_python_sdk.model.survey_element import SurveyElement
from qualtrics_survey_python_sdk.model.survey_metadata import SurveyMetadata