""" Module for Losant API Solution wrapper class """
# pylint: disable=C0301

class Solution(object):
    """ Class containing all the actions for the Solution Resource """

    def __init__(self, client):
        self.client = client

    def delete(self, **kwargs):
        """
        Deletes a solution

        Parameters:
        *  {string} orgId - ID associated with the organization
        *  {string} solutionId - ID associated with the solution
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - If solution was successfully deleted (https://api.losant.com/#/definitions/success)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  404 - Error if solution was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "orgId" in kwargs:
            path_params["orgId"] = kwargs["orgId"]
        if "solutionId" in kwargs:
            path_params["solutionId"] = kwargs["solutionId"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/orgs/{orgId}/solutions/{solutionId}".format(**path_params)

        return self.client.request("DELETE", path, params=query_params, headers=headers, body=body)

    def get(self, **kwargs):
        """
        Retrieves information on a solution

        Parameters:
        *  {string} orgId - ID associated with the organization
        *  {string} solutionId - ID associated with the solution
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Solution information (https://api.losant.com/#/definitions/solution)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  404 - Error if solution was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "orgId" in kwargs:
            path_params["orgId"] = kwargs["orgId"]
        if "solutionId" in kwargs:
            path_params["solutionId"] = kwargs["solutionId"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/orgs/{orgId}/solutions/{solutionId}".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def patch(self, **kwargs):
        """
        Updates information about a solution

        Parameters:
        *  {string} orgId - ID associated with the organization
        *  {string} solutionId - ID associated with the solution
        *  {hash} solution - Object containing new properties of the solution (https://api.losant.com/#/definitions/solutionPatch)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Updated solution information (https://api.losant.com/#/definitions/solution)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  404 - Error if solution was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "orgId" in kwargs:
            path_params["orgId"] = kwargs["orgId"]
        if "solutionId" in kwargs:
            path_params["solutionId"] = kwargs["solutionId"]
        if "solution" in kwargs:
            body = kwargs["solution"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/orgs/{orgId}/solutions/{solutionId}".format(**path_params)

        return self.client.request("PATCH", path, params=query_params, headers=headers, body=body)

