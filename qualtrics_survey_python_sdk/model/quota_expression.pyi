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


class QuotaExpression(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Logic expression for a quota type.
    """


    class MetaOapg:
        required = {
            "QuotaID",
            "Type",
            "Description",
            "LogicType",
            "QuotaType",
            "LeftOperand",
        }
        
        class properties:
            
            
            class LogicType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def QUOTA(cls):
                    return cls("Quota")
            Description = schemas.StrSchema
            
            
            class LeftOperand(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def QuotaID() -> typing.Type['QuotaID']:
                return QuotaID
            
            
            class QuotaType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def SIMPLE(cls):
                    return cls("Simple")
                
                @schemas.classproperty
                def CROSS(cls):
                    return cls("Cross")
                
                @schemas.classproperty
                def NO_LOGIC(cls):
                    return cls("NoLogic")
            
            
            class Type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def EXPRESSION(cls):
                    return cls("Expression")
            
            
            class Operator(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def QUOTA_MET(cls):
                    return cls("QuotaMet")
                
                @schemas.classproperty
                def QUOTA_NOT_MET(cls):
                    return cls("QuotaNotMet")
                
                @schemas.classproperty
                def GREATER_THAN(cls):
                    return cls("GreaterThan")
                
                @schemas.classproperty
                def GREATER_THAN_OR_EQUAL(cls):
                    return cls("GreaterThanOrEqual")
                
                @schemas.classproperty
                def LESS_THAN(cls):
                    return cls("LessThan")
                
                @schemas.classproperty
                def LESS_THAN_OR_EQUAL(cls):
                    return cls("LessThanOrEqual")
                
                @schemas.classproperty
                def EQUAL_TO(cls):
                    return cls("EqualTo")
                
                @schemas.classproperty
                def NOT_EQUAL_TO(cls):
                    return cls("NotEqualTo")
            QuotaName = schemas.StrSchema
            
            
            class SubQuotaID(
                schemas.StrSchema
            ):
                pass
            __annotations__ = {
                "LogicType": LogicType,
                "Description": Description,
                "LeftOperand": LeftOperand,
                "QuotaID": QuotaID,
                "QuotaType": QuotaType,
                "Type": Type,
                "Operator": Operator,
                "QuotaName": QuotaName,
                "SubQuotaID": SubQuotaID,
            }
        additional_properties = schemas.AnyTypeSchema
    
    QuotaID: 'QuotaID'
    Type: MetaOapg.properties.Type
    Description: MetaOapg.properties.Description
    LogicType: MetaOapg.properties.LogicType
    QuotaType: MetaOapg.properties.QuotaType
    LeftOperand: MetaOapg.properties.LeftOperand
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["QuotaID"]) -> 'QuotaID': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Type"]) -> MetaOapg.properties.Type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Description"]) -> MetaOapg.properties.Description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LogicType"]) -> MetaOapg.properties.LogicType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["QuotaType"]) -> MetaOapg.properties.QuotaType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LeftOperand"]) -> MetaOapg.properties.LeftOperand: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Operator"]) -> MetaOapg.properties.Operator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["QuotaName"]) -> MetaOapg.properties.QuotaName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SubQuotaID"]) -> MetaOapg.properties.SubQuotaID: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["QuotaID"], typing_extensions.Literal["Type"], typing_extensions.Literal["Description"], typing_extensions.Literal["LogicType"], typing_extensions.Literal["QuotaType"], typing_extensions.Literal["LeftOperand"], typing_extensions.Literal["Operator"], typing_extensions.Literal["QuotaName"], typing_extensions.Literal["SubQuotaID"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["QuotaID"]) -> 'QuotaID': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Type"]) -> MetaOapg.properties.Type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Description"]) -> MetaOapg.properties.Description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LogicType"]) -> MetaOapg.properties.LogicType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["QuotaType"]) -> MetaOapg.properties.QuotaType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LeftOperand"]) -> MetaOapg.properties.LeftOperand: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Operator"]) -> typing.Union[MetaOapg.properties.Operator, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["QuotaName"]) -> typing.Union[MetaOapg.properties.QuotaName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SubQuotaID"]) -> typing.Union[MetaOapg.properties.SubQuotaID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["QuotaID"], typing_extensions.Literal["Type"], typing_extensions.Literal["Description"], typing_extensions.Literal["LogicType"], typing_extensions.Literal["QuotaType"], typing_extensions.Literal["LeftOperand"], typing_extensions.Literal["Operator"], typing_extensions.Literal["QuotaName"], typing_extensions.Literal["SubQuotaID"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        QuotaID: 'QuotaID',
        Type: typing.Union[MetaOapg.properties.Type, str, ],
        Description: typing.Union[MetaOapg.properties.Description, str, ],
        LogicType: typing.Union[MetaOapg.properties.LogicType, str, ],
        QuotaType: typing.Union[MetaOapg.properties.QuotaType, str, ],
        LeftOperand: typing.Union[MetaOapg.properties.LeftOperand, str, ],
        Operator: typing.Union[MetaOapg.properties.Operator, str, schemas.Unset] = schemas.unset,
        QuotaName: typing.Union[MetaOapg.properties.QuotaName, str, schemas.Unset] = schemas.unset,
        SubQuotaID: typing.Union[MetaOapg.properties.SubQuotaID, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'QuotaExpression':
        return super().__new__(
            cls,
            *args,
            QuotaID=QuotaID,
            Type=Type,
            Description=Description,
            LogicType=LogicType,
            QuotaType=QuotaType,
            LeftOperand=LeftOperand,
            Operator=Operator,
            QuotaName=QuotaName,
            SubQuotaID=SubQuotaID,
            _configuration=_configuration,
            **kwargs,
        )

from qualtrics_survey_python_sdk.model.quota_id import QuotaID
