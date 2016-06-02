Device Recipes
==============


Actions
-------

* `Get <#get>`_
* `Post <#post>`_


Get
***

Returns the device recipes for an application

::

    client.device_recipes.get(**params_dict)


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
    Type: `deviceRecipes <_schemas.rst#devicerecipes>`_

    Collection of device recipes


Errors
``````

404
    Type: `error <_schemas.rst#error>`_

    Error if application was not found


Post
****

Create a new device recipe for an application

::

    client.device_recipes.post(**params_dict)


Parameters
``````````

applicationId
    Type: string

    Required: true

    ID associated with the application

deviceRecipe
    Type: `deviceRecipePost <_schemas.rst#devicerecipepost>`_

    Required: true

    New device recipe information

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
    Type: `deviceRecipe <_schemas.rst#devicerecipe>`_

    Successfully created device recipe


Errors
``````

400
    Type: `error <_schemas.rst#error>`_

    Error if malformed request

404
    Type: `error <_schemas.rst#error>`_

    Error if application was not found
