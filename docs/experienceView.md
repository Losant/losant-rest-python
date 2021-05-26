# Experience View Actions

Details on the various actions that can be performed on the
Experience View resource, including the expected
parameters and the potential responses.

##### Contents

*   [Delete](#delete)
*   [Get](#get)
*   [Linked Resources](#linked-resources)
*   [Patch](#patch)

<br/>

## Delete

Deletes an experience view

```python
result = client.experience_view.delete(
    applicationId=my_application_id,
    experienceViewId=my_experience_view_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Application.cli, all.Organization, all.User, all.User.cli, experienceView.*, or experienceView.delete.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| experienceViewId | string | Y | ID associated with the experience view |  | 575ed78e7ae143cd83dc4aab |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Success](_schemas.md#success) | If experience view was successfully deleted |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if experience view was not found |

<br/>

## Get

Retrieves information on an experience view

```python
result = client.experience_view.get(
    applicationId=my_application_id,
    experienceViewId=my_experience_view_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Application.cli, all.Application.read, all.Organization, all.Organization.read, all.User, all.User.cli, all.User.read, experienceView.*, or experienceView.get.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| experienceViewId | string | Y | ID associated with the experience view |  | 575ed78e7ae143cd83dc4aab |
| version | string | N | Version of this experience view to return | develop | develop |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Experience View](_schemas.md#experience-view) | Experience view information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if experience view was not found |

<br/>

## Linked Resources

Retrieves information on resources linked to an experience view

```python
result = client.experience_view.linked_resources(
    applicationId=my_application_id,
    experienceViewId=my_experience_view_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Application.cli, all.Application.read, all.Organization, all.Organization.read, all.User, all.User.cli, all.User.read, experienceView.*, or experienceView.linkedResources.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| experienceViewId | string | Y | ID associated with the experience view |  | 575ed78e7ae143cd83dc4aab |
| version | string | N | Version of this experience view to query | develop | develop |
| includeCustomNodes | string | N | If the result of the request should also include the details of any custom nodes referenced by returned workflows | false | true |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Experience Linked Resources](_schemas.md#experience-linked-resources) | Linked resource information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if experience view was not found |

<br/>

## Patch

Updates information about an experience view

```python
result = client.experience_view.patch(
    applicationId=my_application_id,
    experienceViewId=my_experience_view_id,
    experienceView=my_experience_view)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Application.cli, all.Organization, all.User, all.User.cli, experienceView.*, or experienceView.patch.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| experienceViewId | string | Y | ID associated with the experience view |  | 575ed78e7ae143cd83dc4aab |
| experienceView | [Experience View Patch](_schemas.md#experience-view-patch) | Y | Object containing new properties of the experience view |  | [Experience View Patch Example](_schemas.md#experience-view-patch-example) |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Experience View](_schemas.md#experience-view) | Updated experience view information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if experience view was not found |
