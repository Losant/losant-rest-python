Applications
============


Actions
-------

* `Get <#get>`_
* `Post <#post>`_


Get
***

Returns the applications owned by the current user

::

    client.applications.get(**params_dict)


Parameters
``````````

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

    

orgId
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
    Type: `applications <_schemas.rst#applications>`_

    Collection of applications


Errors
``````


Post
****

Create a new application owned by the current user

::

    client.applications.post(**params_dict)


Parameters
``````````

application
    Type: `applicationPost <_schemas.rst#applicationpost>`_

    Required: true

    New application information

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
    Type: `application <_schemas.rst#application>`_

    Successfully created application


Errors
``````

400
    Type: `error <_schemas.rst#error>`_

    Error if malformed request
