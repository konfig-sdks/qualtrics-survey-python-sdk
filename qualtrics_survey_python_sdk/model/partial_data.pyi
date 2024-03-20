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


class PartialData(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Specify how long a respondent can leave a survey unfinished before that survey automatically closes. A value of `No` specifies to delete partial completion data. See also `PartialDataCloseAfter`.
    """
    
    @schemas.classproperty
    def FALSE(cls):
        return cls("false")
    
    @schemas.classproperty
    def _1_HOUR(cls):
        return cls("+1 hour")
    
    @schemas.classproperty
    def _4_HOUR(cls):
        return cls("+4 hour")
    
    @schemas.classproperty
    def _1_DAY(cls):
        return cls("+1 day")
    
    @schemas.classproperty
    def _2_DAYS(cls):
        return cls("+2 days")
    
    @schemas.classproperty
    def _3_DAYS(cls):
        return cls("+3 days")
    
    @schemas.classproperty
    def _1_WEEK(cls):
        return cls("+1 week")
    
    @schemas.classproperty
    def _2_WEEKS(cls):
        return cls("+2 weeks")
    
    @schemas.classproperty
    def _1_MONTH(cls):
        return cls("+1 month")
    
    @schemas.classproperty
    def _3_MONTHS(cls):
        return cls("+3 months")
    
    @schemas.classproperty
    def _6_MONTHS(cls):
        return cls("+6 months")
    
    @schemas.classproperty
    def _1_YEAR(cls):
        return cls("+1 year")
