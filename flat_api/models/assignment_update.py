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

from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from flat_api.models.assignment_type import AssignmentType
from flat_api.models.class_attachment_creation import ClassAttachmentCreation
from typing import Optional, Set
from typing_extensions import Self

class AssignmentUpdate(BaseModel):
    """
    Assignment Resource Editing
    """ # noqa: E501
    type: Optional[AssignmentType] = None
    title: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=1000)]] = Field(default=None, description="Title of the assignment")
    description: Optional[StrictStr] = Field(default=None, description="Description and content of the assignment")
    attachments: Optional[List[ClassAttachmentCreation]] = None
    nb_playback_authorized: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The number of playback authorized on the scores of the assignment.", alias="nbPlaybackAuthorized")
    toolset: Optional[StrictStr] = Field(default=None, description="The id of the toolset to apply to this assignment. The toolset will be copied to the assignment as a dedicated object to prevent unexpected changes when making modifications to the template toolset. This property can be set to null to delete the linked toolset and switch back to all the tools available for this assignment. ")
    cover_file: Optional[StrictStr] = Field(default=None, description="The id of the cover to display", alias="coverFile")
    cover: Optional[StrictStr] = Field(default=None, description="The URL of the cover to display")
    max_points: Optional[Union[Annotated[float, Field(le=10000, strict=True, ge=0)], Annotated[int, Field(le=10000, strict=True, ge=0)]]] = Field(default=None, description="If set, the grading will be enabled for the assignement with this value as the maximum of points ", alias="maxPoints")
    release_grades: Optional[StrictStr] = Field(default=None, description="For worksheets, how grading will work for the assignment: - If set to `auto`, the grades will be automatically released when the student submits the submissions - If set to `manual`, the grades will only be set as `draftGrade` and will be released when the teacher returns the submissions ", alias="releaseGrades")
    shuffle_exercises: Optional[StrictBool] = Field(default=None, description="Mixing worksheets exercises for each student", alias="shuffleExercises")
    __properties: ClassVar[List[str]] = ["type", "title", "description", "attachments", "nbPlaybackAuthorized", "toolset", "coverFile", "cover", "maxPoints", "releaseGrades", "shuffleExercises"]

    @field_validator('release_grades')
    def release_grades_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['auto', 'manual']):
            raise ValueError("must be one of enum values ('auto', 'manual')")
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
        """Create an instance of AssignmentUpdate from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in attachments (list)
        _items = []
        if self.attachments:
            for _item in self.attachments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['attachments'] = _items
        # set to None if nb_playback_authorized (nullable) is None
        # and model_fields_set contains the field
        if self.nb_playback_authorized is None and "nb_playback_authorized" in self.model_fields_set:
            _dict['nbPlaybackAuthorized'] = None

        # set to None if toolset (nullable) is None
        # and model_fields_set contains the field
        if self.toolset is None and "toolset" in self.model_fields_set:
            _dict['toolset'] = None

        # set to None if cover_file (nullable) is None
        # and model_fields_set contains the field
        if self.cover_file is None and "cover_file" in self.model_fields_set:
            _dict['coverFile'] = None

        # set to None if cover (nullable) is None
        # and model_fields_set contains the field
        if self.cover is None and "cover" in self.model_fields_set:
            _dict['cover'] = None

        # set to None if max_points (nullable) is None
        # and model_fields_set contains the field
        if self.max_points is None and "max_points" in self.model_fields_set:
            _dict['maxPoints'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AssignmentUpdate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "title": obj.get("title"),
            "description": obj.get("description"),
            "attachments": [ClassAttachmentCreation.from_dict(_item) for _item in obj["attachments"]] if obj.get("attachments") is not None else None,
            "nbPlaybackAuthorized": obj.get("nbPlaybackAuthorized"),
            "toolset": obj.get("toolset"),
            "coverFile": obj.get("coverFile"),
            "cover": obj.get("cover"),
            "maxPoints": obj.get("maxPoints"),
            "releaseGrades": obj.get("releaseGrades"),
            "shuffleExercises": obj.get("shuffleExercises")
        })
        return _obj

