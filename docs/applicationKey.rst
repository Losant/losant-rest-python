Application Key
===============


Actions
-------

* `Get <#get>`_
* `Patch <#patch>`_
* `Delete <#delete>`_


Get
***

Retrieves information on an applicationKey

::

    client.application_key.get(**params_dict)


Parameters
``````````

applicationId
    Type: string

    Required: true

    ID associated with the application

applicationKeyId
    Type: string

    Required: true

    ID associated with the applicationKey

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
    Type: `applicationKey <_schemas.rst#applicationkey>`_

    applicationKey information


Errors
``````

404
    Type: `error <_schemas.rst#error>`_

    Error if applicationKey was not found


Patch
*****

Updates information about an applicationKey

::

    client.application_key.patch(**params_dict)


Parameters
``````````

applicationId
    Type: string

    Required: true

    ID associated with the application

applicationKeyId
    Type: string

    Required: true

    ID associated with the applicationKey

applicationKey
    Type: `applicationKeyPatch <_schemas.rst#applicationkeypatch>`_

    Required: true

    Object containing new properties of the applicationKey

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
    Type: `applicationKey <_schemas.rst#applicationkey>`_

    Updated applicationKey information


Errors
``````

400
    Type: `error <_schemas.rst#error>`_

    Error if malformed request

404
    Type: `error <_schemas.rst#error>`_

    Error if applicationKey was not found


Delete
******

Deletes an applicationKey

::

    client.application_key.delete(**params_dict)


Parameters
``````````

applicationId
    Type: string

    Required: true

    ID associated with the application

applicationKeyId
    Type: string

    Required: true

    ID associated with the applicationKey

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

    If applicationKey was successfully deleted


Errors
``````

404
    Type: `error <_schemas.rst#error>`_

    Error if applicationKey was not found
