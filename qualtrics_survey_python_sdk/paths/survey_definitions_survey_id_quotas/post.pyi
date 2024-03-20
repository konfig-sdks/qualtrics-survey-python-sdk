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

from qualtrics_survey_python_sdk.model.quota_action import QuotaAction as QuotaActionSchema
from qualtrics_survey_python_sdk.model.action_info import ActionInfo as ActionInfoSchema
from qualtrics_survey_python_sdk.model.invalid_request_error_response import InvalidRequestErrorResponse as InvalidRequestErrorResponseSchema
from qualtrics_survey_python_sdk.model.quota_id import QuotaID as QuotaIDSchema
from qualtrics_survey_python_sdk.model.internal_server_error_response import InternalServerErrorResponse as InternalServerErrorResponseSchema
from qualtrics_survey_python_sdk.model.quota_schedule import QuotaSchedule as QuotaScheduleSchema
from qualtrics_survey_python_sdk.model.unauthorized_request_error_response import UnauthorizedRequestErrorResponse as UnauthorizedRequestErrorResponseSchema
from qualtrics_survey_python_sdk.model.end_survey_options import EndSurveyOptions as EndSurveyOptionsSchema
from qualtrics_survey_python_sdk.model.web_service_options import WebServiceOptions as WebServiceOptionsSchema
from qualtrics_survey_python_sdk.model.forbidden_request_error_response import ForbiddenRequestErrorResponse as ForbiddenRequestErrorResponseSchema
from qualtrics_survey_python_sdk.model.create_quota_response import CreateQuotaResponse as CreateQuotaResponseSchema
from qualtrics_survey_python_sdk.model.logic_object import LogicObject as LogicObjectSchema
from qualtrics_survey_python_sdk.model.survey_id import SurveyID as SurveyIDSchema
from qualtrics_survey_python_sdk.model.quota_group_id import QuotaGroupID as QuotaGroupIDSchema
from qualtrics_survey_python_sdk.model.not_found_error_response import NotFoundErrorResponse as NotFoundErrorResponseSchema
from qualtrics_survey_python_sdk.model.cross_logic_def_entry import CrossLogicDefEntry as CrossLogicDefEntrySchema
from qualtrics_survey_python_sdk.model.quota import Quota as QuotaSchema

from qualtrics_survey_python_sdk.type.end_survey_options import EndSurveyOptions
from qualtrics_survey_python_sdk.type.quota_id import QuotaID
from qualtrics_survey_python_sdk.type.quota_action import QuotaAction
from qualtrics_survey_python_sdk.type.web_service_options import WebServiceOptions
from qualtrics_survey_python_sdk.type.action_info import ActionInfo
from qualtrics_survey_python_sdk.type.internal_server_error_response import InternalServerErrorResponse
from qualtrics_survey_python_sdk.type.invalid_request_error_response import InvalidRequestErrorResponse
from qualtrics_survey_python_sdk.type.unauthorized_request_error_response import UnauthorizedRequestErrorResponse
from qualtrics_survey_python_sdk.type.logic_object import LogicObject
from qualtrics_survey_python_sdk.type.cross_logic_def_entry import CrossLogicDefEntry
from qualtrics_survey_python_sdk.type.survey_id import SurveyID
from qualtrics_survey_python_sdk.type.forbidden_request_error_response import ForbiddenRequestErrorResponse
from qualtrics_survey_python_sdk.type.quota_group_id import QuotaGroupID
from qualtrics_survey_python_sdk.type.quota_schedule import QuotaSchedule
from qualtrics_survey_python_sdk.type.quota import Quota
from qualtrics_survey_python_sdk.type.create_quota_response import CreateQuotaResponse
from qualtrics_survey_python_sdk.type.not_found_error_response import NotFoundErrorResponse

from ...api_client import Dictionary
from qualtrics_survey_python_sdk.pydantic.quota import Quota as QuotaPydantic
from qualtrics_survey_python_sdk.pydantic.action_info import ActionInfo as ActionInfoPydantic
from qualtrics_survey_python_sdk.pydantic.quota_action import QuotaAction as QuotaActionPydantic
from qualtrics_survey_python_sdk.pydantic.survey_id import SurveyID as SurveyIDPydantic
from qualtrics_survey_python_sdk.pydantic.quota_group_id import QuotaGroupID as QuotaGroupIDPydantic
from qualtrics_survey_python_sdk.pydantic.web_service_options import WebServiceOptions as WebServiceOptionsPydantic
from qualtrics_survey_python_sdk.pydantic.invalid_request_error_response import InvalidRequestErrorResponse as InvalidRequestErrorResponsePydantic
from qualtrics_survey_python_sdk.pydantic.forbidden_request_error_response import ForbiddenRequestErrorResponse as ForbiddenRequestErrorResponsePydantic
from qualtrics_survey_python_sdk.pydantic.quota_schedule import QuotaSchedule as QuotaSchedulePydantic
from qualtrics_survey_python_sdk.pydantic.unauthorized_request_error_response import UnauthorizedRequestErrorResponse as UnauthorizedRequestErrorResponsePydantic
from qualtrics_survey_python_sdk.pydantic.quota_id import QuotaID as QuotaIDPydantic
from qualtrics_survey_python_sdk.pydantic.not_found_error_response import NotFoundErrorResponse as NotFoundErrorResponsePydantic
from qualtrics_survey_python_sdk.pydantic.cross_logic_def_entry import CrossLogicDefEntry as CrossLogicDefEntryPydantic
from qualtrics_survey_python_sdk.pydantic.logic_object import LogicObject as LogicObjectPydantic
from qualtrics_survey_python_sdk.pydantic.create_quota_response import CreateQuotaResponse as CreateQuotaResponsePydantic
from qualtrics_survey_python_sdk.pydantic.end_survey_options import EndSurveyOptions as EndSurveyOptionsPydantic
from qualtrics_survey_python_sdk.pydantic.internal_server_error_response import InternalServerErrorResponse as InternalServerErrorResponsePydantic

# Query params
QuotaGroupIdSchema = schemas.Schema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'quotaGroupId': typing.Union[QuotaGroupIdSchema, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_quota_group_id = api_client.QueryParameter(
    name="quotaGroupId",
    style=api_client.ParameterStyle.FORM,
    schema=QuotaGroupIDSchema,
    explode=True,
)
# Path params
SurveyIdSchema = schemas.Schema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'surveyId': typing.Union[SurveyIDSchema, ],
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
# body param
SchemaForRequestBodyApplicationJson = QuotaSchema


request_body_quota = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = CreateQuotaResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: CreateQuotaResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: CreateQuotaResponse


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

    def _create_new_quota_mapped_args(
        self,
        name: str,
        occurrences: int,
        logic: typing.Union[LogicObject, typing.List[LogicObject]],
        quota_action: QuotaAction,
        id: QuotaID,
        quota_realm: str,
        survey_id: SurveyID,
        count: typing.Optional[int] = None,
        count_for_undo: typing.Optional[int] = None,
        logic_type: typing.Optional[typing.Union[str]] = None,
        action_element: typing.Optional[typing.Union[SurveyID, QuestionID, BlockID, str]] = None,
        action_info: typing.Optional[ActionInfo] = None,
        action_logic: typing.Optional[ActionInfo] = None,
        quota_schedule: typing.Optional[QuotaSchedule] = None,
        end_survey_options: typing.Optional[EndSurveyOptions] = None,
        web_service_options: typing.Optional[WebServiceOptions] = None,
        cross_logic_def: typing.Optional[typing.List[CrossLogicDefEntry]] = None,
        perform_action_on_user: typing.Optional[bool] = None,
        quota_group_id: typing.Optional[QuotaGroupID] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        _body = {}
        if name is not None:
            _body["Name"] = name
        if occurrences is not None:
            _body["Occurrences"] = occurrences
        if count is not None:
            _body["Count"] = count
        if count_for_undo is not None:
            _body["CountForUndo"] = count_for_undo
        if logic is not None:
            _body["Logic"] = logic
        if logic_type is not None:
            _body["LogicType"] = logic_type
        if quota_action is not None:
            _body["QuotaAction"] = quota_action
        if action_element is not None:
            _body["ActionElement"] = action_element
        if action_info is not None:
            _body["ActionInfo"] = action_info
        if action_logic is not None:
            _body["ActionLogic"] = action_logic
        if id is not None:
            _body["ID"] = id
        if quota_realm is not None:
            _body["QuotaRealm"] = quota_realm
        if quota_schedule is not None:
            _body["QuotaSchedule"] = quota_schedule
        if end_survey_options is not None:
            _body["EndSurveyOptions"] = end_survey_options
        if web_service_options is not None:
            _body["WebServiceOptions"] = web_service_options
        if cross_logic_def is not None:
            _body["CrossLogicDef"] = cross_logic_def
        if perform_action_on_user is not None:
            _body["PerformActionOnUser"] = perform_action_on_user
        args.body = _body
        if quota_group_id is not None:
            _query_params["quotaGroupId"] = quota_group_id
        if survey_id is not None:
            _path_params["surveyId"] = survey_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _acreate_new_quota_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
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
        Create Quota
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_survey_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_quota_group_id,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
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
            path_template='/survey-definitions/{surveyId}/quotas',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_quota.serialize(body, content_type)
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
            prefix_separator_iterator=prefix_separator_iterator,
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


    def _create_new_quota_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
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
        Create Quota
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_survey_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_quota_group_id,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
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
            path_template='/survey-definitions/{surveyId}/quotas',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_quota.serialize(body, content_type)
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
            prefix_separator_iterator=prefix_separator_iterator,
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


class CreateNewQuotaRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_new_quota(
        self,
        name: str,
        occurrences: int,
        logic: typing.Union[LogicObject, typing.List[LogicObject]],
        quota_action: QuotaAction,
        id: QuotaID,
        quota_realm: str,
        survey_id: SurveyID,
        count: typing.Optional[int] = None,
        count_for_undo: typing.Optional[int] = None,
        logic_type: typing.Optional[typing.Union[str]] = None,
        action_element: typing.Optional[typing.Union[SurveyID, QuestionID, BlockID, str]] = None,
        action_info: typing.Optional[ActionInfo] = None,
        action_logic: typing.Optional[ActionInfo] = None,
        quota_schedule: typing.Optional[QuotaSchedule] = None,
        end_survey_options: typing.Optional[EndSurveyOptions] = None,
        web_service_options: typing.Optional[WebServiceOptions] = None,
        cross_logic_def: typing.Optional[typing.List[CrossLogicDefEntry]] = None,
        perform_action_on_user: typing.Optional[bool] = None,
        quota_group_id: typing.Optional[QuotaGroupID] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_quota_mapped_args(
            name=name,
            occurrences=occurrences,
            logic=logic,
            quota_action=quota_action,
            id=id,
            quota_realm=quota_realm,
            survey_id=survey_id,
            count=count,
            count_for_undo=count_for_undo,
            logic_type=logic_type,
            action_element=action_element,
            action_info=action_info,
            action_logic=action_logic,
            quota_schedule=quota_schedule,
            end_survey_options=end_survey_options,
            web_service_options=web_service_options,
            cross_logic_def=cross_logic_def,
            perform_action_on_user=perform_action_on_user,
            quota_group_id=quota_group_id,
        )
        return await self._acreate_new_quota_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def create_new_quota(
        self,
        name: str,
        occurrences: int,
        logic: typing.Union[LogicObject, typing.List[LogicObject]],
        quota_action: QuotaAction,
        id: QuotaID,
        quota_realm: str,
        survey_id: SurveyID,
        count: typing.Optional[int] = None,
        count_for_undo: typing.Optional[int] = None,
        logic_type: typing.Optional[typing.Union[str]] = None,
        action_element: typing.Optional[typing.Union[SurveyID, QuestionID, BlockID, str]] = None,
        action_info: typing.Optional[ActionInfo] = None,
        action_logic: typing.Optional[ActionInfo] = None,
        quota_schedule: typing.Optional[QuotaSchedule] = None,
        end_survey_options: typing.Optional[EndSurveyOptions] = None,
        web_service_options: typing.Optional[WebServiceOptions] = None,
        cross_logic_def: typing.Optional[typing.List[CrossLogicDefEntry]] = None,
        perform_action_on_user: typing.Optional[bool] = None,
        quota_group_id: typing.Optional[QuotaGroupID] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_quota_mapped_args(
            name=name,
            occurrences=occurrences,
            logic=logic,
            quota_action=quota_action,
            id=id,
            quota_realm=quota_realm,
            survey_id=survey_id,
            count=count,
            count_for_undo=count_for_undo,
            logic_type=logic_type,
            action_element=action_element,
            action_info=action_info,
            action_logic=action_logic,
            quota_schedule=quota_schedule,
            end_survey_options=end_survey_options,
            web_service_options=web_service_options,
            cross_logic_def=cross_logic_def,
            perform_action_on_user=perform_action_on_user,
            quota_group_id=quota_group_id,
        )
        return self._create_new_quota_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

class CreateNewQuota(BaseApi):

    async def acreate_new_quota(
        self,
        name: str,
        occurrences: int,
        logic: typing.Union[LogicObject, typing.List[LogicObject]],
        quota_action: QuotaAction,
        id: QuotaID,
        quota_realm: str,
        survey_id: SurveyID,
        count: typing.Optional[int] = None,
        count_for_undo: typing.Optional[int] = None,
        logic_type: typing.Optional[typing.Union[str]] = None,
        action_element: typing.Optional[typing.Union[SurveyID, QuestionID, BlockID, str]] = None,
        action_info: typing.Optional[ActionInfo] = None,
        action_logic: typing.Optional[ActionInfo] = None,
        quota_schedule: typing.Optional[QuotaSchedule] = None,
        end_survey_options: typing.Optional[EndSurveyOptions] = None,
        web_service_options: typing.Optional[WebServiceOptions] = None,
        cross_logic_def: typing.Optional[typing.List[CrossLogicDefEntry]] = None,
        perform_action_on_user: typing.Optional[bool] = None,
        quota_group_id: typing.Optional[QuotaGroupID] = None,
        validate: bool = False,
        **kwargs,
    ) -> CreateQuotaResponsePydantic:
        raw_response = await self.raw.acreate_new_quota(
            name=name,
            occurrences=occurrences,
            logic=logic,
            quota_action=quota_action,
            id=id,
            quota_realm=quota_realm,
            survey_id=survey_id,
            count=count,
            count_for_undo=count_for_undo,
            logic_type=logic_type,
            action_element=action_element,
            action_info=action_info,
            action_logic=action_logic,
            quota_schedule=quota_schedule,
            end_survey_options=end_survey_options,
            web_service_options=web_service_options,
            cross_logic_def=cross_logic_def,
            perform_action_on_user=perform_action_on_user,
            quota_group_id=quota_group_id,
            **kwargs,
        )
        if validate:
            return CreateQuotaResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CreateQuotaResponsePydantic, raw_response.body)
    
    
    def create_new_quota(
        self,
        name: str,
        occurrences: int,
        logic: typing.Union[LogicObject, typing.List[LogicObject]],
        quota_action: QuotaAction,
        id: QuotaID,
        quota_realm: str,
        survey_id: SurveyID,
        count: typing.Optional[int] = None,
        count_for_undo: typing.Optional[int] = None,
        logic_type: typing.Optional[typing.Union[str]] = None,
        action_element: typing.Optional[typing.Union[SurveyID, QuestionID, BlockID, str]] = None,
        action_info: typing.Optional[ActionInfo] = None,
        action_logic: typing.Optional[ActionInfo] = None,
        quota_schedule: typing.Optional[QuotaSchedule] = None,
        end_survey_options: typing.Optional[EndSurveyOptions] = None,
        web_service_options: typing.Optional[WebServiceOptions] = None,
        cross_logic_def: typing.Optional[typing.List[CrossLogicDefEntry]] = None,
        perform_action_on_user: typing.Optional[bool] = None,
        quota_group_id: typing.Optional[QuotaGroupID] = None,
        validate: bool = False,
    ) -> CreateQuotaResponsePydantic:
        raw_response = self.raw.create_new_quota(
            name=name,
            occurrences=occurrences,
            logic=logic,
            quota_action=quota_action,
            id=id,
            quota_realm=quota_realm,
            survey_id=survey_id,
            count=count,
            count_for_undo=count_for_undo,
            logic_type=logic_type,
            action_element=action_element,
            action_info=action_info,
            action_logic=action_logic,
            quota_schedule=quota_schedule,
            end_survey_options=end_survey_options,
            web_service_options=web_service_options,
            cross_logic_def=cross_logic_def,
            perform_action_on_user=perform_action_on_user,
            quota_group_id=quota_group_id,
        )
        if validate:
            return CreateQuotaResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CreateQuotaResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        name: str,
        occurrences: int,
        logic: typing.Union[LogicObject, typing.List[LogicObject]],
        quota_action: QuotaAction,
        id: QuotaID,
        quota_realm: str,
        survey_id: SurveyID,
        count: typing.Optional[int] = None,
        count_for_undo: typing.Optional[int] = None,
        logic_type: typing.Optional[typing.Union[str]] = None,
        action_element: typing.Optional[typing.Union[SurveyID, QuestionID, BlockID, str]] = None,
        action_info: typing.Optional[ActionInfo] = None,
        action_logic: typing.Optional[ActionInfo] = None,
        quota_schedule: typing.Optional[QuotaSchedule] = None,
        end_survey_options: typing.Optional[EndSurveyOptions] = None,
        web_service_options: typing.Optional[WebServiceOptions] = None,
        cross_logic_def: typing.Optional[typing.List[CrossLogicDefEntry]] = None,
        perform_action_on_user: typing.Optional[bool] = None,
        quota_group_id: typing.Optional[QuotaGroupID] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_quota_mapped_args(
            name=name,
            occurrences=occurrences,
            logic=logic,
            quota_action=quota_action,
            id=id,
            quota_realm=quota_realm,
            survey_id=survey_id,
            count=count,
            count_for_undo=count_for_undo,
            logic_type=logic_type,
            action_element=action_element,
            action_info=action_info,
            action_logic=action_logic,
            quota_schedule=quota_schedule,
            end_survey_options=end_survey_options,
            web_service_options=web_service_options,
            cross_logic_def=cross_logic_def,
            perform_action_on_user=perform_action_on_user,
            quota_group_id=quota_group_id,
        )
        return await self._acreate_new_quota_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        name: str,
        occurrences: int,
        logic: typing.Union[LogicObject, typing.List[LogicObject]],
        quota_action: QuotaAction,
        id: QuotaID,
        quota_realm: str,
        survey_id: SurveyID,
        count: typing.Optional[int] = None,
        count_for_undo: typing.Optional[int] = None,
        logic_type: typing.Optional[typing.Union[str]] = None,
        action_element: typing.Optional[typing.Union[SurveyID, QuestionID, BlockID, str]] = None,
        action_info: typing.Optional[ActionInfo] = None,
        action_logic: typing.Optional[ActionInfo] = None,
        quota_schedule: typing.Optional[QuotaSchedule] = None,
        end_survey_options: typing.Optional[EndSurveyOptions] = None,
        web_service_options: typing.Optional[WebServiceOptions] = None,
        cross_logic_def: typing.Optional[typing.List[CrossLogicDefEntry]] = None,
        perform_action_on_user: typing.Optional[bool] = None,
        quota_group_id: typing.Optional[QuotaGroupID] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_quota_mapped_args(
            name=name,
            occurrences=occurrences,
            logic=logic,
            quota_action=quota_action,
            id=id,
            quota_realm=quota_realm,
            survey_id=survey_id,
            count=count,
            count_for_undo=count_for_undo,
            logic_type=logic_type,
            action_element=action_element,
            action_info=action_info,
            action_logic=action_logic,
            quota_schedule=quota_schedule,
            end_survey_options=end_survey_options,
            web_service_options=web_service_options,
            cross_logic_def=cross_logic_def,
            perform_action_on_user=perform_action_on_user,
            quota_group_id=quota_group_id,
        )
        return self._create_new_quota_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

