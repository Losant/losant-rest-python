# Me Actions

Details on the various actions that can be performed on the
Me resource, including the expected
parameters and the potential responses.

##### Contents

*   [Add Recent Item](#add-recent-item)
*   [Delete](#delete)
*   [Disable Two Factor Auth](#disable-two-factor-auth)
*   [Disconnect Github](#disconnect-github)
*   [Disconnect Twitter](#disconnect-twitter)
*   [Enable Two Factor Auth](#enable-two-factor-auth)
*   [Fetch Recent Items](#fetch-recent-items)
*   [Get](#get)
*   [Patch](#patch)
*   [Verify Email](#verify-email)

<br/>

## Add Recent Item

Adds an item to a recent item list

```python
result = client.me.add_recent_item(data=my_data)

print(result)
```

#### Available Parameters

| Name | Type | Required | Description | Default |
| ---- | ---- | -------- | ----------- | ------- |
| data | [Recent Item](_schemas.md#recent-item) | Y | Object containing recent item info |  |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Recent Item List](_schemas.md#recent-item-list) | Updated recent item list |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |

<br/>

## Delete

Deletes the current user

```python
result = client.me.delete(credentials=my_credentials)

print(result)
```

#### Available Parameters

| Name | Type | Required | Description | Default |
| ---- | ---- | -------- | ----------- | ------- |
| credentials | [User Credentials](_schemas.md#user-credentials) | Y | User authentication credentials |  |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Success](_schemas.md#success) | If the user was successfully deleted |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |

<br/>

## Disable Two Factor Auth

Disables two factor auth for the current user

```python
result = client.me.disable_two_factor_auth(data=my_data)

print(result)
```

#### Available Parameters

| Name | Type | Required | Description | Default |
| ---- | ---- | -------- | ----------- | ------- |
| data | [Disable Two Factor Auth](_schemas.md#disable-two-factor-auth) | Y | Object containing two factor auth properties |  |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Me](_schemas.md#me) | Updated user information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |

<br/>

## Disconnect Github

Disconnects the user from Github

```python
result = client.me.disconnect_github()

print(result)
```

#### Available Parameters

No parameters needed for this call.

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Me](_schemas.md#me) | Updated user information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |

<br/>

## Disconnect Twitter

Disconnects the user from Twitter

```python
result = client.me.disconnect_twitter()

print(result)
```

#### Available Parameters

No parameters needed for this call.

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Me](_schemas.md#me) | Updated user information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |

<br/>

## Enable Two Factor Auth

Enables two factor auth for the current user

```python
result = client.me.enable_two_factor_auth(data=my_data)

print(result)
```

#### Available Parameters

| Name | Type | Required | Description | Default |
| ---- | ---- | -------- | ----------- | ------- |
| data | [Enable Two Factor Auth](_schemas.md#enable-two-factor-auth) | Y | Object containing two factor auth properties |  |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Me](_schemas.md#me) | Updated user information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |

<br/>

## Fetch Recent Items

Gets a recent item list

```python
result = client.me.fetch_recent_items(itemType=my_item_type)

print(result)
```

#### Available Parameters

| Name | Type | Required | Description | Default |
| ---- | ---- | -------- | ----------- | ------- |
| parentId | string | N | Parent id of the recent list |  |
| itemType | undefined | Y | Item type to get the recent list of. Accepted values are: application, device, flow, dashboard |  |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Recent Item List](_schemas.md#recent-item-list) | Recent item list |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |

<br/>

## Get

Retrieves information on the current user

```python
result = client.me.get(**optional_params)

print(result)
```

#### Available Parameters

| Name | Type | Required | Description | Default |
| ---- | ---- | -------- | ----------- | ------- |
| includeRecent | undefined | N | Should the user include recent app/dashboard info |  |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Me](_schemas.md#me) | Current user information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |

<br/>

## Patch

Updates information about the current user

```python
result = client.me.patch(user=my_user)

print(result)
```

#### Available Parameters

| Name | Type | Required | Description | Default |
| ---- | ---- | -------- | ----------- | ------- |
| user | [Me Patch](_schemas.md#me-patch) | Y | Object containing new user properties |  |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Me](_schemas.md#me) | Updated user information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |

<br/>

## Verify Email

Sends an email verification to the user

```python
result = client.me.verify_email()

print(result)
```

#### Available Parameters

No parameters needed for this call.

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Success](_schemas.md#success) | If email verification was successfully sent |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
