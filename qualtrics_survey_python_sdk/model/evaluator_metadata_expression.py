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


class EvaluatorMetadataExpression(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Logic expression for a Evaluator Metadata type
    """


    class MetaOapg:
        required = {
            "Type",
            "Description",
            "LogicType",
            "LeftOperand",
            "PersonMeta",
        }
        
        class properties:
            
            
            class LogicType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "EvaluatorMetadata": "EVALUATOR_METADATA",
                    }
                
                @schemas.classproperty
                def EVALUATOR_METADATA(cls):
                    return cls("EvaluatorMetadata")
            Description = schemas.StrSchema
            
            
            class LeftOperand(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^e://Field/.*$',
                    }]
            
            
            class PersonMeta(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 100
            
            
            class Type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "Expression": "EXPRESSION",
                    }
                
                @schemas.classproperty
                def EXPRESSION(cls):
                    return cls("Expression")
        
            @staticmethod
            def Operator() -> typing.Type['ComparisonOperators']:
                return ComparisonOperators
            RightOperand = schemas.StrSchema
            
            
            class SameAsSubjectRightOperand(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^e://Field/.*$',
                    }]
            __annotations__ = {
                "LogicType": LogicType,
                "Description": Description,
                "LeftOperand": LeftOperand,
                "PersonMeta": PersonMeta,
                "Type": Type,
                "Operator": Operator,
                "RightOperand": RightOperand,
                "SameAsSubjectRightOperand": SameAsSubjectRightOperand,
            }
        additional_properties = schemas.AnyTypeSchema
    
    Type: MetaOapg.properties.Type
    Description: MetaOapg.properties.Description
    LogicType: MetaOapg.properties.LogicType
    LeftOperand: MetaOapg.properties.LeftOperand
    PersonMeta: MetaOapg.properties.PersonMeta
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Type"]) -> MetaOapg.properties.Type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Description"]) -> MetaOapg.properties.Description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LogicType"]) -> MetaOapg.properties.LogicType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LeftOperand"]) -> MetaOapg.properties.LeftOperand: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PersonMeta"]) -> MetaOapg.properties.PersonMeta: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Operator"]) -> 'ComparisonOperators': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["RightOperand"]) -> MetaOapg.properties.RightOperand: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SameAsSubjectRightOperand"]) -> MetaOapg.properties.SameAsSubjectRightOperand: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Type"], typing_extensions.Literal["Description"], typing_extensions.Literal["LogicType"], typing_extensions.Literal["LeftOperand"], typing_extensions.Literal["PersonMeta"], typing_extensions.Literal["Operator"], typing_extensions.Literal["RightOperand"], typing_extensions.Literal["SameAsSubjectRightOperand"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Type"]) -> MetaOapg.properties.Type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Description"]) -> MetaOapg.properties.Description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LogicType"]) -> MetaOapg.properties.LogicType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LeftOperand"]) -> MetaOapg.properties.LeftOperand: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PersonMeta"]) -> MetaOapg.properties.PersonMeta: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Operator"]) -> typing.Union['ComparisonOperators', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["RightOperand"]) -> typing.Union[MetaOapg.properties.RightOperand, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SameAsSubjectRightOperand"]) -> typing.Union[MetaOapg.properties.SameAsSubjectRightOperand, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Type"], typing_extensions.Literal["Description"], typing_extensions.Literal["LogicType"], typing_extensions.Literal["LeftOperand"], typing_extensions.Literal["PersonMeta"], typing_extensions.Literal["Operator"], typing_extensions.Literal["RightOperand"], typing_extensions.Literal["SameAsSubjectRightOperand"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Type: typing.Union[MetaOapg.properties.Type, str, ],
        Description: typing.Union[MetaOapg.properties.Description, str, ],
        LogicType: typing.Union[MetaOapg.properties.LogicType, str, ],
        LeftOperand: typing.Union[MetaOapg.properties.LeftOperand, str, ],
        PersonMeta: typing.Union[MetaOapg.properties.PersonMeta, str, ],
        Operator: typing.Union['ComparisonOperators', schemas.Unset] = schemas.unset,
        RightOperand: typing.Union[MetaOapg.properties.RightOperand, str, schemas.Unset] = schemas.unset,
        SameAsSubjectRightOperand: typing.Union[MetaOapg.properties.SameAsSubjectRightOperand, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'EvaluatorMetadataExpression':
        return super().__new__(
            cls,
            *args,
            Type=Type,
            Description=Description,
            LogicType=LogicType,
            LeftOperand=LeftOperand,
            PersonMeta=PersonMeta,
            Operator=Operator,
            RightOperand=RightOperand,
            SameAsSubjectRightOperand=SameAsSubjectRightOperand,
            _configuration=_configuration,
            **kwargs,
        )

from qualtrics_survey_python_sdk.model.comparison_operators import ComparisonOperators
