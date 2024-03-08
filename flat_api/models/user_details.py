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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from flat_api.models.class_roles import ClassRoles
from flat_api.models.flat_locales import FlatLocales
from flat_api.models.organization_roles import OrganizationRoles
from flat_api.models.tutteo_product import TutteoProduct
from flat_api.models.user_azure_details import UserAzureDetails
from flat_api.models.user_community_profile_links import UserCommunityProfileLinks
from typing import Optional, Set
from typing_extensions import Self

class UserDetails(BaseModel):
    """
    UserDetails
    """ # noqa: E501
    id: StrictStr = Field(description="The user unique identifier")
    type: StrictStr = Field(description="The type of user account")
    product: TutteoProduct
    username: StrictStr = Field(description="The user name (unique for the organization)")
    printable_name: Optional[StrictStr] = Field(default=None, description="The name that can be directly printed (name, firstname & lastname, or username)", alias="printableName")
    firstname: Optional[StrictStr] = Field(default=None, description="Firstname of the user (for education users)")
    lastname: Optional[StrictStr] = Field(default=None, description="Lastname of the user (for education users)")
    name: Optional[StrictStr] = Field(default=None, description="A displayable name for the user (for consumer users)")
    picture: Optional[StrictStr] = Field(description="The URL of the picture to display")
    badges: Optional[List[StrictStr]] = Field(default=None, description="List of badges for the user profile:  - `power` - `staff` - `composerOfTheMonth` - `ambassador` - `challenge` ")
    organization: Optional[StrictStr] = Field(default=None, description="Organization ID (for Edu users only)")
    organization_role: Optional[OrganizationRoles] = Field(default=None, alias="organizationRole")
    class_role: Optional[ClassRoles] = Field(default=None, alias="classRole")
    html_url: Optional[StrictStr] = Field(default=None, description="Link to user profile (for Indiv. users only)", alias="htmlUrl")
    bio: Optional[StrictStr] = Field(default=None, description="User's biography")
    registration_date: Optional[datetime] = Field(default=None, description="Date the user signed up", alias="registrationDate")
    liked_scores_count: Optional[StrictInt] = Field(default=None, description="Number of the scores liked by the user", alias="likedScoresCount")
    followers_count: Optional[StrictInt] = Field(default=None, description="Number of followers the user have", alias="followersCount")
    following_count: Optional[StrictInt] = Field(default=None, description="Number of people the user follow", alias="followingCount")
    owned_public_scores_count: Optional[StrictInt] = Field(default=None, description="Number of public scores the user have", alias="ownedPublicScoresCount")
    cover_picture: Optional[StrictStr] = Field(default=None, description="Cover picture (backgroud) for the profile", alias="coverPicture")
    profile_theme: Optional[StrictStr] = Field(default=None, description="Theme (background) for the profile", alias="profileTheme")
    instruments: Optional[List[StrictStr]] = Field(default=None, description="An array of the instrument identifiers. The format of the strings is `{instrument-group}.{instrument-id}`. ")
    links: Optional[UserCommunityProfileLinks] = None
    azure_details: Optional[UserAzureDetails] = Field(default=None, alias="azureDetails")
    private_profile: Optional[StrictBool] = Field(default=None, description="Tell either this user profile is private or not (individual accounts only)", alias="privateProfile")
    locale: Optional[FlatLocales] = None
    groups: Optional[List[StrictStr]] = Field(default=None, description="For Flat for Education accounts, list of Group identifiers the user is part of.")
    picture_file: Optional[StrictStr] = Field(default=None, description="The ID of the user profile picture", alias="pictureFile")
    cover_picture_file: Optional[StrictStr] = Field(default=None, description="The ID of the user profile cover picture", alias="coverPictureFile")
    __properties: ClassVar[List[str]] = ["id", "type", "product", "username", "printableName", "firstname", "lastname", "name", "picture", "badges", "organization", "organizationRole", "classRole", "htmlUrl", "bio", "registrationDate", "likedScoresCount", "followersCount", "followingCount", "ownedPublicScoresCount", "coverPicture", "profileTheme", "instruments", "links", "azureDetails", "privateProfile", "locale", "groups", "pictureFile", "coverPictureFile"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['user', 'guest']):
            raise ValueError("must be one of enum values ('user', 'guest')")
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
        """Create an instance of UserDetails from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of azure_details
        if self.azure_details:
            _dict['azureDetails'] = self.azure_details.to_dict()
        # set to None if picture (nullable) is None
        # and model_fields_set contains the field
        if self.picture is None and "picture" in self.model_fields_set:
            _dict['picture'] = None

        # set to None if cover_picture (nullable) is None
        # and model_fields_set contains the field
        if self.cover_picture is None and "cover_picture" in self.model_fields_set:
            _dict['coverPicture'] = None

        # set to None if picture_file (nullable) is None
        # and model_fields_set contains the field
        if self.picture_file is None and "picture_file" in self.model_fields_set:
            _dict['pictureFile'] = None

        # set to None if cover_picture_file (nullable) is None
        # and model_fields_set contains the field
        if self.cover_picture_file is None and "cover_picture_file" in self.model_fields_set:
            _dict['coverPictureFile'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "product": obj.get("product"),
            "username": obj.get("username"),
            "printableName": obj.get("printableName"),
            "firstname": obj.get("firstname"),
            "lastname": obj.get("lastname"),
            "name": obj.get("name"),
            "picture": obj.get("picture"),
            "badges": obj.get("badges"),
            "organization": obj.get("organization"),
            "organizationRole": obj.get("organizationRole"),
            "classRole": obj.get("classRole"),
            "htmlUrl": obj.get("htmlUrl"),
            "bio": obj.get("bio"),
            "registrationDate": obj.get("registrationDate"),
            "likedScoresCount": obj.get("likedScoresCount"),
            "followersCount": obj.get("followersCount"),
            "followingCount": obj.get("followingCount"),
            "ownedPublicScoresCount": obj.get("ownedPublicScoresCount"),
            "coverPicture": obj.get("coverPicture"),
            "profileTheme": obj.get("profileTheme"),
            "instruments": obj.get("instruments"),
            "links": UserCommunityProfileLinks.from_dict(obj["links"]) if obj.get("links") is not None else None,
            "azureDetails": UserAzureDetails.from_dict(obj["azureDetails"]) if obj.get("azureDetails") is not None else None,
            "privateProfile": obj.get("privateProfile"),
            "locale": obj.get("locale"),
            "groups": obj.get("groups"),
            "pictureFile": obj.get("pictureFile"),
            "coverPictureFile": obj.get("coverPictureFile")
        })
        return _obj


