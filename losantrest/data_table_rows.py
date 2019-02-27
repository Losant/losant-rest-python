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

""" Module for Losant API DataTableRows wrapper class """
# pylint: disable=C0301

class DataTableRows(object):
    """ Class containing all the actions for the Data Table Rows Resource """

    def __init__(self, client):
        self.client = client

    def delete(self, **kwargs):
        """
        Delete rows from a data table

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Organization, all.User, dataTableRows.*, or dataTableRows.delete.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} dataTableId - ID associated with the data table
        *  {hash} query - Query to apply to filter the data table (https://api.losant.com/#/definitions/dataTableQuery)
        *  {string} limit - Limit number of rows to delete from data table
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - If request successfully deletes a set of Data Table rows (https://api.losant.com/#/definitions/dataTableRowsDelete)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  404 - Error if data table was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "dataTableId" in kwargs:
            path_params["dataTableId"] = kwargs["dataTableId"]
        if "query" in kwargs:
            body = kwargs["query"]
        if "limit" in kwargs:
            query_params["limit"] = kwargs["limit"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/data-tables/{dataTableId}/rows/delete".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

    def export(self, **kwargs):
        """
        Request an export of the data table's data

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Application.read, all.Organization, all.Organization.read, all.User, all.User.read, dataTableRows.*, or dataTableRows.export.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} dataTableId - ID associated with the data table
        *  {hash} exportData - Object containing export specifications (https://api.losant.com/#/definitions/dataTableRowsExport)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - If request was successfully queued (https://api.losant.com/#/definitions/success)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  404 - Error if data table was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "dataTableId" in kwargs:
            path_params["dataTableId"] = kwargs["dataTableId"]
        if "exportData" in kwargs:
            body = kwargs["exportData"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/data-tables/{dataTableId}/rows/export".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

    def get(self, **kwargs):
        """
        Returns the rows for a data table

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Application.read, all.Organization, all.Organization.read, all.User, all.User.read, dataTableRows.*, or dataTableRows.get.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} dataTableId - ID associated with the data table
        *  {string} sortColumn - Column to sort the rows by
        *  {string} sortDirection - Direction to sort the rows by. Accepted values are: asc, desc
        *  {string} limit - How many rows to return
        *  {string} offset - How many rows to skip
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Collection of data table rows (https://api.losant.com/#/definitions/dataTableRows)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  404 - Error if data table was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "dataTableId" in kwargs:
            path_params["dataTableId"] = kwargs["dataTableId"]
        if "sortColumn" in kwargs:
            query_params["sortColumn"] = kwargs["sortColumn"]
        if "sortDirection" in kwargs:
            query_params["sortDirection"] = kwargs["sortDirection"]
        if "limit" in kwargs:
            query_params["limit"] = kwargs["limit"]
        if "offset" in kwargs:
            query_params["offset"] = kwargs["offset"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/data-tables/{dataTableId}/rows".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def post(self, **kwargs):
        """
        Inserts a new row(s) into a data table

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Organization, all.User, dataTableRows.*, or dataTableRows.post.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} dataTableId - ID associated with the data table
        *  {hash} dataTableRow - The row(s) to insert (https://api.losant.com/#/definitions/dataTableRowInsert)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  201 - Successfully created data table row, or bulk insert count (https://api.losant.com/#/definitions/dataTableRowInsertResult)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  404 - Error if data table was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "dataTableId" in kwargs:
            path_params["dataTableId"] = kwargs["dataTableId"]
        if "dataTableRow" in kwargs:
            body = kwargs["dataTableRow"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/data-tables/{dataTableId}/rows".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

    def query(self, **kwargs):
        """
        Queries for rows from a data table

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Application.read, all.Organization, all.Organization.read, all.User, all.User.read, dataTableRows.*, or dataTableRows.query.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} dataTableId - ID associated with the data table
        *  {string} sortColumn - Column to sort the rows by
        *  {string} sortDirection - Direction to sort the rows by. Accepted values are: asc, desc
        *  {string} limit - How many rows to return
        *  {string} offset - How many rows to skip
        *  {hash} query - Query to apply to filter the data table (https://api.losant.com/#/definitions/dataTableQuery)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Collection of data table rows (https://api.losant.com/#/definitions/dataTableRows)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  404 - Error if data table was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "dataTableId" in kwargs:
            path_params["dataTableId"] = kwargs["dataTableId"]
        if "sortColumn" in kwargs:
            query_params["sortColumn"] = kwargs["sortColumn"]
        if "sortDirection" in kwargs:
            query_params["sortDirection"] = kwargs["sortDirection"]
        if "limit" in kwargs:
            query_params["limit"] = kwargs["limit"]
        if "offset" in kwargs:
            query_params["offset"] = kwargs["offset"]
        if "query" in kwargs:
            body = kwargs["query"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/data-tables/{dataTableId}/rows/query".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

    def truncate(self, **kwargs):
        """
        Delete all data in the data table

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Organization, all.User, dataTableRows.*, or dataTableRows.truncate.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} dataTableId - ID associated with the data table
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - If request successfully deleted **all** rows in the data table, this will **not** send workflow data table deletion triggers (https://api.losant.com/#/definitions/success)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  404 - Error if data table was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "dataTableId" in kwargs:
            path_params["dataTableId"] = kwargs["dataTableId"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/data-tables/{dataTableId}/rows/truncate".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

