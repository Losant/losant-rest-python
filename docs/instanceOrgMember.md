# Instance Org Member Actions

Details on the various actions that can be performed on the
Instance Org Member resource, including the expected
parameters and the potential responses.

##### Contents

*   [Delete](#delete)
*   [Get](#get)
*   [Patch](#patch)

<br/>

## Delete

Deletes an organization member

```python
result = client.instance_org_member.delete(
    instanceId=my_instance_id,
    orgId=my_org_id,
    userId=my_user_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Instance, all.User, instanceOrgMember.*, or instanceOrgMember.delete.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| instanceId | string | Y | ID associated with the instance |  | 575ec8687ae143cd83dc4a95 |
| orgId | string | Y | ID associated with the organization |  | 575ec8687ae143cd83dc4a97 |
| userId | string | Y | ID associated with the organization member |  | 575ec8687ae143cd83dc4a94 |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Success](_schemas.md#success) | If member was successfully deleted |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if organization or member was not found |

<br/>

## Get

Returns an organization member

```python
result = client.instance_org_member.get(
    instanceId=my_instance_id,
    orgId=my_org_id,
    userId=my_user_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Instance, all.Instance.read, all.User, all.User.read, instanceOrgMember.*, or instanceOrgMember.get.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| instanceId | string | Y | ID associated with the instance |  | 575ec8687ae143cd83dc4a95 |
| orgId | string | Y | ID associated with the organization |  | 575ec8687ae143cd83dc4a97 |
| userId | string | Y | ID associated with the organization member |  | 575ec8687ae143cd83dc4a94 |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Instance Org Member](_schemas.md#instance-org-member) | A single organization member |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if instance, organization, or member was not found |

<br/>

## Patch

Modifies the role of an organization member

```python
result = client.instance_org_member.patch(
    instanceId=my_instance_id,
    orgId=my_org_id,
    userId=my_user_id,
    member=my_member)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Instance, all.User, instanceOrgMember.*, or instanceOrgMember.patch.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| instanceId | string | Y | ID associated with the instance |  | 575ec8687ae143cd83dc4a95 |
| orgId | string | Y | ID associated with the organization |  | 575ec8687ae143cd83dc4a97 |
| userId | string | Y | ID associated with the organization member |  | 575ec8687ae143cd83dc4a94 |
| member | [Instance Org Member Patch](_schemas.md#instance-org-member-patch) | Y | Object containing new member info |  | [Instance Org Member Patch Example](_schemas.md#instance-org-member-patch-example) |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Instance Org Member](_schemas.md#instance-org-member) | The modified organization member |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if organization or member was not found |
