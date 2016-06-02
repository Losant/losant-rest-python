Flow
====


Get
---

Retrieves information on an flow

::

    client.flow.get(params=None)


Parameters
**********

applicationId
    Type: string
    Required: true
    ID associated with the application

flowId
    Type: string
    Required: true
    ID associated with the flow

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
    Type: `flow <_schemas.rst#flow>`_
    Flow information


Errors
******

404
    Type: `error <_schemas.rst#error>`_
    Error if flow was not found


Patch
-----

Updates information about a flow

::

    client.flow.patch(params=None)


Parameters
**********

applicationId
    Type: string
    Required: true
    ID associated with the application

flowId
    Type: string
    Required: true
    ID associated with the flow

flow
    Type: `flowPatch <_schemas.rst#flowPatch>`_
    Required: true
    Object containing new properties of the flow

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
    Type: `flow <_schemas.rst#flow>`_
    Updated flow information


Errors
******

400
    Type: `error <_schemas.rst#error>`_
    Error if malformed request

404
    Type: `error <_schemas.rst#error>`_
    Error if flow is not found


Delete
------

Deletes a flow

::

    client.flow.delete(params=None)


Parameters
**********

applicationId
    Type: string
    Required: true
    ID associated with the application

flowId
    Type: string
    Required: true
    ID associated with the flow

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
    If flow was successfully deleted


Errors
******

404
    Type: `error <_schemas.rst#error>`_
    Error if flow was not found


Debug
-----

Streams real time flow debug events using SSE

::

    client.flow.debug(params=None)


Parameters
**********

applicationId
    Type: string
    Required: true
    ID associated with the application

flowId
    Type: string
    Required: true
    ID associated with the flow

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
    Type: 
    Stream of flow debug events


Errors
******

404
    Type: `error <_schemas.rst#error>`_
    Error if flow was not found


Get Log Entries
---------------

Retrieve the recent log entries about the flows

::

    client.flow.get_log_entries(params=None)


Parameters
**********

applicationId
    Type: string
    Required: true
    ID associated with the application

flowId
    Type: string
    Required: true
    ID associated with the flow

limit
    Type: string
    

since
    Type: string
    

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
    Type: 
    Recent log entries


Errors
******

404
    Type: `error <_schemas.rst#error>`_
    Error if device was not found


Press Virtual Button
--------------------

Presses the specified virtual button on the flow

::

    client.flow.press_virtual_button(params=None)


Parameters
**********

applicationId
    Type: string
    Required: true
    ID associated with the application

flowId
    Type: string
    Required: true
    ID associated with the flow

button
    Type: `virtualButtonPress <_schemas.rst#virtualButtonPress>`_
    Required: true
    Object containing button key and payload

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
    Virtual button was pressed


Errors
******

404
    Type: `error <_schemas.rst#error>`_
    Error if flow was not found


Get Storage Entries
-------------------

Gets the current values in persistent storage

::

    client.flow.get_storage_entries(params=None)


Parameters
**********

applicationId
    Type: string
    Required: true
    ID associated with the application

flowId
    Type: string
    Required: true
    ID associated with the flow

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
    Type: 
    The stored values


Errors
******

404
    Type: `error <_schemas.rst#error>`_
    Error if flow was not found


Set Storage Entry
-----------------

Sets a storage value

::

    client.flow.set_storage_entry(params=None)


Parameters
**********

applicationId
    Type: string
    Required: true
    ID associated with the application

flowId
    Type: string
    Required: true
    ID associated with the flow

entry
    Type: `flowStorageEntry <_schemas.rst#flowStorageEntry>`_
    Required: true
    Object containing storage entry

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
    Value was successfully stored


Errors
******

404
    Type: `error <_schemas.rst#error>`_
    Error if flow was not found
