Device
======


Get
---

Retrieves information on an device

::

    client.device.get(params=None)


Parameters
**********

applicationId
    Type: string
    Required: true
    ID associated with the application

deviceId
    Type: string
    Required: true
    ID associated with the device

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
    Type: `device <_schemas.rst#device>`_
    Device information


Errors
******

404
    Type: `error <_schemas.rst#error>`_
    Error if device was not found


Patch
-----

Updates information about a device

::

    client.device.patch(params=None)


Parameters
**********

applicationId
    Type: string
    Required: true
    ID associated with the application

deviceId
    Type: string
    Required: true
    ID associated with the device

device
    Type: `devicePatch <_schemas.rst#devicePatch>`_
    Required: true
    Object containing new properties of the device

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
    Type: `device <_schemas.rst#device>`_
    Updated device information


Errors
******

400
    Type: `error <_schemas.rst#error>`_
    Error if malformed request

404
    Type: `error <_schemas.rst#error>`_
    Error if device was not found


Delete
------

Deletes a device

::

    client.device.delete(params=None)


Parameters
**********

applicationId
    Type: string
    Required: true
    ID associated with the application

deviceId
    Type: string
    Required: true
    ID associated with the device

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
    If device was successfully deleted


Errors
******

404
    Type: `error <_schemas.rst#error>`_
    Error if device was not found


Get State
---------

Retrieve the last known state(s) of the device

::

    client.device.get_state(params=None)


Parameters
**********

applicationId
    Type: string
    Required: true
    ID associated with the application

deviceId
    Type: string
    Required: true
    ID associated with the device

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
    Type: `deviceStates <_schemas.rst#deviceStates>`_
    Recent device states


Errors
******

404
    Type: `error <_schemas.rst#error>`_
    Error if device was not found


Send State
----------

Send the current state of the device

::

    client.device.send_state(params=None)


Parameters
**********

applicationId
    Type: string
    Required: true
    ID associated with the application

deviceId
    Type: string
    Required: true
    ID associated with the device

deviceState
    Type: `deviceState <_schemas.rst#deviceState>`_
    Required: true
    Object containing the current state of the device

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
    If state was successfully received


Errors
******

400
    Type: `error <_schemas.rst#error>`_
    Error if malformed request

404
    Type: `error <_schemas.rst#error>`_
    Error if device was not found


Get Command
-----------

Retrieve the last known commands(s) sent to the device

::

    client.device.get_command(params=None)


Parameters
**********

applicationId
    Type: string
    Required: true
    ID associated with the application

deviceId
    Type: string
    Required: true
    ID associated with the device

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
    Type: `deviceCommands <_schemas.rst#deviceCommands>`_
    Recent device commands


Errors
******

404
    Type: `error <_schemas.rst#error>`_
    Error if device was not found


Send Command
------------

Send a command to a device

::

    client.device.send_command(params=None)


Parameters
**********

applicationId
    Type: string
    Required: true
    ID associated with the application

deviceId
    Type: string
    Required: true
    ID associated with the device

deviceCommand
    Type: `deviceCommand <_schemas.rst#deviceCommand>`_
    Required: true
    Command to send to the device

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
    If command was successfully sent


Errors
******

400
    Type: `error <_schemas.rst#error>`_
    Error if malformed request

404
    Type: `error <_schemas.rst#error>`_
    Error if device was not found


Get Log Entries
---------------

Retrieve the recent log entries about the device

::

    client.device.get_log_entries(params=None)


Parameters
**********

applicationId
    Type: string
    Required: true
    ID associated with the application

deviceId
    Type: string
    Required: true
    ID associated with the device

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
