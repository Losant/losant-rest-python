Auth
====


Authenticate User
-----------------

Authenticates a user using the provided credentials

::

    client.auth.authenticate_user(params=None)


Parameters
**********

credentials
    Type: `userCredentials <_schemas.rst#userCredentials>`_
    Required: true
    User authentication credentials

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
    Type: `authedUser <_schemas.rst#authedUser>`_
    Successful authentication


Errors
******

400
    Type: `error <_schemas.rst#error>`_
    Error if malformed request

401
    Type: `error <_schemas.rst#error>`_
    Unauthorized error if authentication fails


Authenticate User Github
------------------------

Authenticates a user via GitHub OAuth

::

    client.auth.authenticate_user_github(params=None)


Parameters
**********

oauth
    Type: `githubLogin <_schemas.rst#githubLogin>`_
    Required: true
    User authentication credentials (access token)

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
    Type: `authedUser <_schemas.rst#authedUser>`_
    Successful authentication


Errors
******

400
    Type: `error <_schemas.rst#error>`_
    Error if malformed request

401
    Type: `error <_schemas.rst#error>`_
    Unauthorized error if authentication fails


Authenticate Device
-------------------

Authenticates a device using the provided credentials

::

    client.auth.authenticate_device(params=None)


Parameters
**********

credentials
    Type: `deviceCredentials <_schemas.rst#deviceCredentials>`_
    Required: true
    Device authentication credentials

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
    Type: `authedDevice <_schemas.rst#authedDevice>`_
    Successful authentication


Errors
******

400
    Type: `error <_schemas.rst#error>`_
    Error if malformed request

401
    Type: `error <_schemas.rst#error>`_
    Unauthorized error if authentication fails
