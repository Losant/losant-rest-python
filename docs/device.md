# Device Actions

Details on the various actions that can be performed on the
Device resource, including the expected
parameters and the potential responses.

##### Contents

*   [Delete](#delete)
*   [Export](#export)
*   [Get](#get)
*   [Get Command](#get-command)
*   [Get Composite State](#get-composite-state)
*   [Get Log Entries](#get-log-entries)
*   [Get State](#get-state)
*   [Patch](#patch)
*   [Remove Data](#remove-data)
*   [Send Command](#send-command)
*   [Send State](#send-state)
*   [Set Connection Status](#set-connection-status)

<br/>

## Delete

Deletes a device

```python
result = client.device.delete(
    applicationId=my_application_id,
    deviceId=my_device_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Organization, all.User, device.*, or device.delete.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| deviceId | string | Y | ID associated with the device |  | 575ecf887ae143cd83dc4aa2 |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Success](_schemas.md#success) | If device was successfully deleted |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if device was not found |

<br/>

## Export

Creates a device data export. Defaults to all data.

```python
result = client.device.export(
    applicationId=my_application_id,
    deviceId=my_device_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Application.read, all.Organization, all.Organization.read, all.User, all.User.read, device.*, or device.export.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| deviceId | string | Y | ID associated with the device |  | 575ecf887ae143cd83dc4aa2 |
| start | string | N | Start time of export (ms since epoch - 0 means now, negative is relative to now) | 1 | 1465790400000 |
| end | string | N | End time of export (ms since epoch - 0 means now, negative is relative to now) | 0 | 1465790400000 |
| email | string | N | Email address to send export to. Defaults to current user&#x27;s email. |  | email@example.com |
| callbackUrl | string | N | Callback URL to call with export result |  | https://example.com/cburl |
| includeBlobData | string | N | If set will export any blob attributes in base64 form, otherwise they will be downloadable links which will expire. |  | true |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Success](_schemas.md#success) | If generation of export was successfully started |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if device was not found |

<br/>

## Get

Retrieves information on a device

```python
result = client.device.get(
    applicationId=my_application_id,
    deviceId=my_device_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Application.read, all.Device, all.Device.read, all.Organization, all.Organization.read, all.User, all.User.read, device.*, or device.get.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| deviceId | string | Y | ID associated with the device |  | 575ecf887ae143cd83dc4aa2 |
| excludeConnectionInfo | string | N | If set, do not return connection info |  | true |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Device](_schemas.md#device) | Device information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if device was not found |

<br/>

## Get Command

Retrieve the last known commands(s) sent to the device

```python
result = client.device.get_command(
    applicationId=my_application_id,
    deviceId=my_device_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Application.read, all.Device, all.Device.read, all.Organization, all.Organization.read, all.User, all.User.read, device.*, or device.getCommand.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| deviceId | string | Y | ID associated with the device |  | 575ecf887ae143cd83dc4aa2 |
| limit | string | N | Max command entries to return (ordered by time descending) | 1 | 10 |
| since | string | N | Look for command entries since this time (ms since epoch) |  | 1465790400000 |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Device Commands](_schemas.md#device-commands) | Recent device commands |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if device was not found |

<br/>

## Get Composite State

Retrieve the composite last complete state of the device

```python
result = client.device.get_composite_state(
    applicationId=my_application_id,
    deviceId=my_device_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Application.read, all.Device, all.Device.read, all.Organization, all.Organization.read, all.User, all.User.read, device.*, or device.getCompositeState.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| deviceId | string | Y | ID associated with the device |  | 575ecf887ae143cd83dc4aa2 |
| start | string | N | Start of time range to look at to build composite state | 1 | 1465790400000 |
| end | string | N | End of time range to look at to build composite state | 0 | 1465790400000 |
| attributes | string | N | Comma-separated list of attributes to include. When not provided, returns all attributes. |  | myAttr1,myAttr2 |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Composite Device State](_schemas.md#composite-device-state) | Composite last state of the device |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if device was not found |

<br/>

## Get Log Entries

Retrieve the recent log entries about the device

```python
result = client.device.get_log_entries(
    applicationId=my_application_id,
    deviceId=my_device_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Application.read, all.Device, all.Device.read, all.Organization, all.Organization.read, all.User, all.User.read, device.*, or device.getLogEntries.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| deviceId | string | Y | ID associated with the device |  | 575ecf887ae143cd83dc4aa2 |
| limit | string | N | Max log entries to return (ordered by time descending) | 1 | 10 |
| since | string | N | Look for log entries since this time (ms since epoch) |  | 1465790400000 |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Device Log](_schemas.md#device-log) | Recent log entries |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if device was not found |

<br/>

## Get State

Retrieve the last known state(s) of the device

```python
result = client.device.get_state(
    applicationId=my_application_id,
    deviceId=my_device_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Application.read, all.Device, all.Device.read, all.Organization, all.Organization.read, all.User, all.User.read, device.*, or device.getState.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| deviceId | string | Y | ID associated with the device |  | 575ecf887ae143cd83dc4aa2 |
| limit | string | N | Max state entries to return (ordered by time descending) | 1 | 10 |
| since | string | N | Look for state entries since this time (ms since epoch) |  | 1465790400000 |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Device States](_schemas.md#device-states) | Recent device states |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if device was not found |

<br/>

## Patch

Updates information about a device

```python
result = client.device.patch(
    applicationId=my_application_id,
    deviceId=my_device_id,
    device=my_device)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Organization, all.User, device.*, or device.patch.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| deviceId | string | Y | ID associated with the device |  | 575ecf887ae143cd83dc4aa2 |
| device | [Device Patch](_schemas.md#device-patch) | Y | Object containing new properties of the device |  | [Device Patch Example](_schemas.md#device-patch-example) |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Device](_schemas.md#device) | Updated device information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if device was not found |

<br/>

## Remove Data

Removes all device data for the specified time range. Defaults to all data.

```python
result = client.device.remove_data(
    applicationId=my_application_id,
    deviceId=my_device_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Organization, all.User, device.*, or device.removeData.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| deviceId | string | Y | ID associated with the device |  | 575ecf887ae143cd83dc4aa2 |
| start | string | N | Start time of export (ms since epoch - 0 means now, negative is relative to now) | 1 | 1465790400000 |
| end | string | N | End time of export (ms since epoch - 0 means now, negative is relative to now) | 0 | 1465790400000 |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Success](_schemas.md#success) | If data removal was successfully started |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if device was not found |

<br/>

## Send Command

Send a command to a device

```python
result = client.device.send_command(
    applicationId=my_application_id,
    deviceId=my_device_id,
    deviceCommand=my_device_command)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Device, all.Organization, all.User, device.*, or device.sendCommand.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| deviceId | string | Y | ID associated with the device |  | 575ecf887ae143cd83dc4aa2 |
| deviceCommand | [Device Command](_schemas.md#device-command) | Y | Command to send to the device |  | [Device Command Example](_schemas.md#device-command-example) |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Success](_schemas.md#success) | If command was successfully sent |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if device was not found |

<br/>

## Send State

Send the current state of the device

```python
result = client.device.send_state(
    applicationId=my_application_id,
    deviceId=my_device_id,
    deviceState=my_device_state)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Device, all.Organization, all.User, device.*, or device.sendState.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| deviceId | string | Y | ID associated with the device |  | 575ecf887ae143cd83dc4aa2 |
| deviceState | [Device State or States](_schemas.md#device-state-or-states) | Y | A single device state object, or an array of device state objects |  | [Device State or States Example](_schemas.md#device-state-or-states-example) |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Success](_schemas.md#success) | If state was successfully received |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if device was not found |

<br/>

## Set Connection Status

Set the current connection status of the device

```python
result = client.device.set_connection_status(
    applicationId=my_application_id,
    deviceId=my_device_id,
    connectionStatus=my_connection_status)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Device, all.Organization, all.User, device.*, or device.setConnectionStatus.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| deviceId | string | Y | ID associated with the device |  | 575ecf887ae143cd83dc4aa2 |
| connectionStatus | [Device Connection Status](_schemas.md#device-connection-status) | Y | The current connection status of the device |  | [Device Connection Status Example](_schemas.md#device-connection-status-example) |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Success](_schemas.md#success) | If connection status was successfully applied |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if device was not found |
