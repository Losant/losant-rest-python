Losant Python REST API Client
=============================

The `Losant <https://www.losant.com>`_ REST API client provides a simple way to use the
comprehensive Losant API.  You can authenticate either as a Losant device or with your user
user account, and have access to all the functionality of the Losant platform.

Installation
------------

The latest stable version is available in the Python Package Index (PyPi) and can be installed using

::

    pip install losant-rest


Example
-------

Below is a high-level example of using the Losant Python REST API client to authenticate against
the Losant Platform and report state for a device.

::

    from losantrest import Client
    from analog import Analog

    client = Client()
    creds = {
        "deviceId": "my-device-id",
        "key": "my-app-access-key",
        "secret": "my-app-access-secret"
    }
    response = client.auth.authenticate_device(credentials=creds)

    client.access_token = response["token"]
    app_id = response["applicationId"]

    state = { "temperature": Analog.read() }
    response = client.device.send_state(deviceId="my-device-id",
        applicationId=app_id, deviceState=state)

    print(response)


API Documentation
-----------------

Client
******

A client is a single api instance.  By default, it is unauthenticated, but can be given
an access token to perform authenticated requests.

Constructor
```````````

::

    Client(auth_token=None, url="https://api.losant.com")


The ``Client()`` constructor takes the following arguments:

auth_token
    The access token to be used for authentication - by default there is no access token.  An
    access token can be acquired through either of the `Auth <docs/auth.rst>`_ methods.

url
    The url of the Losant API - by default https://api.losant.com.

Properties
``````````

* auth_token

  The auth token can be accessed or changed after Client creation through this property.

* url

  The api base url can be accessed or changed after Client creation through this property.

Resources
``````````

* application_key (`Application Key <docs/applicationKey.rst>`_)

  Resource wrapper for actions that are preformed on a single Application Key.

* application_keys (`Application Keys <docs/applicationKeys.rst>`_)

  Resource wrapper for actions that are performed on Application Key collections.

* application (`Application <docs/application.rst>`_)

  Resource wrapper for actions that are preformed on a single Application.

* applications (`Applications <docs/applications.rst>`_)

  Resource wrapper for actions that are performed on Application collections.

* auth (`Auth <docs/auth.rst>`_)

  Resource wrapper for the actions to authenticate as a User or as a Device.

* dashboard (`Dashboard <docs/dashboard.rst>`_)

  Resource wrapper for actions that are preformed on a single Dashboard.

* dashboards (`Dashboards <docs/dashboards.rst>`_)

  Resource wrapper for actions that are performed on Dashboard collections.

* data (`Data <docs/data.rst>`_)

  Resource wrapper for querying historical data across an Application.

* device (`Device <docs/device.rst>`_)

  Resource wrapper for actions that are preformed on a single Device.

* devices (`Devices <docs/devices.rst>`_)

  Resource wrapper for actions that are performed on Device collections.

* device_recipe (`Device Recipe <docs/deviceRecipe.rst>`_)

  Resource wrapper for actions that are preformed on a single Device Recipe.

* device_recipes (`Device Recipes <docs/deviceRecipes.rst>`_)

  Resource wrapper for actions that are performed on Device Recipe collections.

* event (`Event <docs/event.rst>`_)

  Resource wrapper for actions that are preformed on a single Event.

* events (`Events <docs/events.rst>`_)

  Resource wrapper for actions that are performed on Event collections.

* flow (`Flow <docs/flow.rst>`_)

  Resource wrapper for actions that are preformed on a single Workflow.

* flows (`Flows <docs/flows.rst>`_)

  Resource wrapper for actions that are performed on Workflow collections.

* me (`Me <docs/me.rst>`_)

  Resource wrapper for actions are performed on the currently authenticated user.

* org (`Org <docs/org.rst>`_)

  Resource wrapper for actions that are preformed on a single Organization.

* orgs (`Orgs <docs/orgs.rst>`_)

  Resource wrapper for actions that are performed on Organization collections.

* webhook (`Webhook <docs/webhook.rst>`_)

  Resource wrapper for actions that are preformed on a single Webhook.

* webhooks (`Webhooks <docs/webhooks.rst>`_)

  Resource wrapper for actions that are performed on Webhook collections.


Copyright (c) 2016 Losant IoT, Inc

https://www.losant.com
