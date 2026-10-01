# User Oauth Client Actions

Details on the various actions that can be performed on the
User Oauth Client resource, including the expected
parameters and the potential responses.

##### Contents

*   [Delete](#delete)
*   [Get](#get)
*   [Patch](#patch)

<br/>

## Delete

Deletes a private OAuth client

```python
result = client.user_oauth_client.delete(clientId=my_client_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.User, only.User, userOauthClient.*, or userOauthClient.delete.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| clientId | string | Y | ID associated with the OAuth client |  | 575ec7417ae143cd83dc4a95 |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Success](_schemas.md#success) | If OAuth client was successfully deleted |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if OAuth client was not found |

<br/>

## Get

Retrieves information on a private OAuth client

```python
result = client.user_oauth_client.get(clientId=my_client_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.User, all.User.bounded, all.User.read, only.User, only.User.bounded, only.User.read, userOauthClient.*, or userOauthClient.get.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| clientId | string | Y | ID associated with the OAuth client |  | 575ec7417ae143cd83dc4a95 |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [User OAuth Client](_schemas.md#user-oauth-client) | OAuth client information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if OAuth client was not found |

<br/>

## Patch

Updates information about a private OAuth client

```python
result = client.user_oauth_client.patch(
    clientId=my_client_id,
    oauthClient=my_oauth_client)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.User, only.User, userOauthClient.*, or userOauthClient.patch.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| clientId | string | Y | ID associated with the OAuth client |  | 575ec7417ae143cd83dc4a95 |
| oauthClient | [User OAuth Client Patch](_schemas.md#user-oauth-client-patch) | Y | Object containing new properties of the OAuth client |  | [User OAuth Client Patch Example](_schemas.md#user-oauth-client-patch-example) |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [User OAuth Client](_schemas.md#user-oauth-client) | Updated OAuth client information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if OAuth client was not found |
