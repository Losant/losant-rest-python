# Instance Org Invites Actions

Details on the various actions that can be performed on the
Instance Org Invites resource, including the expected
parameters and the potential responses.

##### Contents

*   [Get](#get)
*   [Post](#post)

<br/>

## Get

Returns a collection of instance organization invites

```python
result = client.instance_org_invites.get(
    instanceId=my_instance_id,
    orgId=my_org_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Instance, all.Instance.read, all.User, all.User.read, instanceOrgInvites.*, or instanceOrgInvites.get.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| instanceId | string | Y | ID associated with the instance |  | 575ec8687ae143cd83dc4a97 |
| orgId | string | Y | ID associated with the organization |  | 575ec8687ae143cd83dc4a97 |
| sortField | string | N | Field to sort the results by. Accepted values are: email, role, inviteDate | inviteDate | role |
| sortDirection | string | N | Direction to sort the results by. Accepted values are: asc, desc | desc | asc |
| filterField | string | N | Field to filter the results by. Blank or not provided means no filtering. Accepted values are: email, role |  | email |
| filter | string | N | Filter to apply against the filtered field. Supports globbing. Blank or not provided means no filtering. |  | my * instance |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Instance Organization Invitations](_schemas.md#instance-organization-invitations) | A collection of instance organization invitations |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if instance or organization was not found |

<br/>

## Post

Invites a member to an instance organization

```python
result = client.instance_org_invites.post(
    instanceId=my_instance_id,
    orgId=my_org_id,
    invite=my_invite)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Instance, all.User, instanceOrgInvites.*, or instanceOrgInvites.post.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| instanceId | string | Y | ID associated with the instance |  | 575ec8687ae143cd83dc4a97 |
| orgId | string | Y | ID associated with the organization |  | 575ec8687ae143cd83dc4a97 |
| invite | [Organization Invitation Post](_schemas.md#organization-invitation-post) | Y | Object containing new invite info |  | [Organization Invitation Post Example](_schemas.md#organization-invitation-post-example) |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 201 | [Instance Organization Invitations](_schemas.md#instance-organization-invitations) | The new organization invite |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if instance or organization was not found |
