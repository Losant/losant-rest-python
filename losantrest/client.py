""" Module for Losant API Client class """
# pylint: disable=E0401

import requests
from .access_token import AccessToken
from .access_tokens import AccessTokens
from .application_key import ApplicationKey
from .application_keys import ApplicationKeys
from .application import Application
from .applications import Applications
from .auth import Auth
from .dashboard import Dashboard
from .dashboards import Dashboards
from .data import Data
from .device import Device
from .devices import Devices
from .device_recipe import DeviceRecipe
from .device_recipes import DeviceRecipes
from .event import Event
from .events import Events
from .flow import Flow
from .flows import Flows
from .me import Me
from .org import Org
from .orgs import Orgs
from .webhook import Webhook
from .webhooks import Webhooks
from .losant_error import LosantError

class Client(object):
    """
    Losant API

    User API for accessing Losant data

    Built For Version 1.3.7
    """

    def __init__(self, auth_token=None, url="https://api.losant.com"):
        self.url = url
        self.auth_token = auth_token
        self.access_token = AccessToken(self)
        self.access_tokens = AccessTokens(self)
        self.application_key = ApplicationKey(self)
        self.application_keys = ApplicationKeys(self)
        self.application = Application(self)
        self.applications = Applications(self)
        self.auth = Auth(self)
        self.dashboard = Dashboard(self)
        self.dashboards = Dashboards(self)
        self.data = Data(self)
        self.device = Device(self)
        self.devices = Devices(self)
        self.device_recipe = DeviceRecipe(self)
        self.device_recipes = DeviceRecipes(self)
        self.event = Event(self)
        self.events = Events(self)
        self.flow = Flow(self)
        self.flows = Flows(self)
        self.me = Me(self)
        self.org = Org(self)
        self.orgs = Orgs(self)
        self.webhook = Webhook(self)
        self.webhooks = Webhooks(self)

    def request(self, method, path, params=None, headers=None, body=None):
        """ Base method for making a Losant API request """
        if not headers:
            headers = {}
        if not params:
            params = {}

        headers["Accept"] = "application/json"
        headers["Accept-Version"] = "^1.3.7"
        if self.auth_token:
            headers["Authorization"] = "Bearer {0}".format(self.auth_token)

        path = self.url + path
        response = requests.request(method, path, params=params, headers=headers, json=body)

        result = response.text
        try:
            result = response.json()
        except Exception:
            pass

        if response.status_code >= 400:
            raise LosantError(response.status_code, result)

        return result
