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


class QuestionExpression(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Logic expression for a question type.
    """


    class MetaOapg:
        required = {
            "Operator",
            "Type",
            "QuestionIsInLoop",
            "ChoiceLocator",
            "LogicType",
            "QuestionID",
        }
        
        class properties:
        
            @staticmethod
            def ChoiceLocator() -> typing.Type['Locator']:
                return Locator
            
            
            class LogicType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def QUESTION(cls):
                    return cls("Question")
            
            
            class Operator(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def SELECTED(cls):
                    return cls("Selected")
                
                @schemas.classproperty
                def NOT_SELECTED(cls):
                    return cls("NotSelected")
                
                @schemas.classproperty
                def EQUAL_TO(cls):
                    return cls("EqualTo")
                
                @schemas.classproperty
                def NOT_EQUAL_TO(cls):
                    return cls("NotEqualTo")
                
                @schemas.classproperty
                def EMPTY(cls):
                    return cls("Empty")
                
                @schemas.classproperty
                def NOT_EMPTY(cls):
                    return cls("NotEmpty")
                
                @schemas.classproperty
                def DISPLAYED(cls):
                    return cls("Displayed")
                
                @schemas.classproperty
                def NOT_DISPLAYED(cls):
                    return cls("NotDisplayed")
                
                @schemas.classproperty
                def GREATER_THAN(cls):
                    return cls("GreaterThan")
                
                @schemas.classproperty
                def GREATER_THAN_OR_EQUAL(cls):
                    return cls("GreaterThanOrEqual")
                
                @schemas.classproperty
                def LESS_THAN(cls):
                    return cls("LessThan")
                
                @schemas.classproperty
                def LESS_THAN_OR_EQUAL(cls):
                    return cls("LessThanOrEqual")
                
                @schemas.classproperty
                def CONTAINS(cls):
                    return cls("Contains")
                
                @schemas.classproperty
                def DOES_NOT_CONTAIN(cls):
                    return cls("DoesNotContain")
                
                @schemas.classproperty
                def MATCHES_REGEX(cls):
                    return cls("MatchesRegex")
                
                @schemas.classproperty
                def IS_NOT(cls):
                    return cls("IsNot")
                
                @schemas.classproperty
                def UPLOADED(cls):
                    return cls("Uploaded")
                
                @schemas.classproperty
                def NOT_UPLOADED(cls):
                    return cls("NotUploaded")
                
                @schemas.classproperty
                def PDF(cls):
                    return cls("PDF")
                
                @schemas.classproperty
                def DOCUMENT(cls):
                    return cls("Document")
                
                @schemas.classproperty
                def CLICKED_IN(cls):
                    return cls("ClickedIn")
                
                @schemas.classproperty
                def NOT_CLICKED_IN(cls):
                    return cls("NotClickedIn")
                
                @schemas.classproperty
                def EXTENSIONS(cls):
                    return cls("Extensions")
                
                @schemas.classproperty
                def GRAPHIC(cls):
                    return cls("Graphic")
                
                @schemas.classproperty
                def SPREADSHEET(cls):
                    return cls("Spreadsheet")
        
            @staticmethod
            def QuestionID() -> typing.Type['QuestionID']:
                return QuestionID
            
            
            class QuestionIsInLoop(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def TRUE(cls):
                    return cls("true")
                
                @schemas.classproperty
                def FALSE(cls):
                    return cls("false")
            
            
            class Type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def EXPRESSION(cls):
                    return cls("Expression")
            __annotations__ = {
                "ChoiceLocator": ChoiceLocator,
                "LogicType": LogicType,
                "Operator": Operator,
                "QuestionID": QuestionID,
                "QuestionIsInLoop": QuestionIsInLoop,
                "Type": Type,
            }
        additional_properties = schemas.AnyTypeSchema
    
    Operator: MetaOapg.properties.Operator
    Type: MetaOapg.properties.Type
    QuestionIsInLoop: MetaOapg.properties.QuestionIsInLoop
    ChoiceLocator: 'Locator'
    LogicType: MetaOapg.properties.LogicType
    QuestionID: 'QuestionID'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Operator"]) -> MetaOapg.properties.Operator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Type"]) -> MetaOapg.properties.Type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["QuestionIsInLoop"]) -> MetaOapg.properties.QuestionIsInLoop: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ChoiceLocator"]) -> 'Locator': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LogicType"]) -> MetaOapg.properties.LogicType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["QuestionID"]) -> 'QuestionID': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Operator"], typing_extensions.Literal["Type"], typing_extensions.Literal["QuestionIsInLoop"], typing_extensions.Literal["ChoiceLocator"], typing_extensions.Literal["LogicType"], typing_extensions.Literal["QuestionID"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Operator"]) -> MetaOapg.properties.Operator: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Type"]) -> MetaOapg.properties.Type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["QuestionIsInLoop"]) -> MetaOapg.properties.QuestionIsInLoop: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ChoiceLocator"]) -> 'Locator': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LogicType"]) -> MetaOapg.properties.LogicType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["QuestionID"]) -> 'QuestionID': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Operator"], typing_extensions.Literal["Type"], typing_extensions.Literal["QuestionIsInLoop"], typing_extensions.Literal["ChoiceLocator"], typing_extensions.Literal["LogicType"], typing_extensions.Literal["QuestionID"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Operator: typing.Union[MetaOapg.properties.Operator, str, ],
        Type: typing.Union[MetaOapg.properties.Type, str, ],
        QuestionIsInLoop: typing.Union[MetaOapg.properties.QuestionIsInLoop, str, ],
        ChoiceLocator: 'Locator',
        LogicType: typing.Union[MetaOapg.properties.LogicType, str, ],
        QuestionID: 'QuestionID',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'QuestionExpression':
        return super().__new__(
            cls,
            *args,
            Operator=Operator,
            Type=Type,
            QuestionIsInLoop=QuestionIsInLoop,
            ChoiceLocator=ChoiceLocator,
            LogicType=LogicType,
            QuestionID=QuestionID,
            _configuration=_configuration,
            **kwargs,
        )

from qualtrics_survey_python_sdk.model.locator import Locator
from qualtrics_survey_python_sdk.model.question_id import QuestionID