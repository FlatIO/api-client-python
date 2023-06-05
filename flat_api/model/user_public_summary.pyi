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


class UserPublicSummary(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def USER(cls):
                    return cls("user")
                
                @schemas.classproperty
                def GUEST(cls):
                    return cls("guest")
            username = schemas.StrSchema
            printableName = schemas.StrSchema
            firstname = schemas.StrSchema
            lastname = schemas.StrSchema
            name = schemas.StrSchema
            
            
            class picture(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'picture':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class badges(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'badges':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            organization = schemas.StrSchema
        
            @staticmethod
            def organizationRole() -> typing.Type['OrganizationRoles']:
                return OrganizationRoles
        
            @staticmethod
            def classRole() -> typing.Type['ClassRoles']:
                return ClassRoles
            htmlUrl = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "type": type,
                "username": username,
                "printableName": printableName,
                "firstname": firstname,
                "lastname": lastname,
                "name": name,
                "picture": picture,
                "badges": badges,
                "organization": organization,
                "organizationRole": organizationRole,
                "classRole": classRole,
                "htmlUrl": htmlUrl,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["username"]) -> MetaOapg.properties.username: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["printableName"]) -> MetaOapg.properties.printableName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstname"]) -> MetaOapg.properties.firstname: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastname"]) -> MetaOapg.properties.lastname: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["picture"]) -> MetaOapg.properties.picture: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["badges"]) -> MetaOapg.properties.badges: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organization"]) -> MetaOapg.properties.organization: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organizationRole"]) -> 'OrganizationRoles': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["classRole"]) -> 'ClassRoles': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["htmlUrl"]) -> MetaOapg.properties.htmlUrl: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "type", "username", "printableName", "firstname", "lastname", "name", "picture", "badges", "organization", "organizationRole", "classRole", "htmlUrl", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["username"]) -> typing.Union[MetaOapg.properties.username, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["printableName"]) -> typing.Union[MetaOapg.properties.printableName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstname"]) -> typing.Union[MetaOapg.properties.firstname, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastname"]) -> typing.Union[MetaOapg.properties.lastname, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["picture"]) -> typing.Union[MetaOapg.properties.picture, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["badges"]) -> typing.Union[MetaOapg.properties.badges, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organization"]) -> typing.Union[MetaOapg.properties.organization, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organizationRole"]) -> typing.Union['OrganizationRoles', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["classRole"]) -> typing.Union['ClassRoles', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["htmlUrl"]) -> typing.Union[MetaOapg.properties.htmlUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "type", "username", "printableName", "firstname", "lastname", "name", "picture", "badges", "organization", "organizationRole", "classRole", "htmlUrl", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        username: typing.Union[MetaOapg.properties.username, str, schemas.Unset] = schemas.unset,
        printableName: typing.Union[MetaOapg.properties.printableName, str, schemas.Unset] = schemas.unset,
        firstname: typing.Union[MetaOapg.properties.firstname, str, schemas.Unset] = schemas.unset,
        lastname: typing.Union[MetaOapg.properties.lastname, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        picture: typing.Union[MetaOapg.properties.picture, None, str, schemas.Unset] = schemas.unset,
        badges: typing.Union[MetaOapg.properties.badges, list, tuple, schemas.Unset] = schemas.unset,
        organization: typing.Union[MetaOapg.properties.organization, str, schemas.Unset] = schemas.unset,
        organizationRole: typing.Union['OrganizationRoles', schemas.Unset] = schemas.unset,
        classRole: typing.Union['ClassRoles', schemas.Unset] = schemas.unset,
        htmlUrl: typing.Union[MetaOapg.properties.htmlUrl, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UserPublicSummary':
        return super().__new__(
            cls,
            *_args,
            id=id,
            type=type,
            username=username,
            printableName=printableName,
            firstname=firstname,
            lastname=lastname,
            name=name,
            picture=picture,
            badges=badges,
            organization=organization,
            organizationRole=organizationRole,
            classRole=classRole,
            htmlUrl=htmlUrl,
            _configuration=_configuration,
            **kwargs,
        )

from flat_api.model.class_roles import ClassRoles
from flat_api.model.organization_roles import OrganizationRoles