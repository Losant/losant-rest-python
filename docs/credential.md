# Credential Actions

Details on the various actions that can be performed on the
Credential resource, including the expected
parameters and the potential responses.

##### Contents

*   [Delete](#delete)
*   [Get](#get)
*   [Linked Resources](#linked-resources)
*   [Patch](#patch)

<br/>

## Delete

Deletes a credential

```python
result = client.credential.delete(
    applicationId=my_application_id,
    credentialId=my_credential_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Organization, all.User, credential.*, or credential.delete.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| credentialId | string | Y | ID associated with the credential |  | 575ec76c7ae143cd83dc4a96 |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Success](_schemas.md#success) | If credential was successfully deleted |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if credential was not found |

<br/>

## Get

Retrieves information on a credential

```python
result = client.credential.get(
    applicationId=my_application_id,
    credentialId=my_credential_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Application.read, all.Organization, all.Organization.read, all.User, all.User.read, credential.*, or credential.get.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| credentialId | string | Y | ID associated with the credential |  | 575ec76c7ae143cd83dc4a96 |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Credential](_schemas.md#credential) | credential information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if credential was not found |

<br/>

## Linked Resources

Retrieves information on resources linked to a credential

```python
result = client.credential.linked_resources(
    applicationId=my_application_id,
    credentialId=my_credential_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Application.read, all.Organization, all.Organization.read, all.User, all.User.read, credential.*, or credential.linkedResources.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| credentialId | string | Y | ID associated with the credential |  | 575ec76c7ae143cd83dc4a96 |
| includeCustomNodes | string | N | If the result of the request should also include the details of any custom nodes referenced by returned workflows | false | true |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Credential Linked Resources](_schemas.md#credential-linked-resources) | Linked resource information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if credential was not found |

<br/>

## Patch

Updates information about a credential

```python
result = client.credential.patch(
    applicationId=my_application_id,
    credentialId=my_credential_id,
    credential=my_credential)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Organization, all.User, credential.*, or credential.patch.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| credentialId | string | Y | ID associated with the credential |  | 575ec76c7ae143cd83dc4a96 |
| credential | [Credential Patch](_schemas.md#credential-patch) | Y | Object containing new properties of the credential |  | [Credential Patch Example](_schemas.md#credential-patch-example) |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Credential](_schemas.md#credential) | Updated credential information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if credential was not found |
