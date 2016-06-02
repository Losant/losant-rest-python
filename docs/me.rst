Me
==


Actions
-------

* `Get <#get>`_
* `Patch <#patch>`_
* `Delete <#delete>`_
* `Verify Email <#verifyemail>`_
* `Enable Two Factor Auth <#enabletwofactorauth>`_
* `Disable Two Factor Auth <#disabletwofactorauth>`_
* `Disconnect Github <#disconnectgithub>`_
* `Disconnect Twitter <#disconnecttwitter>`_
* `Add Recent Item <#addrecentitem>`_
* `Fetch Recent Items <#fetchrecentitems>`_


Get
***

Retrieves information on the current user

::

    client.me.get(**params_dict)


Parameters
``````````

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
`````````

200
    Type: `me <_schemas.rst#me>`_

    Current user information


Errors
``````


Patch
*****

Updates information about the current user

::

    client.me.patch(**params_dict)


Parameters
``````````

user
    Type: `mePatch <_schemas.rst#mepatch>`_

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
`````````

200
    Type: `me <_schemas.rst#me>`_

    Updated user information


Errors
``````

400
    Type: `error <_schemas.rst#error>`_

    Error if malformed request


Delete
******

Deletes the current user

::

    client.me.delete(**params_dict)


Parameters
``````````

credentials
    Type: `userCredentials <_schemas.rst#usercredentials>`_

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
`````````

200
    Type: `success <_schemas.rst#success>`_

    If the user was successfully deleted


Errors
``````

400
    Type: `error <_schemas.rst#error>`_

    Error if malformed request


Verify Email
************

Sends and email verification to the user

::

    client.me.verify_email(**params_dict)


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
    Type: `success <_schemas.rst#success>`_

    If email verification was successfully sent


Errors
``````

400
    Type: `error <_schemas.rst#error>`_

    Error if malformed request


Enable Two Factor Auth
**********************

Enables two factor auth for the current user

::

    client.me.enable_two_factor_auth(**params_dict)


Parameters
``````````

data
    Type: `enableTwoFactorAuth <_schemas.rst#enabletwofactorauth>`_

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
`````````

200
    Type: `me <_schemas.rst#me>`_

    Updated user information


Errors
``````

400
    Type: `error <_schemas.rst#error>`_

    Error if malformed request


Disable Two Factor Auth
***********************

Disables two factor auth for the current user

::

    client.me.disable_two_factor_auth(**params_dict)


Parameters
``````````

data
    Type: `disableTwoFactorAuth <_schemas.rst#disabletwofactorauth>`_

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
`````````

200
    Type: `me <_schemas.rst#me>`_

    Updated user information


Errors
``````

400
    Type: `error <_schemas.rst#error>`_

    Error if malformed request


Disconnect Github
*****************

Disconnects the user from Github

::

    client.me.disconnect_github(**params_dict)


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
    Type: `me <_schemas.rst#me>`_

    Updated user information


Errors
``````

400
    Type: `error <_schemas.rst#error>`_

    Error if malformed request


Disconnect Twitter
******************

Disconnects the user from Twitter

::

    client.me.disconnect_twitter(**params_dict)


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
    Type: `me <_schemas.rst#me>`_

    Updated user information


Errors
``````

400
    Type: `error <_schemas.rst#error>`_

    Error if malformed request


Add Recent Item
***************

Adds an item to a recent item list

::

    client.me.add_recent_item(**params_dict)


Parameters
``````````

data
    Type: `recentItem <_schemas.rst#recentitem>`_

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
`````````

200
    Type: `recentItemList <_schemas.rst#recentitemlist>`_

    Updated recent item list


Errors
``````

400
    Type: `error <_schemas.rst#error>`_

    Error if malformed request


Fetch Recent Items
******************

Gets a recent item list

::

    client.me.fetch_recent_items(**params_dict)


Parameters
``````````

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
`````````

200
    Type: `recentItemList <_schemas.rst#recentitemlist>`_

    Recent item list


Errors
``````

400
    Type: `error <_schemas.rst#error>`_

    Error if malformed request
