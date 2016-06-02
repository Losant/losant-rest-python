""" Module for Losant API Events wrapper class """
# pylint: disable=C0301

class Events(object):
    """ Class containing all the actions for the Events Resource """

    def __init__(self, client):
        self.client = client

    def get(self, **kwargs):
        """
        Returns the events for an application

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} sortField
        *  {string} sortDirection
        *  {string} page
        *  {string} perPage
        *  {string} filterField
        *  {string} filter
        *  {string} state
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Collection of events (https://api.losant.com/#/definitions/events)

        Errors:
        *  404 - Error if application was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "sortField" in kwargs:
            query_params["sortField"] = kwargs["sortField"]
        if "sortDirection" in kwargs:
            query_params["sortDirection"] = kwargs["sortDirection"]
        if "page" in kwargs:
            query_params["page"] = kwargs["page"]
        if "perPage" in kwargs:
            query_params["perPage"] = kwargs["perPage"]
        if "filterField" in kwargs:
            query_params["filterField"] = kwargs["filterField"]
        if "filter" in kwargs:
            query_params["filter"] = kwargs["filter"]
        if "state" in kwargs:
            query_params["state"] = kwargs["state"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/events".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def post(self, **kwargs):
        """
        Create a new event for an application

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {dict} event - New event information (https://api.losant.com/#/definitions/eventPost)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  201 - Successfully created event (https://api.losant.com/#/definitions/event)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  404 - Error if application was not found (https://api.losant.com/#/definitions/error)
        *  429 - Error if event creation rate limit exceeded (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "event" in kwargs:
            body = kwargs["event"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/events".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

    def most_recent_by_severity(self, **kwargs):
        """
        Returns the first new event ordered by severity and then creation

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} filter
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - The event, plus count of currently new events

        Errors:
        *  404 - Error if application was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "filter" in kwargs:
            query_params["filter"] = kwargs["filter"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/events/mostRecentBySeverity".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

