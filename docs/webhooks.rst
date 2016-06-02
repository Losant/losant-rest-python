Webhooks
========


Get
---

Returns the webhooks for an application

::

    client.webhooks.get(params=None)


Parameters
**********

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
*********

200
    Type: `webhooks <_schemas.rst#webhooks>`_
    Collection of webhooks


Errors
******

404
    Type: `error <_schemas.rst#error>`_
    Error if application was not found


Post
----

Create a new webhook for an application

::

    client.webhooks.post(params=None)


Parameters
**********

applicationId
    Type: string
    Required: true
    ID associated with the application

webhook
    Type: `webhookPost <_schemas.rst#webhookPost>`_
    Required: true
    New webhook information

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

201
    Type: `webhook <_schemas.rst#webhook>`_
    Successfully created webhook


Errors
******

400
    Type: `error <_schemas.rst#error>`_
    Error if malformed request

404
    Type: `error <_schemas.rst#error>`_
    Error if application was not found
