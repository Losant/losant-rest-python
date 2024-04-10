# Instance Audit Log Actions

Details on the various actions that can be performed on the
Instance Audit Log resource, including the expected
parameters and the potential responses.

##### Contents

*   [Get](#get)

<br/>

## Get

Retrieves information on an instance audit log

```python
result = client.instance_audit_log.get(
    instanceId=my_instance_id,
    instanceAuditLogId=my_instance_audit_log_id)

print(result)
```

#### Authentication
The client must be configured with a valid api access token to call this
action. The token must include at least one of the following scopes:
all.Instance, all.Instance.read, all.User, all.User.read, instanceAuditLog.*, or instanceAuditLog.get.

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| instanceId | string | Y | ID associated with the instance |  | 575ec7417ae143cd83dc4a96 |
| instanceAuditLogId | string | Y | ID associated with the instance audit log |  | 57955788124b37010084c053 |
| losantdomain | string | N | Domain scope of request (rarely needed) |  | example.com |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Instance Audit Log](_schemas.md#instance-audit-log) | Instance audit log information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if instance audit log was not found |
