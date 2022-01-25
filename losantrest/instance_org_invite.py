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

""" Module for Losant API InstanceOrgInvite wrapper class """
# pylint: disable=C0301

class InstanceOrgInvite(object):
    """ Class containing all the actions for the Instance Org Invite Resource """

    def __init__(self, client):
        self.client = client

    def delete(self, **kwargs):
        """
        Revokes an instance org invitation

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Instance, all.User, instanceOrgInvite.*, or instanceOrgInvite.delete.

        Parameters:
        *  {string} instanceId - ID associated with the instance
        *  {string} orgId - ID associated with the organization
        *  {string} inviteId - ID associated with the organization invite
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - If an invite was successfully deleted (https://api.losant.com/#/definitions/success)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  404 - Error if instance, organization or invite was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "instanceId" in kwargs:
            path_params["instanceId"] = kwargs["instanceId"]
        if "orgId" in kwargs:
            path_params["orgId"] = kwargs["orgId"]
        if "inviteId" in kwargs:
            path_params["inviteId"] = kwargs["inviteId"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/instances/{instanceId}/orgs/{orgId}/invites/{inviteId}".format(**path_params)

        return self.client.request("DELETE", path, params=query_params, headers=headers, body=body)

    def get(self, **kwargs):
        """
        Returns an organization invite

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Instance, all.Instance.read, all.User, all.User.read, instanceOrgInvite.*, or instanceOrgInvite.get.

        Parameters:
        *  {string} instanceId - ID associated with the instance
        *  {string} orgId - ID associated with the organization
        *  {string} inviteId - ID associated with the organization invite
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - A single organization invite (https://api.losant.com/#/definitions/orgInvite)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  404 - Error if instance, organization, or invite was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "instanceId" in kwargs:
            path_params["instanceId"] = kwargs["instanceId"]
        if "orgId" in kwargs:
            path_params["orgId"] = kwargs["orgId"]
        if "inviteId" in kwargs:
            path_params["inviteId"] = kwargs["inviteId"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/instances/{instanceId}/orgs/{orgId}/invites/{inviteId}".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def resend_invite(self, **kwargs):
        """
        Resend an organization invite with modified role info

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Instance, all.User, instanceOrgInvite.*, or instanceOrgInvite.resendInvite.

        Parameters:
        *  {string} instanceId - ID associated with the instance
        *  {string} orgId - ID associated with the organization
        *  {string} inviteId - ID associated with the organization invite
        *  {hash} roleInfo - Object containing updated role info (https://api.losant.com/#/definitions/orgRoleInfo)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  201 - The new org invite (https://api.losant.com/#/definitions/orgInvite)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  404 - Error if instance, organization, or invite was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "instanceId" in kwargs:
            path_params["instanceId"] = kwargs["instanceId"]
        if "orgId" in kwargs:
            path_params["orgId"] = kwargs["orgId"]
        if "inviteId" in kwargs:
            path_params["inviteId"] = kwargs["inviteId"]
        if "roleInfo" in kwargs:
            body = kwargs["roleInfo"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/instances/{instanceId}/orgs/{orgId}/invites/{inviteId}".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

