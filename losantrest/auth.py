""" Module for Losant API Auth wrapper class """
# pylint: disable=C0301

class Auth(object):
    """ Class containing all the actions for the Auth Resource """

    def __init__(self, client):
        self.client = client

    def authenticate_device(self, **kwargs):
        """
        Authenticates a device using the provided credentials

        Parameters:
        *  {hash} credentials - Device authentication credentials (https://api.losant.com/#/definitions/deviceCredentials)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Successful authentication (https://api.losant.com/#/definitions/authedDevice)

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
        Authenticates a solution user using the provided credentials

        Parameters:
        *  {hash} credentials - Solution user authentication credentials (https://api.losant.com/#/definitions/solutionUserCredentials)
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
        Authenticates a user using the provided credentials

        Parameters:
        *  {hash} credentials - User authentication credentials (https://api.losant.com/#/definitions/userCredentials)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Successful authentication (https://api.losant.com/#/definitions/authedUser)

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
        Authenticates a user via GitHub OAuth

        Parameters:
        *  {hash} oauth - User authentication credentials (access token) (https://api.losant.com/#/definitions/githubLogin)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Successful authentication (https://api.losant.com/#/definitions/authedUser)

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

