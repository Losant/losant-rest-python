""" Module for Losant API DeviceRecipe wrapper class """
# pylint: disable=C0301

class DeviceRecipe(object):
    """ Class containing all the actions for the Device Recipe Resource """

    def __init__(self, client):
        self.client = client

    def bulk_create(self, **kwargs):
        """
        Bulk creates devices using this recipe from a CSV

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} deviceRecipeId - ID associated with the device recipe
        *  {hash} bulkInfo - Object containing bulk creation info (https://api.losant.com/#/definitions/deviceRecipeBulkCreatePost)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  201 - If devices were sucessfully created (https://api.losant.com/#/definitions/deviceRecipeBulkCreate)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  404 - Error if device recipe was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "deviceRecipeId" in kwargs:
            path_params["deviceRecipeId"] = kwargs["deviceRecipeId"]
        if "bulkInfo" in kwargs:
            body = kwargs["bulkInfo"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/device-recipes/{deviceRecipeId}/bulkCreate".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

    def delete(self, **kwargs):
        """
        Deletes a device recipe

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} deviceRecipeId - ID associated with the device recipe
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - If device recipe was successfully deleted (https://api.losant.com/#/definitions/success)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  404 - Error if device recipe was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "deviceRecipeId" in kwargs:
            path_params["deviceRecipeId"] = kwargs["deviceRecipeId"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/device-recipes/{deviceRecipeId}".format(**path_params)

        return self.client.request("DELETE", path, params=query_params, headers=headers, body=body)

    def get(self, **kwargs):
        """
        Retrieves information on a device recipe

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} deviceRecipeId - ID associated with the device recipe
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Device recipe information (https://api.losant.com/#/definitions/deviceRecipe)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  404 - Error if device recipe was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "deviceRecipeId" in kwargs:
            path_params["deviceRecipeId"] = kwargs["deviceRecipeId"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/device-recipes/{deviceRecipeId}".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def patch(self, **kwargs):
        """
        Updates information about a device recipe

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} deviceRecipeId - ID associated with the device recipe
        *  {hash} deviceRecipe - Object containing new properties of the device recipe (https://api.losant.com/#/definitions/deviceRecipePatch)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Updated device recipe information (https://api.losant.com/#/definitions/deviceRecipe)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  404 - Error if device recipe was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "deviceRecipeId" in kwargs:
            path_params["deviceRecipeId"] = kwargs["deviceRecipeId"]
        if "deviceRecipe" in kwargs:
            body = kwargs["deviceRecipe"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/device-recipes/{deviceRecipeId}".format(**path_params)

        return self.client.request("PATCH", path, params=query_params, headers=headers, body=body)

