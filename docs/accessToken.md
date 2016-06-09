# Access Token Actions

Details on the various actions that can be performed on the
Access Token resource, including the expected
parameters and the potential responses.

##### Contents

*   [Delete](#delete)
*   [Get](#get)
*   [Patch](#patch)

<br/>

## Delete

Deletes an accessToken

```python
result = client.access_token.delete(accessTokenId=my_access_token_id)

print(result)
```

#### Available Parameters

| Name | Type | Required | Description | Default |
| ---- | ---- | -------- | ----------- | ------- |
| accessTokenId | string | Y | ID associated with the accessToken |  |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Success](_schemas.md#success) | If accessToken was successfully deleted |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 404 | [Error](_schemas.md#error) | Error if accessToken was not found |

<br/>

## Get

Retrieves information on an accessToken

```python
result = client.access_token.get(accessTokenId=my_access_token_id)

print(result)
```

#### Available Parameters

| Name | Type | Required | Description | Default |
| ---- | ---- | -------- | ----------- | ------- |
| accessTokenId | string | Y | ID associated with the accessToken |  |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Access Token](_schemas.md#access-token) | Access token information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 404 | [Error](_schemas.md#error) | Error if accessToken was not found |

<br/>

## Patch

Updates information about an accessToken

```python
result = client.access_token.patch(
    accessTokenId=my_access_token_id,
    accessToken=my_access_token)

print(result)
```

#### Available Parameters

| Name | Type | Required | Description | Default |
| ---- | ---- | -------- | ----------- | ------- |
| accessTokenId | string | Y | ID associated with the accessToken |  |
| accessToken | [Access Token Patch](_schemas.md#access-token-patch) | Y | Object containing new properties of the accessToken |  |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Access Token](_schemas.md#access-token) | Updated accessToken information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if accessToken was not found |
