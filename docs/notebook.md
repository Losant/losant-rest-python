# Notebook Actions

Details on the various actions that can be performed on the
Notebook resource, including the expected
parameters and the potential responses.

##### Contents

*   [Delete](#delete)
*   [Execute](#execute)
*   [Get](#get)
*   [Logs](#logs)
*   [Patch](#patch)
*   [Request Input Data Export](#request-input-data-export)
*   [Upload](#upload)

<br/>

## Delete

Deletes a notebook

```python
result = client.notebook.delete(
    applicationId=my_application_id,
    notebookId=my_notebook_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Organization, all.User, notebook.*, or notebook.delete.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| notebookId | string | Y | ID associated with the notebook |  | 575ed78e7ae143cd83dc4aab |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Success](_schemas.md#success) | If notebook was successfully deleted |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if notebook was not found |

<br/>

## Execute

Triggers the execution of a notebook

```python
result = client.notebook.execute(
    applicationId=my_application_id,
    notebookId=my_notebook_id,
    executionOptions=my_execution_options)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Organization, all.User, notebook.*, or notebook.execute.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| notebookId | string | Y | ID associated with the notebook |  | 575ed78e7ae143cd83dc4aab |
| executionOptions | [Notebook Execution Options](_schemas.md#notebook-execution-options) | Y | The options for the execution |  | [Notebook Execution Options Example](_schemas.md#notebook-execution-options-example) |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Success](_schemas.md#success) | If execution request was accepted and successfully queued |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if notebook was not found |

<br/>

## Get

Retrieves information on a notebook

```python
result = client.notebook.get(
    applicationId=my_application_id,
    notebookId=my_notebook_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Application.read, all.Organization, all.Organization.read, all.User, all.User.read, notebook.*, or notebook.get.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| notebookId | string | Y | ID associated with the notebook |  | 575ed78e7ae143cd83dc4aab |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Notebook](_schemas.md#notebook) | notebook information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if notebook was not found |

<br/>

## Logs

Retrieves information on notebook executions

```python
result = client.notebook.logs(
    applicationId=my_application_id,
    notebookId=my_notebook_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Application.read, all.Organization, all.Organization.read, all.User, all.User.read, notebook.*, or notebook.logs.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| notebookId | string | Y | ID associated with the notebook |  | 575ed78e7ae143cd83dc4aab |
| limit | string | N | Max log entries to return (ordered by time descending) | 1 | 10 |
| since | string | N | Look for log entries since this time (ms since epoch) |  | 1465790400000 |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Notebook Execution Logs](_schemas.md#notebook-execution-logs) | notebook execution information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if notebook was not found |

<br/>

## Patch

Updates information about a notebook

```python
result = client.notebook.patch(
    applicationId=my_application_id,
    notebookId=my_notebook_id,
    notebook=my_notebook)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Organization, all.User, notebook.*, or notebook.patch.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| notebookId | string | Y | ID associated with the notebook |  | 575ed78e7ae143cd83dc4aab |
| notebook | [Notebook Patch](_schemas.md#notebook-patch) | Y | Object containing new properties of the notebook |  | [Notebook Patch Example](_schemas.md#notebook-patch-example) |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Notebook](_schemas.md#notebook) | Updated notebook information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if notebook was not found |

<br/>

## Request Input Data Export

Requests a combined zip file of the potential input data for a notebook execution

```python
result = client.notebook.request_input_data_export(
    applicationId=my_application_id,
    notebookId=my_notebook_id,
    exportOptions=my_export_options)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Application.read, all.Organization, all.Organization.read, all.User, all.User.read, notebook.*, or notebook.requestInputDataExport.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| notebookId | string | Y | ID associated with the notebook |  | 575ed78e7ae143cd83dc4aab |
| exportOptions | [Notebook Data Export Options](_schemas.md#notebook-data-export-options) | Y | The options for the export |  | [Notebook Data Export Options Example](_schemas.md#notebook-data-export-options-example) |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Success](_schemas.md#success) | If export request was accepted and successfully queued |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if notebook was not found |

<br/>

## Upload

Uploads the jupyter notebook file

```python
result = client.notebook.upload(
    applicationId=my_application_id,
    notebookId=my_notebook_id,
    jupyterFile=my_jupyter_file)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Organization, all.User, notebook.*, or notebook.upload.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| notebookId | string | Y | ID associated with the notebook |  | 575ed78e7ae143cd83dc4aab |
| jupyterFile | file | Y | The jupyter notebook file |  | undefined |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Notebook](_schemas.md#notebook) | Updated notebook information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if notebook was not found |
