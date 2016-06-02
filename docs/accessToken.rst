Access Token
============


Actions
-------

* `Get <#get>`_
* `Patch <#patch>`_
* `Delete <#delete>`_


Get
***

Retrieves information on an accessToken

::

    client.access_token.get(**params_dict)


Parameters
``````````

accessTokenId
    Type: string

    Required: true

    ID associated with the accessToken

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
    Type: `accessToken <_schemas.rst#accesstoken>`_

    Device information


Errors
``````

404
    Type: `error <_schemas.rst#error>`_

    Error if accessToken was not found


Patch
*****

Updates information about a accessToken

::

    client.access_token.patch(**params_dict)


Parameters
``````````

accessTokenId
    Type: string

    Required: true

    ID associated with the accessToken

accessToken
    Type: `accessTokenPatch <_schemas.rst#accesstokenpatch>`_

    Required: true

    Object containing new properties of the accessToken

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
    Type: `accessToken <_schemas.rst#accesstoken>`_

    Updated accessToken information


Errors
``````

400
    Type: `error <_schemas.rst#error>`_

    Error if malformed request

404
    Type: `error <_schemas.rst#error>`_

    Error if accessToken was not found


Delete
******

Deletes a accessToken

::

    client.access_token.delete(**params_dict)


Parameters
``````````

accessTokenId
    Type: string

    Required: true

    ID associated with the accessToken

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

    If accessToken was successfully deleted


Errors
``````

404
    Type: `error <_schemas.rst#error>`_

    Error if accessToken was not found
