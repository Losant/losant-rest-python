"""
The MIT License (MIT)

Copyright (c) 2018 Losant IoT, Inc.

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

""" Module for Losant API FlowVersion wrapper class """
# pylint: disable=C0301

class FlowVersion(object):
    """ Class containing all the actions for the Flow Version Resource """

    def __init__(self, client):
        self.client = client

    def delete(self, **kwargs):
        """
        Deletes a flow version

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Organization, all.User, flowVersion.*, or flowVersion.delete.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} flowId - ID associated with the flow
        *  {string} flowVersionId - ID associated with the flow version
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - If flow version was successfully deleted (https://api.losant.com/#/definitions/success)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  404 - Error if flow version was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "flowId" in kwargs:
            path_params["flowId"] = kwargs["flowId"]
        if "flowVersionId" in kwargs:
            path_params["flowVersionId"] = kwargs["flowVersionId"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/flows/{flowId}/versions/{flowVersionId}".format(**path_params)

        return self.client.request("DELETE", path, params=query_params, headers=headers, body=body)

    def get(self, **kwargs):
        """
        Retrieves information on a flow version

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Application.read, all.Organization, all.Organization.read, all.User, all.User.read, flowVersion.*, or flowVersion.get.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} flowId - ID associated with the flow
        *  {string} flowVersionId - ID associated with the flow version
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Flow version information (https://api.losant.com/#/definitions/flowVersion)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  404 - Error if flow version was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "flowId" in kwargs:
            path_params["flowId"] = kwargs["flowId"]
        if "flowVersionId" in kwargs:
            path_params["flowVersionId"] = kwargs["flowVersionId"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/flows/{flowId}/versions/{flowVersionId}".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def get_log_entries(self, **kwargs):
        """
        Retrieve the recent log entries about runs of this workflow version

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Application.read, all.Organization, all.Organization.read, all.User, all.User.read, flowVersion.*, or flowVersion.log.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} flowId - ID associated with the flow
        *  {string} flowVersionId - ID associated with the flow version
        *  {string} limit - Max log entries to return (ordered by time descending)
        *  {string} since - Look for log entries since this time (ms since epoch)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Recent log entries (https://api.losant.com/#/definitions/flowLog)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  404 - Error if device was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "flowId" in kwargs:
            path_params["flowId"] = kwargs["flowId"]
        if "flowVersionId" in kwargs:
            path_params["flowVersionId"] = kwargs["flowVersionId"]
        if "limit" in kwargs:
            query_params["limit"] = kwargs["limit"]
        if "since" in kwargs:
            query_params["since"] = kwargs["since"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/flows/{flowId}/versions/{flowVersionId}/logs".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def patch(self, **kwargs):
        """
        Updates information about a flow version

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Organization, all.User, flowVersion.*, or flowVersion.patch.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} flowId - ID associated with the flow
        *  {string} flowVersionId - ID associated with the flow version
        *  {hash} flowVersion - Object containing new properties of the flow version (https://api.losant.com/#/definitions/flowVersionPatch)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Updated flow version information (https://api.losant.com/#/definitions/flowVersion)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  404 - Error if flow version was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "flowId" in kwargs:
            path_params["flowId"] = kwargs["flowId"]
        if "flowVersionId" in kwargs:
            path_params["flowVersionId"] = kwargs["flowVersionId"]
        if "flowVersion" in kwargs:
            body = kwargs["flowVersion"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/flows/{flowId}/versions/{flowVersionId}".format(**path_params)

        return self.client.request("PATCH", path, params=query_params, headers=headers, body=body)

