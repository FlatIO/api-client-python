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

from datetime import datetime
from pydantic import BaseModel, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from flat_api.models.group import Group
from flat_api.models.user_public import UserPublic
from typing import Optional, Set
from typing_extensions import Self

class ResourceCollaborator(BaseModel):
    """
    ResourceCollaborator
    """ # noqa: E501
    acl_read: StrictBool = Field(description="`True` if the current user can read the current document ", alias="aclRead")
    acl_write: StrictBool = Field(description="`True` if the current user can modify the current document.  If this is a right of a Collection, the capabilities of the associated user can be lower than this permission, check out the `capabilities` property as the end-user to have the complete possibilities with the collection. ", alias="aclWrite")
    acl_admin: StrictBool = Field(description="`True` if the current user can manage the current document (i.e. share, delete)  If this is a right of a Collection, the capabilities of the associated user can be lower than this permission, check out the `capabilities` property as the end-user to have the complete possibilities with the collection. ", alias="aclAdmin")
    is_collaborator: StrictBool = Field(description="`True` if the current user is a collaborator of the current document (direct or via group). ", alias="isCollaborator")
    collaborator_type: Optional[StrictStr] = Field(default=None, description="The type of the collaborator for the resource ", alias="collaboratorType")
    id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the permission")
    var_date: Optional[datetime] = Field(default=None, description="The date when the permission was added", alias="date")
    score: Optional[StrictStr] = Field(default=None, description="If this object is a permission of a score, this property will contain the unique identifier of the score")
    collection: Optional[StrictStr] = Field(default=None, description="If this object is a permission of a collection, this property will contain the unique identifier of the collection")
    user: Optional[UserPublic] = None
    group: Optional[Group] = None
    user_email: Optional[StrictStr] = Field(default=None, description="If the collaborator is not a user of Flat yet, this field will contain their email. ", alias="userEmail")
    invited: Optional[StrictBool] = Field(default=None, description="If this property is `true`, this is still a pending invitation ")
    __properties: ClassVar[List[str]] = ["aclRead", "aclWrite", "aclAdmin", "isCollaborator", "collaboratorType", "id", "date", "score", "collection", "user", "group", "userEmail", "invited"]

    @field_validator('collaborator_type')
    def collaborator_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['owner', 'user', 'group']):
            raise ValueError("must be one of enum values ('owner', 'user', 'group')")
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
        """Create an instance of ResourceCollaborator from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of group
        if self.group:
            _dict['group'] = self.group.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ResourceCollaborator from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "aclRead": obj.get("aclRead") if obj.get("aclRead") is not None else False,
            "aclWrite": obj.get("aclWrite") if obj.get("aclWrite") is not None else False,
            "aclAdmin": obj.get("aclAdmin") if obj.get("aclAdmin") is not None else False,
            "isCollaborator": obj.get("isCollaborator") if obj.get("isCollaborator") is not None else False,
            "collaboratorType": obj.get("collaboratorType"),
            "id": obj.get("id"),
            "date": obj.get("date"),
            "score": obj.get("score"),
            "collection": obj.get("collection"),
            "user": UserPublic.from_dict(obj["user"]) if obj.get("user") is not None else None,
            "group": Group.from_dict(obj["group"]) if obj.get("group") is not None else None,
            "userEmail": obj.get("userEmail"),
            "invited": obj.get("invited")
        })
        return _obj

