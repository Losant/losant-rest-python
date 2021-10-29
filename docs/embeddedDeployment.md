# Embedded Deployment Actions

Details on the various actions that can be performed on the
Embedded Deployment resource, including the expected
parameters and the potential responses.

##### Contents

*   [Get](#get)

<br/>

## Get

Retrieves information on an embedded deployment

```python
result = client.embedded_deployment.get(
    applicationId=my_application_id,
    embeddedDeploymentId=my_embedded_deployment_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Application.read, all.Organization, all.Organization.read, all.User, all.User.read, embeddedDeployment.*, or embeddedDeployment.get.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| embeddedDeploymentId | string | Y | ID associated with the embedded deployment |  | 575ed78e7ae143cd83dc4aab |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Embedded Deployment](_schemas.md#embedded-deployment) | Embedded deployment information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if embedded deployment was not found |
