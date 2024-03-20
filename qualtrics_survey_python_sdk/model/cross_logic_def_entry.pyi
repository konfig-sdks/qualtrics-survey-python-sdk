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


class CrossLogicDefEntry(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "Description",
            "Occurrences",
            "ID",
            "Logic",
        }
        
        class properties:
            Occurrences = schemas.NumberSchema
            Description = schemas.StrSchema
            
            
            class ID(
                schemas.IntSchema
            ):
                pass
        
            @staticmethod
            def Logic() -> typing.Type['LogicObject']:
                return LogicObject
            Count = schemas.IntSchema
            OverrideOccurrences = schemas.IntSchema
            __annotations__ = {
                "Occurrences": Occurrences,
                "Description": Description,
                "ID": ID,
                "Logic": Logic,
                "Count": Count,
                "OverrideOccurrences": OverrideOccurrences,
            }
    
    Description: MetaOapg.properties.Description
    Occurrences: MetaOapg.properties.Occurrences
    ID: MetaOapg.properties.ID
    Logic: 'LogicObject'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Occurrences"]) -> MetaOapg.properties.Occurrences: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Description"]) -> MetaOapg.properties.Description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ID"]) -> MetaOapg.properties.ID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Logic"]) -> 'LogicObject': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Count"]) -> MetaOapg.properties.Count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OverrideOccurrences"]) -> MetaOapg.properties.OverrideOccurrences: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Occurrences", "Description", "ID", "Logic", "Count", "OverrideOccurrences", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Occurrences"]) -> MetaOapg.properties.Occurrences: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Description"]) -> MetaOapg.properties.Description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ID"]) -> MetaOapg.properties.ID: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Logic"]) -> 'LogicObject': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Count"]) -> typing.Union[MetaOapg.properties.Count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OverrideOccurrences"]) -> typing.Union[MetaOapg.properties.OverrideOccurrences, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Occurrences", "Description", "ID", "Logic", "Count", "OverrideOccurrences", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Description: typing.Union[MetaOapg.properties.Description, str, ],
        Occurrences: typing.Union[MetaOapg.properties.Occurrences, decimal.Decimal, int, float, ],
        ID: typing.Union[MetaOapg.properties.ID, decimal.Decimal, int, ],
        Logic: 'LogicObject',
        Count: typing.Union[MetaOapg.properties.Count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        OverrideOccurrences: typing.Union[MetaOapg.properties.OverrideOccurrences, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CrossLogicDefEntry':
        return super().__new__(
            cls,
            *args,
            Description=Description,
            Occurrences=Occurrences,
            ID=ID,
            Logic=Logic,
            Count=Count,
            OverrideOccurrences=OverrideOccurrences,
            _configuration=_configuration,
            **kwargs,
        )

from qualtrics_survey_python_sdk.model.logic_object import LogicObject
