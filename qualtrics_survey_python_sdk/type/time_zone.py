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


TimeZone = Literal["Africa/Bangui", "Africa/Harare", "Africa/Nairobi", "America/Anchorage", "America/Argentina/Buenos_Aires", "America/Chicago", "America/Denver", "America/La_Paz", "America/Los_Angeles", "America/Montevideo", "America/New_York", "America/Noronha", "America/Phoenix", "America/Rio_Branco", "Asia/Baku", "Asia/Bangkok", "Asia/Calcutta", "Asia/Dhaka", "Asia/Hong_Kong", "Asia/Irkutsk", "Asia/Kabul", "Asia/Karachi", "Asia/Katmandu", "Asia/Krasnoyarsk", "Asia/Tehran", "Asia/Magadan", "Asia/Muscat", "Asia/Novosibirsk", "Asia/Rangoon", "Asia/Seoul", "Asia/Yakutsk", "Asia/Yekaterinburg", "Atlantic/Azores", "Atlantic/Cape_Verde", "Atlantic/Reykjavik", "Australia/Adelaide", "Australia/Brisbane", "Australia/Canberra", "Australia/Darwin", "Canada/Atlantic", "Canada/East-Saskatchewan", "Canada/Newfoundland", "Europe/Athens", "Europe/Berlin", "Europe/London", "Europe/Moscow", "Pacific/Auckland", "Pacific/Fiji", "Pacific/Honolulu", "Pacific/Midway", "Pacific/Tongatapu"]
