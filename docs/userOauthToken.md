# User Oauth Token Actions

Details on the various actions that can be performed on the
User Oauth Token resource, including the expected
parameters and the potential responses.

##### Contents

*   [Delete](#delete)
*   [Get](#get)
*   [Patch](#patch)

<br/>

## Delete

Deletes an OAuth Token

```python
result = client.user_oauth_token.delete(oauthTokenId=my_oauth_token_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.User, only.User, userOauthToken.*, or userOauthToken.delete.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| oauthTokenId | string | Y | ID associated with the OAuth token |  | 575ec7417ae143cd83dc4a95 |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Success](_schemas.md#success) | If OAuth token was successfully deleted |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if OAuth token was not found |

<br/>

## Get

Retrieves information on an OAuth token

```python
result = client.user_oauth_token.get(oauthTokenId=my_oauth_token_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.User, all.User.bounded, all.User.read, only.User, only.User.bounded, only.User.read, userOauthToken.*, or userOauthToken.get.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| oauthTokenId | string | Y | ID associated with the OAuth token |  | 575ec7417ae143cd83dc4a95 |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [User OAuth Token](_schemas.md#user-oauth-token) | OAuth token information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if OAuth token was not found |

<br/>

## Patch

Updates information about an OAuth token

```python
result = client.user_oauth_token.patch(
    oauthTokenId=my_oauth_token_id,
    oauthToken=my_oauth_token)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.User, only.User, userOauthToken.*, or userOauthToken.patch.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| oauthTokenId | string | Y | ID associated with the OAuth token |  | 575ec7417ae143cd83dc4a95 |
| oauthToken | [User OAuth Token Patch](_schemas.md#user-oauth-token-patch) | Y | Object containing new properties of the OAuth token |  | [User OAuth Token Patch Example](_schemas.md#user-oauth-token-patch-example) |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [User OAuth Token](_schemas.md#user-oauth-token) | Updated OAuth token information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if OAuth token was not found |
