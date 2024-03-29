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

from pydantic import BaseModel, Field, StrictBool
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class CollectionCapabilities(BaseModel):
    """
    Capabilities the current user has on this collection. Each capability corresponds to a fine-grained action that a user may take.
    """ # noqa: E501
    can_edit: StrictBool = Field(description="Whether the current user can modify the metadata for the collection ", alias="canEdit")
    can_share: StrictBool = Field(description="Whether the current user can modify the sharing settings for the collection ", alias="canShare")
    can_delete: StrictBool = Field(description="Whether the current user can delete the collection ", alias="canDelete")
    can_add_scores: StrictBool = Field(description="Whether the current user can add scores to the collection  If this collection has the `type` `trash`, this property will be set to `false`. Use `DELETE /v2/scores/{score}` to trash a score. ", alias="canAddScores")
    can_delete_scores: StrictBool = Field(description="Whether the current user can delete scores from the collection  If this collection has the `type` `trash`, this property will be set to `false`. Use `POST /v2/scores/{score}/untrash` to restore a score. ", alias="canDeleteScores")
    __properties: ClassVar[List[str]] = ["canEdit", "canShare", "canDelete", "canAddScores", "canDeleteScores"]

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
        """Create an instance of CollectionCapabilities from a JSON string"""
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
        """Create an instance of CollectionCapabilities from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "canEdit": obj.get("canEdit"),
            "canShare": obj.get("canShare"),
            "canDelete": obj.get("canDelete"),
            "canAddScores": obj.get("canAddScores"),
            "canDeleteScores": obj.get("canDeleteScores")
        })
        return _obj


