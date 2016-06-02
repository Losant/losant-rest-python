""" Module for Losant API Applications wrapper class """
# pylint: disable=C0301

class Applications(object):
    """ Class containing all the actions for the Applications Resource """

    def __init__(self, client):
        self.client = client

    def get(self, **kwargs):
        """
        Returns the applications owned by the current user

        Parameters:
        *  {string} sortField
        *  {string} sortDirection
        *  {string} page
        *  {string} perPage
        *  {string} filterField
        *  {string} filter
        *  {string} orgId
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Collection of applications (https://api.losant.com/#/definitions/applications)

        Errors:
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

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
        if "orgId" in kwargs:
            query_params["orgId"] = kwargs["orgId"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def post(self, **kwargs):
        """
        Create a new application owned by the current user

        Parameters:
        *  {dict} application - New application information (https://api.losant.com/#/definitions/applicationPost)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  201 - Successfully created application (https://api.losant.com/#/definitions/application)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "application" in kwargs:
            body = kwargs["application"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

