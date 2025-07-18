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

""" Module for Losant API Me wrapper class """
# pylint: disable=C0301

class Me(object):
    """ Class containing all the actions for the Me Resource """

    def __init__(self, client):
        self.client = client

    def add_recent_item(self, **kwargs):
        """
        Adds an item to a recent item list

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.User, me.*, or me.addRecentItem.

        Parameters:
        *  {hash} data - Object containing recent item info (https://api.losant.com/#/definitions/recentItem)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Updated recent item list (https://api.losant.com/#/definitions/recentItemList)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "data" in kwargs:
            body = kwargs["data"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/me/recentItems".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

    def change_password(self, **kwargs):
        """
        Changes the current user's password and optionally logs out all other sessions

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.User, me.*, or me.changePassword.

        Parameters:
        *  {hash} data - Object containing the password change info (https://api.losant.com/#/definitions/changePassword)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - A new, valid, auth token (potentially all previous tokens are now invalid) (https://api.losant.com/#/definitions/authedUser)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "data" in kwargs:
            body = kwargs["data"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/me/changePassword".format(**path_params)

        return self.client.request("PATCH", path, params=query_params, headers=headers, body=body)

    def delete(self, **kwargs):
        """
        Deletes the current user

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.User, me.*, or me.delete.

        Parameters:
        *  {hash} credentials - User authentication credentials (https://api.losant.com/#/definitions/userCredentials)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - If the user was successfully deleted (https://api.losant.com/#/definitions/success)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "credentials" in kwargs:
            body = kwargs["credentials"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/me/delete".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

    def device_counts(self, **kwargs):
        """
        Returns device counts by day for the time range specified for all applications the current user owns

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.User, all.User.read, me.*, or me.deviceCounts.

        Parameters:
        *  {string} start - Start of range for device count query (ms since epoch)
        *  {string} end - End of range for device count query (ms since epoch)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Device counts by day (https://api.losant.com/#/definitions/deviceCounts)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "start" in kwargs:
            query_params["start"] = kwargs["start"]
        if "end" in kwargs:
            query_params["end"] = kwargs["end"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/me/deviceCounts".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def disable_two_factor_auth(self, **kwargs):
        """
        Disables multi-factor authentication for the current user

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.User, me.*, or me.disableTwoFactorAuth.

        Parameters:
        *  {hash} data - Object containing multi-factor authentication properties (https://api.losant.com/#/definitions/multiFactorAuthDisable)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Updated user information (https://api.losant.com/#/definitions/me)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "data" in kwargs:
            body = kwargs["data"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/me/disableTwoFactorAuth".format(**path_params)

        return self.client.request("PATCH", path, params=query_params, headers=headers, body=body)

    def disconnect_github(self, **kwargs):
        """
        Disconnects the user from Github

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.User, me.*, or me.disconnectGithub.

        Parameters:
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Updated user information (https://api.losant.com/#/definitions/me)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/me/disconnectGithub".format(**path_params)

        return self.client.request("PATCH", path, params=query_params, headers=headers, body=body)

    def enable_two_factor_auth(self, **kwargs):
        """
        Enables multi-factor authentication for the current user

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.User, me.*, or me.enableTwoFactorAuth.

        Parameters:
        *  {hash} data - Object containing multi-factor authentication properties (https://api.losant.com/#/definitions/multiFactorAuthEnable)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Updated user information (https://api.losant.com/#/definitions/me)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "data" in kwargs:
            body = kwargs["data"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/me/enableTwoFactorAuth".format(**path_params)

        return self.client.request("PATCH", path, params=query_params, headers=headers, body=body)

    def fetch_recent_items(self, **kwargs):
        """
        Gets a recent item list

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.User, all.User.read, me.*, or me.fetchRecentItems.

        Parameters:
        *  {string} parentId - Parent id of the recent list
        *  {undefined} itemType - Item type to get the recent list of. Accepted values are: application, device, flow, dashboard, organization
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Recent item list (https://api.losant.com/#/definitions/recentItemList)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "parentId" in kwargs:
            query_params["parentId"] = kwargs["parentId"]
        if "itemType" in kwargs:
            query_params["itemType"] = kwargs["itemType"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/me/recentItems".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def generate_two_factor_auth(self, **kwargs):
        """
        Returns the multi-factor authentication key for the current user

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.User, me.*, or me.generateTwoFactorAuth.

        Parameters:
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Multi-factor authentication info (https://api.losant.com/#/definitions/multiFactorAuthInfo)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/me/generateTwoFactorAuth".format(**path_params)

        return self.client.request("PATCH", path, params=query_params, headers=headers, body=body)

    def get(self, **kwargs):
        """
        Retrieves information on the current user

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.User, all.User.read, me.*, or me.get.

        Parameters:
        *  {undefined} includeRecent - Should the user include recent app/dashboard info
        *  {string} summaryExclude - Comma-separated list of summary fields to exclude from user summary
        *  {string} summaryInclude - Comma-separated list of summary fields to include in user summary
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Current user information (https://api.losant.com/#/definitions/me)

        Errors:
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "includeRecent" in kwargs:
            query_params["includeRecent"] = kwargs["includeRecent"]
        if "summaryExclude" in kwargs:
            query_params["summaryExclude"] = kwargs["summaryExclude"]
        if "summaryInclude" in kwargs:
            query_params["summaryInclude"] = kwargs["summaryInclude"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/me".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def invite(self, **kwargs):
        """
        Retrieves information for an invitation to an organization

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.User, all.User.read, me.*, or me.invite.

        Parameters:
        *  {string} inviteId - ID associated with the invitation
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Information about invitation (https://api.losant.com/#/definitions/orgInviteUser)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  404 - Error if invite not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

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

        path = "/me/invites/{inviteId}".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def invites(self, **kwargs):
        """
        Retrieves pending organization invitations for a user

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.User, all.User.read, me.*, or me.invites.

        Parameters:
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Information about invitations (https://api.losant.com/#/definitions/orgInvitesUser)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/me/invites".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def notebook_minute_counts(self, **kwargs):
        """
        Returns notebook execution usage by day for the time range specified for all applications the current user owns

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.User, all.User.read, me.*, or me.notebookMinuteCounts.

        Parameters:
        *  {string} start - Start of range for notebook execution query (ms since epoch)
        *  {string} end - End of range for notebook execution query (ms since epoch)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Notebook usage information (https://api.losant.com/#/definitions/notebookMinuteCounts)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "start" in kwargs:
            query_params["start"] = kwargs["start"]
        if "end" in kwargs:
            query_params["end"] = kwargs["end"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/me/notebookMinuteCounts".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def patch(self, **kwargs):
        """
        Updates information about the current user

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.User, me.*, or me.patch.

        Parameters:
        *  {hash} user - Object containing new user properties (https://api.losant.com/#/definitions/mePatch)
        *  {string} summaryExclude - Comma-separated list of summary fields to exclude from user summary
        *  {string} summaryInclude - Comma-separated list of summary fields to include in user summary
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Updated user information (https://api.losant.com/#/definitions/me)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "user" in kwargs:
            body = kwargs["user"]
        if "summaryExclude" in kwargs:
            query_params["summaryExclude"] = kwargs["summaryExclude"]
        if "summaryInclude" in kwargs:
            query_params["summaryInclude"] = kwargs["summaryInclude"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/me".format(**path_params)

        return self.client.request("PATCH", path, params=query_params, headers=headers, body=body)

    def payload_counts(self, **kwargs):
        """
        Returns payload counts for the time range specified for all applications the current user owns

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.User, all.User.read, me.*, or me.payloadCounts.

        Parameters:
        *  {string} start - Start of range for payload count query (ms since epoch)
        *  {string} end - End of range for payload count query (ms since epoch)
        *  {string} asBytes - If the resulting stats should be returned as bytes
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Payload counts, by type and source (https://api.losant.com/#/definitions/payloadStats)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "start" in kwargs:
            query_params["start"] = kwargs["start"]
        if "end" in kwargs:
            query_params["end"] = kwargs["end"]
        if "asBytes" in kwargs:
            query_params["asBytes"] = kwargs["asBytes"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/me/payloadCounts".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def payload_counts_breakdown(self, **kwargs):
        """
        Returns payload counts per resolution in the time range specified for all applications the current user owns

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.User, all.User.read, me.*, or me.payloadCountsBreakdown.

        Parameters:
        *  {string} start - Start of range for payload count query (ms since epoch)
        *  {string} end - End of range for payload count query (ms since epoch)
        *  {string} resolution - Resolution in milliseconds. Accepted values are: 86400000, 3600000
        *  {string} asBytes - If the resulting stats should be returned as bytes
        *  {string} includeNonBillable - If non-billable payloads should be included in the result
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Sum of payload counts by date (https://api.losant.com/#/definitions/payloadCountsBreakdown)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "start" in kwargs:
            query_params["start"] = kwargs["start"]
        if "end" in kwargs:
            query_params["end"] = kwargs["end"]
        if "resolution" in kwargs:
            query_params["resolution"] = kwargs["resolution"]
        if "asBytes" in kwargs:
            query_params["asBytes"] = kwargs["asBytes"]
        if "includeNonBillable" in kwargs:
            query_params["includeNonBillable"] = kwargs["includeNonBillable"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/me/payloadCountsBreakdown".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def refresh_token(self, **kwargs):
        """
        Returns a new auth token based on the current auth token

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.User, or me.*.

        Parameters:
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Successful token regeneration (https://api.losant.com/#/definitions/authedUser)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  401 - Unauthorized error if authentication fails (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/me/refreshToken".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def respond_to_invite(self, **kwargs):
        """
        Accepts or rejects an invitation to an organization

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.User, me.*, or me.respondToInvite.

        Parameters:
        *  {string} inviteId - ID associated with the invitation
        *  {hash} response - Response to invitation (https://api.losant.com/#/definitions/orgInviteActionUser)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Acceptance or rejection of invitation (https://api.losant.com/#/definitions/orgInviteResultUser)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  404 - Error if invitation not found (https://api.losant.com/#/definitions/error)
        *  410 - Error if invitation has expired (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "inviteId" in kwargs:
            path_params["inviteId"] = kwargs["inviteId"]
        if "response" in kwargs:
            body = kwargs["response"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/me/invites/{inviteId}".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

    def transfer_resources(self, **kwargs):
        """
        Moves resources to a new owner

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.User, me.*, or me.transferResources.

        Parameters:
        *  {hash} transfer - Object containing properties of the transfer (https://api.losant.com/#/definitions/resourceTransfer)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - If resource transfer was successful (https://api.losant.com/#/definitions/success)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "transfer" in kwargs:
            body = kwargs["transfer"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/me/transferResources".format(**path_params)

        return self.client.request("PATCH", path, params=query_params, headers=headers, body=body)

    def verify_email(self, **kwargs):
        """
        Sends an email verification to the user

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.User, me.*, or me.verifyEmail.

        Parameters:
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - If email verification was successfully sent (https://api.losant.com/#/definitions/success)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/me/verify-email".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

