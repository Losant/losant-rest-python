# Devices Actions

Details on the various actions that can be performed on the
Devices resource, including the expected
parameters and the potential responses.

##### Contents

*   [Delete](#delete)
*   [Export](#export)
*   [Get](#get)
*   [Patch](#patch)
*   [Post](#post)
*   [Remove Data](#remove-data)
*   [Send Command](#send-command)

<br/>

## Delete

Delete devices

```python
result = client.devices.delete(
    applicationId=my_application_id,
    options=my_options)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Organization, all.User, devices.*, or devices.delete.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| options | [Devices Delete Post](_schemas.md#devices-delete-post) | Y | Object containing device query and email |  | [Devices Delete Post Example](_schemas.md#devices-delete-post-example) |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Devices Deleted](_schemas.md#devices-deleted) | Object indicating number of devices deleted or failed |
| 202 | [Job Enqueued API Result](_schemas.md#job-enqueued-api-result) | If a job was enqueued for the devices to be deleted |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if application was not found |

<br/>

## Export

Creates an export of all device metadata

```python
result = client.devices.export(applicationId=my_application_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Application.read, all.Organization, all.Organization.read, all.User, all.User.read, devices.*, or devices.export.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| email | string | N | Email address to send export to. Defaults to current user&#x27;s email. |  | email@example.com |
| callbackUrl | string | N | Callback URL to call with export result |  | https://example.com/cburl |
| options | [Devices Metadata Export Post](_schemas.md#devices-metadata-export-post) | N | Object containing device query and optionally email or callback |  | [Devices Metadata Export Post Example](_schemas.md#devices-metadata-export-post-example) |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Success](_schemas.md#success) | If generation of export was successfully started |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if application was not found |

<br/>

## Get

Returns the devices for an application

```python
result = client.devices.get(applicationId=my_application_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Application.read, all.Device, all.Device.read, all.Organization, all.Organization.read, all.User, all.User.read, devices.*, or devices.get.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| sortField | string | N | Field to sort the results by. Accepted values are: name, id, creationDate, lastUpdated | name | name |
| sortDirection | string | N | Direction to sort the results by. Accepted values are: asc, desc | asc | asc |
| page | string | N | Which page of results to return | 0 | 0 |
| perPage | string | N | How many items to return per page | 1000 | 10 |
| filterField | string | N | Field to filter the results by. Blank or not provided means no filtering. Accepted values are: name |  | name |
| filter | string | N | Filter to apply against the filtered field. Supports globbing. Blank or not provided means no filtering. |  | my * device |
| deviceClass | [Device Class Filter](_schemas.md#device-class-filter) | N | Filter the devices by the given device class or classes |  | [Device Class Filter Example](_schemas.md#device-class-filter-example) |
| tagFilter | [Device Tag Filter](_schemas.md#device-tag-filter) | N | Array of tag pairs to filter by |  | [Device Tag Filter Example](_schemas.md#device-tag-filter-example) |
| excludeConnectionInfo | string | N | If set, do not return connection info |  | true |
| parentId | string | N | Filter devices as children of a given system id |  | 575ecf887ae143cd83dc4aa2 |
| query | [Advanced Device Query](_schemas.md#advanced-device-query) | N | Device filter JSON object which overrides the filterField, filter, deviceClass, tagFilter, and parentId parameters. |  | [Advanced Device Query Example](_schemas.md#advanced-device-query-example) |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Devices](_schemas.md#devices) | Collection of devices |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if application was not found |

<br/>

## Patch

Update the fields of one or more devices

```python
result = client.devices.patch(applicationId=my_application_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Organization, all.User, devices.*, or devices.patch.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| patchInfo | [Devices Patch](_schemas.md#devices-patch) | N | Object containing device query or IDs and update operations |  | [Devices Patch Example](_schemas.md#devices-patch-example) |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Devices Updated](_schemas.md#devices-updated) | Object including an update log link and the number of devices updated, failed, and skipped |
| 202 | [Job Enqueued API Result](_schemas.md#job-enqueued-api-result) | Successfully queued bulk update job |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if application was not found |

<br/>

## Post

Create a new device for an application

```python
result = client.devices.post(
    applicationId=my_application_id,
    device=my_device)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Organization, all.User, devices.*, or devices.post.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| device | [Device Post](_schemas.md#device-post) | Y | New device information |  | [Device Post Example](_schemas.md#device-post-example) |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 201 | [Device](_schemas.md#device) | Successfully created device |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if application was not found |

<br/>

## Remove Data

Removes all device data for the specified time range. Defaults to all data.

```python
result = client.devices.remove_data(
    applicationId=my_application_id,
    options=my_options)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Organization, all.User, devices.*, or devices.removeData.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| options | [Devices Remove Data Post](_schemas.md#devices-remove-data-post) | Y | Object defining the device data to delete and devices to delete from |  | [Devices Remove Data Post Example](_schemas.md#devices-remove-data-post-example) |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Devices Data Removed](_schemas.md#devices-data-removed) | Object indicating number of devices completed or skipped |
| 202 | [Job Enqueued API Result](_schemas.md#job-enqueued-api-result) | If a job was enqueued for device data to be removed |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if device was not found |

<br/>

## Send Command

Send a command to multiple devices

```python
result = client.devices.send_command(
    applicationId=my_application_id,
    multiDeviceCommand=my_multi_device_command)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Device, all.Organization, all.User, devices.*, or devices.sendCommand.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| multiDeviceCommand | [Multi Device Command](_schemas.md#multi-device-command) | Y | Command to send to the device |  | [Multi Device Command Example](_schemas.md#multi-device-command-example) |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Success](_schemas.md#success) | If command was successfully sent |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if application was not found |
