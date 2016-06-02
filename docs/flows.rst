Flows
=====


Actions
-------

* `Get <#get>`_
* `Post <#post>`_


Get
***

Returns the flows for an application

::

    client.flows.get(**params_dict)


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
    Type: `flows <_schemas.rst#flows>`_

    Collection of flows


Errors
``````

404
    Type: `error <_schemas.rst#error>`_

    Error if application was not found


Post
****

Create a new flow for an application

::

    client.flows.post(**params_dict)


Parameters
``````````

applicationId
    Type: string

    Required: true

    ID associated with the application

flow
    Type: `flowPost <_schemas.rst#flowpost>`_

    Required: true

    New flow information

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
    Type: `flow <_schemas.rst#flow>`_

    Successfully created flow


Errors
``````

400
    Type: `error <_schemas.rst#error>`_

    Error if malformed request

404
    Type: `error <_schemas.rst#error>`_

    Error if application was not found
