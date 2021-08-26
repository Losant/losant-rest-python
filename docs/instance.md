# Instance Actions

Details on the various actions that can be performed on the
Instance resource, including the expected
parameters and the potential responses.

##### Contents

*   [Generate Report](#generate-report)
*   [Get](#get)
*   [Historical Summaries](#historical-summaries)
*   [Patch](#patch)

<br/>

## Generate Report

Generates a CSV report on instance stats

```python
result = client.instance.generate_report(instanceId=my_instance_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Instance, all.Instance.read, all.User, all.User.read, instance.*, or instance.generateReport.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| instanceId | string | Y | ID associated with the instance |  | 575ec8687ae143cd83dc4a97 |
| options | [Instance Report Options Post](_schemas.md#instance-report-options-post) | N | Object containing report configuration |  | [Instance Report Options Post Example](_schemas.md#instance-report-options-post-example) |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Success](_schemas.md#success) | If generation of report was successfully started |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |

<br/>

## Get

Returns an instance

```python
result = client.instance.get(instanceId=my_instance_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Instance, all.Instance.read, all.User, all.User.read, instance.*, or instance.get.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| instanceId | string | Y | ID associated with the instance |  | 575ec8687ae143cd83dc4a97 |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Instance](_schemas.md#instance) | A single instance |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if instance was not found |

<br/>

## Historical Summaries

Return historical summary entries for an instance

```python
result = client.instance.historical_summaries(instanceId=my_instance_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Instance, all.Instance.read, all.User, all.User.read, instance.*, or instance.historicalSummaries.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| instanceId | string | Y | ID associated with the instance |  | 575ec8687ae143cd83dc4a97 |
| month | string | N | Timestamp within the month to report a summary for. | now | 1609459204518 |
| sortField | string | N | Field to sort the results by. Accepted values are: resourceId, currentPeriodStart | currentPeriodStart | resourceId |
| sortDirection | string | N | Direction to sort the results in. Accepted values are: asc, desc | asc | asc |
| page | string | N | Which page of results to return | 0 | 0 |
| perPage | string | N | How many items to return per page | 100 | 10 |
| filterField | string | N | Field to filter the results by. Blank or not provided means no filtering. Accepted values are: resourceType, resourceId, ownerId, ownerType |  | resourceType |
| filter | string | N | Filter to apply against the filtered field. Blank or not provided means no filtering. |  | organization |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Historical Summaries](_schemas.md#historical-summaries) | Collection of historical summaries |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |

<br/>

## Patch

Updates information about an instance

```python
result = client.instance.patch(
    instanceId=my_instance_id,
    instance=my_instance)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Instance, all.User, instance.*, or instance.patch.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| instanceId | string | Y | ID associated with the instance |  | 575ec8687ae143cd83dc4a97 |
| instance | [Instance Patch](_schemas.md#instance-patch) | Y | Updated instance information |  | [Instance Patch Example](_schemas.md#instance-patch-example) |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Instance](_schemas.md#instance) | The updated instance object |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
