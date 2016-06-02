Org
===


Get
---

Retrieves information on an organization

::

    client.org.get(params=None)


Parameters
**********

orgId
    Type: string
    Required: true
    ID associated with the organization

_actions
    Type: boolean
    Return resource actions in response

_links
    Type: boolean
    Return resource link in response

_embedded
    Type: boolean
    Return embedded resources in response


Responses
*********

200
    Type: `org <_schemas.rst#org>`_
    Organization information


Errors
******

404
    Type: `error <_schemas.rst#error>`_
    Error if organization not found


Patch
-----

Updates information about an organization

::

    client.org.patch(params=None)


Parameters
**********

orgId
    Type: string
    Required: true
    ID associated with the organization

organization
    Type: `orgPatch <_schemas.rst#orgPatch>`_
    Required: true
    Object containing new organization properties

_actions
    Type: boolean
    Return resource actions in response

_links
    Type: boolean
    Return resource link in response

_embedded
    Type: boolean
    Return embedded resources in response


Responses
*********

200
    Type: `org <_schemas.rst#org>`_
    Updated organization information


Errors
******

400
    Type: `error <_schemas.rst#error>`_
    Error if malformed request

404
    Type: `error <_schemas.rst#error>`_
    Error if organization was not found


Delete
------

Deletes an organization

::

    client.org.delete(params=None)


Parameters
**********

orgId
    Type: string
    Required: true
    ID associated with the organization

_actions
    Type: boolean
    Return resource actions in response

_links
    Type: boolean
    Return resource link in response

_embedded
    Type: boolean
    Return embedded resources in response


Responses
*********

200
    Type: `success <_schemas.rst#success>`_
    If organization was successfully deleted


Errors
******

404
    Type: `error <_schemas.rst#error>`_
    Error if organization was not found


Pending Invites
---------------

Gets the current pending invites

::

    client.org.pending_invites(params=None)


Parameters
**********

orgId
    Type: string
    Required: true
    ID associated with the organization

_actions
    Type: boolean
    Return resource actions in response

_links
    Type: boolean
    Return resource link in response

_embedded
    Type: boolean
    Return embedded resources in response


Responses
*********

200
    Type: `orgInvites <_schemas.rst#orgInvites>`_
    Invitation information


Errors
******

404
    Type: `error <_schemas.rst#error>`_
    Error if organization not found


Invite Member
-------------

Invites a person to an organization

::

    client.org.invite_member(params=None)


Parameters
**********

orgId
    Type: string
    Required: true
    ID associated with the organization

invite
    Type: `orgInvitePost <_schemas.rst#orgInvitePost>`_
    Required: true
    Object containing new invite info

_actions
    Type: boolean
    Return resource actions in response

_links
    Type: boolean
    Return resource link in response

_embedded
    Type: boolean
    Return embedded resources in response


Responses
*********

200
    Type: `orgInvites <_schemas.rst#orgInvites>`_
    Invitation information


Errors
******

400
    Type: `error <_schemas.rst#error>`_
    Error if malformed request

404
    Type: `error <_schemas.rst#error>`_
    Error if organization not found


Revoke Invite
-------------

Revokes an existing invite

::

    client.org.revoke_invite(params=None)


Parameters
**********

orgId
    Type: string
    Required: true
    ID associated with the organization

inviteId
    Type: string
    Required: true
    Id of invite to revoke

_actions
    Type: boolean
    Return resource actions in response

_links
    Type: boolean
    Return resource link in response

_embedded
    Type: boolean
    Return embedded resources in response


Responses
*********

200
    Type: `orgInvites <_schemas.rst#orgInvites>`_
    Invitation information


Errors
******

400
    Type: `error <_schemas.rst#error>`_
    Error if malformed request

404
    Type: `error <_schemas.rst#error>`_
    Error if organization not found


Modify Member
-------------

Modifies a current org member&#x27;s role

::

    client.org.modify_member(params=None)


Parameters
**********

orgId
    Type: string
    Required: true
    ID associated with the organization

member
    Type: `orgMemberPatch <_schemas.rst#orgMemberPatch>`_
    Required: true
    Object containing new member pair

_actions
    Type: boolean
    Return resource actions in response

_links
    Type: boolean
    Return resource link in response

_embedded
    Type: boolean
    Return embedded resources in response


Responses
*********

200
    Type: `org <_schemas.rst#org>`_
    Updated organization information


Errors
******

400
    Type: `error <_schemas.rst#error>`_
    Error if malformed request

404
    Type: `error <_schemas.rst#error>`_
    Error if organization not found


Remove Member
-------------

Modifies a current org member&#x27;s role

::

    client.org.remove_member(params=None)


Parameters
**********

orgId
    Type: string
    Required: true
    ID associated with the organization

userId
    Type: string
    Required: true
    Id of user to remove

_actions
    Type: boolean
    Return resource actions in response

_links
    Type: boolean
    Return resource link in response

_embedded
    Type: boolean
    Return embedded resources in response


Responses
*********

200
    Type: `org <_schemas.rst#org>`_
    Updated organization information


Errors
******

400
    Type: `error <_schemas.rst#error>`_
    Error if malformed request

404
    Type: `error <_schemas.rst#error>`_
    Error if organization not found
