# coding: utf-8

"""
    Flat API

    The Flat API allows you to easily extend the abilities of the [Flat Platform](https://flat.io), with a wide range of use cases including the following:  * Creating and importing new music scores using MusicXML, MIDI, Guitar Pro (GP3, GP4, GP5, GPX, GP), PowerTab, TuxGuitar and MuseScore files * Browsing, updating, copying, exporting the user's scores (for example in MP3, WAV or MIDI) * Managing educational resources with Flat for Education: creating & updating the organization accounts, the classes, rosters and assignments.  The Flat API is built on HTTP. Our API is RESTful It has predictable resource URLs. It returns HTTP response codes to indicate errors. It also accepts and returns JSON in the HTTP body. The [schema](/swagger.yaml) of this API follows the [OpenAPI Initiative (OAI) specification](https://www.openapis.org/), you can use and work with [compatible Swagger tools](http://swagger.io/open-source-integrations/). This API features Cross-Origin Resource Sharing (CORS) implemented in compliance with [W3C spec](https://www.w3.org/TR/cors/).  You can use your favorite HTTP/REST library for your programming language to use Flat's API. This specification and reference is [available on Github](https://github.com/FlatIO/api-reference).  Getting Started and learn more:  * [API Overview and interoduction](https://flat.io/developers/docs/api/) * [Authentication (Personal Access Tokens or OAuth2)](https://flat.io/developers/docs/api/authentication.html) * [SDKs](https://flat.io/developers/docs/api/sdks.html) * [Rate Limits](https://flat.io/developers/docs/api/rate-limits.html) * [Changelog](https://flat.io/developers/docs/api/changelog.html)   # noqa: E501

    OpenAPI spec version: 2.7.0
    Contact: developers@flat.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ScoreDetails(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'subtitle': 'str',
        'lyricist': 'str',
        'composer': 'str',
        'description': 'str',
        'tags': 'list[str]',
        'creation_type': 'ScoreCreationType',
        'license': 'ScoreLicense',
        'license_text': 'str',
        'duration_time': 'int',
        'number_measures': 'int',
        'main_tempo_qpm': 'int',
        'rights': 'ResourceRights',
        'collaborators': 'list[ResourceCollaborator]',
        'creation_date': 'datetime',
        'modification_date': 'datetime',
        'publication_date': 'datetime',
        'organization': 'str',
        'parent_score': 'str',
        'instruments': 'list[str]',
        'google_drive_file_id': 'str',
        'likes': 'ScoreLikesCounts',
        'comments': 'ScoreCommentsCounts',
        'views': 'ScoreViewsCounts',
        'collections': 'list[str]'
    }

    attribute_map = {
        'subtitle': 'subtitle',
        'lyricist': 'lyricist',
        'composer': 'composer',
        'description': 'description',
        'tags': 'tags',
        'creation_type': 'creationType',
        'license': 'license',
        'license_text': 'licenseText',
        'duration_time': 'durationTime',
        'number_measures': 'numberMeasures',
        'main_tempo_qpm': 'mainTempoQpm',
        'rights': 'rights',
        'collaborators': 'collaborators',
        'creation_date': 'creationDate',
        'modification_date': 'modificationDate',
        'publication_date': 'publicationDate',
        'organization': 'organization',
        'parent_score': 'parentScore',
        'instruments': 'instruments',
        'google_drive_file_id': 'googleDriveFileId',
        'likes': 'likes',
        'comments': 'comments',
        'views': 'views',
        'collections': 'collections'
    }

    def __init__(self, subtitle=None, lyricist=None, composer=None, description=None, tags=None, creation_type=None, license=None, license_text=None, duration_time=None, number_measures=None, main_tempo_qpm=None, rights=None, collaborators=None, creation_date=None, modification_date=None, publication_date=None, organization=None, parent_score=None, instruments=None, google_drive_file_id=None, likes=None, comments=None, views=None, collections=None):  # noqa: E501
        """ScoreDetails - a model defined in OpenAPI"""  # noqa: E501

        self._subtitle = None
        self._lyricist = None
        self._composer = None
        self._description = None
        self._tags = None
        self._creation_type = None
        self._license = None
        self._license_text = None
        self._duration_time = None
        self._number_measures = None
        self._main_tempo_qpm = None
        self._rights = None
        self._collaborators = None
        self._creation_date = None
        self._modification_date = None
        self._publication_date = None
        self._organization = None
        self._parent_score = None
        self._instruments = None
        self._google_drive_file_id = None
        self._likes = None
        self._comments = None
        self._views = None
        self._collections = None
        self.discriminator = None

        if subtitle is not None:
            self.subtitle = subtitle
        if lyricist is not None:
            self.lyricist = lyricist
        if composer is not None:
            self.composer = composer
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if creation_type is not None:
            self.creation_type = creation_type
        if license is not None:
            self.license = license
        if license_text is not None:
            self.license_text = license_text
        if duration_time is not None:
            self.duration_time = duration_time
        if number_measures is not None:
            self.number_measures = number_measures
        if main_tempo_qpm is not None:
            self.main_tempo_qpm = main_tempo_qpm
        if rights is not None:
            self.rights = rights
        if collaborators is not None:
            self.collaborators = collaborators
        if creation_date is not None:
            self.creation_date = creation_date
        if modification_date is not None:
            self.modification_date = modification_date
        if publication_date is not None:
            self.publication_date = publication_date
        if organization is not None:
            self.organization = organization
        if parent_score is not None:
            self.parent_score = parent_score
        if instruments is not None:
            self.instruments = instruments
        if google_drive_file_id is not None:
            self.google_drive_file_id = google_drive_file_id
        if likes is not None:
            self.likes = likes
        if comments is not None:
            self.comments = comments
        if views is not None:
            self.views = views
        if collections is not None:
            self.collections = collections

    @property
    def subtitle(self):
        """Gets the subtitle of this ScoreDetails.  # noqa: E501

        Subtitle of the score  # noqa: E501

        :return: The subtitle of this ScoreDetails.  # noqa: E501
        :rtype: str
        """
        return self._subtitle

    @subtitle.setter
    def subtitle(self, subtitle):
        """Sets the subtitle of this ScoreDetails.

        Subtitle of the score  # noqa: E501

        :param subtitle: The subtitle of this ScoreDetails.  # noqa: E501
        :type: str
        """

        self._subtitle = subtitle

    @property
    def lyricist(self):
        """Gets the lyricist of this ScoreDetails.  # noqa: E501

        Lyricist of the score  # noqa: E501

        :return: The lyricist of this ScoreDetails.  # noqa: E501
        :rtype: str
        """
        return self._lyricist

    @lyricist.setter
    def lyricist(self, lyricist):
        """Sets the lyricist of this ScoreDetails.

        Lyricist of the score  # noqa: E501

        :param lyricist: The lyricist of this ScoreDetails.  # noqa: E501
        :type: str
        """

        self._lyricist = lyricist

    @property
    def composer(self):
        """Gets the composer of this ScoreDetails.  # noqa: E501

        Composer of the score  # noqa: E501

        :return: The composer of this ScoreDetails.  # noqa: E501
        :rtype: str
        """
        return self._composer

    @composer.setter
    def composer(self, composer):
        """Sets the composer of this ScoreDetails.

        Composer of the score  # noqa: E501

        :param composer: The composer of this ScoreDetails.  # noqa: E501
        :type: str
        """

        self._composer = composer

    @property
    def description(self):
        """Gets the description of this ScoreDetails.  # noqa: E501

        Description of the creation  # noqa: E501

        :return: The description of this ScoreDetails.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ScoreDetails.

        Description of the creation  # noqa: E501

        :param description: The description of this ScoreDetails.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this ScoreDetails.  # noqa: E501

        Tags describing the score  # noqa: E501

        :return: The tags of this ScoreDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ScoreDetails.

        Tags describing the score  # noqa: E501

        :param tags: The tags of this ScoreDetails.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def creation_type(self):
        """Gets the creation_type of this ScoreDetails.  # noqa: E501


        :return: The creation_type of this ScoreDetails.  # noqa: E501
        :rtype: ScoreCreationType
        """
        return self._creation_type

    @creation_type.setter
    def creation_type(self, creation_type):
        """Sets the creation_type of this ScoreDetails.


        :param creation_type: The creation_type of this ScoreDetails.  # noqa: E501
        :type: ScoreCreationType
        """

        self._creation_type = creation_type

    @property
    def license(self):
        """Gets the license of this ScoreDetails.  # noqa: E501


        :return: The license of this ScoreDetails.  # noqa: E501
        :rtype: ScoreLicense
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this ScoreDetails.


        :param license: The license of this ScoreDetails.  # noqa: E501
        :type: ScoreLicense
        """

        self._license = license

    @property
    def license_text(self):
        """Gets the license_text of this ScoreDetails.  # noqa: E501

        Additional license text written on the exported/printed score  # noqa: E501

        :return: The license_text of this ScoreDetails.  # noqa: E501
        :rtype: str
        """
        return self._license_text

    @license_text.setter
    def license_text(self, license_text):
        """Sets the license_text of this ScoreDetails.

        Additional license text written on the exported/printed score  # noqa: E501

        :param license_text: The license_text of this ScoreDetails.  # noqa: E501
        :type: str
        """

        self._license_text = license_text

    @property
    def duration_time(self):
        """Gets the duration_time of this ScoreDetails.  # noqa: E501

        In seconds, an approximative duration of the score  # noqa: E501

        :return: The duration_time of this ScoreDetails.  # noqa: E501
        :rtype: int
        """
        return self._duration_time

    @duration_time.setter
    def duration_time(self, duration_time):
        """Sets the duration_time of this ScoreDetails.

        In seconds, an approximative duration of the score  # noqa: E501

        :param duration_time: The duration_time of this ScoreDetails.  # noqa: E501
        :type: int
        """

        self._duration_time = duration_time

    @property
    def number_measures(self):
        """Gets the number_measures of this ScoreDetails.  # noqa: E501

        The number of measures in the score  # noqa: E501

        :return: The number_measures of this ScoreDetails.  # noqa: E501
        :rtype: int
        """
        return self._number_measures

    @number_measures.setter
    def number_measures(self, number_measures):
        """Sets the number_measures of this ScoreDetails.

        The number of measures in the score  # noqa: E501

        :param number_measures: The number_measures of this ScoreDetails.  # noqa: E501
        :type: int
        """

        self._number_measures = number_measures

    @property
    def main_tempo_qpm(self):
        """Gets the main_tempo_qpm of this ScoreDetails.  # noqa: E501

        The main tempo of the score (in QPM)  # noqa: E501

        :return: The main_tempo_qpm of this ScoreDetails.  # noqa: E501
        :rtype: int
        """
        return self._main_tempo_qpm

    @main_tempo_qpm.setter
    def main_tempo_qpm(self, main_tempo_qpm):
        """Sets the main_tempo_qpm of this ScoreDetails.

        The main tempo of the score (in QPM)  # noqa: E501

        :param main_tempo_qpm: The main_tempo_qpm of this ScoreDetails.  # noqa: E501
        :type: int
        """

        self._main_tempo_qpm = main_tempo_qpm

    @property
    def rights(self):
        """Gets the rights of this ScoreDetails.  # noqa: E501


        :return: The rights of this ScoreDetails.  # noqa: E501
        :rtype: ResourceRights
        """
        return self._rights

    @rights.setter
    def rights(self, rights):
        """Sets the rights of this ScoreDetails.


        :param rights: The rights of this ScoreDetails.  # noqa: E501
        :type: ResourceRights
        """

        self._rights = rights

    @property
    def collaborators(self):
        """Gets the collaborators of this ScoreDetails.  # noqa: E501

        The list of the collaborators of the score  # noqa: E501

        :return: The collaborators of this ScoreDetails.  # noqa: E501
        :rtype: list[ResourceCollaborator]
        """
        return self._collaborators

    @collaborators.setter
    def collaborators(self, collaborators):
        """Sets the collaborators of this ScoreDetails.

        The list of the collaborators of the score  # noqa: E501

        :param collaborators: The collaborators of this ScoreDetails.  # noqa: E501
        :type: list[ResourceCollaborator]
        """

        self._collaborators = collaborators

    @property
    def creation_date(self):
        """Gets the creation_date of this ScoreDetails.  # noqa: E501

        The date when the score was created  # noqa: E501

        :return: The creation_date of this ScoreDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this ScoreDetails.

        The date when the score was created  # noqa: E501

        :param creation_date: The creation_date of this ScoreDetails.  # noqa: E501
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def modification_date(self):
        """Gets the modification_date of this ScoreDetails.  # noqa: E501

        The date of the last revision of the score  # noqa: E501

        :return: The modification_date of this ScoreDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._modification_date

    @modification_date.setter
    def modification_date(self, modification_date):
        """Sets the modification_date of this ScoreDetails.

        The date of the last revision of the score  # noqa: E501

        :param modification_date: The modification_date of this ScoreDetails.  # noqa: E501
        :type: datetime
        """

        self._modification_date = modification_date

    @property
    def publication_date(self):
        """Gets the publication_date of this ScoreDetails.  # noqa: E501

        The date when the score was published on Flat  # noqa: E501

        :return: The publication_date of this ScoreDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._publication_date

    @publication_date.setter
    def publication_date(self, publication_date):
        """Sets the publication_date of this ScoreDetails.

        The date when the score was published on Flat  # noqa: E501

        :param publication_date: The publication_date of this ScoreDetails.  # noqa: E501
        :type: datetime
        """

        self._publication_date = publication_date

    @property
    def organization(self):
        """Gets the organization of this ScoreDetails.  # noqa: E501

        If the score has been created in an organization, the identifier of this organization. This property is especially used with the score privacy `organizationPublic`.   # noqa: E501

        :return: The organization of this ScoreDetails.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this ScoreDetails.

        If the score has been created in an organization, the identifier of this organization. This property is especially used with the score privacy `organizationPublic`.   # noqa: E501

        :param organization: The organization of this ScoreDetails.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def parent_score(self):
        """Gets the parent_score of this ScoreDetails.  # noqa: E501

        If the score has been forked, the unique identifier of the parent score.   # noqa: E501

        :return: The parent_score of this ScoreDetails.  # noqa: E501
        :rtype: str
        """
        return self._parent_score

    @parent_score.setter
    def parent_score(self, parent_score):
        """Sets the parent_score of this ScoreDetails.

        If the score has been forked, the unique identifier of the parent score.   # noqa: E501

        :param parent_score: The parent_score of this ScoreDetails.  # noqa: E501
        :type: str
        """

        self._parent_score = parent_score

    @property
    def instruments(self):
        """Gets the instruments of this ScoreDetails.  # noqa: E501

        An array of the instrument identifiers used in the last version of the score. This is mainly used to display a list of the instruments in the Flat's UI or instruments icons. The format of the strings is `{instrument-group}.{instrument-id}`.   # noqa: E501

        :return: The instruments of this ScoreDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._instruments

    @instruments.setter
    def instruments(self, instruments):
        """Sets the instruments of this ScoreDetails.

        An array of the instrument identifiers used in the last version of the score. This is mainly used to display a list of the instruments in the Flat's UI or instruments icons. The format of the strings is `{instrument-group}.{instrument-id}`.   # noqa: E501

        :param instruments: The instruments of this ScoreDetails.  # noqa: E501
        :type: list[str]
        """

        self._instruments = instruments

    @property
    def google_drive_file_id(self):
        """Gets the google_drive_file_id of this ScoreDetails.  # noqa: E501

        If the user uses Google Drive and the score exists on Google Drive, this field will contain the unique identifier of the Flat score on Google Drive. You can access the document using the url: `https://drive.google.com/open?id={googleDriveFileId}`   # noqa: E501

        :return: The google_drive_file_id of this ScoreDetails.  # noqa: E501
        :rtype: str
        """
        return self._google_drive_file_id

    @google_drive_file_id.setter
    def google_drive_file_id(self, google_drive_file_id):
        """Sets the google_drive_file_id of this ScoreDetails.

        If the user uses Google Drive and the score exists on Google Drive, this field will contain the unique identifier of the Flat score on Google Drive. You can access the document using the url: `https://drive.google.com/open?id={googleDriveFileId}`   # noqa: E501

        :param google_drive_file_id: The google_drive_file_id of this ScoreDetails.  # noqa: E501
        :type: str
        """

        self._google_drive_file_id = google_drive_file_id

    @property
    def likes(self):
        """Gets the likes of this ScoreDetails.  # noqa: E501


        :return: The likes of this ScoreDetails.  # noqa: E501
        :rtype: ScoreLikesCounts
        """
        return self._likes

    @likes.setter
    def likes(self, likes):
        """Sets the likes of this ScoreDetails.


        :param likes: The likes of this ScoreDetails.  # noqa: E501
        :type: ScoreLikesCounts
        """

        self._likes = likes

    @property
    def comments(self):
        """Gets the comments of this ScoreDetails.  # noqa: E501


        :return: The comments of this ScoreDetails.  # noqa: E501
        :rtype: ScoreCommentsCounts
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this ScoreDetails.


        :param comments: The comments of this ScoreDetails.  # noqa: E501
        :type: ScoreCommentsCounts
        """

        self._comments = comments

    @property
    def views(self):
        """Gets the views of this ScoreDetails.  # noqa: E501


        :return: The views of this ScoreDetails.  # noqa: E501
        :rtype: ScoreViewsCounts
        """
        return self._views

    @views.setter
    def views(self, views):
        """Sets the views of this ScoreDetails.


        :param views: The views of this ScoreDetails.  # noqa: E501
        :type: ScoreViewsCounts
        """

        self._views = views

    @property
    def collections(self):
        """Gets the collections of this ScoreDetails.  # noqa: E501

        The List of parent collections, which includes all the collections this score is included. Please note that you might not have access to all of them.  # noqa: E501

        :return: The collections of this ScoreDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._collections

    @collections.setter
    def collections(self, collections):
        """Sets the collections of this ScoreDetails.

        The List of parent collections, which includes all the collections this score is included. Please note that you might not have access to all of them.  # noqa: E501

        :param collections: The collections of this ScoreDetails.  # noqa: E501
        :type: list[str]
        """

        self._collections = collections

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ScoreDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
