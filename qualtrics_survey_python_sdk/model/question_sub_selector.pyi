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


class QuestionSubSelector(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Question SubSelector.
    """
    
    @schemas.classproperty
    def SINGLE_ANSWER(cls):
        return cls("SingleAnswer")
    
    @schemas.classproperty
    def DL(cls):
        return cls("DL")
    
    @schemas.classproperty
    def GR(cls):
        return cls("GR")
    
    @schemas.classproperty
    def DND(cls):
        return cls("DND")
    
    @schemas.classproperty
    def LONG(cls):
        return cls("Long")
    
    @schemas.classproperty
    def MEDIUM(cls):
        return cls("Medium")
    
    @schemas.classproperty
    def MULTIPLE_ANSWER(cls):
        return cls("MultipleAnswer")
    
    @schemas.classproperty
    def COLUMNS(cls):
        return cls("Columns")
    
    @schemas.classproperty
    def NO_COLUMNS(cls):
        return cls("NoColumns")
    
    @schemas.classproperty
    def SHORT(cls):
        return cls("Short")
    
    @schemas.classproperty
    def TX(cls):
        return cls("TX")
    
    @schemas.classproperty
    def TXOT(cls):
        return cls("TXOT")
    
    @schemas.classproperty
    def WOTXB(cls):
        return cls("WOTXB")
    
    @schemas.classproperty
    def WOTB(cls):
        return cls("WOTB")
    
    @schemas.classproperty
    def WTB(cls):
        return cls("WTB")
    
    @schemas.classproperty
    def WTXB(cls):
        return cls("WTXB")
    
    @schemas.classproperty
    def WVTB(cls):
        return cls("WVTB")