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


class OrgHierarchyUnitsExpression(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Logic expression for a Org Hierarchy Units type.
    """


    class MetaOapg:
        required = {
            "Description",
            "LogicType",
            "OrgHierarchyID",
        }
        
        class properties:
            Description = schemas.StrSchema
            
            
            class LogicType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ORG_HIERARCHY_UNITS(cls):
                    return cls("OrgHierarchyUnits")
        
            @staticmethod
            def OrgHierarchyID() -> typing.Type['OrgHierarchyID']:
                return OrgHierarchyID
        
            @staticmethod
            def Operator() -> typing.Type['ComparisonOperators']:
                return ComparisonOperators
        
            @staticmethod
            def UnitID() -> typing.Type['OrgHierarchyUnitID']:
                return OrgHierarchyUnitID
            
            
            class UnitName(
                schemas.StrSchema
            ):
                pass
            __annotations__ = {
                "Description": Description,
                "LogicType": LogicType,
                "OrgHierarchyID": OrgHierarchyID,
                "Operator": Operator,
                "UnitID": UnitID,
                "UnitName": UnitName,
            }
        additional_properties = schemas.AnyTypeSchema
    
    Description: MetaOapg.properties.Description
    LogicType: MetaOapg.properties.LogicType
    OrgHierarchyID: 'OrgHierarchyID'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Description"]) -> MetaOapg.properties.Description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LogicType"]) -> MetaOapg.properties.LogicType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OrgHierarchyID"]) -> 'OrgHierarchyID': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Operator"]) -> 'ComparisonOperators': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["UnitID"]) -> 'OrgHierarchyUnitID': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["UnitName"]) -> MetaOapg.properties.UnitName: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Description"], typing_extensions.Literal["LogicType"], typing_extensions.Literal["OrgHierarchyID"], typing_extensions.Literal["Operator"], typing_extensions.Literal["UnitID"], typing_extensions.Literal["UnitName"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Description"]) -> MetaOapg.properties.Description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LogicType"]) -> MetaOapg.properties.LogicType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OrgHierarchyID"]) -> 'OrgHierarchyID': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Operator"]) -> typing.Union['ComparisonOperators', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["UnitID"]) -> typing.Union['OrgHierarchyUnitID', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["UnitName"]) -> typing.Union[MetaOapg.properties.UnitName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Description"], typing_extensions.Literal["LogicType"], typing_extensions.Literal["OrgHierarchyID"], typing_extensions.Literal["Operator"], typing_extensions.Literal["UnitID"], typing_extensions.Literal["UnitName"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Description: typing.Union[MetaOapg.properties.Description, str, ],
        LogicType: typing.Union[MetaOapg.properties.LogicType, str, ],
        OrgHierarchyID: 'OrgHierarchyID',
        Operator: typing.Union['ComparisonOperators', schemas.Unset] = schemas.unset,
        UnitID: typing.Union['OrgHierarchyUnitID', schemas.Unset] = schemas.unset,
        UnitName: typing.Union[MetaOapg.properties.UnitName, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'OrgHierarchyUnitsExpression':
        return super().__new__(
            cls,
            *args,
            Description=Description,
            LogicType=LogicType,
            OrgHierarchyID=OrgHierarchyID,
            Operator=Operator,
            UnitID=UnitID,
            UnitName=UnitName,
            _configuration=_configuration,
            **kwargs,
        )

from qualtrics_survey_python_sdk.model.comparison_operators import ComparisonOperators
from qualtrics_survey_python_sdk.model.org_hierarchy_id import OrgHierarchyID
from qualtrics_survey_python_sdk.model.org_hierarchy_unit_id import OrgHierarchyUnitID
