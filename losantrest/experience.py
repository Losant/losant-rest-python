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

""" Module for Losant API Experience wrapper class """
# pylint: disable=C0301

class Experience(object):
    """ Class containing all the actions for the Experience Resource """

    def __init__(self, client):
        self.client = client

    def bootstrap(self, **kwargs):
        """
        Bootstraps the experience for this application with standard endpoints and views

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Organization, all.User, experience.*, or experience.bootstrap.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {hash} options - Bootstrap options (https://api.losant.com/#/definitions/experienceBootstrapOptions)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - If bootstrap was successful (https://api.losant.com/#/definitions/experienceBootstrapResult)

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

        path = "/applications/{applicationId}/experience/bootstrap".format(**path_params)

        return self.client.request("PATCH", path, params=query_params, headers=headers, body=body)

    def delete(self, **kwargs):
        """
        Deletes multiple parts of an experience including users, groups, slugs, domains, versions, endpoints, views, and workflows

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Organization, all.User, experience.*, or experience.delete.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} keepUsers - If this is set, Experience Users will not be removed.
        *  {string} keepGroups - If this is set, Experience Groups will not be removed.
        *  {string} keepSlugs - If this is set, Experience Slugs will not be removed.
        *  {string} keepDomains - If this is set, Experience Domains will not be removed.
        *  {string} removeVersions - If this is set, all Experience Versions and their contents will be removed (except for develop).
        *  {string} keepViews - If this is set, Experience Views (in the develop version) will not be removed.
        *  {string} keepEndpoints - If this is set, Experience Endpoints (in the develop version) will not be removed.
        *  {string} removeWorkflows - If this is set, all Experience Workflows (in the develop version) will ve removed.
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - If deletion was successful (https://api.losant.com/#/definitions/success)

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
        if "keepUsers" in kwargs:
            query_params["keepUsers"] = kwargs["keepUsers"]
        if "keepGroups" in kwargs:
            query_params["keepGroups"] = kwargs["keepGroups"]
        if "keepSlugs" in kwargs:
            query_params["keepSlugs"] = kwargs["keepSlugs"]
        if "keepDomains" in kwargs:
            query_params["keepDomains"] = kwargs["keepDomains"]
        if "removeVersions" in kwargs:
            query_params["removeVersions"] = kwargs["removeVersions"]
        if "keepViews" in kwargs:
            query_params["keepViews"] = kwargs["keepViews"]
        if "keepEndpoints" in kwargs:
            query_params["keepEndpoints"] = kwargs["keepEndpoints"]
        if "removeWorkflows" in kwargs:
            query_params["removeWorkflows"] = kwargs["removeWorkflows"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/experience".format(**path_params)

        return self.client.request("DELETE", path, params=query_params, headers=headers, body=body)

