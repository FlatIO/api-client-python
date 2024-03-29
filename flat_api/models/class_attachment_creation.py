# coding: utf-8

"""
    Flat API

    The Flat API allows you to easily extend the abilities of the [Flat Platform](https://flat.io), with a wide range of use cases including the following:  * Creating and importing new music scores using MusicXML, MIDI, Guitar Pro (GP3, GP4, GP5, GPX, GP), PowerTab, TuxGuitar and MuseScore files * Browsing, updating, copying, exporting the user's scores (for example in MP3, WAV or MIDI) * Managing educational resources with Flat for Education: creating & updating the organization accounts, the classes, rosters and assignments.  The Flat API is built on HTTP. Our API is RESTful It has predictable resource URLs. It returns HTTP response codes to indicate errors. It also accepts and returns JSON in the HTTP body. The [schema](/swagger.yaml) of this API follows the [OpenAPI Initiative (OAI) specification](https://www.openapis.org/), you can use and work with [compatible Swagger tools](http://swagger.io/open-source-integrations/). This API features Cross-Origin Resource Sharing (CORS) implemented in compliance with [W3C spec](https://www.w3.org/TR/cors/).  You can use your favorite HTTP/REST library for your programming language to use Flat's API. This specification and reference is [available on Github](https://github.com/FlatIO/api-reference).  Getting Started and learn more:  * [API Overview and introduction](https://flat.io/developers/docs/api/) * [Authentication (Personal Access Tokens or OAuth2)](https://flat.io/developers/docs/api/authentication.html) * [SDKs](https://flat.io/developers/docs/api/sdks.html) * [Rate Limits](https://flat.io/developers/docs/api/rate-limits.html) * [Changelog](https://flat.io/developers/docs/api/changelog.html) 

    The version of the OpenAPI document: 2.20.0
    Contact: developers@flat.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from flat_api.models.media_score_sharing_mode import MediaScoreSharingMode
from typing import Optional, Set
from typing_extensions import Self

class ClassAttachmentCreation(BaseModel):
    """
    Attachment creation for an assignment or stream post. This attachment must contain a `score` or an `url`, all the details of this one will be resolved and returned as `ClassAttachment` once the assignment or stream post is created. 
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="The type of the attachment posted: * `rich`, `photo`, `video` are attachment types that are automatically resolved from a `link` attachment. * A `flat` attachment is a score document where the unique identifier will be specified in the `score` property. Its sharing mode will be provided in the `sharingMode` property. ")
    score: Optional[StrictStr] = Field(default=None, description="A unique Flat score identifier. The user creating the assignment must at least have read access to the document. If the user has admin rights, new group permissions will be automatically added for the teachers and students of the class. ")
    worksheet: Optional[StrictStr] = Field(default=None, description="An unique worksheet identifier")
    sharing_mode: Optional[MediaScoreSharingMode] = Field(default=None, alias="sharingMode")
    lock_score_template: Optional[StrictBool] = Field(default=None, description="To be used with a score attached in `sharingMode` `copy` (score used as template). If true, students won't be able to change the original notes of the template.", alias="lockScoreTemplate")
    url: Optional[StrictStr] = Field(default=None, description="The URL of the attachment.")
    google_drive_file_id: Optional[StrictStr] = Field(default=None, description="The ID of the Google Drive File", alias="googleDriveFileId")
    __properties: ClassVar[List[str]] = ["type", "score", "worksheet", "sharingMode", "lockScoreTemplate", "url", "googleDriveFileId"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['rich', 'photo', 'video', 'link', 'flat', 'googleDrive', 'worksheet', 'performance']):
            raise ValueError("must be one of enum values ('rich', 'photo', 'video', 'link', 'flat', 'googleDrive', 'worksheet', 'performance')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ClassAttachmentCreation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClassAttachmentCreation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "score": obj.get("score"),
            "worksheet": obj.get("worksheet"),
            "sharingMode": obj.get("sharingMode"),
            "lockScoreTemplate": obj.get("lockScoreTemplate"),
            "url": obj.get("url"),
            "googleDriveFileId": obj.get("googleDriveFileId")
        })
        return _obj


