# Application Api Tokens Actions

Details on the various actions that can be performed on the
Application Api Tokens resource, including the expected
parameters and the potential responses.

##### Contents

*   [Get](#get)
*   [Post](#post)

<br/>

## Get

Returns the API tokens for an application

```python
result = client.application_api_tokens.get(applicationId=my_application_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Application.read, all.Organization, all.Organization.read, all.User, all.User.read, applicationApiTokens.*, or applicationApiTokens.get.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [API Token](_schemas.md#api-token) | Collection of API tokens |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |

<br/>

## Post

Create a new API token for an application

```python
result = client.application_api_tokens.post(
    applicationId=my_application_id,
    apiToken=my_api_token)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Organization, all.User, applicationApiTokens.*, or applicationApiTokens.post.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| apiToken | [Application API Token Post](_schemas.md#application-api-token-post) | Y | API token information |  | [Application API Token Post Example](_schemas.md#application-api-token-post-example) |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 201 | [API Token](_schemas.md#api-token) | The successfully created API token |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
