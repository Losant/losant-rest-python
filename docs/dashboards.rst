Dashboards
==========


Get
---

Returns the dashboards owned by the current user

::

    client.dashboards.get(params=None)


Parameters
**********

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
    

orgId
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
    Type: `dashboards <_schemas.rst#dashboards>`_
    Collection of dashboards


Errors
******


Post
----

Create a new dasboard owned by the current user

::

    client.dashboards.post(params=None)


Parameters
**********

dashboard
    Type: `dashboardPost <_schemas.rst#dashboardPost>`_
    Required: true
    New dashboard information

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
    Type: `dashboard <_schemas.rst#dashboard>`_
    Successfully created dashboard


Errors
******

400
    Type: `error <_schemas.rst#error>`_
    Error if malformed request
