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


class ScoreRevision(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A score revision metadata
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
            user = schemas.StrSchema
            
            
            class collaborators(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'collaborators':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            creationDate = schemas.DateTimeSchema
            event = schemas.StrSchema
            description = schemas.StrSchema
            autosave = schemas.BoolSchema
        
            @staticmethod
            def statistics() -> typing.Type['ScoreRevisionStatistics']:
                return ScoreRevisionStatistics
            __annotations__ = {
                "id": id,
                "user": user,
                "collaborators": collaborators,
                "creationDate": creationDate,
                "event": event,
                "description": description,
                "autosave": autosave,
                "statistics": statistics,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user"]) -> MetaOapg.properties.user: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["collaborators"]) -> MetaOapg.properties.collaborators: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["creationDate"]) -> MetaOapg.properties.creationDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["event"]) -> MetaOapg.properties.event: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["autosave"]) -> MetaOapg.properties.autosave: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["statistics"]) -> 'ScoreRevisionStatistics': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "user", "collaborators", "creationDate", "event", "description", "autosave", "statistics", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> typing.Union[MetaOapg.properties.user, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["collaborators"]) -> typing.Union[MetaOapg.properties.collaborators, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["creationDate"]) -> typing.Union[MetaOapg.properties.creationDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["event"]) -> typing.Union[MetaOapg.properties.event, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["autosave"]) -> typing.Union[MetaOapg.properties.autosave, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["statistics"]) -> typing.Union['ScoreRevisionStatistics', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "user", "collaborators", "creationDate", "event", "description", "autosave", "statistics", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        user: typing.Union[MetaOapg.properties.user, str, schemas.Unset] = schemas.unset,
        collaborators: typing.Union[MetaOapg.properties.collaborators, list, tuple, schemas.Unset] = schemas.unset,
        creationDate: typing.Union[MetaOapg.properties.creationDate, str, datetime, schemas.Unset] = schemas.unset,
        event: typing.Union[MetaOapg.properties.event, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        autosave: typing.Union[MetaOapg.properties.autosave, bool, schemas.Unset] = schemas.unset,
        statistics: typing.Union['ScoreRevisionStatistics', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ScoreRevision':
        return super().__new__(
            cls,
            *_args,
            id=id,
            user=user,
            collaborators=collaborators,
            creationDate=creationDate,
            event=event,
            description=description,
            autosave=autosave,
            statistics=statistics,
            _configuration=_configuration,
            **kwargs,
        )

from flat_api.model.score_revision_statistics import ScoreRevisionStatistics
