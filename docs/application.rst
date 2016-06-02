Application
===========


Actions
-------

* `Get <#get>`_
* `Patch <#patch>`_
* `Delete <#delete>`_
* `Debug <#debug>`_


Get
***

Retrieves information on an application

::

    client.application.get(**params_dict)


Parameters
``````````

applicationId
    Type: string

    Required: true

    ID of the associated application

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
    Type: `application <_schemas.rst#application>`_

    Application information


Errors
``````

404
    Type: `error <_schemas.rst#error>`_

    Error if application was not found


Patch
*****

Updates information about an application

::

    client.application.patch(**params_dict)


Parameters
``````````

applicationId
    Type: string

    Required: true

    ID of the associated application

application
    Type: `applicationPatch <_schemas.rst#applicationpatch>`_

    Required: true

    Object containing new application properties

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
    Type: `application <_schemas.rst#application>`_

    Updated application information


Errors
``````

400
    Type: `error <_schemas.rst#error>`_

    Error if malformed request

404
    Type: `error <_schemas.rst#error>`_

    Error if application was not found


Delete
******

Deletes an application

::

    client.application.delete(**params_dict)


Parameters
``````````

applicationId
    Type: string

    Required: true

    ID of the associated application

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

    If application was successfully deleted


Errors
``````

404
    Type: `error <_schemas.rst#error>`_

    Error if application was not found


Debug
*****

Streams real time application debug events using SSE

::

    client.application.debug(**params_dict)


Parameters
``````````

applicationId
    Type: string

    Required: true

    ID of the associated application

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
    Type: 

    Stream of application debug events


Errors
``````

404
    Type: `error <_schemas.rst#error>`_

    Error if application was not found
