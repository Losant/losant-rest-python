Application Keys
================


Actions
-------

* `Get <#get>`_
* `Post <#post>`_


Get
***

Returns the applicationKeys for an application

::

    client.application_keys.get(**params_dict)


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
    Type: `applicationKeys <_schemas.rst#applicationkeys>`_

    Collection of applicationKeys


Errors
``````

404
    Type: `error <_schemas.rst#error>`_

    Error if application was not found


Post
****

Create a new applicationKey for an application

::

    client.application_keys.post(**params_dict)


Parameters
``````````

applicationId
    Type: string

    Required: true

    ID associated with the application

applicationKey
    Type: `applicationKeyPost <_schemas.rst#applicationkeypost>`_

    Required: true

    ApplicationKey information

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
    Type: `applicationKey <_schemas.rst#applicationkey>`_

    Successfully created applicationKey


Errors
``````

400
    Type: `error <_schemas.rst#error>`_

    Error if malformed request

404
    Type: `error <_schemas.rst#error>`_

    Error if application was not found
