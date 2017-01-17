# Dashboards Actions

Details on the various actions that can be performed on the
Dashboards resource, including the expected
parameters and the potential responses.

##### Contents

*   [Get](#get)
*   [Post](#post)

<br/>

## Get

Returns the dashboards the current user has permission to see

```python
result = client.dashboards.get(**optional_params)

print(result)
```

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| sortField | string | N | Field to sort the results by. Accepted values are: name, id, creationDate, ownerId | name | name |
| sortDirection | string | N | Direction to sort the results by. Accepted values are: asc, desc | asc | asc |
| page | string | N | Which page of results to return | 0 | 0 |
| perPage | string | N | How many items to return per page | 1000 | 10 |
| filterField | string | N | Field to filter the results by. Blank or not provided means no filtering. Accepted values are: name |  | name |
| filter | string | N | Filter to apply against the filtered field. Supports globbing. Blank or not provided means no filtering. |  | my * dashboard |
| orgId | string | N | If not provided, return all dashboards. If provided but blank, only return dashboards belonging to the current user. If provided and an id, only return dashboards belonging to the given organization id. |  | 575ece7e7ae143cd83dc4a9c |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Dashboards](_schemas.md#dashboards) | Collection of dashboards |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |

<br/>

## Post

Create a new dashboard

```python
result = client.dashboards.post(dashboard=my_dashboard)

print(result)
```

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| dashboard | [Dashboard Post](_schemas.md#dashboard-post) | Y | New dashboard information |  | [Dashboard Post Example](_schemas.md#dashboard-post-example) |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 201 | [Dashboard](_schemas.md#dashboard) | Successfully created dashboard |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
