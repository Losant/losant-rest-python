"""
The MIT License (MIT)

Copyright (c) 2022 Losant IoT, Inc.

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

""" Module for Losant API InstanceOrgInvites wrapper class """
# pylint: disable=C0301

class InstanceOrgInvites(object):
    """ Class containing all the actions for the Instance Org Invites Resource """

    def __init__(self, client):
        self.client = client

    def get(self, **kwargs):
        """
        Returns a collection of instance organization invites

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Instance, all.Instance.read, all.User, all.User.read, instanceOrgInvites.*, or instanceOrgInvites.get.

        Parameters:
        *  {string} instanceId - ID associated with the instance
        *  {string} orgId - ID associated with the organization
        *  {string} sortField - Field to sort the results by. Accepted values are: email, role, inviteDate
        *  {string} sortDirection - Direction to sort the results by. Accepted values are: asc, desc
        *  {string} filterField - Field to filter the results by. Blank or not provided means no filtering. Accepted values are: email, role
        *  {string} filter - Filter to apply against the filtered field. Supports globbing. Blank or not provided means no filtering.
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - A collection of instance organization invitations (https://api.losant.com/#/definitions/orgInviteCollection)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  404 - Error if instance or organization was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "instanceId" in kwargs:
            path_params["instanceId"] = kwargs["instanceId"]
        if "orgId" in kwargs:
            path_params["orgId"] = kwargs["orgId"]
        if "sortField" in kwargs:
            query_params["sortField"] = kwargs["sortField"]
        if "sortDirection" in kwargs:
            query_params["sortDirection"] = kwargs["sortDirection"]
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

        path = "/instances/{instanceId}/orgs/{orgId}/invites".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def post(self, **kwargs):
        """
        Invites a member to an instance organization

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Instance, all.User, instanceOrgInvites.*, or instanceOrgInvites.post.

        Parameters:
        *  {string} instanceId - ID associated with the instance
        *  {string} orgId - ID associated with the organization
        *  {hash} invite - Object containing new invite info (https://api.losant.com/#/definitions/orgInvitePost)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  201 - The new organization invite (https://api.losant.com/#/definitions/orgInviteCollection)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  404 - Error if instance or organization was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "instanceId" in kwargs:
            path_params["instanceId"] = kwargs["instanceId"]
        if "orgId" in kwargs:
            path_params["orgId"] = kwargs["orgId"]
        if "invite" in kwargs:
            body = kwargs["invite"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/instances/{instanceId}/orgs/{orgId}/invites".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

