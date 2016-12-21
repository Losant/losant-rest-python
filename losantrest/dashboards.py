""" Module for Losant API Dashboards wrapper class """
# pylint: disable=C0301

class Dashboards(object):
    """ Class containing all the actions for the Dashboards Resource """

    def __init__(self, client):
        self.client = client

    def get(self, **kwargs):
        """
        Returns the dashboards the current user has permission to see

        Parameters:
        *  {string} sortField - Field to sort the results by. Accepted values are: name, id, creationDate, ownerId
        *  {string} sortDirection - Direction to sort the results by. Accepted values are: asc, desc
        *  {string} page - Which page of results to return
        *  {string} perPage - How many items to return per page
        *  {string} filterField - Field to filter the results by. Blank or not provided means no filtering. Accepted values are: name
        *  {string} filter - Filter to apply against the filtered field. Supports globbing. Blank or not provided means no filtering.
        *  {string} orgId - If not provided, return all dashboards. If provided but blank, only return dashboards belonging to the current user.  If provided and an id, only return dashboards belonging to the given organization id.
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Collection of dashboards (https://api.losant.com/#/definitions/dashboards)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
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
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/dashboards".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def post(self, **kwargs):
        """
        Create a new dashboard

        Parameters:
        *  {hash} dashboard - New dashboard information (https://api.losant.com/#/definitions/dashboardPost)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  201 - Successfully created dashboard (https://api.losant.com/#/definitions/dashboard)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "dashboard" in kwargs:
            body = kwargs["dashboard"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/dashboards".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

