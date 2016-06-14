# Access Tokens Actions

Details on the various actions that can be performed on the
Access Tokens resource, including the expected
parameters and the potential responses.

##### Contents

*   [Get](#get)
*   [Post](#post)

<br/>

## Get

Returns the accessTokens for a user

```python
result = client.access_tokens.get()

print(result)
```

#### Available Parameters

No parameters needed for this call.

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Access Tokens](_schemas.md#access-tokens) | Collection of accessTokens |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |

<br/>

## Post

Create a new accessToken for a user

```python
result = client.access_tokens.post(accessToken=my_access_token)

print(result)
```

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| accessToken | [Access Token Post](_schemas.md#access-token-post) | Y | AccessToken information |  | [Access Token Post Example](_schemas.md#access-token-post-example) |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 201 | [Access Token](_schemas.md#access-token) | The successfully created accessToken |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
