# Private File Actions

Details on the various actions that can be performed on the
Private File resource, including the expected
parameters and the potential responses.

##### Contents

*   [Delete](#delete)
*   [Get](#get)
*   [Move](#move)
*   [Patch](#patch)
*   [Upload](#upload)

<br/>

## Delete

Deletes a private file or directory, if a directory all the contents that directory will also be removed.

```python
result = client.private_file.delete(
    applicationId=my_application_id,
    privateFileId=my_private_file_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Application.cli, all.Organization, all.User, all.User.cli, privateFile.*, or privateFile.delete.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| privateFileId | string | Y | ID associated with the private file |  | 575ec76c7ae143cd83dc4a96 |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Success](_schemas.md#success) | If private file was successfully deleted |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if private file was not found |

<br/>

## Get

Retrieves information on a private file

```python
result = client.private_file.get(
    applicationId=my_application_id,
    privateFileId=my_private_file_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Application.cli, all.Application.read, all.Organization, all.Organization.read, all.User, all.User.cli, all.User.read, privateFile.*, or privateFile.get.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| privateFileId | string | Y | ID associated with the private file |  | 575ec76c7ae143cd83dc4a96 |
| urlTTL | string | N | Time in seconds that the private file url will be valid for. Only applies to private files of type &#x27;file&#x27;. If 0, no url will be returned. | 900 | 900 |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [File Schema](_schemas.md#file-schema) | Private file information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if private file was not found |

<br/>

## Move

Move a private file or the entire contents of a directory

```python
result = client.private_file.move(
    applicationId=my_application_id,
    privateFileId=my_private_file_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Application.cli, all.Organization, all.User, all.User.cli, privateFile.*, or privateFile.move.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| privateFileId | string | Y | ID associated with the private file |  | 575ec76c7ae143cd83dc4a96 |
| name | undefined | N | The new name of the private file or directory |  | fileA |
| parentDirectory | undefined | N | The new parent directory for the private file or directory to move into. |  | /new/location/here |
| urlTTL | string | N | Time in seconds that the private file url will be valid for. Only applies to private files of type &#x27;file&#x27;. If 0, no url will be returned. | 900 | 900 |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 201 | [File Schema](_schemas.md#file-schema) | Returns a new private file or directory that was created by the move, if a directory a job will kick off to move all the directories children. |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if private file was not found |

<br/>

## Patch

Reupload a private file

```python
result = client.private_file.patch(
    applicationId=my_application_id,
    privateFileId=my_private_file_id,
    updates=my_updates)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Application.cli, all.Organization, all.User, all.User.cli, privateFile.*, or privateFile.patch.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| privateFileId | string | Y | ID associated with the private file |  | 575ec76c7ae143cd83dc4a96 |
| updates | [File Patch](_schemas.md#file-patch) | Y | Updated information about the private file |  | [File Patch Example](_schemas.md#file-patch-example) |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 201 | [File Upload Post Response](_schemas.md#file-upload-post-response) | Successfully updated private file and the information needed to upload the file content |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if private file was not found |

<br/>

## Upload

Uploads the private file

```python
result = client.private_file.upload(
    applicationId=my_application_id,
    privateFileId=my_private_file_id,
    privateFile=my_private_file)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Application.cli, all.Organization, all.User, all.User.cli, privateFile.*, or privateFile.upload.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| privateFileId | string | Y | ID associated with the private file |  | 575ec76c7ae143cd83dc4a96 |
| privateFile | file | Y | The content of the private file to upload |  | undefined |
| urlTTL | string | N | Time in seconds that the private file url will be valid for. Only applies to private files of type &#x27;file&#x27;. If 0, no url will be returned. | 900 | 900 |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [File Schema](_schemas.md#file-schema) | Updated private file content |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if file was not found |
