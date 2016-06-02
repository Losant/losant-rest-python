Webhook
=======


Actions
-------

* `Get <#get>`_
* `Patch <#patch>`_
* `Delete <#delete>`_


Get
***

Retrieves information on an webhook

::

    client.webhook.get(**params_dict)


Parameters
``````````

applicationId
    Type: string

    Required: true

    ID associated with the application

webhookId
    Type: string

    Required: true

    ID associated with the webhook

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
    Type: `webhook <_schemas.rst#webhook>`_

    Webhook information


Errors
``````

404
    Type: `error <_schemas.rst#error>`_

    Error if webhook was not found


Patch
*****

Updates information about a webhook

::

    client.webhook.patch(**params_dict)


Parameters
``````````

applicationId
    Type: string

    Required: true

    ID associated with the application

webhookId
    Type: string

    Required: true

    ID associated with the webhook

webhook
    Type: `webhookPatch <_schemas.rst#webhookpatch>`_

    Required: true

    Object containing new properties of the webhook

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
    Type: `webhook <_schemas.rst#webhook>`_

    Updated webhook information


Errors
``````

400
    Type: `error <_schemas.rst#error>`_

    Error if malformed request

404
    Type: `error <_schemas.rst#error>`_

    Error if webhook was not found


Delete
******

Deletes a webhook

::

    client.webhook.delete(**params_dict)


Parameters
``````````

applicationId
    Type: string

    Required: true

    ID associated with the application

webhookId
    Type: string

    Required: true

    ID associated with the webhook

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

    If webhook was successfully deleted


Errors
``````

404
    Type: `error <_schemas.rst#error>`_

    Error if webhook was not found
