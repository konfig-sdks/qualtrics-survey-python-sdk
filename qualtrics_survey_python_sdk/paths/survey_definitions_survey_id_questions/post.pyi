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

from qualtrics_survey_python_sdk.model.validation import Validation as ValidationSchema
from qualtrics_survey_python_sdk.model.block_id import BlockID as BlockIDSchema
from qualtrics_survey_python_sdk.model.invalid_request_error_response import InvalidRequestErrorResponse as InvalidRequestErrorResponseSchema
from qualtrics_survey_python_sdk.model.language import Language as LanguageSchema
from qualtrics_survey_python_sdk.model.internal_server_error_response import InternalServerErrorResponse as InternalServerErrorResponseSchema
from qualtrics_survey_python_sdk.model.image_id import ImageID as ImageIDSchema
from qualtrics_survey_python_sdk.model.randomization import Randomization as RandomizationSchema
from qualtrics_survey_python_sdk.model.question_sub_selector import QuestionSubSelector as QuestionSubSelectorSchema
from qualtrics_survey_python_sdk.model.unauthorized_request_error_response import UnauthorizedRequestErrorResponse as UnauthorizedRequestErrorResponseSchema
from qualtrics_survey_python_sdk.model.forbidden_request_error_response import ForbiddenRequestErrorResponse as ForbiddenRequestErrorResponseSchema
from qualtrics_survey_python_sdk.model.question_id import QuestionID as QuestionIDSchema
from qualtrics_survey_python_sdk.model.question_text import QuestionText as QuestionTextSchema
from qualtrics_survey_python_sdk.model.choice_order import ChoiceOrder as ChoiceOrderSchema
from qualtrics_survey_python_sdk.model.survey_id import SurveyID as SurveyIDSchema
from qualtrics_survey_python_sdk.model.answer_randomization import AnswerRandomization as AnswerRandomizationSchema
from qualtrics_survey_python_sdk.model.question_choices import QuestionChoices as QuestionChoicesSchema
from qualtrics_survey_python_sdk.model.not_found_error_response import NotFoundErrorResponse as NotFoundErrorResponseSchema
from qualtrics_survey_python_sdk.model.recode_values import RecodeValues as RecodeValuesSchema
from qualtrics_survey_python_sdk.model.create_question_response import CreateQuestionResponse as CreateQuestionResponseSchema
from qualtrics_survey_python_sdk.model.question_definition import QuestionDefinition as QuestionDefinitionSchema
from qualtrics_survey_python_sdk.model.question_configuration import QuestionConfiguration as QuestionConfigurationSchema
from qualtrics_survey_python_sdk.model.selection import Selection as SelectionSchema

from qualtrics_survey_python_sdk.type.recode_values import RecodeValues
from qualtrics_survey_python_sdk.type.answer_randomization import AnswerRandomization
from qualtrics_survey_python_sdk.type.validation import Validation
from qualtrics_survey_python_sdk.type.randomization import Randomization
from qualtrics_survey_python_sdk.type.selection import Selection
from qualtrics_survey_python_sdk.type.question_configuration import QuestionConfiguration
from qualtrics_survey_python_sdk.type.internal_server_error_response import InternalServerErrorResponse
from qualtrics_survey_python_sdk.type.invalid_request_error_response import InvalidRequestErrorResponse
from qualtrics_survey_python_sdk.type.unauthorized_request_error_response import UnauthorizedRequestErrorResponse
from qualtrics_survey_python_sdk.type.block_id import BlockID
from qualtrics_survey_python_sdk.type.question_text import QuestionText
from qualtrics_survey_python_sdk.type.language import Language
from qualtrics_survey_python_sdk.type.question_choices import QuestionChoices
from qualtrics_survey_python_sdk.type.survey_id import SurveyID
from qualtrics_survey_python_sdk.type.create_question_response import CreateQuestionResponse
from qualtrics_survey_python_sdk.type.forbidden_request_error_response import ForbiddenRequestErrorResponse
from qualtrics_survey_python_sdk.type.image_id import ImageID
from qualtrics_survey_python_sdk.type.question_definition import QuestionDefinition
from qualtrics_survey_python_sdk.type.question_id import QuestionID
from qualtrics_survey_python_sdk.type.question_sub_selector import QuestionSubSelector
from qualtrics_survey_python_sdk.type.choice_order import ChoiceOrder
from qualtrics_survey_python_sdk.type.not_found_error_response import NotFoundErrorResponse

from ...api_client import Dictionary
from qualtrics_survey_python_sdk.pydantic.question_choices import QuestionChoices as QuestionChoicesPydantic
from qualtrics_survey_python_sdk.pydantic.recode_values import RecodeValues as RecodeValuesPydantic
from qualtrics_survey_python_sdk.pydantic.block_id import BlockID as BlockIDPydantic
from qualtrics_survey_python_sdk.pydantic.survey_id import SurveyID as SurveyIDPydantic
from qualtrics_survey_python_sdk.pydantic.language import Language as LanguagePydantic
from qualtrics_survey_python_sdk.pydantic.selection import Selection as SelectionPydantic
from qualtrics_survey_python_sdk.pydantic.invalid_request_error_response import InvalidRequestErrorResponse as InvalidRequestErrorResponsePydantic
from qualtrics_survey_python_sdk.pydantic.create_question_response import CreateQuestionResponse as CreateQuestionResponsePydantic
from qualtrics_survey_python_sdk.pydantic.forbidden_request_error_response import ForbiddenRequestErrorResponse as ForbiddenRequestErrorResponsePydantic
from qualtrics_survey_python_sdk.pydantic.answer_randomization import AnswerRandomization as AnswerRandomizationPydantic
from qualtrics_survey_python_sdk.pydantic.question_id import QuestionID as QuestionIDPydantic
from qualtrics_survey_python_sdk.pydantic.unauthorized_request_error_response import UnauthorizedRequestErrorResponse as UnauthorizedRequestErrorResponsePydantic
from qualtrics_survey_python_sdk.pydantic.image_id import ImageID as ImageIDPydantic
from qualtrics_survey_python_sdk.pydantic.choice_order import ChoiceOrder as ChoiceOrderPydantic
from qualtrics_survey_python_sdk.pydantic.randomization import Randomization as RandomizationPydantic
from qualtrics_survey_python_sdk.pydantic.not_found_error_response import NotFoundErrorResponse as NotFoundErrorResponsePydantic
from qualtrics_survey_python_sdk.pydantic.question_configuration import QuestionConfiguration as QuestionConfigurationPydantic
from qualtrics_survey_python_sdk.pydantic.question_sub_selector import QuestionSubSelector as QuestionSubSelectorPydantic
from qualtrics_survey_python_sdk.pydantic.question_text import QuestionText as QuestionTextPydantic
from qualtrics_survey_python_sdk.pydantic.validation import Validation as ValidationPydantic
from qualtrics_survey_python_sdk.pydantic.internal_server_error_response import InternalServerErrorResponse as InternalServerErrorResponsePydantic
from qualtrics_survey_python_sdk.pydantic.question_definition import QuestionDefinition as QuestionDefinitionPydantic

# Query params
BlockIdSchema = schemas.Schema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'blockId': typing.Union[BlockIdSchema, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_block_id = api_client.QueryParameter(
    name="blockId",
    style=api_client.ParameterStyle.FORM,
    schema=BlockIDSchema,
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
SchemaForRequestBodyApplicationJson = QuestionDefinitionSchema


request_body_question_definition = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = CreateQuestionResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: CreateQuestionResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: CreateQuestionResponse


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

    def _create_new_question_mapped_args(
        self,
        survey_id: SurveyID,
        choice_order: typing.Optional[ChoiceOrder] = None,
        choices: typing.Optional[QuestionChoices] = None,
        configuration: typing.Optional[QuestionConfiguration] = None,
        data_export_tag: typing.Optional[str] = None,
        language: typing.Optional[Language] = None,
        next_answer_id: typing.Optional[int] = None,
        next_choice_id: typing.Optional[int] = None,
        question_description: typing.Optional[str] = None,
        question_id: typing.Optional[QuestionID] = None,
        question_text: typing.Optional[QuestionText] = None,
        question_type: typing.Optional[str] = None,
        randomization: typing.Optional[Randomization] = None,
        recode_values: typing.Optional[RecodeValues] = None,
        selector: typing.Optional[str] = None,
        sub_selector: typing.Optional[QuestionSubSelector] = None,
        validation: typing.Optional[Validation] = None,
        answer_order: typing.Optional[ChoiceOrder] = None,
        answers: typing.Optional[QuestionChoices] = None,
        answer_randomization: typing.Optional[AnswerRandomization] = None,
        choice_data_export_tags: typing.Optional[bool] = None,
        default_choices: typing.Optional[bool] = None,
        labels: typing.Optional[Selection] = None,
        graphics: typing.Optional[ImageID] = None,
        graphics_description: typing.Optional[str] = None,
        block_id: typing.Optional[BlockID] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        _body = {}
        if choice_order is not None:
            _body["ChoiceOrder"] = choice_order
        if choices is not None:
            _body["Choices"] = choices
        if configuration is not None:
            _body["Configuration"] = configuration
        if data_export_tag is not None:
            _body["DataExportTag"] = data_export_tag
        if language is not None:
            _body["Language"] = language
        if next_answer_id is not None:
            _body["NextAnswerId"] = next_answer_id
        if next_choice_id is not None:
            _body["NextChoiceId"] = next_choice_id
        if question_description is not None:
            _body["QuestionDescription"] = question_description
        if question_id is not None:
            _body["QuestionID"] = question_id
        if question_text is not None:
            _body["QuestionText"] = question_text
        if question_type is not None:
            _body["QuestionType"] = question_type
        if randomization is not None:
            _body["Randomization"] = randomization
        if recode_values is not None:
            _body["RecodeValues"] = recode_values
        if selector is not None:
            _body["Selector"] = selector
        if sub_selector is not None:
            _body["SubSelector"] = sub_selector
        if validation is not None:
            _body["Validation"] = validation
        if answer_order is not None:
            _body["AnswerOrder"] = answer_order
        if answers is not None:
            _body["Answers"] = answers
        if answer_randomization is not None:
            _body["AnswerRandomization"] = answer_randomization
        if choice_data_export_tags is not None:
            _body["ChoiceDataExportTags"] = choice_data_export_tags
        if default_choices is not None:
            _body["DefaultChoices"] = default_choices
        if labels is not None:
            _body["Labels"] = labels
        if graphics is not None:
            _body["Graphics"] = graphics
        if graphics_description is not None:
            _body["GraphicsDescription"] = graphics_description
        args.body = _body
        if block_id is not None:
            _query_params["blockId"] = block_id
        if survey_id is not None:
            _path_params["surveyId"] = survey_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _acreate_new_question_oapg(
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
        Create Question
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
            request_query_block_id,
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
            path_template='/survey-definitions/{surveyId}/questions',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_question_definition.serialize(body, content_type)
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


    def _create_new_question_oapg(
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
        Create Question
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
            request_query_block_id,
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
            path_template='/survey-definitions/{surveyId}/questions',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_question_definition.serialize(body, content_type)
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


class CreateNewQuestionRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_new_question(
        self,
        survey_id: SurveyID,
        choice_order: typing.Optional[ChoiceOrder] = None,
        choices: typing.Optional[QuestionChoices] = None,
        configuration: typing.Optional[QuestionConfiguration] = None,
        data_export_tag: typing.Optional[str] = None,
        language: typing.Optional[Language] = None,
        next_answer_id: typing.Optional[int] = None,
        next_choice_id: typing.Optional[int] = None,
        question_description: typing.Optional[str] = None,
        question_id: typing.Optional[QuestionID] = None,
        question_text: typing.Optional[QuestionText] = None,
        question_type: typing.Optional[str] = None,
        randomization: typing.Optional[Randomization] = None,
        recode_values: typing.Optional[RecodeValues] = None,
        selector: typing.Optional[str] = None,
        sub_selector: typing.Optional[QuestionSubSelector] = None,
        validation: typing.Optional[Validation] = None,
        answer_order: typing.Optional[ChoiceOrder] = None,
        answers: typing.Optional[QuestionChoices] = None,
        answer_randomization: typing.Optional[AnswerRandomization] = None,
        choice_data_export_tags: typing.Optional[bool] = None,
        default_choices: typing.Optional[bool] = None,
        labels: typing.Optional[Selection] = None,
        graphics: typing.Optional[ImageID] = None,
        graphics_description: typing.Optional[str] = None,
        block_id: typing.Optional[BlockID] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_question_mapped_args(
            survey_id=survey_id,
            choice_order=choice_order,
            choices=choices,
            configuration=configuration,
            data_export_tag=data_export_tag,
            language=language,
            next_answer_id=next_answer_id,
            next_choice_id=next_choice_id,
            question_description=question_description,
            question_id=question_id,
            question_text=question_text,
            question_type=question_type,
            randomization=randomization,
            recode_values=recode_values,
            selector=selector,
            sub_selector=sub_selector,
            validation=validation,
            answer_order=answer_order,
            answers=answers,
            answer_randomization=answer_randomization,
            choice_data_export_tags=choice_data_export_tags,
            default_choices=default_choices,
            labels=labels,
            graphics=graphics,
            graphics_description=graphics_description,
            block_id=block_id,
        )
        return await self._acreate_new_question_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def create_new_question(
        self,
        survey_id: SurveyID,
        choice_order: typing.Optional[ChoiceOrder] = None,
        choices: typing.Optional[QuestionChoices] = None,
        configuration: typing.Optional[QuestionConfiguration] = None,
        data_export_tag: typing.Optional[str] = None,
        language: typing.Optional[Language] = None,
        next_answer_id: typing.Optional[int] = None,
        next_choice_id: typing.Optional[int] = None,
        question_description: typing.Optional[str] = None,
        question_id: typing.Optional[QuestionID] = None,
        question_text: typing.Optional[QuestionText] = None,
        question_type: typing.Optional[str] = None,
        randomization: typing.Optional[Randomization] = None,
        recode_values: typing.Optional[RecodeValues] = None,
        selector: typing.Optional[str] = None,
        sub_selector: typing.Optional[QuestionSubSelector] = None,
        validation: typing.Optional[Validation] = None,
        answer_order: typing.Optional[ChoiceOrder] = None,
        answers: typing.Optional[QuestionChoices] = None,
        answer_randomization: typing.Optional[AnswerRandomization] = None,
        choice_data_export_tags: typing.Optional[bool] = None,
        default_choices: typing.Optional[bool] = None,
        labels: typing.Optional[Selection] = None,
        graphics: typing.Optional[ImageID] = None,
        graphics_description: typing.Optional[str] = None,
        block_id: typing.Optional[BlockID] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_question_mapped_args(
            survey_id=survey_id,
            choice_order=choice_order,
            choices=choices,
            configuration=configuration,
            data_export_tag=data_export_tag,
            language=language,
            next_answer_id=next_answer_id,
            next_choice_id=next_choice_id,
            question_description=question_description,
            question_id=question_id,
            question_text=question_text,
            question_type=question_type,
            randomization=randomization,
            recode_values=recode_values,
            selector=selector,
            sub_selector=sub_selector,
            validation=validation,
            answer_order=answer_order,
            answers=answers,
            answer_randomization=answer_randomization,
            choice_data_export_tags=choice_data_export_tags,
            default_choices=default_choices,
            labels=labels,
            graphics=graphics,
            graphics_description=graphics_description,
            block_id=block_id,
        )
        return self._create_new_question_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

class CreateNewQuestion(BaseApi):

    async def acreate_new_question(
        self,
        survey_id: SurveyID,
        choice_order: typing.Optional[ChoiceOrder] = None,
        choices: typing.Optional[QuestionChoices] = None,
        configuration: typing.Optional[QuestionConfiguration] = None,
        data_export_tag: typing.Optional[str] = None,
        language: typing.Optional[Language] = None,
        next_answer_id: typing.Optional[int] = None,
        next_choice_id: typing.Optional[int] = None,
        question_description: typing.Optional[str] = None,
        question_id: typing.Optional[QuestionID] = None,
        question_text: typing.Optional[QuestionText] = None,
        question_type: typing.Optional[str] = None,
        randomization: typing.Optional[Randomization] = None,
        recode_values: typing.Optional[RecodeValues] = None,
        selector: typing.Optional[str] = None,
        sub_selector: typing.Optional[QuestionSubSelector] = None,
        validation: typing.Optional[Validation] = None,
        answer_order: typing.Optional[ChoiceOrder] = None,
        answers: typing.Optional[QuestionChoices] = None,
        answer_randomization: typing.Optional[AnswerRandomization] = None,
        choice_data_export_tags: typing.Optional[bool] = None,
        default_choices: typing.Optional[bool] = None,
        labels: typing.Optional[Selection] = None,
        graphics: typing.Optional[ImageID] = None,
        graphics_description: typing.Optional[str] = None,
        block_id: typing.Optional[BlockID] = None,
        validate: bool = False,
        **kwargs,
    ) -> CreateQuestionResponsePydantic:
        raw_response = await self.raw.acreate_new_question(
            survey_id=survey_id,
            choice_order=choice_order,
            choices=choices,
            configuration=configuration,
            data_export_tag=data_export_tag,
            language=language,
            next_answer_id=next_answer_id,
            next_choice_id=next_choice_id,
            question_description=question_description,
            question_id=question_id,
            question_text=question_text,
            question_type=question_type,
            randomization=randomization,
            recode_values=recode_values,
            selector=selector,
            sub_selector=sub_selector,
            validation=validation,
            answer_order=answer_order,
            answers=answers,
            answer_randomization=answer_randomization,
            choice_data_export_tags=choice_data_export_tags,
            default_choices=default_choices,
            labels=labels,
            graphics=graphics,
            graphics_description=graphics_description,
            block_id=block_id,
            **kwargs,
        )
        if validate:
            return CreateQuestionResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CreateQuestionResponsePydantic, raw_response.body)
    
    
    def create_new_question(
        self,
        survey_id: SurveyID,
        choice_order: typing.Optional[ChoiceOrder] = None,
        choices: typing.Optional[QuestionChoices] = None,
        configuration: typing.Optional[QuestionConfiguration] = None,
        data_export_tag: typing.Optional[str] = None,
        language: typing.Optional[Language] = None,
        next_answer_id: typing.Optional[int] = None,
        next_choice_id: typing.Optional[int] = None,
        question_description: typing.Optional[str] = None,
        question_id: typing.Optional[QuestionID] = None,
        question_text: typing.Optional[QuestionText] = None,
        question_type: typing.Optional[str] = None,
        randomization: typing.Optional[Randomization] = None,
        recode_values: typing.Optional[RecodeValues] = None,
        selector: typing.Optional[str] = None,
        sub_selector: typing.Optional[QuestionSubSelector] = None,
        validation: typing.Optional[Validation] = None,
        answer_order: typing.Optional[ChoiceOrder] = None,
        answers: typing.Optional[QuestionChoices] = None,
        answer_randomization: typing.Optional[AnswerRandomization] = None,
        choice_data_export_tags: typing.Optional[bool] = None,
        default_choices: typing.Optional[bool] = None,
        labels: typing.Optional[Selection] = None,
        graphics: typing.Optional[ImageID] = None,
        graphics_description: typing.Optional[str] = None,
        block_id: typing.Optional[BlockID] = None,
        validate: bool = False,
    ) -> CreateQuestionResponsePydantic:
        raw_response = self.raw.create_new_question(
            survey_id=survey_id,
            choice_order=choice_order,
            choices=choices,
            configuration=configuration,
            data_export_tag=data_export_tag,
            language=language,
            next_answer_id=next_answer_id,
            next_choice_id=next_choice_id,
            question_description=question_description,
            question_id=question_id,
            question_text=question_text,
            question_type=question_type,
            randomization=randomization,
            recode_values=recode_values,
            selector=selector,
            sub_selector=sub_selector,
            validation=validation,
            answer_order=answer_order,
            answers=answers,
            answer_randomization=answer_randomization,
            choice_data_export_tags=choice_data_export_tags,
            default_choices=default_choices,
            labels=labels,
            graphics=graphics,
            graphics_description=graphics_description,
            block_id=block_id,
        )
        if validate:
            return CreateQuestionResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CreateQuestionResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        survey_id: SurveyID,
        choice_order: typing.Optional[ChoiceOrder] = None,
        choices: typing.Optional[QuestionChoices] = None,
        configuration: typing.Optional[QuestionConfiguration] = None,
        data_export_tag: typing.Optional[str] = None,
        language: typing.Optional[Language] = None,
        next_answer_id: typing.Optional[int] = None,
        next_choice_id: typing.Optional[int] = None,
        question_description: typing.Optional[str] = None,
        question_id: typing.Optional[QuestionID] = None,
        question_text: typing.Optional[QuestionText] = None,
        question_type: typing.Optional[str] = None,
        randomization: typing.Optional[Randomization] = None,
        recode_values: typing.Optional[RecodeValues] = None,
        selector: typing.Optional[str] = None,
        sub_selector: typing.Optional[QuestionSubSelector] = None,
        validation: typing.Optional[Validation] = None,
        answer_order: typing.Optional[ChoiceOrder] = None,
        answers: typing.Optional[QuestionChoices] = None,
        answer_randomization: typing.Optional[AnswerRandomization] = None,
        choice_data_export_tags: typing.Optional[bool] = None,
        default_choices: typing.Optional[bool] = None,
        labels: typing.Optional[Selection] = None,
        graphics: typing.Optional[ImageID] = None,
        graphics_description: typing.Optional[str] = None,
        block_id: typing.Optional[BlockID] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_question_mapped_args(
            survey_id=survey_id,
            choice_order=choice_order,
            choices=choices,
            configuration=configuration,
            data_export_tag=data_export_tag,
            language=language,
            next_answer_id=next_answer_id,
            next_choice_id=next_choice_id,
            question_description=question_description,
            question_id=question_id,
            question_text=question_text,
            question_type=question_type,
            randomization=randomization,
            recode_values=recode_values,
            selector=selector,
            sub_selector=sub_selector,
            validation=validation,
            answer_order=answer_order,
            answers=answers,
            answer_randomization=answer_randomization,
            choice_data_export_tags=choice_data_export_tags,
            default_choices=default_choices,
            labels=labels,
            graphics=graphics,
            graphics_description=graphics_description,
            block_id=block_id,
        )
        return await self._acreate_new_question_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        survey_id: SurveyID,
        choice_order: typing.Optional[ChoiceOrder] = None,
        choices: typing.Optional[QuestionChoices] = None,
        configuration: typing.Optional[QuestionConfiguration] = None,
        data_export_tag: typing.Optional[str] = None,
        language: typing.Optional[Language] = None,
        next_answer_id: typing.Optional[int] = None,
        next_choice_id: typing.Optional[int] = None,
        question_description: typing.Optional[str] = None,
        question_id: typing.Optional[QuestionID] = None,
        question_text: typing.Optional[QuestionText] = None,
        question_type: typing.Optional[str] = None,
        randomization: typing.Optional[Randomization] = None,
        recode_values: typing.Optional[RecodeValues] = None,
        selector: typing.Optional[str] = None,
        sub_selector: typing.Optional[QuestionSubSelector] = None,
        validation: typing.Optional[Validation] = None,
        answer_order: typing.Optional[ChoiceOrder] = None,
        answers: typing.Optional[QuestionChoices] = None,
        answer_randomization: typing.Optional[AnswerRandomization] = None,
        choice_data_export_tags: typing.Optional[bool] = None,
        default_choices: typing.Optional[bool] = None,
        labels: typing.Optional[Selection] = None,
        graphics: typing.Optional[ImageID] = None,
        graphics_description: typing.Optional[str] = None,
        block_id: typing.Optional[BlockID] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_question_mapped_args(
            survey_id=survey_id,
            choice_order=choice_order,
            choices=choices,
            configuration=configuration,
            data_export_tag=data_export_tag,
            language=language,
            next_answer_id=next_answer_id,
            next_choice_id=next_choice_id,
            question_description=question_description,
            question_id=question_id,
            question_text=question_text,
            question_type=question_type,
            randomization=randomization,
            recode_values=recode_values,
            selector=selector,
            sub_selector=sub_selector,
            validation=validation,
            answer_order=answer_order,
            answers=answers,
            answer_randomization=answer_randomization,
            choice_data_export_tags=choice_data_export_tags,
            default_choices=default_choices,
            labels=labels,
            graphics=graphics,
            graphics_description=graphics_description,
            block_id=block_id,
        )
        return self._create_new_question_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

