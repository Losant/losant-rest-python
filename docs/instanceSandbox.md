# Instance Sandbox Actions

Details on the various actions that can be performed on the
Instance Sandbox resource, including the expected
parameters and the potential responses.

##### Contents

*   [Delete](#delete)
*   [Get](#get)
*   [Undelete](#undelete)

<br/>

## Delete

Deletes a sandbox user account

```python
result = client.instance_sandbox.delete(
    instanceId=my_instance_id,
    instanceSandboxId=my_instance_sandbox_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Instance, all.User, instanceSandbox.*, or instanceSandbox.delete.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| instanceId | string | Y | ID associated with the instance |  | 575ec8687ae143cd83dc4a97 |
| instanceSandboxId | string | Y | ID associated with the sandbox user |  | 575ec8687ae143cd83dc4a97 |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Success](_schemas.md#success) | If a sandbox was successfully deleted |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if instance, organization or invite was not found |

<br/>

## Get

Returns a sandbox user

```python
result = client.instance_sandbox.get(
    instanceId=my_instance_id,
    instanceSandboxId=my_instance_sandbox_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Instance, all.Instance.read, all.User, all.User.read, instanceSandbox.*, or instanceSandbox.get.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| instanceId | string | Y | ID associated with the instance |  | 575ec8687ae143cd83dc4a97 |
| instanceSandboxId | string | Y | ID associated with the sandbox user |  | 575ec8687ae143cd83dc4a97 |
| summaryExclude | string | N | Comma-separated list of summary fields to exclude from user summary |  | payloadCount |
| summaryInclude | string | N | Comma-separated list of summary fields to include in user summary |  | payloadCount |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Instance Sandbox User](_schemas.md#instance-sandbox-user) | A single sandbox user |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if sandbox was not found |

<br/>

## Undelete

Restores a sandbox user account

```python
result = client.instance_sandbox.undelete(
    instanceId=my_instance_id,
    instanceSandboxId=my_instance_sandbox_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Instance, all.User, instanceSandbox.*, or instanceSandbox.undelete.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| instanceId | string | Y | ID associated with the instance |  | 575ec8687ae143cd83dc4a97 |
| instanceSandboxId | string | Y | ID associated with the sandbox user |  | 575ec8687ae143cd83dc4a97 |
| summaryExclude | string | N | Comma-separated list of summary fields to exclude from user summary |  | payloadCount |
| summaryInclude | string | N | Comma-separated list of summary fields to include in user summary |  | payloadCount |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Instance Sandbox User](_schemas.md#instance-sandbox-user) | A single restored sandbox user |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if sandbox was not found |
