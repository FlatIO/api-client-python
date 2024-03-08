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

from pydantic import BaseModel, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from flat_api.models.score_creation_type import ScoreCreationType
from flat_api.models.score_license import ScoreLicense
from flat_api.models.score_privacy import ScorePrivacy
from typing import Optional, Set
from typing_extensions import Self

class ScoreModification(BaseModel):
    """
    Edit the score metadata
    """ # noqa: E501
    title: Optional[StrictStr] = Field(default=None, description="The title of the score")
    subtitle: Optional[StrictStr] = Field(default=None, description="The subtitle of the score")
    composer: Optional[StrictStr] = Field(default=None, description="The composer of the score")
    lyricist: Optional[StrictStr] = Field(default=None, description="The lyricist of the score")
    arranger: Optional[StrictStr] = Field(default=None, description="The arranger of the score")
    privacy: Optional[ScorePrivacy] = None
    sharing_key: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="When using the `privacy` mode `privateLink`, this property can be used to set a custom sharing key, otherwise a new key will be generated.", alias="sharingKey")
    description: Optional[Annotated[str, Field(strict=True, max_length=2000)]] = Field(default=None, description="Description of the creation")
    tags: Optional[List[StrictStr]] = Field(default=None, description="Tags describing the score")
    creation_type: Optional[ScoreCreationType] = Field(default=None, alias="creationType")
    license: Optional[ScoreLicense] = None
    license_text: Optional[StrictStr] = Field(default=None, description="The rights info written on the score", alias="licenseText")
    __properties: ClassVar[List[str]] = ["title", "subtitle", "composer", "lyricist", "arranger", "privacy", "sharingKey", "description", "tags", "creationType", "license", "licenseText"]

    @field_validator('sharing_key')
    def sharing_key_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-f0-9]{128}$", value):
            raise ValueError(r"must validate the regular expression /^[a-f0-9]{128}$/")
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
        """Create an instance of ScoreModification from a JSON string"""
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
        # set to None if subtitle (nullable) is None
        # and model_fields_set contains the field
        if self.subtitle is None and "subtitle" in self.model_fields_set:
            _dict['subtitle'] = None

        # set to None if composer (nullable) is None
        # and model_fields_set contains the field
        if self.composer is None and "composer" in self.model_fields_set:
            _dict['composer'] = None

        # set to None if lyricist (nullable) is None
        # and model_fields_set contains the field
        if self.lyricist is None and "lyricist" in self.model_fields_set:
            _dict['lyricist'] = None

        # set to None if arranger (nullable) is None
        # and model_fields_set contains the field
        if self.arranger is None and "arranger" in self.model_fields_set:
            _dict['arranger'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if creation_type (nullable) is None
        # and model_fields_set contains the field
        if self.creation_type is None and "creation_type" in self.model_fields_set:
            _dict['creationType'] = None

        # set to None if license (nullable) is None
        # and model_fields_set contains the field
        if self.license is None and "license" in self.model_fields_set:
            _dict['license'] = None

        # set to None if license_text (nullable) is None
        # and model_fields_set contains the field
        if self.license_text is None and "license_text" in self.model_fields_set:
            _dict['licenseText'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ScoreModification from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "title": obj.get("title"),
            "subtitle": obj.get("subtitle"),
            "composer": obj.get("composer"),
            "lyricist": obj.get("lyricist"),
            "arranger": obj.get("arranger"),
            "privacy": obj.get("privacy"),
            "sharingKey": obj.get("sharingKey"),
            "description": obj.get("description"),
            "tags": obj.get("tags"),
            "creationType": obj.get("creationType"),
            "license": obj.get("license"),
            "licenseText": obj.get("licenseText")
        })
        return _obj

