# Application Certificate Authority Actions

Details on the various actions that can be performed on the
Application Certificate Authority resource, including the expected
parameters and the potential responses.

##### Contents

*   [Delete](#delete)
*   [Get](#get)
*   [Patch](#patch)

<br/>

## Delete

Deletes an application certificate authority

```python
result = client.application_certificate_authority.delete(
    applicationId=my_application_id,
    applicationCertificateAuthorityId=my_application_certificate_authority_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Organization, all.User, applicationCertificateAuthority.*, or applicationCertificateAuthority.delete.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| applicationCertificateAuthorityId | string | Y | ID associated with the application certificate authority |  | 575ec76c7ae143cd83dc4a96 |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Success](_schemas.md#success) | If application certificate authority was successfully deleted |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if application certificate authority was not found |

<br/>

## Get

Retrieves information on an application certificate authority

```python
result = client.application_certificate_authority.get(
    applicationId=my_application_id,
    applicationCertificateAuthorityId=my_application_certificate_authority_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Application.read, all.Organization, all.Organization.read, all.User, all.User.read, applicationCertificateAuthority.*, or applicationCertificateAuthority.get.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| applicationCertificateAuthorityId | string | Y | ID associated with the application certificate authority |  | 575ec76c7ae143cd83dc4a96 |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Application Certificate Authority](_schemas.md#application-certificate-authority) | Application certificate authority information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if application certificate authority was not found |

<br/>

## Patch

Updates information about an application certificate authority

```python
result = client.application_certificate_authority.patch(
    applicationId=my_application_id,
    applicationCertificateAuthorityId=my_application_certificate_authority_id,
    applicationCertificateAuthority=my_application_certificate_authority)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Application, all.Organization, all.User, applicationCertificateAuthority.*, or applicationCertificateAuthority.patch.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| applicationCertificateAuthorityId | string | Y | ID associated with the application certificate authority |  | 575ec76c7ae143cd83dc4a96 |
| applicationCertificateAuthority | [Application Certificate Authority Patch](_schemas.md#application-certificate-authority-patch) | Y | Object containing new properties of the application certificate authority |  | [Application Certificate Authority Patch Example](_schemas.md#application-certificate-authority-patch-example) |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Application Certificate Authority](_schemas.md#application-certificate-authority) | Updated application certificate authority information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if application certificate authority was not found |
