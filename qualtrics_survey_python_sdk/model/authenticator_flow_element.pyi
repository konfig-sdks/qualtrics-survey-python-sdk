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


class AuthenticatorFlowElement(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Require respondents to authenticate (login)
    """


    class MetaOapg:
        required = {
            "FieldData",
            "Options",
            "Type",
            "PanelData",
            "SSOOptions",
            "FilterDataFields",
        }
        
        class properties:
            
            
            class Type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def AUTHENTICATOR(cls):
                    return cls("Authenticator")
        
            @staticmethod
            def PanelData() -> typing.Type['AuthenticatorFlowElementPanelData']:
                return AuthenticatorFlowElementPanelData
        
            @staticmethod
            def FieldData() -> typing.Type['BranchLogic']:
                return BranchLogic
            FilterDataFields = schemas.BoolSchema
        
            @staticmethod
            def SSOOptions() -> typing.Type['AuthenticatorFlowElementSsoOptions']:
                return AuthenticatorFlowElementSsoOptions
        
            @staticmethod
            def Options() -> typing.Type['AuthenticatorFlowElementOptions']:
                return AuthenticatorFlowElementOptions
        
            @staticmethod
            def FlowID() -> typing.Type['FlowID']:
                return FlowID
        
            @staticmethod
            def Flow() -> typing.Type['Flow']:
                return Flow
            __annotations__ = {
                "Type": Type,
                "PanelData": PanelData,
                "FieldData": FieldData,
                "FilterDataFields": FilterDataFields,
                "SSOOptions": SSOOptions,
                "Options": Options,
                "FlowID": FlowID,
                "Flow": Flow,
            }
        additional_properties = schemas.AnyTypeSchema
    
    FieldData: 'BranchLogic'
    Options: 'AuthenticatorFlowElementOptions'
    Type: MetaOapg.properties.Type
    PanelData: 'AuthenticatorFlowElementPanelData'
    SSOOptions: 'AuthenticatorFlowElementSsoOptions'
    FilterDataFields: MetaOapg.properties.FilterDataFields
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FieldData"]) -> 'BranchLogic': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Options"]) -> 'AuthenticatorFlowElementOptions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Type"]) -> MetaOapg.properties.Type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PanelData"]) -> 'AuthenticatorFlowElementPanelData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SSOOptions"]) -> 'AuthenticatorFlowElementSsoOptions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FilterDataFields"]) -> MetaOapg.properties.FilterDataFields: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FlowID"]) -> 'FlowID': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Flow"]) -> 'Flow': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["FieldData"], typing_extensions.Literal["Options"], typing_extensions.Literal["Type"], typing_extensions.Literal["PanelData"], typing_extensions.Literal["SSOOptions"], typing_extensions.Literal["FilterDataFields"], typing_extensions.Literal["FlowID"], typing_extensions.Literal["Flow"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FieldData"]) -> 'BranchLogic': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Options"]) -> 'AuthenticatorFlowElementOptions': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Type"]) -> MetaOapg.properties.Type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PanelData"]) -> 'AuthenticatorFlowElementPanelData': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SSOOptions"]) -> 'AuthenticatorFlowElementSsoOptions': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FilterDataFields"]) -> MetaOapg.properties.FilterDataFields: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FlowID"]) -> typing.Union['FlowID', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Flow"]) -> typing.Union['Flow', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["FieldData"], typing_extensions.Literal["Options"], typing_extensions.Literal["Type"], typing_extensions.Literal["PanelData"], typing_extensions.Literal["SSOOptions"], typing_extensions.Literal["FilterDataFields"], typing_extensions.Literal["FlowID"], typing_extensions.Literal["Flow"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        FieldData: 'BranchLogic',
        Options: 'AuthenticatorFlowElementOptions',
        Type: typing.Union[MetaOapg.properties.Type, str, ],
        PanelData: 'AuthenticatorFlowElementPanelData',
        SSOOptions: 'AuthenticatorFlowElementSsoOptions',
        FilterDataFields: typing.Union[MetaOapg.properties.FilterDataFields, bool, ],
        FlowID: typing.Union['FlowID', schemas.Unset] = schemas.unset,
        Flow: typing.Union['Flow', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'AuthenticatorFlowElement':
        return super().__new__(
            cls,
            *args,
            FieldData=FieldData,
            Options=Options,
            Type=Type,
            PanelData=PanelData,
            SSOOptions=SSOOptions,
            FilterDataFields=FilterDataFields,
            FlowID=FlowID,
            Flow=Flow,
            _configuration=_configuration,
            **kwargs,
        )

from qualtrics_survey_python_sdk.model.authenticator_flow_element_options import AuthenticatorFlowElementOptions
from qualtrics_survey_python_sdk.model.authenticator_flow_element_panel_data import AuthenticatorFlowElementPanelData
from qualtrics_survey_python_sdk.model.authenticator_flow_element_sso_options import AuthenticatorFlowElementSsoOptions
from qualtrics_survey_python_sdk.model.branch_logic import BranchLogic
from qualtrics_survey_python_sdk.model.flow import Flow
from qualtrics_survey_python_sdk.model.flow_id import FlowID