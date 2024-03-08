# coding: utf-8

"""
    Flat API

    The Flat API allows you to easily extend the abilities of the [Flat Platform](https://flat.io), with a wide range of use cases including the following:  * Creating and importing new music scores using MusicXML, MIDI, Guitar Pro (GP3, GP4, GP5, GPX, GP), PowerTab, TuxGuitar and MuseScore files * Browsing, updating, copying, exporting the user's scores (for example in MP3, WAV or MIDI) * Managing educational resources with Flat for Education: creating & updating the organization accounts, the classes, rosters and assignments.  The Flat API is built on HTTP. Our API is RESTful It has predictable resource URLs. It returns HTTP response codes to indicate errors. It also accepts and returns JSON in the HTTP body. The [schema](/swagger.yaml) of this API follows the [OpenAPI Initiative (OAI) specification](https://www.openapis.org/), you can use and work with [compatible Swagger tools](http://swagger.io/open-source-integrations/). This API features Cross-Origin Resource Sharing (CORS) implemented in compliance with [W3C spec](https://www.w3.org/TR/cors/).  You can use your favorite HTTP/REST library for your programming language to use Flat's API. This specification and reference is [available on Github](https://github.com/FlatIO/api-reference).  Getting Started and learn more:  * [API Overview and introduction](https://flat.io/developers/docs/api/) * [Authentication (Personal Access Tokens or OAuth2)](https://flat.io/developers/docs/api/authentication.html) * [SDKs](https://flat.io/developers/docs/api/sdks.html) * [Rate Limits](https://flat.io/developers/docs/api/rate-limits.html) * [Changelog](https://flat.io/developers/docs/api/changelog.html) 

    The version of the OpenAPI document: 2.20.0
    Contact: developers@flat.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flat_api.models.class_assignment import ClassAssignment

class TestClassAssignment(unittest.TestCase):
    """ClassAssignment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClassAssignment:
        """Test ClassAssignment
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClassAssignment`
        """
        model = ClassAssignment()
        if include_optional:
            return ClassAssignment(
                id = '',
                type = 'none',
                capabilities = flat_api.models.assignment_copy_response_capabilities.AssignmentCopyResponse_capabilities(
                    can_edit = True, 
                    can_publish_in_class = True, 
                    can_publish_in_class_error = flat_api.models.assignment_copy_response_capabilities_can_publish_in_class_error.AssignmentCopyResponse_capabilities_canPublishInClassError(
                        code = '', 
                        message = '', ), 
                    can_archive = True, 
                    can_unarchive = True, ),
                title = '',
                description = '',
                cover = '',
                cover_file = '',
                attachments = [
                    {"type":"video","url":"https://www.youtube.com/watch?v=SNbRUiBZ4Uw","title":"Flat - The online collaborative music notation software","description":"Discover Flat on https://flat.io","html":"<iframe width=\"560\" height=\"315\" src=\"https://www.youtube.com/embed/SNbRUiBZ4Uw\" frameborder=\"0\" allowfullscreen></iframe>","thumbnailUrl":"https://i.ytimg.com/vi/SNbRUiBZ4Uw/maxresdefault.jpg","thumbnailHeight":1052,"thumbnailWidth":1868,"authorName":"Flat","authorUrl":"https://www.youtube.com/channel/UCEUIbEP9Rba_g0r4eeGhmXw"}
                    ],
                use_dedicated_attachments = True,
                max_points = 1.337,
                release_grades = 'auto',
                shuffle_exercises = True,
                toolset = '',
                nb_playback_authorized = 1.337,
                creator = '',
                state = 'draft',
                classroom = '',
                creation_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                scheduled_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                assignee_mode = 'everyone',
                assigned_students = [
                    ''
                    ],
                submissions = [
                    {"id":"58c4955c226ffff257211a90","classroom":"58c4725345cd836264f0b29e","assignment":"58c49068524c03ec576ca43c","creator":"559eb5c7f0d4d5e46d03781d","creationDate":"2020-08-12T00:25:00.748000Z","submissionDate":"2020-08-12T00:45:22.748000Z","attachments":[{"type":"flat","score":"58c4955a226ffff257211a8d","title":"Hello - Student"}],"returnDate":"2020-08-15T00:25:00.748000Z","returnCreator":"559eb5c7f0d4d5e46d000000","grade":80,"draftGrade":82,"googleClassroom":{"id":"CgsI-00000000000","state":"turned_in","alternateLink":"http://classroom.google.com/c/music-theory/a/first-assignment/submissions/student/my-submission"}}
                    ],
                google_classroom = {"id":"1235665432","state":"draft","alternateLink":"http://classroom.google.com/c/music-theory/a/first-assignment/detail"},
                microsoft_graph = {"id":"8e460d32-d2d4-46b3-8e1a-9b7677a48fda","state":"draft","alternateLink":"https://teams.microsoft.com/l/entity","categories":["0a012acd-6e78-4cd0-89a9-80d296e48f82"]},
                mfc = flat_api.models.class_assignment_mfc.ClassAssignment_mfc(
                    id = '', 
                    alternate_link = '', ),
                canvas = flat_api.models.class_assignment_canvas.ClassAssignment_canvas(
                    id = '', 
                    alternate_link = '', ),
                lti = flat_api.models.class_assignment_lti.ClassAssignment_lti(
                    id = '', ),
                issue = ''
            )
        else:
            return ClassAssignment(
                id = '',
                type = 'none',
                capabilities = flat_api.models.assignment_copy_response_capabilities.AssignmentCopyResponse_capabilities(
                    can_edit = True, 
                    can_publish_in_class = True, 
                    can_publish_in_class_error = flat_api.models.assignment_copy_response_capabilities_can_publish_in_class_error.AssignmentCopyResponse_capabilities_canPublishInClassError(
                        code = '', 
                        message = '', ), 
                    can_archive = True, 
                    can_unarchive = True, ),
                title = '',
                attachments = [
                    {"type":"video","url":"https://www.youtube.com/watch?v=SNbRUiBZ4Uw","title":"Flat - The online collaborative music notation software","description":"Discover Flat on https://flat.io","html":"<iframe width=\"560\" height=\"315\" src=\"https://www.youtube.com/embed/SNbRUiBZ4Uw\" frameborder=\"0\" allowfullscreen></iframe>","thumbnailUrl":"https://i.ytimg.com/vi/SNbRUiBZ4Uw/maxresdefault.jpg","thumbnailHeight":1052,"thumbnailWidth":1868,"authorName":"Flat","authorUrl":"https://www.youtube.com/channel/UCEUIbEP9Rba_g0r4eeGhmXw"}
                    ],
        )
        """

    def testClassAssignment(self):
        """Test ClassAssignment"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
