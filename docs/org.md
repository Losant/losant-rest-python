# Org Actions

Details on the various actions that can be performed on the
Org resource, including the expected
parameters and the potential responses.

##### Contents

*   [Delete](#delete)
*   [Get](#get)
*   [Invite Member](#invite-member)
*   [Modify Member](#modify-member)
*   [Patch](#patch)
*   [Pending Invites](#pending-invites)
*   [Remove Member](#remove-member)
*   [Revoke Invite](#revoke-invite)

<br/>

## Delete

Deletes an organization

```python
result = client.org.delete(orgId=my_org_id)

print(result)
```

#### Available Parameters

| Name | Type | Required | Description | Default |
| ---- | ---- | -------- | ----------- | ------- |
| orgId | string | Y | ID associated with the organization |  |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Success](_schemas.md#success) | If organization was successfully deleted |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 404 | [Error](_schemas.md#error) | Error if organization was not found |

<br/>

## Get

Retrieves information on an organization

```python
result = client.org.get(orgId=my_org_id)

print(result)
```

#### Available Parameters

| Name | Type | Required | Description | Default |
| ---- | ---- | -------- | ----------- | ------- |
| orgId | string | Y | ID associated with the organization |  |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Organization](_schemas.md#organization) | Organization information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 404 | [Error](_schemas.md#error) | Error if organization not found |

<br/>

## Invite Member

Invites a person to an organization

```python
result = client.org.invite_member(
    orgId=my_org_id,
    invite=my_invite)

print(result)
```

#### Available Parameters

| Name | Type | Required | Description | Default |
| ---- | ---- | -------- | ----------- | ------- |
| orgId | string | Y | ID associated with the organization |  |
| invite | [Organization Invitation Post](_schemas.md#organization-invitation-post) | Y | Object containing new invite info |  |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Organization Invitations](_schemas.md#organization-invitations) | Invitation information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if organization not found |

<br/>

## Modify Member

Modifies a current org member&#x27;s role

```python
result = client.org.modify_member(
    orgId=my_org_id,
    member=my_member)

print(result)
```

#### Available Parameters

| Name | Type | Required | Description | Default |
| ---- | ---- | -------- | ----------- | ------- |
| orgId | string | Y | ID associated with the organization |  |
| member | [Organization Member Patch](_schemas.md#organization-member-patch) | Y | Object containing new member pair |  |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Organization](_schemas.md#organization) | Updated organization information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if organization not found |

<br/>

## Patch

Updates information about an organization

```python
result = client.org.patch(
    orgId=my_org_id,
    organization=my_organization)

print(result)
```

#### Available Parameters

| Name | Type | Required | Description | Default |
| ---- | ---- | -------- | ----------- | ------- |
| orgId | string | Y | ID associated with the organization |  |
| organization | [Organization Patch](_schemas.md#organization-patch) | Y | Object containing new organization properties |  |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Organization](_schemas.md#organization) | Updated organization information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if organization was not found |

<br/>

## Pending Invites

Gets the current pending invites

```python
result = client.org.pending_invites(orgId=my_org_id)

print(result)
```

#### Available Parameters

| Name | Type | Required | Description | Default |
| ---- | ---- | -------- | ----------- | ------- |
| orgId | string | Y | ID associated with the organization |  |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Organization Invitations](_schemas.md#organization-invitations) | Invitation information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 404 | [Error](_schemas.md#error) | Error if organization not found |

<br/>

## Remove Member

Modifies a current org member&#x27;s role

```python
result = client.org.remove_member(
    orgId=my_org_id,
    userId=my_user_id)

print(result)
```

#### Available Parameters

| Name | Type | Required | Description | Default |
| ---- | ---- | -------- | ----------- | ------- |
| orgId | string | Y | ID associated with the organization |  |
| userId | string | Y | Id of user to remove |  |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Organization](_schemas.md#organization) | Updated organization information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if organization not found |

<br/>

## Revoke Invite

Revokes an existing invite

```python
result = client.org.revoke_invite(
    orgId=my_org_id,
    inviteId=my_invite_id)

print(result)
```

#### Available Parameters

| Name | Type | Required | Description | Default |
| ---- | ---- | -------- | ----------- | ------- |
| orgId | string | Y | ID associated with the organization |  |
| inviteId | string | Y | Id of invite to revoke |  |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Organization Invitations](_schemas.md#organization-invitations) | Invitation information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if organization not found |
