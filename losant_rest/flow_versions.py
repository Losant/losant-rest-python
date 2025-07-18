"""
The MIT License (MIT)

Copyright (c) 2025 Losant IoT, Inc.

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


import json

""" Module for Losant API FlowVersions wrapper class """
# pylint: disable=C0301

class FlowVersions(object):
    """ Class containing all the actions for the Flow Versions Resource """

    def __init__(self, client):
        self.client = client

    def delete(self, **kwargs):
        """
        Delete flow versions

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Organization, all.User, flowVersions.*, or flowVersions.delete.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} flowId - ID associated with the flow
        *  {hash} options - Object containing flow version deletion options (https://api.losant.com/#/definitions/flowVersionsDeletePost)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Object indicating number of flow versions deleted or failed (https://api.losant.com/#/definitions/bulkDeleteResponse)
        *  202 - If a job was enqueued for the flow versions to be deleted (https://api.losant.com/#/definitions/jobEnqueuedResult)

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
        if "flowId" in kwargs:
            path_params["flowId"] = kwargs["flowId"]
        if "options" in kwargs:
            body = kwargs["options"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/flows/{flowId}/versions/delete".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

    def get(self, **kwargs):
        """
        Returns the flow versions for a flow

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Application.read, all.Organization, all.Organization.read, all.User, all.User.read, flowVersions.*, or flowVersions.get.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} flowId - ID associated with the flow
        *  {string} sortField - Field to sort the results by. Accepted values are: version, id, creationDate, lastUpdated
        *  {string} sortDirection - Direction to sort the results by. Accepted values are: asc, desc
        *  {string} page - Which page of results to return
        *  {string} perPage - How many items to return per page
        *  {string} filterField - Field to filter the results by. Blank or not provided means no filtering. Accepted values are: version
        *  {string} filter - Filter to apply against the filtered field. Supports globbing. Blank or not provided means no filtering.
        *  {string} includeCustomNodes - If the result of the request should also include the details of any custom nodes referenced by the returned workflows
        *  {hash} query - Workflow filter JSON object which overrides the filterField and filter parameters. (https://api.losant.com/#/definitions/advancedFlowVersionQuery)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Collection of flow versions (https://api.losant.com/#/definitions/flowVersions)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  404 - Error if flow was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "flowId" in kwargs:
            path_params["flowId"] = kwargs["flowId"]
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
        if "includeCustomNodes" in kwargs:
            query_params["includeCustomNodes"] = kwargs["includeCustomNodes"]
        if "query" in kwargs:
            query_params["query"] = json.dumps(kwargs["query"])
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/flows/{flowId}/versions".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def post(self, **kwargs):
        """
        Create or replace a flow version for a flow

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Organization, all.User, flowVersions.*, or flowVersions.post.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} flowId - ID associated with the flow
        *  {hash} flowVersion - New flow version information (https://api.losant.com/#/definitions/flowVersionPost)
        *  {string} includeCustomNodes - If the result of the request should also include the details of any custom nodes referenced by the returned workflows
        *  {string} allowReplacement - Allow replacement of an existing flow version with same version name
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  201 - Successfully created flow version (https://api.losant.com/#/definitions/flowVersion)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  404 - Error if flow was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "flowId" in kwargs:
            path_params["flowId"] = kwargs["flowId"]
        if "flowVersion" in kwargs:
            body = kwargs["flowVersion"]
        if "includeCustomNodes" in kwargs:
            query_params["includeCustomNodes"] = kwargs["includeCustomNodes"]
        if "allowReplacement" in kwargs:
            query_params["allowReplacement"] = kwargs["allowReplacement"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/flows/{flowId}/versions".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

