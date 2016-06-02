Access Tokens
=============


Actions
-------

* `Get <#get>`_
* `Post <#post>`_


Get
***

Returns the accessTokens for a user

::

    client.access_tokens.get(**params_dict)


Parameters
``````````

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
    Type: `accessTokens <_schemas.rst#accesstokens>`_

    Collection of accessTokens


Errors
``````


Post
****

Create a new accessKey for a user

::

    client.access_tokens.post(**params_dict)


Parameters
``````````

accessToken
    Type: `accessToken <_schemas.rst#accesstoken>`_

    Required: true

    AccessToken information

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
    Type: `accessToken <_schemas.rst#accesstoken>`_

    Successfully created access token


Errors
``````

400
    Type: `error <_schemas.rst#error>`_

    Error if malformed request
