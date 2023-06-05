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


class AssignmentCopyResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
        
            @staticmethod
            def type() -> typing.Type['AssignmentType']:
                return AssignmentType
            
            
            class capabilities(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "canArchive",
                        "canPublishInClass",
                        "canUnarchive",
                        "canEdit",
                    }
                    
                    class properties:
                        canEdit = schemas.BoolSchema
                        canPublishInClass = schemas.BoolSchema
                        
                        
                        class canPublishInClassError(
                            schemas.DictSchema
                        ):
                        
                        
                            class MetaOapg:
                                required = {
                                    "code",
                                    "message",
                                }
                                
                                class properties:
                                    code = schemas.StrSchema
                                    message = schemas.StrSchema
                                    __annotations__ = {
                                        "code": code,
                                        "message": message,
                                    }
                            
                            code: MetaOapg.properties.code
                            message: MetaOapg.properties.message
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
                            
                            @typing.overload
                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                            
                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["code", "message", ], str]):
                                # dict_instance[name] accessor
                                return super().__getitem__(name)
                            
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                            
                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["code", "message", ], str]):
                                return super().get_item_oapg(name)
                            
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[dict, frozendict.frozendict, ],
                                code: typing.Union[MetaOapg.properties.code, str, ],
                                message: typing.Union[MetaOapg.properties.message, str, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> 'canPublishInClassError':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    code=code,
                                    message=message,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        canArchive = schemas.BoolSchema
                        canUnarchive = schemas.BoolSchema
                        __annotations__ = {
                            "canEdit": canEdit,
                            "canPublishInClass": canPublishInClass,
                            "canPublishInClassError": canPublishInClassError,
                            "canArchive": canArchive,
                            "canUnarchive": canUnarchive,
                        }
                
                canArchive: MetaOapg.properties.canArchive
                canPublishInClass: MetaOapg.properties.canPublishInClass
                canUnarchive: MetaOapg.properties.canUnarchive
                canEdit: MetaOapg.properties.canEdit
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["canEdit"]) -> MetaOapg.properties.canEdit: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["canPublishInClass"]) -> MetaOapg.properties.canPublishInClass: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["canPublishInClassError"]) -> MetaOapg.properties.canPublishInClassError: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["canArchive"]) -> MetaOapg.properties.canArchive: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["canUnarchive"]) -> MetaOapg.properties.canUnarchive: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["canEdit", "canPublishInClass", "canPublishInClassError", "canArchive", "canUnarchive", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["canEdit"]) -> MetaOapg.properties.canEdit: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["canPublishInClass"]) -> MetaOapg.properties.canPublishInClass: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["canPublishInClassError"]) -> typing.Union[MetaOapg.properties.canPublishInClassError, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["canArchive"]) -> MetaOapg.properties.canArchive: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["canUnarchive"]) -> MetaOapg.properties.canUnarchive: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["canEdit", "canPublishInClass", "canPublishInClassError", "canArchive", "canUnarchive", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    canArchive: typing.Union[MetaOapg.properties.canArchive, bool, ],
                    canPublishInClass: typing.Union[MetaOapg.properties.canPublishInClass, bool, ],
                    canUnarchive: typing.Union[MetaOapg.properties.canUnarchive, bool, ],
                    canEdit: typing.Union[MetaOapg.properties.canEdit, bool, ],
                    canPublishInClassError: typing.Union[MetaOapg.properties.canPublishInClassError, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'capabilities':
                    return super().__new__(
                        cls,
                        *_args,
                        canArchive=canArchive,
                        canPublishInClass=canPublishInClass,
                        canUnarchive=canUnarchive,
                        canEdit=canEdit,
                        canPublishInClassError=canPublishInClassError,
                        _configuration=_configuration,
                        **kwargs,
                    )
            title = schemas.StrSchema
            description = schemas.StrSchema
            cover = schemas.StrSchema
            coverFile = schemas.StrSchema
            
            
            class attachments(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['MediaAttachment']:
                        return MediaAttachment
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['MediaAttachment'], typing.List['MediaAttachment']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'attachments':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'MediaAttachment':
                    return super().__getitem__(i)
            useDedicatedAttachments = schemas.BoolSchema
            maxPoints = schemas.NumberSchema
            
            
            class releaseGrades(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def AUTO(cls):
                    return cls("auto")
                
                @schemas.classproperty
                def MANUAL(cls):
                    return cls("manual")
            shuffleExercises = schemas.BoolSchema
            toolset = schemas.StrSchema
            nbPlaybackAuthorized = schemas.NumberSchema
            resource = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "type": type,
                "capabilities": capabilities,
                "title": title,
                "description": description,
                "cover": cover,
                "coverFile": coverFile,
                "attachments": attachments,
                "useDedicatedAttachments": useDedicatedAttachments,
                "maxPoints": maxPoints,
                "releaseGrades": releaseGrades,
                "shuffleExercises": shuffleExercises,
                "toolset": toolset,
                "nbPlaybackAuthorized": nbPlaybackAuthorized,
                "resource": resource,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'AssignmentType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["capabilities"]) -> MetaOapg.properties.capabilities: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cover"]) -> MetaOapg.properties.cover: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coverFile"]) -> MetaOapg.properties.coverFile: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attachments"]) -> MetaOapg.properties.attachments: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["useDedicatedAttachments"]) -> MetaOapg.properties.useDedicatedAttachments: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxPoints"]) -> MetaOapg.properties.maxPoints: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["releaseGrades"]) -> MetaOapg.properties.releaseGrades: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shuffleExercises"]) -> MetaOapg.properties.shuffleExercises: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["toolset"]) -> MetaOapg.properties.toolset: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nbPlaybackAuthorized"]) -> MetaOapg.properties.nbPlaybackAuthorized: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resource"]) -> MetaOapg.properties.resource: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "type", "capabilities", "title", "description", "cover", "coverFile", "attachments", "useDedicatedAttachments", "maxPoints", "releaseGrades", "shuffleExercises", "toolset", "nbPlaybackAuthorized", "resource", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union['AssignmentType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["capabilities"]) -> typing.Union[MetaOapg.properties.capabilities, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cover"]) -> typing.Union[MetaOapg.properties.cover, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coverFile"]) -> typing.Union[MetaOapg.properties.coverFile, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attachments"]) -> typing.Union[MetaOapg.properties.attachments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["useDedicatedAttachments"]) -> typing.Union[MetaOapg.properties.useDedicatedAttachments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxPoints"]) -> typing.Union[MetaOapg.properties.maxPoints, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["releaseGrades"]) -> typing.Union[MetaOapg.properties.releaseGrades, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shuffleExercises"]) -> typing.Union[MetaOapg.properties.shuffleExercises, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["toolset"]) -> typing.Union[MetaOapg.properties.toolset, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nbPlaybackAuthorized"]) -> typing.Union[MetaOapg.properties.nbPlaybackAuthorized, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resource"]) -> typing.Union[MetaOapg.properties.resource, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "type", "capabilities", "title", "description", "cover", "coverFile", "attachments", "useDedicatedAttachments", "maxPoints", "releaseGrades", "shuffleExercises", "toolset", "nbPlaybackAuthorized", "resource", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        type: typing.Union['AssignmentType', schemas.Unset] = schemas.unset,
        capabilities: typing.Union[MetaOapg.properties.capabilities, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        cover: typing.Union[MetaOapg.properties.cover, str, schemas.Unset] = schemas.unset,
        coverFile: typing.Union[MetaOapg.properties.coverFile, str, schemas.Unset] = schemas.unset,
        attachments: typing.Union[MetaOapg.properties.attachments, list, tuple, schemas.Unset] = schemas.unset,
        useDedicatedAttachments: typing.Union[MetaOapg.properties.useDedicatedAttachments, bool, schemas.Unset] = schemas.unset,
        maxPoints: typing.Union[MetaOapg.properties.maxPoints, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        releaseGrades: typing.Union[MetaOapg.properties.releaseGrades, str, schemas.Unset] = schemas.unset,
        shuffleExercises: typing.Union[MetaOapg.properties.shuffleExercises, bool, schemas.Unset] = schemas.unset,
        toolset: typing.Union[MetaOapg.properties.toolset, str, schemas.Unset] = schemas.unset,
        nbPlaybackAuthorized: typing.Union[MetaOapg.properties.nbPlaybackAuthorized, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        resource: typing.Union[MetaOapg.properties.resource, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AssignmentCopyResponse':
        return super().__new__(
            cls,
            *_args,
            id=id,
            type=type,
            capabilities=capabilities,
            title=title,
            description=description,
            cover=cover,
            coverFile=coverFile,
            attachments=attachments,
            useDedicatedAttachments=useDedicatedAttachments,
            maxPoints=maxPoints,
            releaseGrades=releaseGrades,
            shuffleExercises=shuffleExercises,
            toolset=toolset,
            nbPlaybackAuthorized=nbPlaybackAuthorized,
            resource=resource,
            _configuration=_configuration,
            **kwargs,
        )

from flat_api.model.assignment_type import AssignmentType
from flat_api.model.media_attachment import MediaAttachment