# Losant Python REST API Client

[![Build Status](https://travis-ci.org/Losant/losant-rest-python.svg?branch=master)](https://travis-ci.org/Losant/losant-rest-python) [![PyPI version](https://badge.fury.io/py/losant-rest.svg)](https://badge.fury.io/py/losant-rest)

The [Losant](https://www.losant.com) REST API client provides a simple way to
use the comprehensive Losant API.  You can authenticate either as a Losant
device or with your user account, and have access to all the functionality
of the Losant platform.

This client works with both Python 2.7 and 3. It uses
[Requests](https://github.com/kennethreitz/requests/) under the
covers for the actual HTTP communication.

<br/>

## Installation

The latest stable version is available in the Python Package Index (PyPi)
and can be installed using

```bash
pip install losant-rest
```

<br/>

## Example

Below is a high-level example of using the Losant Python REST API client to
authenticate against the Losant Platform and report state for a device.

```python
from losantrest import Client
from analog import AnalogSensor

client = Client()
creds = {
    'deviceId': 'my-device-id',
    'key': 'my-app-access-key',
    'secret': 'my-app-access-secret'
}
response = client.auth.authenticate_device(credentials=creds)

client.auth_token = response['token']
app_id = response['applicationId']

state = {'data': {'temperature': AnalogSensor.read()}}
response = client.device.send_state(deviceId='my-device-id',
    applicationId=app_id, deviceState=state)

print(response)
""" {'success': True} """
```

<br/>

## API Documentation

### Client

A client is a single api instance.  By default, it is unauthenticated,
but can be given an access token to perform authenticated requests.

#### Constructor

```python
Client(auth_token=None, url="https://api.losant.com")
```

The ``Client()`` constructor takes the following arguments:

*   auth_token  
The access token to be used for authentication - by default there is no access
token.  An access token can be acquired through either of
the [Auth](docs/auth.md) methods.

*   url  
The url of the Losant API - by default <https://api.losant.com>.

#### Properties

*   auth_token  
The auth token can be accessed or changed after Client creation
through this property.

*   url  
The api base url can be accessed or changed after Client creation
through this property.

#### Resources

Each of the following is a property on the client object, and returns
a wrapper for the actions against that particular resource.  See each
resource documentation file for more information.

*   [application_key](docs/applicationKey.md)  
Contains all the actions that can be performed against a single
[Application Key](https://docs.losant.com/applications/access-keys/) -
for instance, getting info on a single key or revoking a key.

*   [application_keys](docs/applicationKeys.md)  
Contains all of the actions that can be performed against the collection of
[Application Keys](https://docs.losant.com/applications/access-keys/) belonging
to an Application - such as listing all keys or creating a new key.

*   [application](docs/application.md)  
Contains all of the actions that can be performed against a single
[Application](https://docs.losant.com/applications/overview/),
which include things like getting info on an application or
modifying an application.

*   [applications](docs/applications.md)  
Contains all of the actions that can be performed against the set of
[Applications](https://docs.losant.com/applications/overview/) that the
currently authenticated user has access to - such as
listing the applications or creating a new application.

*   [auth](docs/auth.md)  
Contains the actions used for authenticating against the api, either as a
user or as a device.  The result of authentication calls contain the auth_token
needed for authenticated calls - see the examples for more details.

*   [dashboard](docs/dashboard.md)  
Contains all of the actions that can be performed against a single
[Dashboard](https://docs.losant.com/dashboards/overview/),
which include things like getting info on a dashboard or
modifying a dashboard.

*   [dashboards](docs/dashboards.md)  
Contains all of the actions that can be performed against the set of
[Dashboards](https://docs.losant.com/dashboards/overview/) that the
currently authenticated user has access to - such as
listing the dashboards or creating a new dashboard.

*   [data](docs/data.md)  
Contains the actions for querying against historical Device
data across an Application.

*   [device](docs/device.md)  
Contains all the actions that can be performed against a single
[Device](https://docs.losant.com/devices/overview/) -
for instance, getting info on a single device or reporting the current
state of a device.

*   [devices](docs/devices.md)  
Contains all of the actions that can be performed against the collection of
[Devices](https://docs.losant.com/devices/overview/) belonging
to an Application - such as listing all devices or sending a command to a set
of devices.

*   [device_recipe](docs/deviceRecipe.md)  
Contains all the actions that can be performed against a single
[Device Recipe](https://docs.losant.com/devices/device-recipes/), which
include things like removing a device recipe or creating a device
from a device recipe.

*   [device_recipes](docs/deviceRecipes.md)  
Contains all the actions that can be performed against the collection of
[Device Recipes](https://docs.losant.com/devices/device-recipes/) belonging
to an Application - such as listing recipes or creating a new recipe.

*   [event](docs/event.md)  
Contains all the actions that can be performed against a single
[Event](https://docs.losant.com/events/overview/), such as commenting on
or changing the state of an event.

*   [events](docs/events.md)  
Contains all the actions that can be performed against the collection of
[Events](https://docs.losant.com/events/overview/) belonging
to an Application - such as listing open events or creating a new event.

*   [flow](docs/flow.md)  
Contains all the actions that can be performed against a single
[Workflow](https://docs.losant.com/workflows/overview/), such as enabling or
disabling a workflow, or triggering a virtual button in the workflow.

*   [flows](docs/flows.md)  
Contains all the actions that can be performed against the collection of
[Workflows](https://docs.losant.com/workflows/overview/) belonging
to an Application - such as listing the workflows or creating a new workflow.

*   [me](docs/me.md)  
Contains the actions for operating against the currently authenticated
[User](https://docs.losant.com/user-accounts/overview/) such as changing
the password or linking against external services.

*   [org](docs/org.md)  
Contains all the actions that can be performed against a single
[Organization](https://docs.losant.com/organizations/overview/), things like
inviting a user to the organization, or modifying the organization.

*   [orgs](docs/orgs.md)  
Contains all of the actions that can be performed against the set of
[Organizations](https://docs.losant.com/organizations/overview/) that the
currently authenticated user has access to - such as
listing the organizations or creating a new organization.

*   [webhook](docs/webhook.md)  
Contains all the actions that can be performed against a single
[Webhook](https://docs.losant.com/applications/webhooks/), for instance
modifying the verification settings or removing the webhook.

*   [webhooks](docs/webhooks.md)  
Contains all the actions that can be performed against the collection of
[Webhooks](https://docs.losant.com/applications/webhooks/) belonging
to an Application - such as listing the webhooks or creating a new webhook.

<br/>

*****

Copyright (c) 2016 Losant IoT, Inc

<https://www.losant.com>
