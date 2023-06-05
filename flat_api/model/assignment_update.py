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


class AssignmentUpdate(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Assignment Resource Editing
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def type() -> typing.Type['AssignmentType']:
                return AssignmentType
            
            
            class title(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 1000
                    min_length = 1
            description = schemas.StrSchema
            
            
            class attachments(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ClassAttachmentCreation']:
                        return ClassAttachmentCreation
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['ClassAttachmentCreation'], typing.List['ClassAttachmentCreation']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'attachments':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ClassAttachmentCreation':
                    return super().__getitem__(i)
            
            
            class nbPlaybackAuthorized(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'nbPlaybackAuthorized':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class toolset(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'toolset':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class coverFile(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'coverFile':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class cover(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'cover':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class maxPoints(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 100
                    inclusive_minimum = 0
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'maxPoints':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class releaseGrades(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "auto": "AUTO",
                        "manual": "MANUAL",
                    }
                
                @schemas.classproperty
                def AUTO(cls):
                    return cls("auto")
                
                @schemas.classproperty
                def MANUAL(cls):
                    return cls("manual")
            shuffleExercises = schemas.BoolSchema
            __annotations__ = {
                "type": type,
                "title": title,
                "description": description,
                "attachments": attachments,
                "nbPlaybackAuthorized": nbPlaybackAuthorized,
                "toolset": toolset,
                "coverFile": coverFile,
                "cover": cover,
                "maxPoints": maxPoints,
                "releaseGrades": releaseGrades,
                "shuffleExercises": shuffleExercises,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'AssignmentType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attachments"]) -> MetaOapg.properties.attachments: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nbPlaybackAuthorized"]) -> MetaOapg.properties.nbPlaybackAuthorized: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["toolset"]) -> MetaOapg.properties.toolset: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coverFile"]) -> MetaOapg.properties.coverFile: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cover"]) -> MetaOapg.properties.cover: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxPoints"]) -> MetaOapg.properties.maxPoints: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["releaseGrades"]) -> MetaOapg.properties.releaseGrades: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shuffleExercises"]) -> MetaOapg.properties.shuffleExercises: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "title", "description", "attachments", "nbPlaybackAuthorized", "toolset", "coverFile", "cover", "maxPoints", "releaseGrades", "shuffleExercises", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union['AssignmentType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attachments"]) -> typing.Union[MetaOapg.properties.attachments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nbPlaybackAuthorized"]) -> typing.Union[MetaOapg.properties.nbPlaybackAuthorized, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["toolset"]) -> typing.Union[MetaOapg.properties.toolset, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coverFile"]) -> typing.Union[MetaOapg.properties.coverFile, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cover"]) -> typing.Union[MetaOapg.properties.cover, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxPoints"]) -> typing.Union[MetaOapg.properties.maxPoints, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["releaseGrades"]) -> typing.Union[MetaOapg.properties.releaseGrades, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shuffleExercises"]) -> typing.Union[MetaOapg.properties.shuffleExercises, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "title", "description", "attachments", "nbPlaybackAuthorized", "toolset", "coverFile", "cover", "maxPoints", "releaseGrades", "shuffleExercises", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        type: typing.Union['AssignmentType', schemas.Unset] = schemas.unset,
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        attachments: typing.Union[MetaOapg.properties.attachments, list, tuple, schemas.Unset] = schemas.unset,
        nbPlaybackAuthorized: typing.Union[MetaOapg.properties.nbPlaybackAuthorized, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        toolset: typing.Union[MetaOapg.properties.toolset, None, str, schemas.Unset] = schemas.unset,
        coverFile: typing.Union[MetaOapg.properties.coverFile, None, str, schemas.Unset] = schemas.unset,
        cover: typing.Union[MetaOapg.properties.cover, None, str, schemas.Unset] = schemas.unset,
        maxPoints: typing.Union[MetaOapg.properties.maxPoints, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        releaseGrades: typing.Union[MetaOapg.properties.releaseGrades, str, schemas.Unset] = schemas.unset,
        shuffleExercises: typing.Union[MetaOapg.properties.shuffleExercises, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AssignmentUpdate':
        return super().__new__(
            cls,
            *_args,
            type=type,
            title=title,
            description=description,
            attachments=attachments,
            nbPlaybackAuthorized=nbPlaybackAuthorized,
            toolset=toolset,
            coverFile=coverFile,
            cover=cover,
            maxPoints=maxPoints,
            releaseGrades=releaseGrades,
            shuffleExercises=shuffleExercises,
            _configuration=_configuration,
            **kwargs,
        )

from flat_api.model.assignment_type import AssignmentType
from flat_api.model.class_attachment_creation import ClassAttachmentCreation
