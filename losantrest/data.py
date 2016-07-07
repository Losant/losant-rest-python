""" Module for Losant API Data wrapper class """
# pylint: disable=C0301

class Data(object):
    """ Class containing all the actions for the Data Resource """

    def __init__(self, client):
        self.client = client

    def last_value_query(self, **kwargs):
        """
        Returns the last known data for the given attribute

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {hash} query - The query parameters (https://api.losant.com/#/definitions/lastValueQuery)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Last known data for the requested attribute (https://api.losant.com/#/definitions/lastValueData)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  404 - Error if application was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "query" in kwargs:
            body = kwargs["query"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/data/last-value-query".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

    def time_series_query(self, **kwargs):
        """
        Returns the data for the given query

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {hash} query - The query parameters (https://api.losant.com/#/definitions/timeSeriesQuery)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Data for requested time range (https://api.losant.com/#/definitions/timeSeriesData)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  404 - Error if application was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "query" in kwargs:
            body = kwargs["query"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/data/time-series-query".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

