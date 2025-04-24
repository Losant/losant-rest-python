# Device Attributes Actions

Details on the various actions that can be performed on the
Device Attributes resource, including the expected
parameters and the potential responses.

##### Contents

*   [Get](#get)
*   [Post](#post)

<br/>

## Get

Returns the attributes for a device

```python
result = client.device_attributes.get(
    applicationId=my_application_id,
    deviceId=my_device_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Application.read, all.Device, all.Device.read, all.Organization, all.Organization.read, all.User, all.User.read, deviceAttributes.*, or deviceAttributes.get.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| deviceId | string | Y | ID associated with the device |  | 575ecf887ae143cd83dc4aa2 |
| sortField | string | N | Field to sort the results by. Accepted values are: name, dataType | name | status |
| sortDirection | string | N | Direction to sort the results by. Accepted values are: asc, desc | asc | asc |
| filterField | string | N | Field to filter the results by. Blank or not provided means no filtering. Accepted values are: name, dataType |  | status |
| filter | string | N | Filter to apply against the filtered field. Supports globbing. Blank or not provided means no filtering. |  | number |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Device Attributes](_schemas.md#device-attributes) | Collection of device attributes |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if device was not found |

<br/>

## Post

Adds a new attribute to a device

```python
result = client.device_attributes.post(
    applicationId=my_application_id,
    deviceId=my_device_id,
    deviceAttribute=my_device_attribute)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Organization, all.User, deviceAttributes.*, or deviceAttributes.post.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| deviceId | string | Y | ID associated with the device |  | 575ecf887ae143cd83dc4aa2 |
| deviceAttribute | [Device Attribute Post](_schemas.md#device-attribute-post) | Y | Device attribute information |  | [Device Attribute Post Example](_schemas.md#device-attribute-post-example) |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 201 | [Device Attribute](_schemas.md#device-attribute) | Successfully created device attribute |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if device was not found |
