"""
The MIT License (MIT)

Copyright (c) 2019 Losant IoT, Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

""" Module for Losant API SolutionUser wrapper class """
# pylint: disable=C0301

class SolutionUser(object):
    """ Class containing all the actions for the Solution User Resource """

    def __init__(self, client):
        self.client = client

    def delete(self, **kwargs):
        """
        Deletes a solution user

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Organization, all.User, solutionUser.*, or solutionUser.delete.

        Parameters:
        *  {string} orgId - ID associated with the organization
        *  {string} solutionId - ID associated with the solution
        *  {string} solutionUserId - ID associated with the solution user
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - If solution user was successfully deleted (https://api.losant.com/#/definitions/success)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  404 - Error if solution user was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "orgId" in kwargs:
            path_params["orgId"] = kwargs["orgId"]
        if "solutionId" in kwargs:
            path_params["solutionId"] = kwargs["solutionId"]
        if "solutionUserId" in kwargs:
            path_params["solutionUserId"] = kwargs["solutionUserId"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/orgs/{orgId}/solutions/{solutionId}/users/{solutionUserId}".format(**path_params)

        return self.client.request("DELETE", path, params=query_params, headers=headers, body=body)

    def get(self, **kwargs):
        """
        Retrieves information on a solution user

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Organization, all.Organization.read, all.User, all.User.read, solutionUser.*, or solutionUser.get.

        Parameters:
        *  {string} orgId - ID associated with the organization
        *  {string} solutionId - ID associated with the solution
        *  {string} solutionUserId - ID associated with the solution user
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Solution user information (https://api.losant.com/#/definitions/solutionUser)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  404 - Error if solution user was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "orgId" in kwargs:
            path_params["orgId"] = kwargs["orgId"]
        if "solutionId" in kwargs:
            path_params["solutionId"] = kwargs["solutionId"]
        if "solutionUserId" in kwargs:
            path_params["solutionUserId"] = kwargs["solutionUserId"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/orgs/{orgId}/solutions/{solutionId}/users/{solutionUserId}".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def patch(self, **kwargs):
        """
        Updates information about a solution user

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Organization, all.User, solutionUser.*, or solutionUser.patch.

        Parameters:
        *  {string} orgId - ID associated with the organization
        *  {string} solutionId - ID associated with the solution
        *  {string} solutionUserId - ID associated with the solution user
        *  {hash} solutionUser - Object containing new properties of the solution user (https://api.losant.com/#/definitions/solutionUserPatch)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Updated solution user information (https://api.losant.com/#/definitions/solutionUser)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  404 - Error if solution user was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "orgId" in kwargs:
            path_params["orgId"] = kwargs["orgId"]
        if "solutionId" in kwargs:
            path_params["solutionId"] = kwargs["solutionId"]
        if "solutionUserId" in kwargs:
            path_params["solutionUserId"] = kwargs["solutionUserId"]
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

        path = "/orgs/{orgId}/solutions/{solutionId}/users/{solutionUserId}".format(**path_params)

        return self.client.request("PATCH", path, params=query_params, headers=headers, body=body)

