Device Recipe
=============


Get
---

Retrieves information on a device recipe

::

    client.device_recipe.get(params=None)


Parameters
**********

applicationId
    Type: string
    Required: true
    ID associated with the application

deviceRecipeId
    Type: string
    Required: true
    ID associated with the device recipe

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
    Type: `deviceRecipe <_schemas.rst#deviceRecipe>`_
    Device recipe information


Errors
******

404
    Type: `error <_schemas.rst#error>`_
    Error if device recipe was not found


Patch
-----

Updates information about a device recipe

::

    client.device_recipe.patch(params=None)


Parameters
**********

applicationId
    Type: string
    Required: true
    ID associated with the application

deviceRecipeId
    Type: string
    Required: true
    ID associated with the device recipe

deviceRecipe
    Type: `deviceRecipePatch <_schemas.rst#deviceRecipePatch>`_
    Required: true
    Object containing new properties of the device recipe

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
    Type: `deviceRecipe <_schemas.rst#deviceRecipe>`_
    Updated device recipe information


Errors
******

400
    Type: `error <_schemas.rst#error>`_
    Error if malformed request

404
    Type: `error <_schemas.rst#error>`_
    Error if device recipe was not found


Delete
------

Deletes a device recipe

::

    client.device_recipe.delete(params=None)


Parameters
**********

applicationId
    Type: string
    Required: true
    ID associated with the application

deviceRecipeId
    Type: string
    Required: true
    ID associated with the device recipe

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
    If device recipe was successfully deleted


Errors
******

404
    Type: `error <_schemas.rst#error>`_
    Error if device recipe was not found


Bulk Create
-----------

Bulk creates devices using this recipe from a CSV

::

    client.device_recipe.bulk_create(params=None)


Parameters
**********

applicationId
    Type: string
    Required: true
    ID associated with the application

deviceRecipeId
    Type: string
    Required: true
    ID associated with the device recipe

bulkInfo
    Type: `deviceRecipeBulkCreatePost <_schemas.rst#deviceRecipeBulkCreatePost>`_
    Required: true
    Object containing bulk creation info

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
    Type: `deviceRecipeBulkCreate <_schemas.rst#deviceRecipeBulkCreate>`_
    If devices were sucessfully created


Errors
******

404
    Type: `error <_schemas.rst#error>`_
    Error if device recipe was not found
