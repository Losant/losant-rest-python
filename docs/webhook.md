# Webhook Actions

Details on the various actions that can be performed on the
Webhook resource, including the expected
parameters and the potential responses.

##### Contents

*   [Delete](#delete)
*   [Get](#get)
*   [Patch](#patch)

<br/>

## Delete

Deletes a webhook

```python
result = client.webhook.delete(
    applicationId=my_application_id,
    webhookId=my_webhook_id)

print(result)
```

#### Available Parameters

| Name | Type | Required | Description | Default |
| ---- | ---- | -------- | ----------- | ------- |
| applicationId | string | Y | ID associated with the application |  |
| webhookId | string | Y | ID associated with the webhook |  |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Success](_schemas.md#success) | If webhook was successfully deleted |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 404 | [Error](_schemas.md#error) | Error if webhook was not found |

<br/>

## Get

Retrieves information on a webhook

```python
result = client.webhook.get(
    applicationId=my_application_id,
    webhookId=my_webhook_id)

print(result)
```

#### Available Parameters

| Name | Type | Required | Description | Default |
| ---- | ---- | -------- | ----------- | ------- |
| applicationId | string | Y | ID associated with the application |  |
| webhookId | string | Y | ID associated with the webhook |  |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Webhook](_schemas.md#webhook) | Webhook information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 404 | [Error](_schemas.md#error) | Error if webhook was not found |

<br/>

## Patch

Updates information about a webhook

```python
result = client.webhook.patch(
    applicationId=my_application_id,
    webhookId=my_webhook_id,
    webhook=my_webhook)

print(result)
```

#### Available Parameters

| Name | Type | Required | Description | Default |
| ---- | ---- | -------- | ----------- | ------- |
| applicationId | string | Y | ID associated with the application |  |
| webhookId | string | Y | ID associated with the webhook |  |
| webhook | [Webhook Patch](_schemas.md#webhook-patch) | Y | Object containing new properties of the webhook |  |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Webhook](_schemas.md#webhook) | Updated webhook information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if webhook was not found |
