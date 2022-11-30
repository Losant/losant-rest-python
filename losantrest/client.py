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

""" Module for Losant API Client class """
# pylint: disable=E0401

import requests
try:
    from collections.abc import Mapping
except ImportError:
    from collections import Mapping
import sys
from .application import Application
from .application_api_token import ApplicationApiToken
from .application_api_tokens import ApplicationApiTokens
from .application_certificate import ApplicationCertificate
from .application_certificate_authorities import ApplicationCertificateAuthorities
from .application_certificate_authority import ApplicationCertificateAuthority
from .application_certificates import ApplicationCertificates
from .application_dashboard import ApplicationDashboard
from .application_dashboards import ApplicationDashboards
from .application_key import ApplicationKey
from .application_keys import ApplicationKeys
from .application_template import ApplicationTemplate
from .application_templates import ApplicationTemplates
from .applications import Applications
from .audit_log import AuditLog
from .audit_logs import AuditLogs
from .auth import Auth
from .dashboard import Dashboard
from .dashboards import Dashboards
from .data import Data
from .data_table import DataTable
from .data_table_row import DataTableRow
from .data_table_rows import DataTableRows
from .data_tables import DataTables
from .device import Device
from .device_recipe import DeviceRecipe
from .device_recipes import DeviceRecipes
from .devices import Devices
from .edge_deployment import EdgeDeployment
from .edge_deployments import EdgeDeployments
from .embedded_deployment import EmbeddedDeployment
from .embedded_deployments import EmbeddedDeployments
from .event import Event
from .events import Events
from .experience import Experience
from .experience_domain import ExperienceDomain
from .experience_domains import ExperienceDomains
from .experience_endpoint import ExperienceEndpoint
from .experience_endpoints import ExperienceEndpoints
from .experience_group import ExperienceGroup
from .experience_groups import ExperienceGroups
from .experience_slug import ExperienceSlug
from .experience_slugs import ExperienceSlugs
from .experience_user import ExperienceUser
from .experience_users import ExperienceUsers
from .experience_version import ExperienceVersion
from .experience_versions import ExperienceVersions
from .experience_view import ExperienceView
from .experience_views import ExperienceViews
from .file import File
from .files import Files
from .flow import Flow
from .flow_version import FlowVersion
from .flow_versions import FlowVersions
from .flows import Flows
from .instance import Instance
from .instance_api_token import InstanceApiToken
from .instance_api_tokens import InstanceApiTokens
from .instance_custom_node import InstanceCustomNode
from .instance_custom_nodes import InstanceCustomNodes
from .instance_member import InstanceMember
from .instance_members import InstanceMembers
from .instance_org import InstanceOrg
from .instance_org_invite import InstanceOrgInvite
from .instance_org_invites import InstanceOrgInvites
from .instance_org_member import InstanceOrgMember
from .instance_org_members import InstanceOrgMembers
from .instance_orgs import InstanceOrgs
from .instance_sandbox import InstanceSandbox
from .instance_sandboxes import InstanceSandboxes
from .instances import Instances
from .integration import Integration
from .integrations import Integrations
from .me import Me
from .notebook import Notebook
from .notebooks import Notebooks
from .org import Org
from .org_invites import OrgInvites
from .orgs import Orgs
from .resource_job import ResourceJob
from .resource_jobs import ResourceJobs
from .user_api_token import UserApiToken
from .user_api_tokens import UserApiTokens
from .webhook import Webhook
from .webhooks import Webhooks
from .losant_error import LosantError

if sys.version_info[0] == 3:
    basestring = str

class Client(object):
    """
    Losant API

    User API for accessing Losant data

    Built For Version 1.24.0
    """

    def __init__(self, auth_token=None, url="https://api.losant.com"):
        self.url = url
        self.auth_token = auth_token
        self.application = Application(self)
        self.application_api_token = ApplicationApiToken(self)
        self.application_api_tokens = ApplicationApiTokens(self)
        self.application_certificate = ApplicationCertificate(self)
        self.application_certificate_authorities = ApplicationCertificateAuthorities(self)
        self.application_certificate_authority = ApplicationCertificateAuthority(self)
        self.application_certificates = ApplicationCertificates(self)
        self.application_dashboard = ApplicationDashboard(self)
        self.application_dashboards = ApplicationDashboards(self)
        self.application_key = ApplicationKey(self)
        self.application_keys = ApplicationKeys(self)
        self.application_template = ApplicationTemplate(self)
        self.application_templates = ApplicationTemplates(self)
        self.applications = Applications(self)
        self.audit_log = AuditLog(self)
        self.audit_logs = AuditLogs(self)
        self.auth = Auth(self)
        self.dashboard = Dashboard(self)
        self.dashboards = Dashboards(self)
        self.data = Data(self)
        self.data_table = DataTable(self)
        self.data_table_row = DataTableRow(self)
        self.data_table_rows = DataTableRows(self)
        self.data_tables = DataTables(self)
        self.device = Device(self)
        self.device_recipe = DeviceRecipe(self)
        self.device_recipes = DeviceRecipes(self)
        self.devices = Devices(self)
        self.edge_deployment = EdgeDeployment(self)
        self.edge_deployments = EdgeDeployments(self)
        self.embedded_deployment = EmbeddedDeployment(self)
        self.embedded_deployments = EmbeddedDeployments(self)
        self.event = Event(self)
        self.events = Events(self)
        self.experience = Experience(self)
        self.experience_domain = ExperienceDomain(self)
        self.experience_domains = ExperienceDomains(self)
        self.experience_endpoint = ExperienceEndpoint(self)
        self.experience_endpoints = ExperienceEndpoints(self)
        self.experience_group = ExperienceGroup(self)
        self.experience_groups = ExperienceGroups(self)
        self.experience_slug = ExperienceSlug(self)
        self.experience_slugs = ExperienceSlugs(self)
        self.experience_user = ExperienceUser(self)
        self.experience_users = ExperienceUsers(self)
        self.experience_version = ExperienceVersion(self)
        self.experience_versions = ExperienceVersions(self)
        self.experience_view = ExperienceView(self)
        self.experience_views = ExperienceViews(self)
        self.file = File(self)
        self.files = Files(self)
        self.flow = Flow(self)
        self.flow_version = FlowVersion(self)
        self.flow_versions = FlowVersions(self)
        self.flows = Flows(self)
        self.instance = Instance(self)
        self.instance_api_token = InstanceApiToken(self)
        self.instance_api_tokens = InstanceApiTokens(self)
        self.instance_custom_node = InstanceCustomNode(self)
        self.instance_custom_nodes = InstanceCustomNodes(self)
        self.instance_member = InstanceMember(self)
        self.instance_members = InstanceMembers(self)
        self.instance_org = InstanceOrg(self)
        self.instance_org_invite = InstanceOrgInvite(self)
        self.instance_org_invites = InstanceOrgInvites(self)
        self.instance_org_member = InstanceOrgMember(self)
        self.instance_org_members = InstanceOrgMembers(self)
        self.instance_orgs = InstanceOrgs(self)
        self.instance_sandbox = InstanceSandbox(self)
        self.instance_sandboxes = InstanceSandboxes(self)
        self.instances = Instances(self)
        self.integration = Integration(self)
        self.integrations = Integrations(self)
        self.me = Me(self)
        self.notebook = Notebook(self)
        self.notebooks = Notebooks(self)
        self.org = Org(self)
        self.org_invites = OrgInvites(self)
        self.orgs = Orgs(self)
        self.resource_job = ResourceJob(self)
        self.resource_jobs = ResourceJobs(self)
        self.user_api_token = UserApiToken(self)
        self.user_api_tokens = UserApiTokens(self)
        self.webhook = Webhook(self)
        self.webhooks = Webhooks(self)

    def request(self, method, path, params=None, headers=None, body=None):
        """ Base method for making a Losant API request """
        if not headers:
            headers = {}
        if not params:
            params = {}

        headers["Accept"] = "application/json"
        headers["Accept-Version"] = "^1.24.0"
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
        if not isinstance(data, Mapping):
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
