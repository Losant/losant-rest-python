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

""" Module for Losant API ExperienceEndpoints wrapper class """
# pylint: disable=C0301

class ExperienceEndpoints(object):
    """ Class containing all the actions for the Experience Endpoints Resource """

    def __init__(self, client):
        self.client = client

    def get(self, **kwargs):
        """
        Returns the experience endpoints for an application

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Application.read, all.Organization, all.Organization.read, all.User, all.User.read, experienceEndpoints.*, or experienceEndpoints.get.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} sortField - Field to sort the results by. Accepted values are: order, method, route, id, creationDate, requestCount
        *  {string} sortDirection - Direction to sort the results by. Accepted values are: asc, desc
        *  {string} filterField - Field to filter the results by. Blank or not provided means no filtering. Accepted values are: method, route
        *  {string} filter - Filter to apply against the filtered field. Supports globbing. Blank or not provided means no filtering.
        *  {string} experienceGroupId - Filter endpoints to those only in the specified group
        *  {string} requestCountDuration - If set, a count of recent requests is included on each endpoint for the duration requested (milliseconds)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Collection of experience endpoints (https://api.losant.com/#/definitions/experienceEndpoints)

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
        if "filterField" in kwargs:
            query_params["filterField"] = kwargs["filterField"]
        if "filter" in kwargs:
            query_params["filter"] = kwargs["filter"]
        if "experienceGroupId" in kwargs:
            query_params["experienceGroupId"] = kwargs["experienceGroupId"]
        if "requestCountDuration" in kwargs:
            query_params["requestCountDuration"] = kwargs["requestCountDuration"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/experience/endpoints".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def post(self, **kwargs):
        """
        Create a new experience endpoint for an application

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Organization, all.User, experienceEndpoints.*, or experienceEndpoints.post.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {hash} experienceEndpoint - New experience endpoint information (https://api.losant.com/#/definitions/experienceEndpointPost)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  201 - Successfully created experience endpoint (https://api.losant.com/#/definitions/experienceEndpoint)

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
        if "experienceEndpoint" in kwargs:
            body = kwargs["experienceEndpoint"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/experience/endpoints".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

    def stats(self, **kwargs):
        """
        Get statistics about endpoint requests

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Application.read, all.Organization, all.Organization.read, all.User, all.User.read, experienceEndpoints.*, or experienceEndpoints.stats.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} statGrouping - Field to group the statistics by. Accepted values are: statusCode, endpointId
        *  {string} duration - Duration in milliseconds
        *  {string} resolution - Resolution in milliseconds
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Statistics for endpoint requests (https://api.losant.com/#/definitions/experienceEndpointStats)

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
        if "statGrouping" in kwargs:
            query_params["statGrouping"] = kwargs["statGrouping"]
        if "duration" in kwargs:
            query_params["duration"] = kwargs["duration"]
        if "resolution" in kwargs:
            query_params["resolution"] = kwargs["resolution"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/experience/endpoints/stats".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

