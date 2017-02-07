# Solution Actions

Details on the various actions that can be performed on the
Solution resource, including the expected
parameters and the potential responses.

##### Contents

*   [Delete](#delete)
*   [Get](#get)
*   [Patch](#patch)

<br/>

## Delete

Deletes a solution

```python
result = client.solution.delete(
    orgId=my_org_id,
    solutionId=my_solution_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Organization, all.User, solution.*, or solution.delete.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| orgId | string | Y | ID associated with the organization |  | 575ed6e87ae143cd83dc4aa8 |
| solutionId | string | Y | ID associated with the solution |  | 57955788124b37010084c053 |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Success](_schemas.md#success) | If solution was successfully deleted |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if solution was not found |

<br/>

## Get

Retrieves information on a solution

```python
result = client.solution.get(
    orgId=my_org_id,
    solutionId=my_solution_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Organization, all.Organization.read, all.User, all.User.read, solution.*, or solution.get.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| orgId | string | Y | ID associated with the organization |  | 575ed6e87ae143cd83dc4aa8 |
| solutionId | string | Y | ID associated with the solution |  | 57955788124b37010084c053 |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Solution](_schemas.md#solution) | Solution information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if solution was not found |

<br/>

## Patch

Updates information about a solution

```python
result = client.solution.patch(
    orgId=my_org_id,
    solutionId=my_solution_id,
    solution=my_solution)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Organization, all.User, solution.*, or solution.patch.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| orgId | string | Y | ID associated with the organization |  | 575ed6e87ae143cd83dc4aa8 |
| solutionId | string | Y | ID associated with the solution |  | 57955788124b37010084c053 |
| solution | [Solution Patch](_schemas.md#solution-patch) | Y | Object containing new properties of the solution |  | [Solution Patch Example](_schemas.md#solution-patch-example) |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Solution](_schemas.md#solution) | Updated solution information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if solution was not found |
