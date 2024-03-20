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

from qualtrics_survey_python_sdk.model.referenced_block_id import ReferencedBlockID as ReferencedBlockIDSchema
from qualtrics_survey_python_sdk.model.block_id import BlockID as BlockIDSchema
from qualtrics_survey_python_sdk.model.request_successful_response import RequestSuccessfulResponse as RequestSuccessfulResponseSchema
from qualtrics_survey_python_sdk.model.block_definition import BlockDefinition as BlockDefinitionSchema
from qualtrics_survey_python_sdk.model.invalid_request_error_response import InvalidRequestErrorResponse as InvalidRequestErrorResponseSchema
from qualtrics_survey_python_sdk.model.library_id import LibraryID as LibraryIDSchema
from qualtrics_survey_python_sdk.model.internal_server_error_response import InternalServerErrorResponse as InternalServerErrorResponseSchema
from qualtrics_survey_python_sdk.model.block_elements import BlockElements as BlockElementsSchema
from qualtrics_survey_python_sdk.model.unauthorized_request_error_response import UnauthorizedRequestErrorResponse as UnauthorizedRequestErrorResponseSchema
from qualtrics_survey_python_sdk.model.forbidden_request_error_response import ForbiddenRequestErrorResponse as ForbiddenRequestErrorResponseSchema
from qualtrics_survey_python_sdk.model.survey_id import SurveyID as SurveyIDSchema
from qualtrics_survey_python_sdk.model.block_options import BlockOptions as BlockOptionsSchema
from qualtrics_survey_python_sdk.model.not_found_error_response import NotFoundErrorResponse as NotFoundErrorResponseSchema

from qualtrics_survey_python_sdk.type.library_id import LibraryID
from qualtrics_survey_python_sdk.type.block_elements import BlockElements
from qualtrics_survey_python_sdk.type.internal_server_error_response import InternalServerErrorResponse
from qualtrics_survey_python_sdk.type.invalid_request_error_response import InvalidRequestErrorResponse
from qualtrics_survey_python_sdk.type.unauthorized_request_error_response import UnauthorizedRequestErrorResponse
from qualtrics_survey_python_sdk.type.block_options import BlockOptions
from qualtrics_survey_python_sdk.type.referenced_block_id import ReferencedBlockID
from qualtrics_survey_python_sdk.type.block_id import BlockID
from qualtrics_survey_python_sdk.type.block_definition import BlockDefinition
from qualtrics_survey_python_sdk.type.survey_id import SurveyID
from qualtrics_survey_python_sdk.type.forbidden_request_error_response import ForbiddenRequestErrorResponse
from qualtrics_survey_python_sdk.type.not_found_error_response import NotFoundErrorResponse
from qualtrics_survey_python_sdk.type.request_successful_response import RequestSuccessfulResponse

from ...api_client import Dictionary
from qualtrics_survey_python_sdk.pydantic.block_id import BlockID as BlockIDPydantic
from qualtrics_survey_python_sdk.pydantic.survey_id import SurveyID as SurveyIDPydantic
from qualtrics_survey_python_sdk.pydantic.block_options import BlockOptions as BlockOptionsPydantic
from qualtrics_survey_python_sdk.pydantic.referenced_block_id import ReferencedBlockID as ReferencedBlockIDPydantic
from qualtrics_survey_python_sdk.pydantic.invalid_request_error_response import InvalidRequestErrorResponse as InvalidRequestErrorResponsePydantic
from qualtrics_survey_python_sdk.pydantic.forbidden_request_error_response import ForbiddenRequestErrorResponse as ForbiddenRequestErrorResponsePydantic
from qualtrics_survey_python_sdk.pydantic.request_successful_response import RequestSuccessfulResponse as RequestSuccessfulResponsePydantic
from qualtrics_survey_python_sdk.pydantic.block_elements import BlockElements as BlockElementsPydantic
from qualtrics_survey_python_sdk.pydantic.unauthorized_request_error_response import UnauthorizedRequestErrorResponse as UnauthorizedRequestErrorResponsePydantic
from qualtrics_survey_python_sdk.pydantic.block_definition import BlockDefinition as BlockDefinitionPydantic
from qualtrics_survey_python_sdk.pydantic.not_found_error_response import NotFoundErrorResponse as NotFoundErrorResponsePydantic
from qualtrics_survey_python_sdk.pydantic.library_id import LibraryID as LibraryIDPydantic
from qualtrics_survey_python_sdk.pydantic.internal_server_error_response import InternalServerErrorResponse as InternalServerErrorResponsePydantic

# Path params
SurveyIdSchema = schemas.Schema
BlockIdSchema = schemas.Schema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'surveyId': typing.Union[SurveyIDSchema, ],
        'blockId': typing.Union[BlockIDSchema, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_survey_id = api_client.PathParameter(
    name="surveyId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=SurveyIDSchema,
    required=True,
)
request_path_block_id = api_client.PathParameter(
    name="blockId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=BlockIDSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = BlockDefinitionSchema


request_body_block_definition = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = RequestSuccessfulResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: RequestSuccessfulResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: RequestSuccessfulResponse


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
SchemaFor404ResponseBodyApplicationJson = NotFoundErrorResponseSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: NotFoundErrorResponse


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: NotFoundErrorResponse


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
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
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _update_definition_block_mapped_args(
        self,
        survey_id: SurveyID,
        block_id: BlockID,
        block_elements: typing.Optional[BlockElements] = None,
        type: typing.Optional[str] = None,
        sub_type: typing.Optional[str] = None,
        id: typing.Optional[BlockID] = None,
        description: typing.Optional[str] = None,
        library_id: typing.Optional[LibraryID] = None,
        referenced_block_id: typing.Optional[ReferencedBlockID] = None,
        options: typing.Optional[BlockOptions] = None,
        body: typing.Optional[BlockDefinition] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if block_elements is not None:
            _body["BlockElements"] = block_elements
        if type is not None:
            _body["Type"] = type
        if sub_type is not None:
            _body["SubType"] = sub_type
        if id is not None:
            _body["ID"] = id
        if description is not None:
            _body["Description"] = description
        if library_id is not None:
            _body["LibraryID"] = library_id
        if referenced_block_id is not None:
            _body["ReferencedBlockID"] = referenced_block_id
        if options is not None:
            _body["Options"] = options
        args.body = body if body is not None else _body
        if survey_id is not None:
            _path_params["surveyId"] = survey_id
        if block_id is not None:
            _path_params["blockId"] = block_id
        args.path = _path_params
        return args

    async def _aupdate_definition_block_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
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
        Update Block
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_survey_id,
            request_path_block_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/survey-definitions/{surveyId}/blocks/{blockId}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_block_definition.serialize(body, content_type)
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


    def _update_definition_block_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
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
        Update Block
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_survey_id,
            request_path_block_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/survey-definitions/{surveyId}/blocks/{blockId}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_block_definition.serialize(body, content_type)
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


class UpdateDefinitionBlockRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_definition_block(
        self,
        survey_id: SurveyID,
        block_id: BlockID,
        block_elements: typing.Optional[BlockElements] = None,
        type: typing.Optional[str] = None,
        sub_type: typing.Optional[str] = None,
        id: typing.Optional[BlockID] = None,
        description: typing.Optional[str] = None,
        library_id: typing.Optional[LibraryID] = None,
        referenced_block_id: typing.Optional[ReferencedBlockID] = None,
        options: typing.Optional[BlockOptions] = None,
        body: typing.Optional[BlockDefinition] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_definition_block_mapped_args(
            body=body,
            survey_id=survey_id,
            block_id=block_id,
            block_elements=block_elements,
            type=type,
            sub_type=sub_type,
            id=id,
            description=description,
            library_id=library_id,
            referenced_block_id=referenced_block_id,
            options=options,
        )
        return await self._aupdate_definition_block_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_definition_block(
        self,
        survey_id: SurveyID,
        block_id: BlockID,
        block_elements: typing.Optional[BlockElements] = None,
        type: typing.Optional[str] = None,
        sub_type: typing.Optional[str] = None,
        id: typing.Optional[BlockID] = None,
        description: typing.Optional[str] = None,
        library_id: typing.Optional[LibraryID] = None,
        referenced_block_id: typing.Optional[ReferencedBlockID] = None,
        options: typing.Optional[BlockOptions] = None,
        body: typing.Optional[BlockDefinition] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_definition_block_mapped_args(
            body=body,
            survey_id=survey_id,
            block_id=block_id,
            block_elements=block_elements,
            type=type,
            sub_type=sub_type,
            id=id,
            description=description,
            library_id=library_id,
            referenced_block_id=referenced_block_id,
            options=options,
        )
        return self._update_definition_block_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdateDefinitionBlock(BaseApi):

    async def aupdate_definition_block(
        self,
        survey_id: SurveyID,
        block_id: BlockID,
        block_elements: typing.Optional[BlockElements] = None,
        type: typing.Optional[str] = None,
        sub_type: typing.Optional[str] = None,
        id: typing.Optional[BlockID] = None,
        description: typing.Optional[str] = None,
        library_id: typing.Optional[LibraryID] = None,
        referenced_block_id: typing.Optional[ReferencedBlockID] = None,
        options: typing.Optional[BlockOptions] = None,
        body: typing.Optional[BlockDefinition] = None,
        validate: bool = False,
        **kwargs,
    ) -> RequestSuccessfulResponsePydantic:
        raw_response = await self.raw.aupdate_definition_block(
            body=body,
            survey_id=survey_id,
            block_id=block_id,
            block_elements=block_elements,
            type=type,
            sub_type=sub_type,
            id=id,
            description=description,
            library_id=library_id,
            referenced_block_id=referenced_block_id,
            options=options,
            **kwargs,
        )
        if validate:
            return RequestSuccessfulResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(RequestSuccessfulResponsePydantic, raw_response.body)
    
    
    def update_definition_block(
        self,
        survey_id: SurveyID,
        block_id: BlockID,
        block_elements: typing.Optional[BlockElements] = None,
        type: typing.Optional[str] = None,
        sub_type: typing.Optional[str] = None,
        id: typing.Optional[BlockID] = None,
        description: typing.Optional[str] = None,
        library_id: typing.Optional[LibraryID] = None,
        referenced_block_id: typing.Optional[ReferencedBlockID] = None,
        options: typing.Optional[BlockOptions] = None,
        body: typing.Optional[BlockDefinition] = None,
        validate: bool = False,
    ) -> RequestSuccessfulResponsePydantic:
        raw_response = self.raw.update_definition_block(
            body=body,
            survey_id=survey_id,
            block_id=block_id,
            block_elements=block_elements,
            type=type,
            sub_type=sub_type,
            id=id,
            description=description,
            library_id=library_id,
            referenced_block_id=referenced_block_id,
            options=options,
        )
        if validate:
            return RequestSuccessfulResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(RequestSuccessfulResponsePydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        survey_id: SurveyID,
        block_id: BlockID,
        block_elements: typing.Optional[BlockElements] = None,
        type: typing.Optional[str] = None,
        sub_type: typing.Optional[str] = None,
        id: typing.Optional[BlockID] = None,
        description: typing.Optional[str] = None,
        library_id: typing.Optional[LibraryID] = None,
        referenced_block_id: typing.Optional[ReferencedBlockID] = None,
        options: typing.Optional[BlockOptions] = None,
        body: typing.Optional[BlockDefinition] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_definition_block_mapped_args(
            body=body,
            survey_id=survey_id,
            block_id=block_id,
            block_elements=block_elements,
            type=type,
            sub_type=sub_type,
            id=id,
            description=description,
            library_id=library_id,
            referenced_block_id=referenced_block_id,
            options=options,
        )
        return await self._aupdate_definition_block_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        survey_id: SurveyID,
        block_id: BlockID,
        block_elements: typing.Optional[BlockElements] = None,
        type: typing.Optional[str] = None,
        sub_type: typing.Optional[str] = None,
        id: typing.Optional[BlockID] = None,
        description: typing.Optional[str] = None,
        library_id: typing.Optional[LibraryID] = None,
        referenced_block_id: typing.Optional[ReferencedBlockID] = None,
        options: typing.Optional[BlockOptions] = None,
        body: typing.Optional[BlockDefinition] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_definition_block_mapped_args(
            body=body,
            survey_id=survey_id,
            block_id=block_id,
            block_elements=block_elements,
            type=type,
            sub_type=sub_type,
            id=id,
            description=description,
            library_id=library_id,
            referenced_block_id=referenced_block_id,
            options=options,
        )
        return self._update_definition_block_oapg(
            body=args.body,
            path_params=args.path,
        )
