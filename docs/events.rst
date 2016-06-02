Events
======


Actions
-------

* `Get <#get>`_
* `Post <#post>`_
* `Most Recent by Severity <#mostrecentbyseverity>`_


Get
***

Returns the events for an application

::

    client.events.get(**params_dict)


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

    

state
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
    Type: `events <_schemas.rst#events>`_

    Collection of events


Errors
``````

404
    Type: `error <_schemas.rst#error>`_

    Error if application was not found


Post
****

Create a new event for an application

::

    client.events.post(**params_dict)


Parameters
``````````

applicationId
    Type: string

    Required: true

    ID associated with the application

event
    Type: `eventPost <_schemas.rst#eventpost>`_

    Required: true

    New event information

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
    Type: `event <_schemas.rst#event>`_

    Successfully created event


Errors
``````

400
    Type: `error <_schemas.rst#error>`_

    Error if malformed request

404
    Type: `error <_schemas.rst#error>`_

    Error if application was not found

429
    Type: `error <_schemas.rst#error>`_

    Error if event creation rate limit exceeded


Most Recent by Severity
***********************

Returns the first new event ordered by severity and then creation

::

    client.events.most_recent_by_severity(**params_dict)


Parameters
``````````

applicationId
    Type: string

    Required: true

    ID associated with the application

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
    Type: 

    The event, plus count of currently new events


Errors
``````

404
    Type: `error <_schemas.rst#error>`_

    Error if application was not found
