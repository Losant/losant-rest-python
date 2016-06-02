Dashboard
=========


Actions
-------

* `Get <#get>`_
* `Patch <#patch>`_
* `Delete <#delete>`_


Get
***

Retrieves information on an dashboard

::

    client.dashboard.get(**params_dict)


Parameters
``````````

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
`````````

200
    Type: `dashboard <_schemas.rst#dashboard>`_

    Dashboard information


Errors
``````

404
    Type: `error <_schemas.rst#error>`_

    Error if dashboard was not found


Patch
*****

Updates information about a dashboard

::

    client.dashboard.patch(**params_dict)


Parameters
``````````

dashboardId
    Type: string

    Required: true

    ID of the associated dashboard

dashboard
    Type: `dashboardPatch <_schemas.rst#dashboardpatch>`_

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
`````````

200
    Type: `dashboard <_schemas.rst#dashboard>`_

    Update dashboard information


Errors
``````

400
    Type: `error <_schemas.rst#error>`_

    Error if malformed request

404
    Type: `error <_schemas.rst#error>`_

    Error if dashboard was not found


Delete
******

Deletes an dashboard

::

    client.dashboard.delete(**params_dict)


Parameters
``````````

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
`````````

200
    Type: `success <_schemas.rst#success>`_

    If dashboard was successfully deleted


Errors
``````

404
    Type: `error <_schemas.rst#error>`_

    Error if dashboard was not found
