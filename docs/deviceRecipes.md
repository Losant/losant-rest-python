# Device Recipes Actions

Details on the various actions that can be performed on the
Device Recipes resource, including the expected
parameters and the potential responses.

##### Contents

*   [Get](#get)
*   [Post](#post)

<br/>

## Get

Returns the device recipes for an application

```python
result = client.device_recipes.get(applicationId=my_application_id)

print(result)
```

#### Available Parameters

| Name | Type | Required | Description | Default |
| ---- | ---- | -------- | ----------- | ------- |
| applicationId | string | Y | ID associated with the application |  |
| sortField | string | N | Field to sort the results by. Accepted values are: name, id, creationDate | name |
| sortDirection | string | N | Direction to sort the results by. Accepted values are: asc, desc | asc |
| page | string | N | Which page of results to return | 0 |
| perPage | string | N | How many items to return per page | 1000 |
| filterField | string | N | Field to filter the results by. Blank or not provided means no filtering. Accepted values are: name |  |
| filter | string | N | Filter to apply against the filtered field. Supports globbing. Blank or not provided means no filtering. |  |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Device Recipes](_schemas.md#device-recipes) | Collection of device recipes |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 404 | [Error](_schemas.md#error) | Error if application was not found |

<br/>

## Post

Create a new device recipe for an application

```python
result = client.device_recipes.post(
    applicationId=my_application_id,
    deviceRecipe=my_device_recipe)

print(result)
```

#### Available Parameters

| Name | Type | Required | Description | Default |
| ---- | ---- | -------- | ----------- | ------- |
| applicationId | string | Y | ID associated with the application |  |
| deviceRecipe | [Device Recipe Post](_schemas.md#device-recipe-post) | Y | New device recipe information |  |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 201 | [Device Recipe](_schemas.md#device-recipe) | Successfully created device recipe |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if application was not found |
