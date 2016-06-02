Dashboard
=========


Get
---

Retrieves information on an dashboard

::

    client.dashboard.get(params=None)


Parameters
**********

dashboardId
    Type: string
    Required: true
    ID of the associated dashboard

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
    Type: `dashboard <_schemas.rst#dashboard>`_
    Dashboard information


Errors
******

404
    Type: `error <_schemas.rst#error>`_
    Error if dashboard was not found


Patch
-----

Updates information about a dashboard

::

    client.dashboard.patch(params=None)


Parameters
**********

dashboardId
    Type: string
    Required: true
    ID of the associated dashboard

dashboard
    Type: `dashboardPatch <_schemas.rst#dashboardPatch>`_
    Required: true
    Object containing new dashboard properties

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
    Type: `dashboard <_schemas.rst#dashboard>`_
    Update dashboard information


Errors
******

400
    Type: `error <_schemas.rst#error>`_
    Error if malformed request

404
    Type: `error <_schemas.rst#error>`_
    Error if dashboard was not found


Delete
------

Deletes an dashboard

::

    client.dashboard.delete(params=None)


Parameters
**********

dashboardId
    Type: string
    Required: true
    ID of the associated dashboard

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
    If dashboard was successfully deleted


Errors
******

404
    Type: `error <_schemas.rst#error>`_
    Error if dashboard was not found
