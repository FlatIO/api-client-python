# Changelog

## 0.3.0

* feat(edu): Public release of the first education APIs:
  * `/v2/classes`: Classes management
  * `/v2/classes/{class}/assignments`: Flat Assignments and Submissions
  * `/v2/organizations/users`: Organization accounts management
  * `/v2/organizations/invitations`: Organization invitations for admins and teachers
  * `/v2/organizations/lti/credentials`: LTI credentials management
  * `/v2/groups/{group}` and `/groups/{group}/users`: List of groups and users part of groups
  * `/scores/{score}/submissions`: Submissions linked to a score
* feat(edu): New OAuth2 scopes:
  * `edu.classes`: Full, permissive scope to manage the classes.
  * `edu.classes.readonly`: Read-only access to the classes.
  * `edu.assignments`: Read-write access to the assignments and submissions.
  * `edu.assignments.readonly`: Read-only access to the assignments and submissions.
  * `edu.admin`: Full, permissive scope to manage all the admin of an organization.
  * `edu.admin.lti`: Access and manage the LTI Credentials for an organization.
  * `edu.admin.lti.readonly`: Read-only access to the LTI Credentials of an organization.
  * `edu.admin.users`: Access and manage the users and invitations of the organization.
  * `edu.admin.users.readonly`: Read-only access to the users and invitations of the organization.
* fix(spec): Add missing scopes in specification for `GET /scores/{score}/revisions/{revision}` and `GET /scores/{score}/revisions/{revision}/{format}`

## 0.2.0

* feat(scores): add support of private links sharing with `sharingKey`.
* feat(comments): Make "revision" optional when creating comments and support of "last" keyword.
* fix(revisions): Missing `id` property in `ScoreRevision`.
* update(spec): Specify `binary` response type for `GET /scores/{score}/revisions/{revision}/{format}`

## 0.1.0

Initial release
