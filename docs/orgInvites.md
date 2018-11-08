# Org Invites Actions

Details on the various actions that can be performed on the
Org Invites resource, including the expected
parameters and the potential responses.

##### Contents

*   [Get](#get)
*   [Post](#post)

<br/>

## Get

Gets information about an invite

```python
result = client.org_invites.get(
    token=my_token,
    email=my_email)

print(result)
```

#### Authentication
No api access token is required to call this action.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| token | string | Y | The token associated with the invite |  | aTokenString |
| email | string | Y | The email associated with the invite |  | example@example.com |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Organization Invitation Information](_schemas.md#organization-invitation-information) | Information about invite |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if invite not found |
| 410 | [Error](_schemas.md#error) | Error if invite has expired |

<br/>

## Post

Accepts/Rejects an invite

```python
result = client.org_invites.post(invite=my_invite)

print(result)
```

#### Authentication
No api access token is required to call this action.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| invite | [Organization Invitation Action](_schemas.md#organization-invitation-action) | Y | Invite info and acceptance |  | [Organization Invitation Action Example](_schemas.md#organization-invitation-action-example) |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Organization Invitation Result](_schemas.md#organization-invitation-result) | Acceptance/Rejection of invite |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if invite not found |
| 410 | [Error](_schemas.md#error) | Error if invite has expired |
