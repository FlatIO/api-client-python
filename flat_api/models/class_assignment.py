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
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from flat_api.models.assignment_copy_response_capabilities import AssignmentCopyResponseCapabilities
from flat_api.models.assignment_submission import AssignmentSubmission
from flat_api.models.assignment_type import AssignmentType
from flat_api.models.class_assignment_canvas import ClassAssignmentCanvas
from flat_api.models.class_assignment_lti import ClassAssignmentLti
from flat_api.models.class_assignment_mfc import ClassAssignmentMfc
from flat_api.models.google_classroom_coursework import GoogleClassroomCoursework
from flat_api.models.media_attachment import MediaAttachment
from flat_api.models.microsoft_graph_assignment import MicrosoftGraphAssignment
from typing import Optional, Set
from typing_extensions import Self

class ClassAssignment(BaseModel):
    """
    ClassAssignment
    """ # noqa: E501
    id: StrictStr = Field(description="Unique identifier of the assignment")
    type: AssignmentType
    capabilities: AssignmentCopyResponseCapabilities
    title: StrictStr = Field(description="Title of the assignment")
    description: Optional[StrictStr] = Field(default=None, description="Description and content of the assignment")
    cover: Optional[StrictStr] = Field(default=None, description="The URL of the cover to display")
    cover_file: Optional[StrictStr] = Field(default=None, description="The id of the cover to display", alias="coverFile")
    attachments: List[MediaAttachment]
    use_dedicated_attachments: Optional[StrictBool] = Field(default=None, description="For all assignments created after 02/2023, all the underlying resources must be dedicated and stored in the assignment. This boolean indicates that this assignment only supports dedicated attachments. ", alias="useDedicatedAttachments")
    max_points: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="If set, the grading will be enabled for the assignement ", alias="maxPoints")
    release_grades: Optional[StrictStr] = Field(default=None, description="For worksheets, how grading will work for the assignment: - If set to `auto`, the grades will be automatically released when the student submits the submissions - If set to `manual`, the grades will only be set as `draftGrade` and will be released when the teacher returns the submissions ", alias="releaseGrades")
    shuffle_exercises: Optional[StrictBool] = Field(default=None, description="Mixing worksheets exercises for each student", alias="shuffleExercises")
    toolset: Optional[StrictStr] = Field(default=None, description="The id of the associated toolset")
    nb_playback_authorized: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The number of playback authorized on the scores of the assignment.", alias="nbPlaybackAuthorized")
    creator: Optional[StrictStr] = Field(default=None, description="The User unique identifier of the creator of this assignment ")
    state: Optional[StrictStr] = Field(default=None, description="State of the assignment")
    classroom: Optional[StrictStr] = Field(default=None, description="The unique identifier of the class where this assignment was posted")
    creation_date: Optional[datetime] = Field(default=None, description="The creation date of this assignment", alias="creationDate")
    scheduled_date: Optional[datetime] = Field(default=None, description="The publication (scheduled) date of the assignment. If this one is specified, the assignment will only be listed to the teachers of the class. ", alias="scheduledDate")
    due_date: Optional[datetime] = Field(default=None, description="The due date of this assignment, late submissions will be marked as paste due. ", alias="dueDate")
    assignee_mode: Optional[StrictStr] = Field(default=None, description="Possible modes of assigning assignments", alias="assigneeMode")
    assigned_students: Optional[List[StrictStr]] = Field(default=None, description="Identifiers for the students that have access to the assignment", alias="assignedStudents")
    submissions: Optional[List[AssignmentSubmission]] = None
    google_classroom: Optional[GoogleClassroomCoursework] = Field(default=None, alias="googleClassroom")
    microsoft_graph: Optional[MicrosoftGraphAssignment] = Field(default=None, alias="microsoftGraph")
    mfc: Optional[ClassAssignmentMfc] = None
    canvas: Optional[ClassAssignmentCanvas] = None
    lti: Optional[ClassAssignmentLti] = None
    issue: Optional[StrictStr] = Field(default=None, description="Detected issue for this assignment")
    __properties: ClassVar[List[str]] = ["id", "type", "capabilities", "title", "description", "cover", "coverFile", "attachments", "useDedicatedAttachments", "maxPoints", "releaseGrades", "shuffleExercises", "toolset", "nbPlaybackAuthorized", "creator", "state", "classroom", "creationDate", "scheduledDate", "dueDate", "assigneeMode", "assignedStudents", "submissions", "googleClassroom", "microsoftGraph", "mfc", "canvas", "lti", "issue"]

    @field_validator('release_grades')
    def release_grades_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['auto', 'manual']):
            raise ValueError("must be one of enum values ('auto', 'manual')")
        return value

    @field_validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['draft', 'active', 'archived']):
            raise ValueError("must be one of enum values ('draft', 'active', 'archived')")
        return value

    @field_validator('assignee_mode')
    def assignee_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['everyone', 'selected']):
            raise ValueError("must be one of enum values ('everyone', 'selected')")
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
        """Create an instance of ClassAssignment from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of capabilities
        if self.capabilities:
            _dict['capabilities'] = self.capabilities.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in attachments (list)
        _items = []
        if self.attachments:
            for _item in self.attachments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['attachments'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in submissions (list)
        _items = []
        if self.submissions:
            for _item in self.submissions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['submissions'] = _items
        # override the default output from pydantic by calling `to_dict()` of google_classroom
        if self.google_classroom:
            _dict['googleClassroom'] = self.google_classroom.to_dict()
        # override the default output from pydantic by calling `to_dict()` of microsoft_graph
        if self.microsoft_graph:
            _dict['microsoftGraph'] = self.microsoft_graph.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mfc
        if self.mfc:
            _dict['mfc'] = self.mfc.to_dict()
        # override the default output from pydantic by calling `to_dict()` of canvas
        if self.canvas:
            _dict['canvas'] = self.canvas.to_dict()
        # override the default output from pydantic by calling `to_dict()` of lti
        if self.lti:
            _dict['lti'] = self.lti.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClassAssignment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "capabilities": AssignmentCopyResponseCapabilities.from_dict(obj["capabilities"]) if obj.get("capabilities") is not None else None,
            "title": obj.get("title"),
            "description": obj.get("description"),
            "cover": obj.get("cover"),
            "coverFile": obj.get("coverFile"),
            "attachments": [MediaAttachment.from_dict(_item) for _item in obj["attachments"]] if obj.get("attachments") is not None else None,
            "useDedicatedAttachments": obj.get("useDedicatedAttachments"),
            "maxPoints": obj.get("maxPoints"),
            "releaseGrades": obj.get("releaseGrades"),
            "shuffleExercises": obj.get("shuffleExercises"),
            "toolset": obj.get("toolset"),
            "nbPlaybackAuthorized": obj.get("nbPlaybackAuthorized"),
            "creator": obj.get("creator"),
            "state": obj.get("state"),
            "classroom": obj.get("classroom"),
            "creationDate": obj.get("creationDate"),
            "scheduledDate": obj.get("scheduledDate"),
            "dueDate": obj.get("dueDate"),
            "assigneeMode": obj.get("assigneeMode"),
            "assignedStudents": obj.get("assignedStudents"),
            "submissions": [AssignmentSubmission.from_dict(_item) for _item in obj["submissions"]] if obj.get("submissions") is not None else None,
            "googleClassroom": GoogleClassroomCoursework.from_dict(obj["googleClassroom"]) if obj.get("googleClassroom") is not None else None,
            "microsoftGraph": MicrosoftGraphAssignment.from_dict(obj["microsoftGraph"]) if obj.get("microsoftGraph") is not None else None,
            "mfc": ClassAssignmentMfc.from_dict(obj["mfc"]) if obj.get("mfc") is not None else None,
            "canvas": ClassAssignmentCanvas.from_dict(obj["canvas"]) if obj.get("canvas") is not None else None,
            "lti": ClassAssignmentLti.from_dict(obj["lti"]) if obj.get("lti") is not None else None,
            "issue": obj.get("issue")
        })
        return _obj


