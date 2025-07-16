# Application Job Logs Actions

Details on the various actions that can be performed on the
Application Job Logs resource, including the expected
parameters and the potential responses.

##### Contents

*   [Get](#get)

<br/>

## Get

Returns the job logs for an application

```python
result = client.application_job_logs.get(applicationId=my_application_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Application.read, all.Organization, all.Organization.read, all.User, all.User.read, applicationJobLogs.*, or applicationJobLogs.get.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| sortField | string | N | Field to sort the results by. Accepted values are: name, status, resourceType, runQueuedAt, runStartedAt, runCompletedAt | runQueuedAt | status |
| sortDirection | string | N | Direction to sort the results by. Accepted values are: asc, desc | asc | asc |
| page | string | N | Which page of results to return | 0 | 0 |
| perPage | string | N | How many items to return per page | 100 | 10 |
| query | [Advanced Application Job Log Query](_schemas.md#advanced-application-job-log-query) | N | Filter application job logs by a query. |  | [Advanced Application Job Log Query Example](_schemas.md#advanced-application-job-log-query-example) |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Application Job Logs](_schemas.md#application-job-logs) | Collection of application job logs |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if application was not found |
