Devices
=======


Actions
-------

* `Get <#get>`_
* `Post <#post>`_


Get
***

Returns the devices for an application

::

    client.devices.get(**params_dict)


Parameters
``````````

applicationId
    Type: string

    Required: true

    ID associated with the application

sortField
    Type: string

    

sortDirection
    Type: string

    

page
    Type: string

    

perPage
    Type: string

    

filterField
    Type: string

    

filter
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
`````````

200
    Type: `devices <_schemas.rst#devices>`_

    Collection of devices


Errors
``````

404
    Type: `error <_schemas.rst#error>`_

    Error if application was not found


Post
****

Create a new device for an application

::

    client.devices.post(**params_dict)


Parameters
``````````

applicationId
    Type: string

    Required: true

    ID associated with the application

device
    Type: `devicePost <_schemas.rst#devicepost>`_

    Required: true

    New device information

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

201
    Type: `device <_schemas.rst#device>`_

    Successfully created device


Errors
``````

400
    Type: `error <_schemas.rst#error>`_

    Error if malformed request

404
    Type: `error <_schemas.rst#error>`_

    Error if application was not found
