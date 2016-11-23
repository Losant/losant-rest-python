# Device Actions

Details on the various actions that can be performed on the
Device resource, including the expected
parameters and the potential responses.

##### Contents

*   [Delete](#delete)
*   [Export](#export)
*   [Get](#get)
*   [Get Command](#get-command)
*   [Get Log Entries](#get-log-entries)
*   [Get State](#get-state)
*   [Patch](#patch)
*   [Remove Data](#remove-data)
*   [Send Command](#send-command)
*   [Send State](#send-state)

<br/>

## Delete

Deletes a device

```python
result = client.device.delete(
    applicationId=my_application_id,
    deviceId=my_device_id)

print(result)
```

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| deviceId | string | Y | ID associated with the device |  | 575ecf887ae143cd83dc4aa2 |

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

Creates a device data export (to be emailed to the requestor). Defaults to all data.

```python
result = client.device.export(
    applicationId=my_application_id,
    deviceId=my_device_id)

print(result)
```

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| deviceId | string | Y | ID associated with the device |  | 575ecf887ae143cd83dc4aa2 |
| start | string | N | Start time of export (ms since epoch - 0 means now, negative is relative to now) | 1 | 1465790400000 |
| end | string | N | End time of export (ms since epoch - 0 means now, negative is relative to now) | 0 | 1465790400000 |

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

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| deviceId | string | Y | ID associated with the device |  | 575ecf887ae143cd83dc4aa2 |

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

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| deviceId | string | Y | ID associated with the device |  | 575ecf887ae143cd83dc4aa2 |
| limit | string | N | Max command entries to return (ordered by time descending) | 1 | 10 |
| since | string | N | Look for command entries since this time (ms since epoch) |  | 1465790400000 |

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

## Get Log Entries

Retrieve the recent log entries about the device

```python
result = client.device.get_log_entries(
    applicationId=my_application_id,
    deviceId=my_device_id)

print(result)
```

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| deviceId | string | Y | ID associated with the device |  | 575ecf887ae143cd83dc4aa2 |
| limit | string | N | Max log entries to return (ordered by time descending) | 1 | 10 |
| since | string | N | Look for log entries since this time (ms since epoch) |  | 1465790400000 |

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

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| deviceId | string | Y | ID associated with the device |  | 575ecf887ae143cd83dc4aa2 |
| limit | string | N | Max state entries to return (ordered by time descending) | 1 | 10 |
| since | string | N | Look for state entries since this time (ms since epoch) |  | 1465790400000 |

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

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| deviceId | string | Y | ID associated with the device |  | 575ecf887ae143cd83dc4aa2 |
| device | [Device Patch](_schemas.md#device-patch) | Y | Object containing new properties of the device |  | [Device Patch Example](_schemas.md#device-patch-example) |

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

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| deviceId | string | Y | ID associated with the device |  | 575ecf887ae143cd83dc4aa2 |
| start | string | N | Start time of export (ms since epoch - 0 means now, negative is relative to now) | 1 | 1465790400000 |
| end | string | N | End time of export (ms since epoch - 0 means now, negative is relative to now) | 0 | 1465790400000 |

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

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| deviceId | string | Y | ID associated with the device |  | 575ecf887ae143cd83dc4aa2 |
| deviceCommand | [Device Command](_schemas.md#device-command) | Y | Command to send to the device |  | [Device Command Example](_schemas.md#device-command-example) |

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

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| deviceId | string | Y | ID associated with the device |  | 575ecf887ae143cd83dc4aa2 |
| deviceState | [Single or Multiple Device States](_schemas.md#single-or-multiple-device-states) | Y | A single device state object, or an array of device state objects |  | [Single or Multiple Device States Example](_schemas.md#single-or-multiple-device-states-example) |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Success](_schemas.md#success) | If state was successfully received |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if device was not found |
