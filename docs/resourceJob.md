# Resource Job Actions

Details on the various actions that can be performed on the
Resource Job resource, including the expected
parameters and the potential responses.

##### Contents

*   [Cancel Execution](#cancel-execution)
*   [Delete](#delete)
*   [Execute](#execute)
*   [Get](#get)
*   [Logs](#logs)
*   [Patch](#patch)

<br/>

## Cancel Execution

Marks a specific resource job execution for cancellation

```python
result = client.resource_job.cancel_execution(
    applicationId=my_application_id,
    resourceJobId=my_resource_job_id,
    executionId=my_execution_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Organization, all.User, resourceJob.*, or resourceJob.cancelExecution.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| resourceJobId | string | Y | ID associated with the resource job |  | 575ec8687ae143cd83dc4a97 |
| executionId | undefined | Y | The ID of the execution to cancel |  | 632e18632f59592e773a4153 |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Success](_schemas.md#success) | If the execution was successfully marked for cancellation |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if execution was not found |

<br/>

## Delete

Deletes a resource job

```python
result = client.resource_job.delete(
    applicationId=my_application_id,
    resourceJobId=my_resource_job_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Organization, all.User, resourceJob.*, or resourceJob.delete.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| resourceJobId | string | Y | ID associated with the resource job |  | 575ec8687ae143cd83dc4a97 |
| includeWorkflows | string | N | If the workflows that trigger from this resource job should also be deleted. |  | true |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Success](_schemas.md#success) | If resource job was successfully deleted |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if resource job was not found |

<br/>

## Execute

Queues the execution of a resource job

```python
result = client.resource_job.execute(
    applicationId=my_application_id,
    resourceJobId=my_resource_job_id,
    executionOptions=my_execution_options)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Organization, all.User, resourceJob.*, or resourceJob.execute.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| resourceJobId | string | Y | ID associated with the resource job |  | 575ec8687ae143cd83dc4a97 |
| executionOptions | [Resource Job Execution Options](_schemas.md#resource-job-execution-options) | Y | The options for the execution |  | [Resource Job Execution Options Example](_schemas.md#resource-job-execution-options-example) |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Success With Execution ID](_schemas.md#success-with-execution-id) | If the job was successfully queued |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if resource job was not found |

<br/>

## Get

Returns a resource job

```python
result = client.resource_job.get(
    applicationId=my_application_id,
    resourceJobId=my_resource_job_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Application.read, all.Organization, all.Organization.read, all.User, all.User.read, resourceJob.*, or resourceJob.get.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| resourceJobId | string | Y | ID associated with the resource job |  | 575ec8687ae143cd83dc4a97 |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Resource Job](_schemas.md#resource-job) | A single resource job |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if application was not found |

<br/>

## Logs

Retrieves information on resource job executions

```python
result = client.resource_job.logs(
    applicationId=my_application_id,
    resourceJobId=my_resource_job_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Application.read, all.Organization, all.Organization.read, all.User, all.User.read, resourceJob.*, or resourceJob.logs.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| resourceJobId | string | Y | ID associated with the resource job |  | 575ec8687ae143cd83dc4a97 |
| limit | string | N | Max log entries to return (ordered by time descending) | 1 | 10 |
| since | string | N | Look for log entries since this time (ms since epoch) |  | 1465790400000 |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Resource Job Execution Logs](_schemas.md#resource-job-execution-logs) | Resource job execution information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if resource job was not found |

<br/>

## Patch

Update a resource job

```python
result = client.resource_job.patch(
    applicationId=my_application_id,
    resourceJobId=my_resource_job_id,
    resourceJob=my_resource_job)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Organization, all.User, resourceJob.*, or resourceJob.patch.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| resourceJobId | string | Y | ID associated with the resource job |  | 575ec8687ae143cd83dc4a97 |
| resourceJob | [Resource Job Patch](_schemas.md#resource-job-patch) | Y | The new resource job configuration |  | [Resource Job Patch Example](_schemas.md#resource-job-patch-example) |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 201 | [Resource Job](_schemas.md#resource-job) | Successfully updated resource job |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if resource job was not found |
