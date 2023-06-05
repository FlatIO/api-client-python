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


class MediaAttachment(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Media attachment. The API will automatically resolve the details, oEmbed,
and media available if possible and return them in this object

    """


    class MetaOapg:
        required = {
            "type",
        }
        
        class properties:
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "rich": "RICH",
                        "photo": "PHOTO",
                        "video": "VIDEO",
                        "link": "LINK",
                        "flat": "FLAT",
                        "googleDrive": "GOOGLE_DRIVE",
                        "worksheet": "WORKSHEET",
                        "performance": "PERFORMANCE",
                    }
                
                @schemas.classproperty
                def RICH(cls):
                    return cls("rich")
                
                @schemas.classproperty
                def PHOTO(cls):
                    return cls("photo")
                
                @schemas.classproperty
                def VIDEO(cls):
                    return cls("video")
                
                @schemas.classproperty
                def LINK(cls):
                    return cls("link")
                
                @schemas.classproperty
                def FLAT(cls):
                    return cls("flat")
                
                @schemas.classproperty
                def GOOGLE_DRIVE(cls):
                    return cls("googleDrive")
                
                @schemas.classproperty
                def WORKSHEET(cls):
                    return cls("worksheet")
                
                @schemas.classproperty
                def PERFORMANCE(cls):
                    return cls("performance")
            score = schemas.StrSchema
            revision = schemas.StrSchema
            worksheet = schemas.StrSchema
            dedicated = schemas.BoolSchema
            track = schemas.StrSchema
        
            @staticmethod
            def sharingMode() -> typing.Type['MediaScoreSharingMode']:
                return MediaScoreSharingMode
            lockScoreTemplate = schemas.BoolSchema
            title = schemas.StrSchema
            description = schemas.StrSchema
            html = schemas.StrSchema
            htmlWidth = schemas.StrSchema
            htmlHeight = schemas.StrSchema
            url = schemas.StrSchema
            thumbnailUrl = schemas.StrSchema
            thumbnailWidth = schemas.IntSchema
            thumbnailHeight = schemas.IntSchema
            authorName = schemas.StrSchema
            authorUrl = schemas.StrSchema
            iconUrl = schemas.StrSchema
            mimeType = schemas.StrSchema
            googleDriveFileId = schemas.StrSchema
            __annotations__ = {
                "type": type,
                "score": score,
                "revision": revision,
                "worksheet": worksheet,
                "dedicated": dedicated,
                "track": track,
                "sharingMode": sharingMode,
                "lockScoreTemplate": lockScoreTemplate,
                "title": title,
                "description": description,
                "html": html,
                "htmlWidth": htmlWidth,
                "htmlHeight": htmlHeight,
                "url": url,
                "thumbnailUrl": thumbnailUrl,
                "thumbnailWidth": thumbnailWidth,
                "thumbnailHeight": thumbnailHeight,
                "authorName": authorName,
                "authorUrl": authorUrl,
                "iconUrl": iconUrl,
                "mimeType": mimeType,
                "googleDriveFileId": googleDriveFileId,
            }
    
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["score"]) -> MetaOapg.properties.score: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["revision"]) -> MetaOapg.properties.revision: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["worksheet"]) -> MetaOapg.properties.worksheet: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dedicated"]) -> MetaOapg.properties.dedicated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["track"]) -> MetaOapg.properties.track: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sharingMode"]) -> 'MediaScoreSharingMode': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lockScoreTemplate"]) -> MetaOapg.properties.lockScoreTemplate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["html"]) -> MetaOapg.properties.html: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["htmlWidth"]) -> MetaOapg.properties.htmlWidth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["htmlHeight"]) -> MetaOapg.properties.htmlHeight: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["thumbnailUrl"]) -> MetaOapg.properties.thumbnailUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["thumbnailWidth"]) -> MetaOapg.properties.thumbnailWidth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["thumbnailHeight"]) -> MetaOapg.properties.thumbnailHeight: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authorName"]) -> MetaOapg.properties.authorName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authorUrl"]) -> MetaOapg.properties.authorUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["iconUrl"]) -> MetaOapg.properties.iconUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mimeType"]) -> MetaOapg.properties.mimeType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["googleDriveFileId"]) -> MetaOapg.properties.googleDriveFileId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "score", "revision", "worksheet", "dedicated", "track", "sharingMode", "lockScoreTemplate", "title", "description", "html", "htmlWidth", "htmlHeight", "url", "thumbnailUrl", "thumbnailWidth", "thumbnailHeight", "authorName", "authorUrl", "iconUrl", "mimeType", "googleDriveFileId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["score"]) -> typing.Union[MetaOapg.properties.score, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["revision"]) -> typing.Union[MetaOapg.properties.revision, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["worksheet"]) -> typing.Union[MetaOapg.properties.worksheet, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dedicated"]) -> typing.Union[MetaOapg.properties.dedicated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["track"]) -> typing.Union[MetaOapg.properties.track, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sharingMode"]) -> typing.Union['MediaScoreSharingMode', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lockScoreTemplate"]) -> typing.Union[MetaOapg.properties.lockScoreTemplate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["html"]) -> typing.Union[MetaOapg.properties.html, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["htmlWidth"]) -> typing.Union[MetaOapg.properties.htmlWidth, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["htmlHeight"]) -> typing.Union[MetaOapg.properties.htmlHeight, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> typing.Union[MetaOapg.properties.url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["thumbnailUrl"]) -> typing.Union[MetaOapg.properties.thumbnailUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["thumbnailWidth"]) -> typing.Union[MetaOapg.properties.thumbnailWidth, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["thumbnailHeight"]) -> typing.Union[MetaOapg.properties.thumbnailHeight, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authorName"]) -> typing.Union[MetaOapg.properties.authorName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authorUrl"]) -> typing.Union[MetaOapg.properties.authorUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["iconUrl"]) -> typing.Union[MetaOapg.properties.iconUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mimeType"]) -> typing.Union[MetaOapg.properties.mimeType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["googleDriveFileId"]) -> typing.Union[MetaOapg.properties.googleDriveFileId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "score", "revision", "worksheet", "dedicated", "track", "sharingMode", "lockScoreTemplate", "title", "description", "html", "htmlWidth", "htmlHeight", "url", "thumbnailUrl", "thumbnailWidth", "thumbnailHeight", "authorName", "authorUrl", "iconUrl", "mimeType", "googleDriveFileId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        score: typing.Union[MetaOapg.properties.score, str, schemas.Unset] = schemas.unset,
        revision: typing.Union[MetaOapg.properties.revision, str, schemas.Unset] = schemas.unset,
        worksheet: typing.Union[MetaOapg.properties.worksheet, str, schemas.Unset] = schemas.unset,
        dedicated: typing.Union[MetaOapg.properties.dedicated, bool, schemas.Unset] = schemas.unset,
        track: typing.Union[MetaOapg.properties.track, str, schemas.Unset] = schemas.unset,
        sharingMode: typing.Union['MediaScoreSharingMode', schemas.Unset] = schemas.unset,
        lockScoreTemplate: typing.Union[MetaOapg.properties.lockScoreTemplate, bool, schemas.Unset] = schemas.unset,
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        html: typing.Union[MetaOapg.properties.html, str, schemas.Unset] = schemas.unset,
        htmlWidth: typing.Union[MetaOapg.properties.htmlWidth, str, schemas.Unset] = schemas.unset,
        htmlHeight: typing.Union[MetaOapg.properties.htmlHeight, str, schemas.Unset] = schemas.unset,
        url: typing.Union[MetaOapg.properties.url, str, schemas.Unset] = schemas.unset,
        thumbnailUrl: typing.Union[MetaOapg.properties.thumbnailUrl, str, schemas.Unset] = schemas.unset,
        thumbnailWidth: typing.Union[MetaOapg.properties.thumbnailWidth, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        thumbnailHeight: typing.Union[MetaOapg.properties.thumbnailHeight, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        authorName: typing.Union[MetaOapg.properties.authorName, str, schemas.Unset] = schemas.unset,
        authorUrl: typing.Union[MetaOapg.properties.authorUrl, str, schemas.Unset] = schemas.unset,
        iconUrl: typing.Union[MetaOapg.properties.iconUrl, str, schemas.Unset] = schemas.unset,
        mimeType: typing.Union[MetaOapg.properties.mimeType, str, schemas.Unset] = schemas.unset,
        googleDriveFileId: typing.Union[MetaOapg.properties.googleDriveFileId, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MediaAttachment':
        return super().__new__(
            cls,
            *_args,
            type=type,
            score=score,
            revision=revision,
            worksheet=worksheet,
            dedicated=dedicated,
            track=track,
            sharingMode=sharingMode,
            lockScoreTemplate=lockScoreTemplate,
            title=title,
            description=description,
            html=html,
            htmlWidth=htmlWidth,
            htmlHeight=htmlHeight,
            url=url,
            thumbnailUrl=thumbnailUrl,
            thumbnailWidth=thumbnailWidth,
            thumbnailHeight=thumbnailHeight,
            authorName=authorName,
            authorUrl=authorUrl,
            iconUrl=iconUrl,
            mimeType=mimeType,
            googleDriveFileId=googleDriveFileId,
            _configuration=_configuration,
            **kwargs,
        )

from flat_api.model.media_score_sharing_mode import MediaScoreSharingMode
