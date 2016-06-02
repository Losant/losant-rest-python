Orgs
====


Actions
-------

* `Get <#get>`_
* `Post <#post>`_


Get
***

Returns the organizations associated with the current user

::

    client.orgs.get(**params_dict)


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
    Type: `orgs <_schemas.rst#orgs>`_

    Collection of organizations


Errors
``````


Post
****

Create a new organization

::

    client.orgs.post(**params_dict)


Parameters
``````````

organization
    Type: `orgPost <_schemas.rst#orgpost>`_

    Required: true

    New organization information

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
    Type: `org <_schemas.rst#org>`_

    Successfully created organization


Errors
``````

400
    Type: `error <_schemas.rst#error>`_

    Error if malformed request
