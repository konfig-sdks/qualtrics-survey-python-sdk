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


class SurveyProtection(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Survey is either publicly available or restricted by invitation only
    """


    class MetaOapg:
        enum_value_to_name = {
            "PublicSurvey": "PUBLIC_SURVEY",
            "ByInvitation": "BY_INVITATION",
            "PasswordProtected": "PASSWORD_PROTECTED",
        }
    
    @schemas.classproperty
    def PUBLIC_SURVEY(cls):
        return cls("PublicSurvey")
    
    @schemas.classproperty
    def BY_INVITATION(cls):
        return cls("ByInvitation")
    
    @schemas.classproperty
    def PASSWORD_PROTECTED(cls):
        return cls("PasswordProtected")
