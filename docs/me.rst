Me
==


Get
---

Retrieves information on the current user

::

    client.me.get(params=None)


Parameters
**********

includeRecent
    Type: 
    Should the user include recent app/dashboard info

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
    Type: `me <_schemas.rst#me>`_
    Current user information


Errors
******


Patch
-----

Updates information about the current user

::

    client.me.patch(params=None)


Parameters
**********

user
    Type: `mePatch <_schemas.rst#mePatch>`_
    Required: true
    Object containing new user properties

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
    Type: `me <_schemas.rst#me>`_
    Updated user information


Errors
******

400
    Type: `error <_schemas.rst#error>`_
    Error if malformed request


Delete
------

Deletes the current user

::

    client.me.delete(params=None)


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
    Type: `success <_schemas.rst#success>`_
    If the user was successfully deleted


Errors
******

400
    Type: `error <_schemas.rst#error>`_
    Error if malformed request


Verify Email
------------

Sends and email verification to the user

::

    client.me.verify_email(params=None)


Parameters
**********

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
    Type: `success <_schemas.rst#success>`_
    If email verification was successfully sent


Errors
******

400
    Type: `error <_schemas.rst#error>`_
    Error if malformed request


Enable Two Factor Auth
----------------------

Enables two factor auth for the current user

::

    client.me.enable_two_factor_auth(params=None)


Parameters
**********

data
    Type: `enableTwoFactorAuth <_schemas.rst#enableTwoFactorAuth>`_
    Required: true
    Object containing two factor auth properties

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
    Type: `me <_schemas.rst#me>`_
    Updated user information


Errors
******

400
    Type: `error <_schemas.rst#error>`_
    Error if malformed request


Disable Two Factor Auth
-----------------------

Disables two factor auth for the current user

::

    client.me.disable_two_factor_auth(params=None)


Parameters
**********

data
    Type: `disableTwoFactorAuth <_schemas.rst#disableTwoFactorAuth>`_
    Required: true
    Object containing two factor auth properties

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
    Type: `me <_schemas.rst#me>`_
    Updated user information


Errors
******

400
    Type: `error <_schemas.rst#error>`_
    Error if malformed request


Disconnect Github
-----------------

Disconnects the user from Github

::

    client.me.disconnect_github(params=None)


Parameters
**********

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
    Type: `me <_schemas.rst#me>`_
    Updated user information


Errors
******

400
    Type: `error <_schemas.rst#error>`_
    Error if malformed request


Disconnect Twitter
------------------

Disconnects the user from Twitter

::

    client.me.disconnect_twitter(params=None)


Parameters
**********

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
    Type: `me <_schemas.rst#me>`_
    Updated user information


Errors
******

400
    Type: `error <_schemas.rst#error>`_
    Error if malformed request


Add Recent Item
---------------

Adds an item to a recent item list

::

    client.me.add_recent_item(params=None)


Parameters
**********

data
    Type: `recentItem <_schemas.rst#recentItem>`_
    Required: true
    Object containing recent item info

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
    Type: `recentItemList <_schemas.rst#recentItemList>`_
    Updated recent item list


Errors
******

400
    Type: `error <_schemas.rst#error>`_
    Error if malformed request


Fetch Recent Items
------------------

Gets a recent item list

::

    client.me.fetch_recent_items(params=None)


Parameters
**********

parentId
    Type: string
    

itemType
    Type: 
    

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
    Type: `recentItemList <_schemas.rst#recentItemList>`_
    Recent item list


Errors
******

400
    Type: `error <_schemas.rst#error>`_
    Error if malformed request
