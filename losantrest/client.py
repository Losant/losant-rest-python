""" Module for Losant API Client class """
# pylint: disable=E0401

import requests
import collections
import sys
from .access_token import AccessToken
from .access_tokens import AccessTokens
from .application import Application
from .application_key import ApplicationKey
from .application_keys import ApplicationKeys
from .applications import Applications
from .auth import Auth
from .dashboard import Dashboard
from .dashboards import Dashboards
from .data import Data
from .device import Device
from .device_recipe import DeviceRecipe
from .device_recipes import DeviceRecipes
from .devices import Devices
from .event import Event
from .events import Events
from .flow import Flow
from .flows import Flows
from .me import Me
from .org import Org
from .orgs import Orgs
from .solution import Solution
from .solution_user import SolutionUser
from .solution_users import SolutionUsers
from .solutions import Solutions
from .webhook import Webhook
from .webhooks import Webhooks
from .losant_error import LosantError

if sys.version_info[0] == 3:
    basestring = str

class Client(object):
    """
    Losant API

    User API for accessing Losant data

    Built For Version 1.5.1
    """

    def __init__(self, auth_token=None, url="https://api.losant.com"):
        self.url = url
        self.auth_token = auth_token
        self.access_token = AccessToken(self)
        self.access_tokens = AccessTokens(self)
        self.application = Application(self)
        self.application_key = ApplicationKey(self)
        self.application_keys = ApplicationKeys(self)
        self.applications = Applications(self)
        self.auth = Auth(self)
        self.dashboard = Dashboard(self)
        self.dashboards = Dashboards(self)
        self.data = Data(self)
        self.device = Device(self)
        self.device_recipe = DeviceRecipe(self)
        self.device_recipes = DeviceRecipes(self)
        self.devices = Devices(self)
        self.event = Event(self)
        self.events = Events(self)
        self.flow = Flow(self)
        self.flows = Flows(self)
        self.me = Me(self)
        self.org = Org(self)
        self.orgs = Orgs(self)
        self.solution = Solution(self)
        self.solution_user = SolutionUser(self)
        self.solution_users = SolutionUsers(self)
        self.solutions = Solutions(self)
        self.webhook = Webhook(self)
        self.webhooks = Webhooks(self)

    def request(self, method, path, params=None, headers=None, body=None):
        """ Base method for making a Losant API request """
        if not headers:
            headers = {}
        if not params:
            params = {}

        headers["Accept"] = "application/json"
        headers["Accept-Version"] = "^1.5.1"
        if self.auth_token:
            headers["Authorization"] = "Bearer {0}".format(self.auth_token)

        path = self.url + path
        params = self.flatten_params(params)
        response = requests.request(method, path, params=params, headers=headers, json=body)

        result = response.text
        try:
            result = response.json()
        except Exception:
            pass

        if response.status_code >= 400:
            raise LosantError(response.status_code, result)

        return result

    def flatten_params(self, data, base_key=None):
        """ Flatten out nested arrays and dicts in query params into correct format """
        result = {}

        if data is None:
            return result

        map_data = None
        if not isinstance(data, collections.Mapping):
            map_data = []
            for idx, val in enumerate(data):
                map_data.append([str(idx), val])
        else:
            map_data = list(data.items())

        for key, value in map_data:
            if not base_key is None:
                key = base_key + "[" + key + "]"

            if isinstance(value, basestring) or not hasattr(value, "__iter__"):
                result[key] = value
            else:
                result.update(self.flatten_params(value, key))

        return result
