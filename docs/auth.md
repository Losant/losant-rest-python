# Auth Actions

Details on the various actions that can be performed on the
Auth resource, including the expected
parameters and the potential responses.

##### Contents

*   [Authenticate Device](#authenticate-device)
*   [Authenticate User](#authenticate-user)
*   [Authenticate User Github](#authenticate-user-github)

<br/>

## Authenticate Device

Authenticates a device using the provided credentials

```python
result = client.auth.authenticate_device(credentials=my_credentials)

print(result)
```

#### Available Parameters

| Name | Type | Required | Description | Default |
| ---- | ---- | -------- | ----------- | ------- |
| credentials | [Device Credentials](_schemas.md#device-credentials) | Y | Device authentication credentials |  |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Authenticated Device](_schemas.md#authenticated-device) | Successful authentication |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 401 | [Error](_schemas.md#error) | Unauthorized error if authentication fails |

<br/>

## Authenticate User

Authenticates a user using the provided credentials

```python
result = client.auth.authenticate_user(credentials=my_credentials)

print(result)
```

#### Available Parameters

| Name | Type | Required | Description | Default |
| ---- | ---- | -------- | ----------- | ------- |
| credentials | [User Credentials](_schemas.md#user-credentials) | Y | User authentication credentials |  |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Authenticated User](_schemas.md#authenticated-user) | Successful authentication |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 401 | [Error](_schemas.md#error) | Unauthorized error if authentication fails |

<br/>

## Authenticate User Github

Authenticates a user via GitHub OAuth

```python
result = client.auth.authenticate_user_github(oauth=my_oauth)

print(result)
```

#### Available Parameters

| Name | Type | Required | Description | Default |
| ---- | ---- | -------- | ----------- | ------- |
| oauth | [Github Login](_schemas.md#github-login) | Y | User authentication credentials (access token) |  |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Authenticated User](_schemas.md#authenticated-user) | Successful authentication |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 401 | [Error](_schemas.md#error) | Unauthorized error if authentication fails |
