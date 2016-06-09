# Device Recipe Actions

Details on the various actions that can be performed on the
Device Recipe resource, including the expected
parameters and the potential responses.

##### Contents

*   [Bulk Create](#bulk-create)
*   [Delete](#delete)
*   [Get](#get)
*   [Patch](#patch)

<br/>

## Bulk Create

Bulk creates devices using this recipe from a CSV

```python
result = client.device_recipe.bulk_create(
    applicationId=my_application_id,
    deviceRecipeId=my_device_recipe_id,
    bulkInfo=my_bulk_info)

print(result)
```

#### Available Parameters

| Name | Type | Required | Description | Default |
| ---- | ---- | -------- | ----------- | ------- |
| applicationId | string | Y | ID associated with the application |  |
| deviceRecipeId | string | Y | ID associated with the device recipe |  |
| bulkInfo | [Device Recipe Bulk Create Post](_schemas.md#device-recipe-bulk-create-post) | Y | Object containing bulk creation info |  |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 201 | [Device Recipe Bulk Create](_schemas.md#device-recipe-bulk-create) | If devices were sucessfully created |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 404 | [Error](_schemas.md#error) | Error if device recipe was not found |

<br/>

## Delete

Deletes a device recipe

```python
result = client.device_recipe.delete(
    applicationId=my_application_id,
    deviceRecipeId=my_device_recipe_id)

print(result)
```

#### Available Parameters

| Name | Type | Required | Description | Default |
| ---- | ---- | -------- | ----------- | ------- |
| applicationId | string | Y | ID associated with the application |  |
| deviceRecipeId | string | Y | ID associated with the device recipe |  |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Success](_schemas.md#success) | If device recipe was successfully deleted |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 404 | [Error](_schemas.md#error) | Error if device recipe was not found |

<br/>

## Get

Retrieves information on a device recipe

```python
result = client.device_recipe.get(
    applicationId=my_application_id,
    deviceRecipeId=my_device_recipe_id)

print(result)
```

#### Available Parameters

| Name | Type | Required | Description | Default |
| ---- | ---- | -------- | ----------- | ------- |
| applicationId | string | Y | ID associated with the application |  |
| deviceRecipeId | string | Y | ID associated with the device recipe |  |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Device Recipe](_schemas.md#device-recipe) | Device recipe information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 404 | [Error](_schemas.md#error) | Error if device recipe was not found |

<br/>

## Patch

Updates information about a device recipe

```python
result = client.device_recipe.patch(
    applicationId=my_application_id,
    deviceRecipeId=my_device_recipe_id,
    deviceRecipe=my_device_recipe)

print(result)
```

#### Available Parameters

| Name | Type | Required | Description | Default |
| ---- | ---- | -------- | ----------- | ------- |
| applicationId | string | Y | ID associated with the application |  |
| deviceRecipeId | string | Y | ID associated with the device recipe |  |
| deviceRecipe | [Device Recipe Patch](_schemas.md#device-recipe-patch) | Y | Object containing new properties of the device recipe |  |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Device Recipe](_schemas.md#device-recipe) | Updated device recipe information |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if device recipe was not found |
