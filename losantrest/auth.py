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

""" Module for Losant API Auth wrapper class """
# pylint: disable=C0301

class Auth(object):
    """ Class containing all the actions for the Auth Resource """

    def __init__(self, client):
        self.client = client

    def authenticate_device(self, **kwargs):
        """
        Authenticates a device using the provided credentials.

        Authentication:
        No api access token is required to call this action.

        Parameters:
        *  {hash} credentials - Device authentication credentials (https://api.losant.com/#/definitions/deviceCredentials)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Successful authentication. The included api access token has the scope 'all.Device'. (https://api.losant.com/#/definitions/authedDevice)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  401 - Unauthorized error if authentication fails (https://api.losant.com/#/definitions/error)
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

        path = "/auth/device".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

    def authenticate_solution_user(self, **kwargs):
        """
        Authenticates a solution user using the provided credentials.

        Authentication:
        No api access token is required to call this action.

        Parameters:
        *  {hash} credentials - Solution user authentication credentials. The included api access token has the scope 'all.SolutionUser'. (https://api.losant.com/#/definitions/solutionUserCredentials)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Successful authentication (https://api.losant.com/#/definitions/authedSolutionUser)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  401 - Unauthorized error if authentication fails (https://api.losant.com/#/definitions/error)
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

        path = "/auth/solutionUser".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

    def authenticate_user(self, **kwargs):
        """
        Authenticates a user using the provided credentials.

        Authentication:
        No api access token is required to call this action.

        Parameters:
        *  {hash} credentials - User authentication credentials (https://api.losant.com/#/definitions/userCredentials)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Successful authentication. The included api access token has the scope 'all.User'. (https://api.losant.com/#/definitions/authedUser)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  401 - Unauthorized error if authentication fails (https://api.losant.com/#/definitions/error)
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

        path = "/auth/user".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

    def authenticate_user_github(self, **kwargs):
        """
        Authenticates a user via GitHub OAuth.

        Authentication:
        No api access token is required to call this action.

        Parameters:
        *  {hash} oauth - User authentication credentials (access token) (https://api.losant.com/#/definitions/githubLogin)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Successful authentication. The included api access token has the scope 'all.User'. (https://api.losant.com/#/definitions/authedUser)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  401 - Unauthorized error if authentication fails (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "oauth" in kwargs:
            body = kwargs["oauth"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/auth/user/github".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

