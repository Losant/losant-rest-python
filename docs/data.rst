Data
====


Actions
-------

* `Time Series Query <#timeseriesquery>`_
* `Last Value Query <#lastvaluequery>`_


Time Series Query
*****************

Returns the data for the given query

::

    client.data.time_series_query(**params_dict)


Parameters
``````````

applicationId
    Type: string

    Required: true

    ID associated with the application

query
    Type: `timeSeriesQuery <_schemas.rst#timeseriesquery>`_

    Required: true

    The query parameters

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
    Type: `timeSeriesData <_schemas.rst#timeseriesdata>`_

    Data for requested time range


Errors
``````

404
    Type: `error <_schemas.rst#error>`_

    Error if application was not found


Last Value Query
****************

Returns the last known data for the given attribute

::

    client.data.last_value_query(**params_dict)


Parameters
``````````

applicationId
    Type: string

    Required: true

    ID associated with the application

query
    Type: `lastValueQuery <_schemas.rst#lastvaluequery>`_

    Required: true

    The query parameters

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
    Type: `lastValueData <_schemas.rst#lastvaluedata>`_

    Last known data for the requested attribute


Errors
``````

404
    Type: `error <_schemas.rst#error>`_

    Error if application was not found
