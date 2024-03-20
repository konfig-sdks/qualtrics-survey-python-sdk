# coding: utf-8

"""
    Qualtrics Survey API

    The Qualtrics Survey endpoints give you access to the structure of the surveys you create.   Surveys have a complex structure, and you are encouraged to become familiar with the structure using your brand's Qualtrics page to build surveys at first. Then you can query those surveys using these endpoints.   Once you are familiar, you can use this API to create surveys on the fly, or modify existing surveys in your library. 

    The version of the OpenAPI document: 3.0.0
    Created by: https://www.qualtrics.com/support/
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel


class AuthenticatorFlowElementSsoOptionsToken(BaseModel):
    # Encryption method for the token.
    encryption_method: typing.Optional[Literal["3DES", "AES128", "BLOWFISH"]] = Field(None, alias='EncryptionMethod')

    # Token key.
    key: typing.Optional[str] = Field(None, alias='Key')

    # Leeway.
    leeway: typing.Optional[int] = Field(None, alias='Leeway')

    # MacMethod.
    mac_method: typing.Optional[Literal["md5", "MD5", "sha1", "sha256", "sha512"]] = Field(None, alias='MacMethod')

    # Block Cipher.
    block_cipher: typing.Optional[Literal["CBC", "ECB"]] = Field(None, alias='BlockCipher')
    class Config:
        arbitrary_types_allowed = True
