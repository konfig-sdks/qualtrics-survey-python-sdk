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


class Language(
    schemas.ComposedSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Question translations
    """


    class MetaOapg:
        
        
        class one_of_0(
            schemas.ListSchema
        ):
        
        
            class MetaOapg:
                max_items = 0
                items = schemas.StrSchema
        
            def __new__(
                cls,
                arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                _configuration: typing.Optional[schemas.Configuration] = None,
            ) -> 'one_of_0':
                return super().__new__(
                    cls,
                    arg,
                    _configuration=_configuration,
                )
        
            def __getitem__(self, i: int) -> MetaOapg.items:
                return super().__getitem__(i)
        
        
        class one_of_1(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                
                class additional_properties(
                    schemas.DictSchema
                ):
                
                
                    class MetaOapg:
                        
                        class properties:
                            QuestionText = schemas.StrSchema
                        
                            @staticmethod
                            def Choices() -> typing.Type['QuestionChoices']:
                                return QuestionChoices
                            __annotations__ = {
                                "QuestionText": QuestionText,
                                "Choices": Choices,
                            }
                        additional_properties = schemas.AnyTypeSchema
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["QuestionText"]) -> MetaOapg.properties.QuestionText: ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["Choices"]) -> 'QuestionChoices': ...
                    
                    @typing.overload
                    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
                    
                    def __getitem__(self, name: typing.Union[typing_extensions.Literal["QuestionText"], typing_extensions.Literal["Choices"], str, ]):
                        # dict_instance[name] accessor
                        return super().__getitem__(name)
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["QuestionText"]) -> typing.Union[MetaOapg.properties.QuestionText, schemas.Unset]: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["Choices"]) -> typing.Union['QuestionChoices', schemas.Unset]: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
                    
                    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["QuestionText"], typing_extensions.Literal["Choices"], str, ]):
                        return super().get_item_oapg(name)
                
                    def __new__(
                        cls,
                        *args: typing.Union[dict, frozendict.frozendict, ],
                        QuestionText: typing.Union[MetaOapg.properties.QuestionText, str, schemas.Unset] = schemas.unset,
                        Choices: typing.Union['QuestionChoices', schemas.Unset] = schemas.unset,
                        _configuration: typing.Optional[schemas.Configuration] = None,
                        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    ) -> 'additional_properties':
                        return super().__new__(
                            cls,
                            *args,
                            QuestionText=QuestionText,
                            Choices=Choices,
                            _configuration=_configuration,
                            **kwargs,
                        )
            
            def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                return super().get_item_oapg(name)
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, ],
            ) -> 'one_of_1':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def one_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                cls.one_of_0,
                cls.one_of_1,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Language':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from qualtrics_survey_python_sdk.model.question_choices import QuestionChoices
