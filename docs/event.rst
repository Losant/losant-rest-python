Event
=====


Get
---

Retrieves information on an event

::

    client.event.get(params=None)


Parameters
**********

applicationId
    Type: string
    Required: true
    ID associated with the application

eventId
    Type: string
    Required: true
    ID associated with the event

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
    Type: `event <_schemas.rst#event>`_
    Event information


Errors
******

404
    Type: `error <_schemas.rst#error>`_
    Error if event was not found


Patch
-----

Updates information about an event

::

    client.event.patch(params=None)


Parameters
**********

applicationId
    Type: string
    Required: true
    ID associated with the application

eventId
    Type: string
    Required: true
    ID associated with the event

event
    Type: `eventPatch <_schemas.rst#eventPatch>`_
    Required: true
    Object containing new properties of the event

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
    Type: `event <_schemas.rst#event>`_
    Updated event information


Errors
******

400
    Type: `error <_schemas.rst#error>`_
    Error if malformed request

404
    Type: `error <_schemas.rst#error>`_
    Error if event is not found


Delete
------

Deletes an event

::

    client.event.delete(params=None)


Parameters
**********

applicationId
    Type: string
    Required: true
    ID associated with the application

eventId
    Type: string
    Required: true
    ID associated with the event

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
    If event was successfully deleted


Errors
******

404
    Type: `error <_schemas.rst#error>`_
    Error if event was not found
