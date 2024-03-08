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
from pydantic import BaseModel, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from flat_api.models.collection_app import CollectionApp
from flat_api.models.collection_capabilities import CollectionCapabilities
from flat_api.models.collection_privacy import CollectionPrivacy
from flat_api.models.collection_type import CollectionType
from flat_api.models.resource_collaborator import ResourceCollaborator
from flat_api.models.resource_rights import ResourceRights
from flat_api.models.user_public_summary import UserPublicSummary
from typing import Optional, Set
from typing_extensions import Self

class Collection(BaseModel):
    """
    Collection of scores
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Unique identifier of the collection")
    title: Optional[StrictStr] = Field(default=None, description="The title of the collection")
    html_url: Optional[StrictStr] = Field(default=None, description="The url where the collection can be viewed in a web browser", alias="htmlUrl")
    type: Optional[CollectionType] = None
    privacy: Optional[CollectionPrivacy] = None
    sharing_key: Optional[StrictStr] = Field(default=None, description="The private sharing key of the collection (available when the `privacy` mode is set to `privateLink`)", alias="sharingKey")
    app: Optional[CollectionApp] = None
    creation_date: Optional[datetime] = Field(default=None, description="The date when the collection was created", alias="creationDate")
    user: Optional[UserPublicSummary] = None
    organization: Optional[StrictStr] = Field(default=None, description="If the score has been created in an organization, the identifier of this organization.  ")
    rights: Optional[ResourceRights] = None
    collaborators: Optional[List[ResourceCollaborator]] = Field(default=None, description="The list of the collaborators of the collection")
    capabilities: CollectionCapabilities
    collections: Optional[List[StrictStr]] = Field(default=None, description="The List of parent collections, which includes all the collections this score is included. Please note that you might not have access to all of them.")
    __properties: ClassVar[List[str]] = ["id", "title", "htmlUrl", "type", "privacy", "sharingKey", "app", "creationDate", "user", "organization", "rights", "collaborators", "capabilities", "collections"]

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
        """Create an instance of Collection from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of app
        if self.app:
            _dict['app'] = self.app.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rights
        if self.rights:
            _dict['rights'] = self.rights.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in collaborators (list)
        _items = []
        if self.collaborators:
            for _item in self.collaborators:
                if _item:
                    _items.append(_item.to_dict())
            _dict['collaborators'] = _items
        # override the default output from pydantic by calling `to_dict()` of capabilities
        if self.capabilities:
            _dict['capabilities'] = self.capabilities.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Collection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "title": obj.get("title"),
            "htmlUrl": obj.get("htmlUrl"),
            "type": obj.get("type"),
            "privacy": obj.get("privacy"),
            "sharingKey": obj.get("sharingKey"),
            "app": CollectionApp.from_dict(obj["app"]) if obj.get("app") is not None else None,
            "creationDate": obj.get("creationDate"),
            "user": UserPublicSummary.from_dict(obj["user"]) if obj.get("user") is not None else None,
            "organization": obj.get("organization"),
            "rights": ResourceRights.from_dict(obj["rights"]) if obj.get("rights") is not None else None,
            "collaborators": [ResourceCollaborator.from_dict(_item) for _item in obj["collaborators"]] if obj.get("collaborators") is not None else None,
            "capabilities": CollectionCapabilities.from_dict(obj["capabilities"]) if obj.get("capabilities") is not None else None,
            "collections": obj.get("collections")
        })
        return _obj


