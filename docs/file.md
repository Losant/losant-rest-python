# File Actions

Details on the various actions that can be performed on the
File resource, including the expected
parameters and the potential responses.

##### Contents

*   [Delete](#delete)
*   [Get](#get)
*   [Move](#move)
*   [Patch](#patch)
*   [Upload](#upload)

<br/>

## Delete

Deletes a file or directory, if directory all the contents that directory will also be removed.

```python
result = client.file.delete(
    applicationId=my_application_id,
    fileId=my_file_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Organization, all.User, file.*, or file.delete.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| fileId | string | Y | ID associated with the file |  | 575ec76c7ae143cd83dc4a96 |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Success](_schemas.md#success) | If file was successfully deleted |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if event was not found |

<br/>

## Get

Retrieves information on a file

```python
result = client.file.get(
    applicationId=my_application_id,
    fileId=my_file_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Application.read, all.Organization, all.Organization.read, all.User, all.User.read, file.*, or file.get.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| fileId | string | Y | ID associated with the file |  | 575ec76c7ae143cd83dc4a96 |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [File Schema](_schemas.md#file-schema) | file information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if file was not found |

<br/>

## Move

Move a file or the entire contents of a directory

```python
result = client.file.move(
    applicationId=my_application_id,
    fileId=my_file_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Organization, all.User, file.*, or file.move.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| fileId | string | Y | ID associated with the file |  | 575ec76c7ae143cd83dc4a96 |
| name | undefined | N | The new name of the file or directory |  | fileA |
| parentDirectory | undefined | N | The new parent directory for the file or directory to move into. |  | /new/location/here |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 201 | [File Schema](_schemas.md#file-schema) | Returns a new file or directory that was created by the move, if a directory a job will kick off to move all the directories children. |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if application was not found |

<br/>

## Patch

Reupload a file

```python
result = client.file.patch(
    applicationId=my_application_id,
    fileId=my_file_id,
    updates=my_updates)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Organization, all.User, file.*, or file.patch.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| fileId | string | Y | ID associated with the file |  | 575ec76c7ae143cd83dc4a96 |
| updates | [File Patch](_schemas.md#file-patch) | Y | Reupload a file |  | [File Patch Example](_schemas.md#file-patch-example) |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 201 | [File Upload Post Response](_schemas.md#file-upload-post-response) | Successfully updated file and returned a post url to respond with |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if application was not found |

<br/>

## Upload

Uploads the file

```python
result = client.file.upload(
    applicationId=my_application_id,
    fileId=my_file_id,
    file=my_file)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Organization, all.User, file.*, or file.upload.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| fileId | string | Y | ID associated with the file |  | 575ec76c7ae143cd83dc4a96 |
| file | file | Y | The content of the file to upload |  | undefined |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [File Schema](_schemas.md#file-schema) | Updated file content |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if application was not found |
