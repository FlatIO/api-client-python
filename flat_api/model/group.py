# coding: utf-8

"""
    Flat API

    The Flat API allows you to easily extend the abilities of the [Flat Platform](https://flat.io), with a wide range of use cases including the following:  * Creating and importing new music scores using MusicXML, MIDI, Guitar Pro (GP3, GP4, GP5, GPX, GP), PowerTab, TuxGuitar and MuseScore files * Browsing, updating, copying, exporting the user's scores (for example in MP3, WAV or MIDI) * Managing educational resources with Flat for Education: creating & updating the organization accounts, the classes, rosters and assignments.  The Flat API is built on HTTP. Our API is RESTful It has predictable resource URLs. It returns HTTP response codes to indicate errors. It also accepts and returns JSON in the HTTP body. The [schema](/swagger.yaml) of this API follows the [OpenAPI Initiative (OAI) specification](https://www.openapis.org/), you can use and work with [compatible Swagger tools](http://swagger.io/open-source-integrations/). This API features Cross-Origin Resource Sharing (CORS) implemented in compliance with [W3C spec](https://www.w3.org/TR/cors/).  You can use your favorite HTTP/REST library for your programming language to use Flat's API. This specification and reference is [available on Github](https://github.com/FlatIO/api-reference).  Getting Started and learn more:  * [API Overview and introduction](https://flat.io/developers/docs/api/) * [Authentication (Personal Access Tokens or OAuth2)](https://flat.io/developers/docs/api/authentication.html) * [SDKs](https://flat.io/developers/docs/api/sdks.html) * [Rate Limits](https://flat.io/developers/docs/api/rate-limits.html) * [Changelog](https://flat.io/developers/docs/api/changelog.html)   # noqa: E501

    The version of the OpenAPI document: 2.18.0
    Contact: developers@flat.io
    Generated by: https://openapi-generator.tech
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

from flat_api import schemas  # noqa: F401


class Group(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A group of users
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
            name = schemas.StrSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "generic": "GENERIC",
                        "classTeachers": "CLASS_TEACHERS",
                        "classStudents": "CLASS_STUDENTS",
                    }
                
                @schemas.classproperty
                def GENERIC(cls):
                    return cls("generic")
                
                @schemas.classproperty
                def CLASS_TEACHERS(cls):
                    return cls("classTeachers")
                
                @schemas.classproperty
                def CLASS_STUDENTS(cls):
                    return cls("classStudents")
            usersCount = schemas.NumberSchema
            readOnly = schemas.BoolSchema
            organization = schemas.StrSchema
            creationDate = schemas.DateTimeSchema
            __annotations__ = {
                "id": id,
                "name": name,
                "type": type,
                "usersCount": usersCount,
                "readOnly": readOnly,
                "organization": organization,
                "creationDate": creationDate,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["usersCount"]) -> MetaOapg.properties.usersCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["readOnly"]) -> MetaOapg.properties.readOnly: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organization"]) -> MetaOapg.properties.organization: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["creationDate"]) -> MetaOapg.properties.creationDate: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "type", "usersCount", "readOnly", "organization", "creationDate", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["usersCount"]) -> typing.Union[MetaOapg.properties.usersCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["readOnly"]) -> typing.Union[MetaOapg.properties.readOnly, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organization"]) -> typing.Union[MetaOapg.properties.organization, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["creationDate"]) -> typing.Union[MetaOapg.properties.creationDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "type", "usersCount", "readOnly", "organization", "creationDate", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        usersCount: typing.Union[MetaOapg.properties.usersCount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        readOnly: typing.Union[MetaOapg.properties.readOnly, bool, schemas.Unset] = schemas.unset,
        organization: typing.Union[MetaOapg.properties.organization, str, schemas.Unset] = schemas.unset,
        creationDate: typing.Union[MetaOapg.properties.creationDate, str, datetime, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Group':
        return super().__new__(
            cls,
            *_args,
            id=id,
            name=name,
            type=type,
            usersCount=usersCount,
            readOnly=readOnly,
            organization=organization,
            creationDate=creationDate,
            _configuration=_configuration,
            **kwargs,
        )
