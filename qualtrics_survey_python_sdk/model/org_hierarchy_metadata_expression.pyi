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


class OrgHierarchyMetadataExpression(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Logic expression for a Org Hierarchy Metadata type.
    """


    class MetaOapg:
        required = {
            "Type",
            "Description",
            "LogicType",
        }
        
        class properties:
            Description = schemas.StrSchema
            
            
            class LogicType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ORG_HIERARCHY_METADATA(cls):
                    return cls("OrgHierarchyMetadata")
            
            
            class Type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def EXPRESSION(cls):
                    return cls("Expression")
            
            
            class Field(
                schemas.StrSchema
            ):
                pass
            
            
            class Operator(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ARRAY_CONTAINS(cls):
                    return cls("ArrayContains")
        
            @staticmethod
            def OrgHierarchyDef() -> typing.Type['OrgHierarchyMetadataExpressionOrgHierarchyDef']:
                return OrgHierarchyMetadataExpressionOrgHierarchyDef
        
            @staticmethod
            def OrgHierarchyID() -> typing.Type['OrgHierarchyID']:
                return OrgHierarchyID
            
            
            class Value(
                schemas.StrSchema
            ):
                pass
            __annotations__ = {
                "Description": Description,
                "LogicType": LogicType,
                "Type": Type,
                "Field": Field,
                "Operator": Operator,
                "OrgHierarchyDef": OrgHierarchyDef,
                "OrgHierarchyID": OrgHierarchyID,
                "Value": Value,
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
    def __getitem__(self, name: typing_extensions.Literal["Field"]) -> MetaOapg.properties.Field: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Operator"]) -> MetaOapg.properties.Operator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OrgHierarchyDef"]) -> 'OrgHierarchyMetadataExpressionOrgHierarchyDef': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OrgHierarchyID"]) -> 'OrgHierarchyID': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Value"]) -> MetaOapg.properties.Value: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Type"], typing_extensions.Literal["Description"], typing_extensions.Literal["LogicType"], typing_extensions.Literal["Field"], typing_extensions.Literal["Operator"], typing_extensions.Literal["OrgHierarchyDef"], typing_extensions.Literal["OrgHierarchyID"], typing_extensions.Literal["Value"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Type"]) -> MetaOapg.properties.Type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Description"]) -> MetaOapg.properties.Description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LogicType"]) -> MetaOapg.properties.LogicType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Field"]) -> typing.Union[MetaOapg.properties.Field, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Operator"]) -> typing.Union[MetaOapg.properties.Operator, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OrgHierarchyDef"]) -> typing.Union['OrgHierarchyMetadataExpressionOrgHierarchyDef', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OrgHierarchyID"]) -> typing.Union['OrgHierarchyID', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Value"]) -> typing.Union[MetaOapg.properties.Value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Type"], typing_extensions.Literal["Description"], typing_extensions.Literal["LogicType"], typing_extensions.Literal["Field"], typing_extensions.Literal["Operator"], typing_extensions.Literal["OrgHierarchyDef"], typing_extensions.Literal["OrgHierarchyID"], typing_extensions.Literal["Value"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Type: typing.Union[MetaOapg.properties.Type, str, ],
        Description: typing.Union[MetaOapg.properties.Description, str, ],
        LogicType: typing.Union[MetaOapg.properties.LogicType, str, ],
        Field: typing.Union[MetaOapg.properties.Field, str, schemas.Unset] = schemas.unset,
        Operator: typing.Union[MetaOapg.properties.Operator, str, schemas.Unset] = schemas.unset,
        OrgHierarchyDef: typing.Union['OrgHierarchyMetadataExpressionOrgHierarchyDef', schemas.Unset] = schemas.unset,
        OrgHierarchyID: typing.Union['OrgHierarchyID', schemas.Unset] = schemas.unset,
        Value: typing.Union[MetaOapg.properties.Value, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'OrgHierarchyMetadataExpression':
        return super().__new__(
            cls,
            *args,
            Type=Type,
            Description=Description,
            LogicType=LogicType,
            Field=Field,
            Operator=Operator,
            OrgHierarchyDef=OrgHierarchyDef,
            OrgHierarchyID=OrgHierarchyID,
            Value=Value,
            _configuration=_configuration,
            **kwargs,
        )

from qualtrics_survey_python_sdk.model.org_hierarchy_id import OrgHierarchyID
from qualtrics_survey_python_sdk.model.org_hierarchy_metadata_expression_org_hierarchy_def import OrgHierarchyMetadataExpressionOrgHierarchyDef
