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


class ScoreCreation(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            title = schemas.StrSchema
        
            @staticmethod
            def privacy() -> typing.Type['ScorePrivacy']:
                return ScorePrivacy
            collection = schemas.StrSchema
            googleDriveFolder = schemas.StrSchema
            
            
            class builderData(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "scoreData",
                    }
                    
                    class properties:
                        
                        
                        class scoreData(
                            schemas.DictSchema
                        ):
                        
                        
                            class MetaOapg:
                                required = {
                                    "instruments",
                                }
                                
                                class properties:
                                    useTabStaff = schemas.BoolSchema
                                    useChordGrid = schemas.BoolSchema
                                    fifths = schemas.NumberSchema
                                    nbBeats = schemas.NumberSchema
                                    beatType = schemas.NumberSchema
                                    
                                    
                                    class instruments(
                                        schemas.ListSchema
                                    ):
                                    
                                    
                                        class MetaOapg:
                                            
                                            
                                            class items(
                                                schemas.DictSchema
                                            ):
                                            
                                            
                                                class MetaOapg:
                                                    required = {
                                                        "instrument",
                                                        "group",
                                                    }
                                                    
                                                    class properties:
                                                        group = schemas.StrSchema
                                                        instrument = schemas.StrSchema
                                                        longName = schemas.StrSchema
                                                        shortName = schemas.StrSchema
                                                        hasQuarterTone = schemas.BoolSchema
                                                        __annotations__ = {
                                                            "group": group,
                                                            "instrument": instrument,
                                                            "longName": longName,
                                                            "shortName": shortName,
                                                            "hasQuarterTone": hasQuarterTone,
                                                        }
                                                
                                                instrument: MetaOapg.properties.instrument
                                                group: MetaOapg.properties.group
                                                
                                                @typing.overload
                                                def __getitem__(self, name: typing_extensions.Literal["group"]) -> MetaOapg.properties.group: ...
                                                
                                                @typing.overload
                                                def __getitem__(self, name: typing_extensions.Literal["instrument"]) -> MetaOapg.properties.instrument: ...
                                                
                                                @typing.overload
                                                def __getitem__(self, name: typing_extensions.Literal["longName"]) -> MetaOapg.properties.longName: ...
                                                
                                                @typing.overload
                                                def __getitem__(self, name: typing_extensions.Literal["shortName"]) -> MetaOapg.properties.shortName: ...
                                                
                                                @typing.overload
                                                def __getitem__(self, name: typing_extensions.Literal["hasQuarterTone"]) -> MetaOapg.properties.hasQuarterTone: ...
                                                
                                                @typing.overload
                                                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                                
                                                def __getitem__(self, name: typing.Union[typing_extensions.Literal["group", "instrument", "longName", "shortName", "hasQuarterTone", ], str]):
                                                    # dict_instance[name] accessor
                                                    return super().__getitem__(name)
                                                
                                                
                                                @typing.overload
                                                def get_item_oapg(self, name: typing_extensions.Literal["group"]) -> MetaOapg.properties.group: ...
                                                
                                                @typing.overload
                                                def get_item_oapg(self, name: typing_extensions.Literal["instrument"]) -> MetaOapg.properties.instrument: ...
                                                
                                                @typing.overload
                                                def get_item_oapg(self, name: typing_extensions.Literal["longName"]) -> typing.Union[MetaOapg.properties.longName, schemas.Unset]: ...
                                                
                                                @typing.overload
                                                def get_item_oapg(self, name: typing_extensions.Literal["shortName"]) -> typing.Union[MetaOapg.properties.shortName, schemas.Unset]: ...
                                                
                                                @typing.overload
                                                def get_item_oapg(self, name: typing_extensions.Literal["hasQuarterTone"]) -> typing.Union[MetaOapg.properties.hasQuarterTone, schemas.Unset]: ...
                                                
                                                @typing.overload
                                                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                                
                                                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["group", "instrument", "longName", "shortName", "hasQuarterTone", ], str]):
                                                    return super().get_item_oapg(name)
                                                
                                            
                                                def __new__(
                                                    cls,
                                                    *_args: typing.Union[dict, frozendict.frozendict, ],
                                                    instrument: typing.Union[MetaOapg.properties.instrument, str, ],
                                                    group: typing.Union[MetaOapg.properties.group, str, ],
                                                    longName: typing.Union[MetaOapg.properties.longName, str, schemas.Unset] = schemas.unset,
                                                    shortName: typing.Union[MetaOapg.properties.shortName, str, schemas.Unset] = schemas.unset,
                                                    hasQuarterTone: typing.Union[MetaOapg.properties.hasQuarterTone, bool, schemas.Unset] = schemas.unset,
                                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                                ) -> 'items':
                                                    return super().__new__(
                                                        cls,
                                                        *_args,
                                                        instrument=instrument,
                                                        group=group,
                                                        longName=longName,
                                                        shortName=shortName,
                                                        hasQuarterTone=hasQuarterTone,
                                                        _configuration=_configuration,
                                                        **kwargs,
                                                    )
                                    
                                        def __new__(
                                            cls,
                                            _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                                            _configuration: typing.Optional[schemas.Configuration] = None,
                                        ) -> 'instruments':
                                            return super().__new__(
                                                cls,
                                                _arg,
                                                _configuration=_configuration,
                                            )
                                    
                                        def __getitem__(self, i: int) -> MetaOapg.items:
                                            return super().__getitem__(i)
                                    __annotations__ = {
                                        "useTabStaff": useTabStaff,
                                        "useChordGrid": useChordGrid,
                                        "fifths": fifths,
                                        "nbBeats": nbBeats,
                                        "beatType": beatType,
                                        "instruments": instruments,
                                    }
                            
                            instruments: MetaOapg.properties.instruments
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["useTabStaff"]) -> MetaOapg.properties.useTabStaff: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["useChordGrid"]) -> MetaOapg.properties.useChordGrid: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["fifths"]) -> MetaOapg.properties.fifths: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["nbBeats"]) -> MetaOapg.properties.nbBeats: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["beatType"]) -> MetaOapg.properties.beatType: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["instruments"]) -> MetaOapg.properties.instruments: ...
                            
                            @typing.overload
                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                            
                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["useTabStaff", "useChordGrid", "fifths", "nbBeats", "beatType", "instruments", ], str]):
                                # dict_instance[name] accessor
                                return super().__getitem__(name)
                            
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["useTabStaff"]) -> typing.Union[MetaOapg.properties.useTabStaff, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["useChordGrid"]) -> typing.Union[MetaOapg.properties.useChordGrid, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["fifths"]) -> typing.Union[MetaOapg.properties.fifths, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["nbBeats"]) -> typing.Union[MetaOapg.properties.nbBeats, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["beatType"]) -> typing.Union[MetaOapg.properties.beatType, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["instruments"]) -> MetaOapg.properties.instruments: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                            
                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["useTabStaff", "useChordGrid", "fifths", "nbBeats", "beatType", "instruments", ], str]):
                                return super().get_item_oapg(name)
                            
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[dict, frozendict.frozendict, ],
                                instruments: typing.Union[MetaOapg.properties.instruments, list, tuple, ],
                                useTabStaff: typing.Union[MetaOapg.properties.useTabStaff, bool, schemas.Unset] = schemas.unset,
                                useChordGrid: typing.Union[MetaOapg.properties.useChordGrid, bool, schemas.Unset] = schemas.unset,
                                fifths: typing.Union[MetaOapg.properties.fifths, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                                nbBeats: typing.Union[MetaOapg.properties.nbBeats, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                                beatType: typing.Union[MetaOapg.properties.beatType, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> 'scoreData':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    instruments=instruments,
                                    useTabStaff=useTabStaff,
                                    useChordGrid=useChordGrid,
                                    fifths=fifths,
                                    nbBeats=nbBeats,
                                    beatType=beatType,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        
                        
                        class layoutData(
                            schemas.DictSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                class properties:
                                    notesSpacingCoeff = schemas.NumberSchema
                                    
                                    
                                    class lengthUnit(
                                        schemas.EnumBase,
                                        schemas.StrSchema
                                    ):
                                    
                                    
                                        class MetaOapg:
                                            enum_value_to_name = {
                                                "cm": "CM",
                                                "inch": "INCH",
                                            }
                                        
                                        @schemas.classproperty
                                        def CM(cls):
                                            return cls("cm")
                                        
                                        @schemas.classproperty
                                        def INCH(cls):
                                            return cls("inch")
                                    pageHeight = schemas.NumberSchema
                                    pageWidth = schemas.NumberSchema
                                    pageMarginTop = schemas.NumberSchema
                                    pageMarginBottom = schemas.NumberSchema
                                    pageMarginLeft = schemas.NumberSchema
                                    pageMarginRight = schemas.NumberSchema
                                    __annotations__ = {
                                        "notesSpacingCoeff": notesSpacingCoeff,
                                        "lengthUnit": lengthUnit,
                                        "pageHeight": pageHeight,
                                        "pageWidth": pageWidth,
                                        "pageMarginTop": pageMarginTop,
                                        "pageMarginBottom": pageMarginBottom,
                                        "pageMarginLeft": pageMarginLeft,
                                        "pageMarginRight": pageMarginRight,
                                    }
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["notesSpacingCoeff"]) -> MetaOapg.properties.notesSpacingCoeff: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["lengthUnit"]) -> MetaOapg.properties.lengthUnit: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["pageHeight"]) -> MetaOapg.properties.pageHeight: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["pageWidth"]) -> MetaOapg.properties.pageWidth: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["pageMarginTop"]) -> MetaOapg.properties.pageMarginTop: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["pageMarginBottom"]) -> MetaOapg.properties.pageMarginBottom: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["pageMarginLeft"]) -> MetaOapg.properties.pageMarginLeft: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["pageMarginRight"]) -> MetaOapg.properties.pageMarginRight: ...
                            
                            @typing.overload
                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                            
                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["notesSpacingCoeff", "lengthUnit", "pageHeight", "pageWidth", "pageMarginTop", "pageMarginBottom", "pageMarginLeft", "pageMarginRight", ], str]):
                                # dict_instance[name] accessor
                                return super().__getitem__(name)
                            
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["notesSpacingCoeff"]) -> typing.Union[MetaOapg.properties.notesSpacingCoeff, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["lengthUnit"]) -> typing.Union[MetaOapg.properties.lengthUnit, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["pageHeight"]) -> typing.Union[MetaOapg.properties.pageHeight, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["pageWidth"]) -> typing.Union[MetaOapg.properties.pageWidth, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["pageMarginTop"]) -> typing.Union[MetaOapg.properties.pageMarginTop, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["pageMarginBottom"]) -> typing.Union[MetaOapg.properties.pageMarginBottom, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["pageMarginLeft"]) -> typing.Union[MetaOapg.properties.pageMarginLeft, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["pageMarginRight"]) -> typing.Union[MetaOapg.properties.pageMarginRight, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                            
                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["notesSpacingCoeff", "lengthUnit", "pageHeight", "pageWidth", "pageMarginTop", "pageMarginBottom", "pageMarginLeft", "pageMarginRight", ], str]):
                                return super().get_item_oapg(name)
                            
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[dict, frozendict.frozendict, ],
                                notesSpacingCoeff: typing.Union[MetaOapg.properties.notesSpacingCoeff, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                                lengthUnit: typing.Union[MetaOapg.properties.lengthUnit, str, schemas.Unset] = schemas.unset,
                                pageHeight: typing.Union[MetaOapg.properties.pageHeight, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                                pageWidth: typing.Union[MetaOapg.properties.pageWidth, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                                pageMarginTop: typing.Union[MetaOapg.properties.pageMarginTop, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                                pageMarginBottom: typing.Union[MetaOapg.properties.pageMarginBottom, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                                pageMarginLeft: typing.Union[MetaOapg.properties.pageMarginLeft, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                                pageMarginRight: typing.Union[MetaOapg.properties.pageMarginRight, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> 'layoutData':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    notesSpacingCoeff=notesSpacingCoeff,
                                    lengthUnit=lengthUnit,
                                    pageHeight=pageHeight,
                                    pageWidth=pageWidth,
                                    pageMarginTop=pageMarginTop,
                                    pageMarginBottom=pageMarginBottom,
                                    pageMarginLeft=pageMarginLeft,
                                    pageMarginRight=pageMarginRight,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        __annotations__ = {
                            "scoreData": scoreData,
                            "layoutData": layoutData,
                        }
                
                scoreData: MetaOapg.properties.scoreData
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["scoreData"]) -> MetaOapg.properties.scoreData: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["layoutData"]) -> MetaOapg.properties.layoutData: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["scoreData", "layoutData", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["scoreData"]) -> MetaOapg.properties.scoreData: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["layoutData"]) -> typing.Union[MetaOapg.properties.layoutData, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["scoreData", "layoutData", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    scoreData: typing.Union[MetaOapg.properties.scoreData, dict, frozendict.frozendict, ],
                    layoutData: typing.Union[MetaOapg.properties.layoutData, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'builderData':
                    return super().__new__(
                        cls,
                        *_args,
                        scoreData=scoreData,
                        layoutData=layoutData,
                        _configuration=_configuration,
                        **kwargs,
                    )
            filename = schemas.StrSchema
            data = schemas.StrSchema
            
            
            class dataEncoding(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "base64": "BASE64",
                    }
                
                @schemas.classproperty
                def BASE64(cls):
                    return cls("base64")
        
            @staticmethod
            def source() -> typing.Type['ScoreSource']:
                return ScoreSource
            __annotations__ = {
                "title": title,
                "privacy": privacy,
                "collection": collection,
                "googleDriveFolder": googleDriveFolder,
                "builderData": builderData,
                "filename": filename,
                "data": data,
                "dataEncoding": dataEncoding,
                "source": source,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["privacy"]) -> 'ScorePrivacy': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["collection"]) -> MetaOapg.properties.collection: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["googleDriveFolder"]) -> MetaOapg.properties.googleDriveFolder: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["builderData"]) -> MetaOapg.properties.builderData: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filename"]) -> MetaOapg.properties.filename: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dataEncoding"]) -> MetaOapg.properties.dataEncoding: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source"]) -> 'ScoreSource': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "privacy", "collection", "googleDriveFolder", "builderData", "filename", "data", "dataEncoding", "source", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["privacy"]) -> typing.Union['ScorePrivacy', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["collection"]) -> typing.Union[MetaOapg.properties.collection, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["googleDriveFolder"]) -> typing.Union[MetaOapg.properties.googleDriveFolder, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["builderData"]) -> typing.Union[MetaOapg.properties.builderData, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filename"]) -> typing.Union[MetaOapg.properties.filename, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> typing.Union[MetaOapg.properties.data, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dataEncoding"]) -> typing.Union[MetaOapg.properties.dataEncoding, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source"]) -> typing.Union['ScoreSource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "privacy", "collection", "googleDriveFolder", "builderData", "filename", "data", "dataEncoding", "source", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        privacy: typing.Union['ScorePrivacy', schemas.Unset] = schemas.unset,
        collection: typing.Union[MetaOapg.properties.collection, str, schemas.Unset] = schemas.unset,
        googleDriveFolder: typing.Union[MetaOapg.properties.googleDriveFolder, str, schemas.Unset] = schemas.unset,
        builderData: typing.Union[MetaOapg.properties.builderData, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        filename: typing.Union[MetaOapg.properties.filename, str, schemas.Unset] = schemas.unset,
        data: typing.Union[MetaOapg.properties.data, str, schemas.Unset] = schemas.unset,
        dataEncoding: typing.Union[MetaOapg.properties.dataEncoding, str, schemas.Unset] = schemas.unset,
        source: typing.Union['ScoreSource', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ScoreCreation':
        return super().__new__(
            cls,
            *_args,
            title=title,
            privacy=privacy,
            collection=collection,
            googleDriveFolder=googleDriveFolder,
            builderData=builderData,
            filename=filename,
            data=data,
            dataEncoding=dataEncoding,
            source=source,
            _configuration=_configuration,
            **kwargs,
        )

from flat_api.model.score_privacy import ScorePrivacy
from flat_api.model.score_source import ScoreSource