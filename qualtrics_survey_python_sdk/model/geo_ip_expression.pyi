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


class GeoIPExpression(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Logic expression for a Geo IP type.
    """


    class MetaOapg:
        required = {
            "Type",
            "Description",
            "LogicType",
        }
        
        class properties:
            
            
            class LogicType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def GEO_IP(cls):
                    return cls("GeoIP")
            Description = schemas.StrSchema
            
            
            class Type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def EXPRESSION(cls):
                    return cls("Expression")
            
            
            class LeftOperand(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def LOC__POSTAL_CODE(cls):
                    return cls("loc://PostalCode")
                
                @schemas.classproperty
                def LOC__CITY(cls):
                    return cls("loc://City")
                
                @schemas.classproperty
                def LOC__REGION(cls):
                    return cls("loc://Region")
                
                @schemas.classproperty
                def LOC__AREA_CODE(cls):
                    return cls("loc://AreaCode")
                
                @schemas.classproperty
                def LOC__COUNTRY_NAME(cls):
                    return cls("loc://CountryName")
                
                @schemas.classproperty
                def LOC__COUNTRY_CODE(cls):
                    return cls("loc://CountryCode")
                
                @schemas.classproperty
                def LOCATION_MAP(cls):
                    return cls("LocationMap")
        
            @staticmethod
            def Operator() -> typing.Type['ComparisonOperators']:
                return ComparisonOperators
            RightOperand = schemas.StrSchema
            __annotations__ = {
                "LogicType": LogicType,
                "Description": Description,
                "Type": Type,
                "LeftOperand": LeftOperand,
                "Operator": Operator,
                "RightOperand": RightOperand,
            }
        additional_properties = schemas.AnyTypeSchema
    
    Type: MetaOapg.properties.Type
    Description: MetaOapg.properties.Description
    LogicType: MetaOapg.properties.LogicType
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Type"]) -> MetaOapg.properties.Type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Description"]) -> MetaOapg.properties.Description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LogicType"]) -> MetaOapg.properties.LogicType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LeftOperand"]) -> MetaOapg.properties.LeftOperand: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Operator"]) -> 'ComparisonOperators': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["RightOperand"]) -> MetaOapg.properties.RightOperand: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Type"], typing_extensions.Literal["Description"], typing_extensions.Literal["LogicType"], typing_extensions.Literal["LeftOperand"], typing_extensions.Literal["Operator"], typing_extensions.Literal["RightOperand"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Type"]) -> MetaOapg.properties.Type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Description"]) -> MetaOapg.properties.Description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LogicType"]) -> MetaOapg.properties.LogicType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LeftOperand"]) -> typing.Union[MetaOapg.properties.LeftOperand, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Operator"]) -> typing.Union['ComparisonOperators', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["RightOperand"]) -> typing.Union[MetaOapg.properties.RightOperand, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Type"], typing_extensions.Literal["Description"], typing_extensions.Literal["LogicType"], typing_extensions.Literal["LeftOperand"], typing_extensions.Literal["Operator"], typing_extensions.Literal["RightOperand"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Type: typing.Union[MetaOapg.properties.Type, str, ],
        Description: typing.Union[MetaOapg.properties.Description, str, ],
        LogicType: typing.Union[MetaOapg.properties.LogicType, str, ],
        LeftOperand: typing.Union[MetaOapg.properties.LeftOperand, str, schemas.Unset] = schemas.unset,
        Operator: typing.Union['ComparisonOperators', schemas.Unset] = schemas.unset,
        RightOperand: typing.Union[MetaOapg.properties.RightOperand, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'GeoIPExpression':
        return super().__new__(
            cls,
            *args,
            Type=Type,
            Description=Description,
            LogicType=LogicType,
            LeftOperand=LeftOperand,
            Operator=Operator,
            RightOperand=RightOperand,
            _configuration=_configuration,
            **kwargs,
        )

from qualtrics_survey_python_sdk.model.comparison_operators import ComparisonOperators
