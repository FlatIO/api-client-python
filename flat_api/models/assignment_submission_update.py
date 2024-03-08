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

from pydantic import BaseModel, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from flat_api.models.class_attachment_creation import ClassAttachmentCreation
from typing import Optional, Set
from typing_extensions import Self

class AssignmentSubmissionUpdate(BaseModel):
    """
    Assignment Submission creation
    """ # noqa: E501
    attachments: Optional[List[ClassAttachmentCreation]] = None
    submit: Optional[StrictBool] = Field(default=None, description="If `true`, the submission will be marked as done")
    draft_grade: Optional[Union[Annotated[float, Field(le=10000, strict=True, ge=0)], Annotated[int, Field(le=10000, strict=True, ge=0)]]] = Field(default=None, description="Optional grade. If unset, no grade was set. This value is only visible by the teacher, and we will be set to `grade` once the teacher returns the submission", alias="draftGrade")
    grade: Optional[Union[Annotated[float, Field(le=10000, strict=True, ge=0)], Annotated[int, Field(le=10000, strict=True, ge=0)]]] = Field(default=None, description="Optional grade. If unset, no grade was set.")
    exercises_ids: Optional[List[StrictStr]] = Field(default=None, description="The ids of exercises when they need to be in a specific order", alias="exercisesIds")
    var_return: Optional[StrictBool] = Field(default=None, description="If `true`, the submission will be marked as done", alias="return")
    __properties: ClassVar[List[str]] = ["attachments", "submit", "draftGrade", "grade", "exercisesIds", "return"]

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
        """Create an instance of AssignmentSubmissionUpdate from a JSON string"""
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
        # set to None if draft_grade (nullable) is None
        # and model_fields_set contains the field
        if self.draft_grade is None and "draft_grade" in self.model_fields_set:
            _dict['draftGrade'] = None

        # set to None if grade (nullable) is None
        # and model_fields_set contains the field
        if self.grade is None and "grade" in self.model_fields_set:
            _dict['grade'] = None

        # set to None if exercises_ids (nullable) is None
        # and model_fields_set contains the field
        if self.exercises_ids is None and "exercises_ids" in self.model_fields_set:
            _dict['exercisesIds'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AssignmentSubmissionUpdate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "attachments": [ClassAttachmentCreation.from_dict(_item) for _item in obj["attachments"]] if obj.get("attachments") is not None else None,
            "submit": obj.get("submit"),
            "draftGrade": obj.get("draftGrade"),
            "grade": obj.get("grade"),
            "exercisesIds": obj.get("exercisesIds"),
            "return": obj.get("return")
        })
        return _obj

