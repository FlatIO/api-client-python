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
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from flat_api.models.class_details_canvas import ClassDetailsCanvas
from flat_api.models.class_details_clever import ClassDetailsClever
from flat_api.models.class_details_google_classroom import ClassDetailsGoogleClassroom
from flat_api.models.class_details_google_drive import ClassDetailsGoogleDrive
from flat_api.models.class_details_issues import ClassDetailsIssues
from flat_api.models.class_details_lti import ClassDetailsLti
from flat_api.models.class_details_mfc import ClassDetailsMfc
from flat_api.models.class_details_microsoft_graph import ClassDetailsMicrosoftGraph
from flat_api.models.class_grade_level import ClassGradeLevel
from flat_api.models.class_state import ClassState
from flat_api.models.group_details import GroupDetails
from typing import Optional, Set
from typing_extensions import Self

class ClassDetails(BaseModel):
    """
    A classroom
    """ # noqa: E501
    id: StrictStr = Field(description="The unique identifier of the class")
    state: Optional[ClassState] = None
    name: Optional[StrictStr] = Field(default=None, description="The name of the class")
    section: Optional[StrictStr] = Field(default=None, description="The section of the class")
    description: Optional[StrictStr] = Field(default=None, description="An optionnal description for this class")
    organization: Optional[StrictStr] = Field(default=None, description="The unique identifier of the Organization owning this class")
    owner: Optional[StrictStr] = Field(default=None, description="The unique identifier of the User owning this class")
    creation_date: Optional[datetime] = Field(default=None, description="The date when the class was create", alias="creationDate")
    enrollment_code: Optional[StrictStr] = Field(default=None, description="[Teachers only] The enrollment code that can be used by the students to join the class ", alias="enrollmentCode")
    theme: Optional[StrictStr] = Field(default=None, description="The theme identifier using in Flat User Interface")
    assignments_count: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The number of assignments created in the class", alias="assignmentsCount")
    students_group: Optional[GroupDetails] = Field(default=None, alias="studentsGroup")
    teachers_group: Optional[GroupDetails] = Field(default=None, alias="teachersGroup")
    issues: Optional[ClassDetailsIssues] = None
    google_classroom: Optional[ClassDetailsGoogleClassroom] = Field(default=None, alias="googleClassroom")
    google_drive: Optional[ClassDetailsGoogleDrive] = Field(default=None, alias="googleDrive")
    microsoft_graph: Optional[ClassDetailsMicrosoftGraph] = Field(default=None, alias="microsoftGraph")
    lti: Optional[ClassDetailsLti] = None
    canvas: Optional[ClassDetailsCanvas] = None
    mfc: Optional[ClassDetailsMfc] = None
    clever: Optional[ClassDetailsClever] = None
    level: Optional[ClassGradeLevel] = None
    skills_focused: Optional[List[StrictStr]] = Field(default=None, description="Specific skills that will be focused in classroom", alias="skillsFocused")
    size: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Number of students in the classroom")
    __properties: ClassVar[List[str]] = ["id", "state", "name", "section", "description", "organization", "owner", "creationDate", "enrollmentCode", "theme", "assignmentsCount", "studentsGroup", "teachersGroup", "issues", "googleClassroom", "googleDrive", "microsoftGraph", "lti", "canvas", "mfc", "clever", "level", "skillsFocused", "size"]

    @field_validator('skills_focused')
    def skills_focused_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['notation', 'sight-reading', 'performance-instrumental', 'ear-training', 'music-theory', 'composition', 'jazz-ensemble', 'music-technology', 'other']):
                raise ValueError("each list item must be one of ('notation', 'sight-reading', 'performance-instrumental', 'ear-training', 'music-theory', 'composition', 'jazz-ensemble', 'music-technology', 'other')")
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
        """Create an instance of ClassDetails from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of students_group
        if self.students_group:
            _dict['studentsGroup'] = self.students_group.to_dict()
        # override the default output from pydantic by calling `to_dict()` of teachers_group
        if self.teachers_group:
            _dict['teachersGroup'] = self.teachers_group.to_dict()
        # override the default output from pydantic by calling `to_dict()` of issues
        if self.issues:
            _dict['issues'] = self.issues.to_dict()
        # override the default output from pydantic by calling `to_dict()` of google_classroom
        if self.google_classroom:
            _dict['googleClassroom'] = self.google_classroom.to_dict()
        # override the default output from pydantic by calling `to_dict()` of google_drive
        if self.google_drive:
            _dict['googleDrive'] = self.google_drive.to_dict()
        # override the default output from pydantic by calling `to_dict()` of microsoft_graph
        if self.microsoft_graph:
            _dict['microsoftGraph'] = self.microsoft_graph.to_dict()
        # override the default output from pydantic by calling `to_dict()` of lti
        if self.lti:
            _dict['lti'] = self.lti.to_dict()
        # override the default output from pydantic by calling `to_dict()` of canvas
        if self.canvas:
            _dict['canvas'] = self.canvas.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mfc
        if self.mfc:
            _dict['mfc'] = self.mfc.to_dict()
        # override the default output from pydantic by calling `to_dict()` of clever
        if self.clever:
            _dict['clever'] = self.clever.to_dict()
        # set to None if size (nullable) is None
        # and model_fields_set contains the field
        if self.size is None and "size" in self.model_fields_set:
            _dict['size'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClassDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "state": obj.get("state"),
            "name": obj.get("name"),
            "section": obj.get("section"),
            "description": obj.get("description"),
            "organization": obj.get("organization"),
            "owner": obj.get("owner"),
            "creationDate": obj.get("creationDate"),
            "enrollmentCode": obj.get("enrollmentCode"),
            "theme": obj.get("theme"),
            "assignmentsCount": obj.get("assignmentsCount"),
            "studentsGroup": GroupDetails.from_dict(obj["studentsGroup"]) if obj.get("studentsGroup") is not None else None,
            "teachersGroup": GroupDetails.from_dict(obj["teachersGroup"]) if obj.get("teachersGroup") is not None else None,
            "issues": ClassDetailsIssues.from_dict(obj["issues"]) if obj.get("issues") is not None else None,
            "googleClassroom": ClassDetailsGoogleClassroom.from_dict(obj["googleClassroom"]) if obj.get("googleClassroom") is not None else None,
            "googleDrive": ClassDetailsGoogleDrive.from_dict(obj["googleDrive"]) if obj.get("googleDrive") is not None else None,
            "microsoftGraph": ClassDetailsMicrosoftGraph.from_dict(obj["microsoftGraph"]) if obj.get("microsoftGraph") is not None else None,
            "lti": ClassDetailsLti.from_dict(obj["lti"]) if obj.get("lti") is not None else None,
            "canvas": ClassDetailsCanvas.from_dict(obj["canvas"]) if obj.get("canvas") is not None else None,
            "mfc": ClassDetailsMfc.from_dict(obj["mfc"]) if obj.get("mfc") is not None else None,
            "clever": ClassDetailsClever.from_dict(obj["clever"]) if obj.get("clever") is not None else None,
            "level": obj.get("level"),
            "skillsFocused": obj.get("skillsFocused"),
            "size": obj.get("size")
        })
        return _obj


