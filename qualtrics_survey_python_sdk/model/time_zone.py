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


class TimeZone(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        enum_value_to_name = {
            "Africa/Bangui": "AFRICA_BANGUI",
            "Africa/Harare": "AFRICA_HARARE",
            "Africa/Nairobi": "AFRICA_NAIROBI",
            "America/Anchorage": "AMERICA_ANCHORAGE",
            "America/Argentina/Buenos_Aires": "AMERICA_ARGENTINA_BUENOS_AIRES",
            "America/Chicago": "AMERICA_CHICAGO",
            "America/Denver": "AMERICA_DENVER",
            "America/La_Paz": "AMERICA_LA_PAZ",
            "America/Los_Angeles": "AMERICA_LOS_ANGELES",
            "America/Montevideo": "AMERICA_MONTEVIDEO",
            "America/New_York": "AMERICA_NEW_YORK",
            "America/Noronha": "AMERICA_NORONHA",
            "America/Phoenix": "AMERICA_PHOENIX",
            "America/Rio_Branco": "AMERICA_RIO_BRANCO",
            "Asia/Baku": "ASIA_BAKU",
            "Asia/Bangkok": "ASIA_BANGKOK",
            "Asia/Calcutta": "ASIA_CALCUTTA",
            "Asia/Dhaka": "ASIA_DHAKA",
            "Asia/Hong_Kong": "ASIA_HONG_KONG",
            "Asia/Irkutsk": "ASIA_IRKUTSK",
            "Asia/Kabul": "ASIA_KABUL",
            "Asia/Karachi": "ASIA_KARACHI",
            "Asia/Katmandu": "ASIA_KATMANDU",
            "Asia/Krasnoyarsk": "ASIA_KRASNOYARSK",
            "Asia/Tehran": "ASIA_TEHRAN",
            "Asia/Magadan": "ASIA_MAGADAN",
            "Asia/Muscat": "ASIA_MUSCAT",
            "Asia/Novosibirsk": "ASIA_NOVOSIBIRSK",
            "Asia/Rangoon": "ASIA_RANGOON",
            "Asia/Seoul": "ASIA_SEOUL",
            "Asia/Yakutsk": "ASIA_YAKUTSK",
            "Asia/Yekaterinburg": "ASIA_YEKATERINBURG",
            "Atlantic/Azores": "ATLANTIC_AZORES",
            "Atlantic/Cape_Verde": "ATLANTIC_CAPE_VERDE",
            "Atlantic/Reykjavik": "ATLANTIC_REYKJAVIK",
            "Australia/Adelaide": "AUSTRALIA_ADELAIDE",
            "Australia/Brisbane": "AUSTRALIA_BRISBANE",
            "Australia/Canberra": "AUSTRALIA_CANBERRA",
            "Australia/Darwin": "AUSTRALIA_DARWIN",
            "Canada/Atlantic": "CANADA_ATLANTIC",
            "Canada/East-Saskatchewan": "CANADA_EASTSASKATCHEWAN",
            "Canada/Newfoundland": "CANADA_NEWFOUNDLAND",
            "Europe/Athens": "EUROPE_ATHENS",
            "Europe/Berlin": "EUROPE_BERLIN",
            "Europe/London": "EUROPE_LONDON",
            "Europe/Moscow": "EUROPE_MOSCOW",
            "Pacific/Auckland": "PACIFIC_AUCKLAND",
            "Pacific/Fiji": "PACIFIC_FIJI",
            "Pacific/Honolulu": "PACIFIC_HONOLULU",
            "Pacific/Midway": "PACIFIC_MIDWAY",
            "Pacific/Tongatapu": "PACIFIC_TONGATAPU",
        }
    
    @schemas.classproperty
    def AFRICA_BANGUI(cls):
        return cls("Africa/Bangui")
    
    @schemas.classproperty
    def AFRICA_HARARE(cls):
        return cls("Africa/Harare")
    
    @schemas.classproperty
    def AFRICA_NAIROBI(cls):
        return cls("Africa/Nairobi")
    
    @schemas.classproperty
    def AMERICA_ANCHORAGE(cls):
        return cls("America/Anchorage")
    
    @schemas.classproperty
    def AMERICA_ARGENTINA_BUENOS_AIRES(cls):
        return cls("America/Argentina/Buenos_Aires")
    
    @schemas.classproperty
    def AMERICA_CHICAGO(cls):
        return cls("America/Chicago")
    
    @schemas.classproperty
    def AMERICA_DENVER(cls):
        return cls("America/Denver")
    
    @schemas.classproperty
    def AMERICA_LA_PAZ(cls):
        return cls("America/La_Paz")
    
    @schemas.classproperty
    def AMERICA_LOS_ANGELES(cls):
        return cls("America/Los_Angeles")
    
    @schemas.classproperty
    def AMERICA_MONTEVIDEO(cls):
        return cls("America/Montevideo")
    
    @schemas.classproperty
    def AMERICA_NEW_YORK(cls):
        return cls("America/New_York")
    
    @schemas.classproperty
    def AMERICA_NORONHA(cls):
        return cls("America/Noronha")
    
    @schemas.classproperty
    def AMERICA_PHOENIX(cls):
        return cls("America/Phoenix")
    
    @schemas.classproperty
    def AMERICA_RIO_BRANCO(cls):
        return cls("America/Rio_Branco")
    
    @schemas.classproperty
    def ASIA_BAKU(cls):
        return cls("Asia/Baku")
    
    @schemas.classproperty
    def ASIA_BANGKOK(cls):
        return cls("Asia/Bangkok")
    
    @schemas.classproperty
    def ASIA_CALCUTTA(cls):
        return cls("Asia/Calcutta")
    
    @schemas.classproperty
    def ASIA_DHAKA(cls):
        return cls("Asia/Dhaka")
    
    @schemas.classproperty
    def ASIA_HONG_KONG(cls):
        return cls("Asia/Hong_Kong")
    
    @schemas.classproperty
    def ASIA_IRKUTSK(cls):
        return cls("Asia/Irkutsk")
    
    @schemas.classproperty
    def ASIA_KABUL(cls):
        return cls("Asia/Kabul")
    
    @schemas.classproperty
    def ASIA_KARACHI(cls):
        return cls("Asia/Karachi")
    
    @schemas.classproperty
    def ASIA_KATMANDU(cls):
        return cls("Asia/Katmandu")
    
    @schemas.classproperty
    def ASIA_KRASNOYARSK(cls):
        return cls("Asia/Krasnoyarsk")
    
    @schemas.classproperty
    def ASIA_TEHRAN(cls):
        return cls("Asia/Tehran")
    
    @schemas.classproperty
    def ASIA_MAGADAN(cls):
        return cls("Asia/Magadan")
    
    @schemas.classproperty
    def ASIA_MUSCAT(cls):
        return cls("Asia/Muscat")
    
    @schemas.classproperty
    def ASIA_NOVOSIBIRSK(cls):
        return cls("Asia/Novosibirsk")
    
    @schemas.classproperty
    def ASIA_RANGOON(cls):
        return cls("Asia/Rangoon")
    
    @schemas.classproperty
    def ASIA_SEOUL(cls):
        return cls("Asia/Seoul")
    
    @schemas.classproperty
    def ASIA_YAKUTSK(cls):
        return cls("Asia/Yakutsk")
    
    @schemas.classproperty
    def ASIA_YEKATERINBURG(cls):
        return cls("Asia/Yekaterinburg")
    
    @schemas.classproperty
    def ATLANTIC_AZORES(cls):
        return cls("Atlantic/Azores")
    
    @schemas.classproperty
    def ATLANTIC_CAPE_VERDE(cls):
        return cls("Atlantic/Cape_Verde")
    
    @schemas.classproperty
    def ATLANTIC_REYKJAVIK(cls):
        return cls("Atlantic/Reykjavik")
    
    @schemas.classproperty
    def AUSTRALIA_ADELAIDE(cls):
        return cls("Australia/Adelaide")
    
    @schemas.classproperty
    def AUSTRALIA_BRISBANE(cls):
        return cls("Australia/Brisbane")
    
    @schemas.classproperty
    def AUSTRALIA_CANBERRA(cls):
        return cls("Australia/Canberra")
    
    @schemas.classproperty
    def AUSTRALIA_DARWIN(cls):
        return cls("Australia/Darwin")
    
    @schemas.classproperty
    def CANADA_ATLANTIC(cls):
        return cls("Canada/Atlantic")
    
    @schemas.classproperty
    def CANADA_EASTSASKATCHEWAN(cls):
        return cls("Canada/East-Saskatchewan")
    
    @schemas.classproperty
    def CANADA_NEWFOUNDLAND(cls):
        return cls("Canada/Newfoundland")
    
    @schemas.classproperty
    def EUROPE_ATHENS(cls):
        return cls("Europe/Athens")
    
    @schemas.classproperty
    def EUROPE_BERLIN(cls):
        return cls("Europe/Berlin")
    
    @schemas.classproperty
    def EUROPE_LONDON(cls):
        return cls("Europe/London")
    
    @schemas.classproperty
    def EUROPE_MOSCOW(cls):
        return cls("Europe/Moscow")
    
    @schemas.classproperty
    def PACIFIC_AUCKLAND(cls):
        return cls("Pacific/Auckland")
    
    @schemas.classproperty
    def PACIFIC_FIJI(cls):
        return cls("Pacific/Fiji")
    
    @schemas.classproperty
    def PACIFIC_HONOLULU(cls):
        return cls("Pacific/Honolulu")
    
    @schemas.classproperty
    def PACIFIC_MIDWAY(cls):
        return cls("Pacific/Midway")
    
    @schemas.classproperty
    def PACIFIC_TONGATAPU(cls):
        return cls("Pacific/Tongatapu")
