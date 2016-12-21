""" Module for Losant API Devices wrapper class """
# pylint: disable=C0301

class Devices(object):
    """ Class containing all the actions for the Devices Resource """

    def __init__(self, client):
        self.client = client

    def export(self, **kwargs):
        """
        Creates an export of all device metadata.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} email - Email address to send export to.  Defaults to current user&#x27;s email.
        *  {string} callbackUrl - Callback URL to call with export result.
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - If generation of export was successfully started (https://api.losant.com/#/definitions/success)

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
        if "email" in kwargs:
            query_params["email"] = kwargs["email"]
        if "callbackUrl" in kwargs:
            query_params["callbackUrl"] = kwargs["callbackUrl"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/devices/export".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

    def get(self, **kwargs):
        """
        Returns the devices for an application

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} sortField - Field to sort the results by. Accepted values are: name, id, creationDate
        *  {string} sortDirection - Direction to sort the results by. Accepted values are: asc, desc
        *  {string} page - Which page of results to return
        *  {string} perPage - How many items to return per page
        *  {string} filterField - Field to filter the results by. Blank or not provided means no filtering. Accepted values are: name
        *  {string} filter - Filter to apply against the filtered field. Supports globbing. Blank or not provided means no filtering.
        *  {hash} tagFilter - Array of tag pairs to filter by. (https://api.losant.com/#/definitions/deviceTagFilter)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Collection of devices (https://api.losant.com/#/definitions/devices)

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
        if "tagFilter" in kwargs:
            query_params["tagFilter"] = kwargs["tagFilter"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/devices".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def post(self, **kwargs):
        """
        Create a new device for an application

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {hash} device - New device information (https://api.losant.com/#/definitions/devicePost)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  201 - Successfully created device (https://api.losant.com/#/definitions/device)

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
        if "device" in kwargs:
            body = kwargs["device"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/devices".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

    def send_command(self, **kwargs):
        """
        Send a command to multiple devices

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {hash} multiDeviceCommand - Command to send to the device (https://api.losant.com/#/definitions/multiDeviceCommand)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - If command was successfully sent (https://api.losant.com/#/definitions/success)

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
        if "multiDeviceCommand" in kwargs:
            body = kwargs["multiDeviceCommand"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/devices/command".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

