# Instance Sandboxes Actions

Details on the various actions that can be performed on the
Instance Sandboxes resource, including the expected
parameters and the potential responses.

##### Contents

*   [Get](#get)

<br/>

## Get

Returns a collection of instance sandboxes

```python
result = client.instance_sandboxes.get(instanceId=my_instance_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Instance, all.Instance.read, all.User, all.User.read, instanceSandboxes.*, or instanceSandboxes.get.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| instanceId | string | Y | ID associated with the instance |  | 575ec8687ae143cd83dc4a97 |
| sortField | string | N | Field to sort the results by. Accepted values are: firstName, lastName, email, id, creationDate, lastSuccessfulLogin, lastFailedLogin, failedLoginCount, lastUpdated | email | firstName |
| sortDirection | string | N | Direction to sort the results by. Accepted values are: asc, desc | asc | asc |
| startingAfterId | string | N | Exclusive ID from which to begin querying |  | 575ec8687ae143cd83dc4a97 |
| endingBeforeId | string | N | Exclusive ID at which to end querying |  | 575ec8687ae143cd83dc4a97 |
| limit | string | N | How many items to return | 100 | 10 |
| filterField | string | N | Field to filter the results by. Blank or not provided means no filtering. Accepted values are: firstName, lastName, email |  | firstName |
| filter | string | N | Filter to apply against the filtered field. Supports globbing. Blank or not provided means no filtering. |  | my * instance |
| includeDeleted | string | N | If the result of the request should also include deleted sandboxes. |  | true |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Instance Sandboxes](_schemas.md#instance-sandboxes) | Collection of instance sandboxes |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
