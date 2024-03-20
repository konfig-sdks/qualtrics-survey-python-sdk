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


class AuthenticatorFlowElementOptions(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    SSO options.
    """


    class MetaOapg:
        
        class properties:
            maxAttempts = schemas.IntSchema
        
            @staticmethod
            def authenticationError() -> typing.Type['AuthenticatorMessage']:
                return AuthenticatorMessage
        
            @staticmethod
            def failedAuthenticationError() -> typing.Type['AuthenticatorMessage']:
                return AuthenticatorMessage
        
            @staticmethod
            def questionText() -> typing.Type['AuthenticatorMessage']:
                return AuthenticatorMessage
            allowRetake = schemas.BoolSchema
            loadExistingSession = schemas.BoolSchema
            __annotations__ = {
                "maxAttempts": maxAttempts,
                "authenticationError": authenticationError,
                "failedAuthenticationError": failedAuthenticationError,
                "questionText": questionText,
                "allowRetake": allowRetake,
                "loadExistingSession": loadExistingSession,
            }
        additional_properties = schemas.AnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxAttempts"]) -> MetaOapg.properties.maxAttempts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authenticationError"]) -> 'AuthenticatorMessage': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["failedAuthenticationError"]) -> 'AuthenticatorMessage': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["questionText"]) -> 'AuthenticatorMessage': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allowRetake"]) -> MetaOapg.properties.allowRetake: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["loadExistingSession"]) -> MetaOapg.properties.loadExistingSession: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["maxAttempts"], typing_extensions.Literal["authenticationError"], typing_extensions.Literal["failedAuthenticationError"], typing_extensions.Literal["questionText"], typing_extensions.Literal["allowRetake"], typing_extensions.Literal["loadExistingSession"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxAttempts"]) -> typing.Union[MetaOapg.properties.maxAttempts, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authenticationError"]) -> typing.Union['AuthenticatorMessage', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["failedAuthenticationError"]) -> typing.Union['AuthenticatorMessage', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["questionText"]) -> typing.Union['AuthenticatorMessage', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allowRetake"]) -> typing.Union[MetaOapg.properties.allowRetake, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["loadExistingSession"]) -> typing.Union[MetaOapg.properties.loadExistingSession, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["maxAttempts"], typing_extensions.Literal["authenticationError"], typing_extensions.Literal["failedAuthenticationError"], typing_extensions.Literal["questionText"], typing_extensions.Literal["allowRetake"], typing_extensions.Literal["loadExistingSession"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        maxAttempts: typing.Union[MetaOapg.properties.maxAttempts, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        authenticationError: typing.Union['AuthenticatorMessage', schemas.Unset] = schemas.unset,
        failedAuthenticationError: typing.Union['AuthenticatorMessage', schemas.Unset] = schemas.unset,
        questionText: typing.Union['AuthenticatorMessage', schemas.Unset] = schemas.unset,
        allowRetake: typing.Union[MetaOapg.properties.allowRetake, bool, schemas.Unset] = schemas.unset,
        loadExistingSession: typing.Union[MetaOapg.properties.loadExistingSession, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'AuthenticatorFlowElementOptions':
        return super().__new__(
            cls,
            *args,
            maxAttempts=maxAttempts,
            authenticationError=authenticationError,
            failedAuthenticationError=failedAuthenticationError,
            questionText=questionText,
            allowRetake=allowRetake,
            loadExistingSession=loadExistingSession,
            _configuration=_configuration,
            **kwargs,
        )

from qualtrics_survey_python_sdk.model.authenticator_message import AuthenticatorMessage