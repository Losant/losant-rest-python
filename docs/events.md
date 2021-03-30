# Events Actions

Details on the various actions that can be performed on the
Events resource, including the expected
parameters and the potential responses.

##### Contents

*   [Delete](#delete)
*   [Export](#export)
*   [Get](#get)
*   [Most Recent by Severity](#most-recent-by-severity)
*   [Patch](#patch)
*   [Post](#post)

<br/>

## Delete

Delete events

```python
result = client.events.delete(applicationId=my_application_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Application.read, all.Organization, all.Organization.read, all.User, all.User.read, events.*, or events.delete.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| query | [Advanced Event Query](_schemas.md#advanced-event-query) | N | Query to apply to filter the events |  | [Advanced Event Query Example](_schemas.md#advanced-event-query-example) |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Events Deleted](_schemas.md#events-deleted) | If request successfully deletes a set of Events |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if events were not found |

<br/>

## Export

Request an export of an application&#x27;s event data

```python
result = client.events.export(applicationId=my_application_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Application.read, all.Organization, all.Organization.read, all.User, all.User.read, events.*, or events.export.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| exportData | [Event Export Options](_schemas.md#event-export-options) | N | Export options for events |  | [Event Export Options Example](_schemas.md#event-export-options-example) |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Success](_schemas.md#success) | If generation of export was successfully started |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if application was not found |

<br/>

## Get

Returns the events for an application

```python
result = client.events.get(applicationId=my_application_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Application.read, all.Organization, all.Organization.read, all.User, all.User.read, events.*, or events.get.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| sortField | string | N | Field to sort the results by. Accepted values are: subject, id, creationDate, lastUpdated, level, state, deviceId | creationDate | subject |
| sortDirection | string | N | Direction to sort the results by. Accepted values are: asc, desc | desc | asc |
| page | string | N | Which page of results to return | 0 | 0 |
| perPage | string | N | How many items to return per page | 100 | 10 |
| filterField | string | N | Field to filter the results by. Blank or not provided means no filtering. Accepted values are: subject |  | subject |
| filter | string | N | Filter to apply against the filtered field. Supports globbing. Blank or not provided means no filtering. |  | abnormal power to * |
| state | string | N | If provided, return events only in the given state. Accepted values are: new, acknowledged, resolved |  | new |
| query | [Advanced Event Query](_schemas.md#advanced-event-query) | N | Event filter JSON object which overrides the filterField, filter, and state parameters. |  | [Advanced Event Query Example](_schemas.md#advanced-event-query-example) |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Events](_schemas.md#events) | Collection of events |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if application was not found |

<br/>

## Most Recent by Severity

Returns the first new event ordered by severity and then creation

```python
result = client.events.most_recent_by_severity(applicationId=my_application_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Application.read, all.Organization, all.Organization.read, all.User, all.User.read, events.*, or events.mostRecentBySeverity.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| filter | string | N | Filter to apply against event subjects. Supports globbing. Blank or not provided means no filtering. |  | abnormal power to * |
| query | [Advanced Event Query](_schemas.md#advanced-event-query) | N | Event filter JSON object which overrides the filter parameter. |  | [Advanced Event Query Example](_schemas.md#advanced-event-query-example) |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | undefined | The event, plus count of currently new events |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 404 | [Error](_schemas.md#error) | Error if application was not found |

<br/>

## Patch

Asynchronously updates information for matching events by subject and/or current state

```python
result = client.events.patch(
    applicationId=my_application_id,
    updates=my_updates)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Organization, all.User, events.*, or events.patch.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| filterField | string | N | Field to filter the events to act on by. Blank or not provided means no filtering. Accepted values are: subject |  | subject |
| filter | string | N | Filter to apply against the filtered field. Supports globbing. Blank or not provided means no filtering. |  | abnormal power to * |
| state | string | N | If provided, act on events only in the given state. Accepted values are: new, acknowledged, resolved |  | new |
| query | [Advanced Event Query](_schemas.md#advanced-event-query) | N | Event filter JSON object which overrides the filterField, filter, and state parameters. |  | [Advanced Event Query Example](_schemas.md#advanced-event-query-example) |
| updates | [Event Patch](_schemas.md#event-patch) | Y | Object containing updated information for the events |  | [Event Patch Example](_schemas.md#event-patch-example) |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Success](_schemas.md#success) | If the bulk update has been successfully started |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if application is not found |

<br/>

## Post

Create a new event for an application

```python
result = client.events.post(
    applicationId=my_application_id,
    event=my_event)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Organization, all.User, events.*, or events.post.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| event | [Event Post](_schemas.md#event-post) | Y | New event information |  | [Event Post Example](_schemas.md#event-post-example) |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 201 | [Event](_schemas.md#event) | Successfully created event |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if application was not found |
| 429 | [Error](_schemas.md#error) | Error if event creation rate limit exceeded |
