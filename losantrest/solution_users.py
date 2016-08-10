""" Module for Losant API SolutionUsers wrapper class """
# pylint: disable=C0301

class SolutionUsers(object):
    """ Class containing all the actions for the Solution Users Resource """

    def __init__(self, client):
        self.client = client

    def get(self, **kwargs):
        """
        Returns the users for the solution

        Parameters:
        *  {string} orgId - ID associated with the organization
        *  {string} solutionId - ID associated with the solution
        *  {string} sortField - Field to sort the results by. Accepted values are: email, firstName, lastName, id, creationDate, lastLogin
        *  {string} sortDirection - Direction to sort the results by. Accepted values are: asc, desc
        *  {string} page - Which page of results to return
        *  {string} perPage - How many items to return per page
        *  {string} filterField - Field to filter the results by. Blank or not provided means no filtering. Accepted values are: email, firstName, lastName
        *  {string} filter - Filter to apply against the filtered field. Supports globbing. Blank or not provided means no filtering.
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Collection of solution users (https://api.losant.com/#/definitions/solutionUsers)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "orgId" in kwargs:
            path_params["orgId"] = kwargs["orgId"]
        if "solutionId" in kwargs:
            path_params["solutionId"] = kwargs["solutionId"]
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
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/orgs/{orgId}/solutions/{solutionId}/users".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def post(self, **kwargs):
        """
        Create a new solution user

        Parameters:
        *  {string} orgId - ID associated with the organization
        *  {string} solutionId - ID associated with the solution
        *  {hash} solutionUser - New solution user information (https://api.losant.com/#/definitions/solutionUserPost)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  201 - Successfully created solution user (https://api.losant.com/#/definitions/solutionUser)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "orgId" in kwargs:
            path_params["orgId"] = kwargs["orgId"]
        if "solutionId" in kwargs:
            path_params["solutionId"] = kwargs["solutionId"]
        if "solutionUser" in kwargs:
            body = kwargs["solutionUser"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/orgs/{orgId}/solutions/{solutionId}/users".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

