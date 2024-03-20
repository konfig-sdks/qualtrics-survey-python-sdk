# coding: utf-8

"""
    Qualtrics Survey API

    The Qualtrics Survey endpoints give you access to the structure of the surveys you create.   Surveys have a complex structure, and you are encouraged to become familiar with the structure using your brand's Qualtrics page to build surveys at first. Then you can query those surveys using these endpoints.   Once you are familiar, you can use this API to create surveys on the fly, or modify existing surveys in your library. 

    The version of the OpenAPI document: 3.0.0
    Created by: https://www.qualtrics.com/support/
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from qualtrics_survey_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from qualtrics_survey_python_sdk.api_response import AsyncGeneratorResponse
from qualtrics_survey_python_sdk import api_client, exceptions
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

from qualtrics_survey_python_sdk.model.survey_metadata import SurveyMetadata as SurveyMetadataSchema
from qualtrics_survey_python_sdk.model.unauthorized_request_error_response import UnauthorizedRequestErrorResponse as UnauthorizedRequestErrorResponseSchema
from qualtrics_survey_python_sdk.model.forbidden_request_error_response import ForbiddenRequestErrorResponse as ForbiddenRequestErrorResponseSchema
from qualtrics_survey_python_sdk.model.project_category import ProjectCategory as ProjectCategorySchema
from qualtrics_survey_python_sdk.model.create_survey_request import CreateSurveyRequest as CreateSurveyRequestSchema
from qualtrics_survey_python_sdk.model.language_code import LanguageCode as LanguageCodeSchema
from qualtrics_survey_python_sdk.model.create_survey_response import CreateSurveyResponse as CreateSurveyResponseSchema
from qualtrics_survey_python_sdk.model.invalid_request_error_response import InvalidRequestErrorResponse as InvalidRequestErrorResponseSchema
from qualtrics_survey_python_sdk.model.survey_element import SurveyElement as SurveyElementSchema
from qualtrics_survey_python_sdk.model.internal_server_error_response import InternalServerErrorResponse as InternalServerErrorResponseSchema

from qualtrics_survey_python_sdk.type.create_survey_request import CreateSurveyRequest
from qualtrics_survey_python_sdk.type.survey_element import SurveyElement
from qualtrics_survey_python_sdk.type.project_category import ProjectCategory
from qualtrics_survey_python_sdk.type.forbidden_request_error_response import ForbiddenRequestErrorResponse
from qualtrics_survey_python_sdk.type.internal_server_error_response import InternalServerErrorResponse
from qualtrics_survey_python_sdk.type.invalid_request_error_response import InvalidRequestErrorResponse
from qualtrics_survey_python_sdk.type.unauthorized_request_error_response import UnauthorizedRequestErrorResponse
from qualtrics_survey_python_sdk.type.create_survey_response import CreateSurveyResponse
from qualtrics_survey_python_sdk.type.survey_metadata import SurveyMetadata
from qualtrics_survey_python_sdk.type.language_code import LanguageCode

from ...api_client import Dictionary
from qualtrics_survey_python_sdk.pydantic.project_category import ProjectCategory as ProjectCategoryPydantic
from qualtrics_survey_python_sdk.pydantic.unauthorized_request_error_response import UnauthorizedRequestErrorResponse as UnauthorizedRequestErrorResponsePydantic
from qualtrics_survey_python_sdk.pydantic.create_survey_request import CreateSurveyRequest as CreateSurveyRequestPydantic
from qualtrics_survey_python_sdk.pydantic.survey_metadata import SurveyMetadata as SurveyMetadataPydantic
from qualtrics_survey_python_sdk.pydantic.survey_element import SurveyElement as SurveyElementPydantic
from qualtrics_survey_python_sdk.pydantic.language_code import LanguageCode as LanguageCodePydantic
from qualtrics_survey_python_sdk.pydantic.create_survey_response import CreateSurveyResponse as CreateSurveyResponsePydantic
from qualtrics_survey_python_sdk.pydantic.forbidden_request_error_response import ForbiddenRequestErrorResponse as ForbiddenRequestErrorResponsePydantic
from qualtrics_survey_python_sdk.pydantic.invalid_request_error_response import InvalidRequestErrorResponse as InvalidRequestErrorResponsePydantic
from qualtrics_survey_python_sdk.pydantic.internal_server_error_response import InternalServerErrorResponse as InternalServerErrorResponsePydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = CreateSurveyRequestSchema


request_body_create_survey_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'public_oauth2',
    'public_oauth2',
]
SchemaFor200ResponseBodyApplicationJson = CreateSurveyResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: CreateSurveyResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: CreateSurveyResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = InvalidRequestErrorResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: InvalidRequestErrorResponse


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: InvalidRequestErrorResponse


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = UnauthorizedRequestErrorResponseSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: UnauthorizedRequestErrorResponse


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: UnauthorizedRequestErrorResponse


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationJson = ForbiddenRequestErrorResponseSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: ForbiddenRequestErrorResponse


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: ForbiddenRequestErrorResponse


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)
SchemaFor500ResponseBodyApplicationJson = InternalServerErrorResponseSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: InternalServerErrorResponse


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: InternalServerErrorResponse


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
    '403': _response_for_403,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_definition_mapped_args(
        self,
        survey_name: typing.Optional[str] = None,
        language: typing.Optional[LanguageCode] = None,
        project_category: typing.Optional[ProjectCategory] = None,
        survey_entry: typing.Optional[SurveyMetadata] = None,
        survey_elements: typing.Optional[typing.List[SurveyElement]] = None,
        body: typing.Optional[CreateSurveyRequest] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if survey_name is not None:
            _body["SurveyName"] = survey_name
        if language is not None:
            _body["Language"] = language
        if project_category is not None:
            _body["ProjectCategory"] = project_category
        if survey_entry is not None:
            _body["SurveyEntry"] = survey_entry
        if survey_elements is not None:
            _body["SurveyElements"] = survey_elements
        args.body = body if body is not None else _body
        return args

    async def _acreate_definition_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create Survey
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/survey-definitions',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_create_survey_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _create_definition_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create Survey
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/survey-definitions',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_create_survey_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CreateDefinitionRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_definition(
        self,
        survey_name: typing.Optional[str] = None,
        language: typing.Optional[LanguageCode] = None,
        project_category: typing.Optional[ProjectCategory] = None,
        survey_entry: typing.Optional[SurveyMetadata] = None,
        survey_elements: typing.Optional[typing.List[SurveyElement]] = None,
        body: typing.Optional[CreateSurveyRequest] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_definition_mapped_args(
            body=body,
            survey_name=survey_name,
            language=language,
            project_category=project_category,
            survey_entry=survey_entry,
            survey_elements=survey_elements,
        )
        return await self._acreate_definition_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_definition(
        self,
        survey_name: typing.Optional[str] = None,
        language: typing.Optional[LanguageCode] = None,
        project_category: typing.Optional[ProjectCategory] = None,
        survey_entry: typing.Optional[SurveyMetadata] = None,
        survey_elements: typing.Optional[typing.List[SurveyElement]] = None,
        body: typing.Optional[CreateSurveyRequest] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_definition_mapped_args(
            body=body,
            survey_name=survey_name,
            language=language,
            project_category=project_category,
            survey_entry=survey_entry,
            survey_elements=survey_elements,
        )
        return self._create_definition_oapg(
            body=args.body,
        )

class CreateDefinition(BaseApi):

    async def acreate_definition(
        self,
        survey_name: typing.Optional[str] = None,
        language: typing.Optional[LanguageCode] = None,
        project_category: typing.Optional[ProjectCategory] = None,
        survey_entry: typing.Optional[SurveyMetadata] = None,
        survey_elements: typing.Optional[typing.List[SurveyElement]] = None,
        body: typing.Optional[CreateSurveyRequest] = None,
        validate: bool = False,
        **kwargs,
    ) -> CreateSurveyResponsePydantic:
        raw_response = await self.raw.acreate_definition(
            body=body,
            survey_name=survey_name,
            language=language,
            project_category=project_category,
            survey_entry=survey_entry,
            survey_elements=survey_elements,
            **kwargs,
        )
        if validate:
            return CreateSurveyResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CreateSurveyResponsePydantic, raw_response.body)
    
    
    def create_definition(
        self,
        survey_name: typing.Optional[str] = None,
        language: typing.Optional[LanguageCode] = None,
        project_category: typing.Optional[ProjectCategory] = None,
        survey_entry: typing.Optional[SurveyMetadata] = None,
        survey_elements: typing.Optional[typing.List[SurveyElement]] = None,
        body: typing.Optional[CreateSurveyRequest] = None,
        validate: bool = False,
    ) -> CreateSurveyResponsePydantic:
        raw_response = self.raw.create_definition(
            body=body,
            survey_name=survey_name,
            language=language,
            project_category=project_category,
            survey_entry=survey_entry,
            survey_elements=survey_elements,
        )
        if validate:
            return CreateSurveyResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CreateSurveyResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        survey_name: typing.Optional[str] = None,
        language: typing.Optional[LanguageCode] = None,
        project_category: typing.Optional[ProjectCategory] = None,
        survey_entry: typing.Optional[SurveyMetadata] = None,
        survey_elements: typing.Optional[typing.List[SurveyElement]] = None,
        body: typing.Optional[CreateSurveyRequest] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_definition_mapped_args(
            body=body,
            survey_name=survey_name,
            language=language,
            project_category=project_category,
            survey_entry=survey_entry,
            survey_elements=survey_elements,
        )
        return await self._acreate_definition_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        survey_name: typing.Optional[str] = None,
        language: typing.Optional[LanguageCode] = None,
        project_category: typing.Optional[ProjectCategory] = None,
        survey_entry: typing.Optional[SurveyMetadata] = None,
        survey_elements: typing.Optional[typing.List[SurveyElement]] = None,
        body: typing.Optional[CreateSurveyRequest] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_definition_mapped_args(
            body=body,
            survey_name=survey_name,
            language=language,
            project_category=project_category,
            survey_entry=survey_entry,
            survey_elements=survey_elements,
        )
        return self._create_definition_oapg(
            body=args.body,
        )

