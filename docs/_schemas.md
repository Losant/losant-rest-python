# Schemas

*   [API Token](#api-token)
*   [API Token Patch](#api-token-patch)
*   [Application](#application)
*   [Application API Token Post](#application-api-token-post)
*   [Application Key](#application-key)
*   [Application Key Patch](#application-key-patch)
*   [Application Key Post](#application-key-post)
*   [Application Keys](#application-keys)
*   [Application Patch](#application-patch)
*   [Application Post](#application-post)
*   [Applications](#applications)
*   [Audit Log](#audit-log)
*   [Audit Log Filter](#audit-log-filter)
*   [Audit Logs](#audit-logs)
*   [Authenticated Device](#authenticated-device)
*   [Authenticated Solution User](#authenticated-solution-user)
*   [Authenticated User](#authenticated-user)
*   [Composite Device State](#composite-device-state)
*   [Dashboard](#dashboard)
*   [Dashboard Context Instance](#dashboard-context-instance)
*   [Dashboard Patch](#dashboard-patch)
*   [Dashboard Post](#dashboard-post)
*   [Dashboards](#dashboards)
*   [Device](#device)
*   [Device Command](#device-command)
*   [Device Commands](#device-commands)
*   [Device Credentials](#device-credentials)
*   [Device Log](#device-log)
*   [Device Patch](#device-patch)
*   [Device Post](#device-post)
*   [Device Recipe](#device-recipe)
*   [Device Recipe Bulk Create](#device-recipe-bulk-create)
*   [Device Recipe Bulk Create Post](#device-recipe-bulk-create-post)
*   [Device Recipe Patch](#device-recipe-patch)
*   [Device Recipe Post](#device-recipe-post)
*   [Device Recipes](#device-recipes)
*   [Single or Multiple Device States](#single-or-multiple-device-states)
*   [Device States](#device-states)
*   [Device Tag Filter](#device-tag-filter)
*   [Devices](#devices)
*   [Disable Two Factor Auth](#disable-two-factor-auth)
*   [Enable Two Factor Auth](#enable-two-factor-auth)
*   [Error](#error)
*   [Event](#event)
*   [Event Patch](#event-patch)
*   [Event Post](#event-post)
*   [Events](#events)
*   [Workflow](#workflow)
*   [Workflow Log](#workflow-log)
*   [Workflow Patch](#workflow-patch)
*   [Workflow Post](#workflow-post)
*   [Workflow Storage Entries](#workflow-storage-entries)
*   [Workflow Storage Entry](#workflow-storage-entry)
*   [Workflows](#workflows)
*   [Github Login](#github-login)
*   [Last Value Data](#last-value-data)
*   [Last Value Query](#last-value-query)
*   [Me](#me)
*   [Me Patch](#me-patch)
*   [Multi Device Command](#multi-device-command)
*   [Organization](#organization)
*   [Organization Invitation Action](#organization-invitation-action)
*   [Organization Invitation Information](#organization-invitation-information)
*   [Organization Invitation Post](#organization-invitation-post)
*   [Organization Invitation Result](#organization-invitation-result)
*   [Organization Invitations](#organization-invitations)
*   [Organization Member Patch](#organization-member-patch)
*   [Organization Patch](#organization-patch)
*   [Organization Post](#organization-post)
*   [Organizations](#organizations)
*   [Payload Counts](#payload-counts)
*   [Recent Item](#recent-item)
*   [Recent Item List](#recent-item-list)
*   [Resource Transfer](#resource-transfer)
*   [Solution](#solution)
*   [Solution Patch](#solution-patch)
*   [Solution Post](#solution-post)
*   [Solution User](#solution-user)
*   [User Credentials](#user-credentials)
*   [Solution User Patch](#solution-user-patch)
*   [Solution User Post](#solution-user-post)
*   [Solution Users](#solution-users)
*   [Solutions](#solutions)
*   [Success](#success)
*   [Time Series Data](#time-series-data)
*   [Time Series Query](#time-series-query)
*   [User Credentials](#user-credentials)
*   [Virtual Button Press](#virtual-button-press)
*   [Webhook](#webhook)
*   [Webhook Patch](#webhook-patch)
*   [Webhook Post](#webhook-post)
*   [Webhooks](#webhooks)

## API Token

Schema for a single API Token

### <a name="api-token-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "apiTokenId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "ownerId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "ownerType": {
      "type": "string",
      "enum": [
        "application"
      ]
    },
    "creatorId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "creatorType": {
      "type": "string",
      "enum": [
        "apiToken",
        "user",
        "flow"
      ]
    },
    "creatorName": {
      "type": "string",
      "maxLength": 1024
    },
    "name": {
      "type": "string",
      "minLength": 1,
      "maxLength": 255
    },
    "description": {
      "type": "string",
      "maxLength": 32767
    },
    "creationDate": {
      "type": "string",
      "format": "date-time"
    },
    "lastUpdated": {
      "type": "string",
      "format": "date-time"
    },
    "expirationDate": {
      "type": "string",
      "format": "date-time"
    },
    "scope": {
      "type": "array",
      "items": {
        "type": "string",
        "minLength": 1,
        "maxLength": 1024
      }
    },
    "status": {
      "type": "string",
      "enum": [
        "active",
        "inactive"
      ]
    },
    "token": {
      "type": "string",
      "minLength": 1
    }
  }
}
```
### <a name="api-token-example"></a> Example

```json
{
  "id": "575ec7417ae143cd83dc4a95",
  "apiTokenId": "575ec7417ae143cd83dc4a95",
  "creatorId": "575ed70c7ae143cd83dc4aa9",
  "creatorType": "user",
  "ownerId": "575ec8687ae143cd83dc4a97",
  "ownerType": "application",
  "name": "My API Token",
  "creationDate": "2016-06-13T04:00:00.000Z",
  "lastUpdated": "2016-06-13T04:00:00.000Z",
  "expirationDate": "2017-06-13T04:00:00.000Z",
  "scope": [
    "all.Application"
  ],
  "status": "active",
  "token": "the_actual_token_string"
}
```

<br/>

## API Token Patch

Schema for the body of an API Token modification request

### <a name="api-token-patch-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "minLength": 1,
      "maxLength": 255
    },
    "description": {
      "type": "string",
      "maxLength": 32767
    },
    "status": {
      "type": "string",
      "enum": [
        "active",
        "inactive"
      ]
    }
  },
  "additionalProperties": false
}
```
### <a name="api-token-patch-example"></a> Example

```json
{
  "name": "My Updated API Token",
  "status": "inactive"
}
```

<br/>

## Application

Schema for a single Application

### <a name="application-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "applicationId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "creationDate": {
      "type": "string",
      "format": "date-time"
    },
    "lastUpdated": {
      "type": "string",
      "format": "date-time"
    },
    "ownerId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "ownerType": {
      "type": "string",
      "enum": [
        "user",
        "organization"
      ]
    },
    "name": {
      "type": "string",
      "minLength": 1,
      "maxLength": 255
    },
    "description": {
      "type": "string",
      "maxLength": 32767
    },
    "summary": {
      "type": "object",
      "properties": {
        "deviceCount": {
          "type": "number"
        },
        "flowCount": {
          "type": "number"
        },
        "webhookCount": {
          "type": "number"
        },
        "eventCount": {
          "type": "number"
        },
        "keyCount": {
          "type": "number"
        },
        "deviceRecipeCount": {
          "type": "number"
        }
      }
    }
  }
}
```
### <a name="application-example"></a> Example

```json
{
  "id": "575ec8687ae143cd83dc4a97",
  "applicationId": "575ec8687ae143cd83dc4a97",
  "creationDate": "2016-06-13T04:00:00.000Z",
  "lastUpdated": "2016-06-13T04:00:00.000Z",
  "ownerId": "575ed70c7ae143cd83dc4aa9",
  "ownerType": "user",
  "name": "My Application",
  "description": "The is the best application description",
  "summary": {
    "deviceCount": 5,
    "flowCount": 2,
    "webhookCount": 0,
    "eventCount": 0,
    "keyCount": 1,
    "deviceRecipeCount": 0
  }
}
```

<br/>

## Application API Token Post

Schema for the body of an Application API Token creation request

### <a name="application-api-token-post-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "minLength": 1,
      "maxLength": 255
    },
    "description": {
      "type": "string",
      "maxLength": 32767
    },
    "expirationDate": {
      "type": "string",
      "format": "date-time"
    },
    "scope": {
      "type": "array",
      "items": {
        "type": "string",
        "enum": [
          "all.Application",
          "all.Application.read",
          "all.Device",
          "all.Device.read",
          "application.*",
          "applicationApiToken.*",
          "applicationApiTokens.*",
          "applicationKey.*",
          "applicationKeys.*",
          "data.*",
          "device.*",
          "deviceRecipe.*",
          "deviceRecipes.*",
          "devices.*",
          "event.*",
          "events.*",
          "flow.*",
          "flows.*",
          "webhook.*",
          "webhooks.*",
          "application.delete",
          "application.get",
          "application.patch",
          "application.payloadCounts",
          "applicationApiToken.delete",
          "applicationApiToken.get",
          "applicationApiToken.patch",
          "applicationApiTokens.get",
          "applicationApiTokens.post",
          "applicationKey.delete",
          "applicationKey.get",
          "applicationKey.patch",
          "applicationKeys.get",
          "applicationKeys.post",
          "data.lastValueQuery",
          "data.timeSeriesQuery",
          "device.delete",
          "device.export",
          "device.get",
          "device.getCommand",
          "device.getCompositeState",
          "device.getLogEntries",
          "device.getState",
          "device.patch",
          "device.removeData",
          "device.sendCommand",
          "device.sendState",
          "deviceRecipe.bulkCreate",
          "deviceRecipe.delete",
          "deviceRecipe.get",
          "deviceRecipe.patch",
          "deviceRecipes.get",
          "deviceRecipes.post",
          "devices.export",
          "devices.get",
          "devices.post",
          "devices.sendCommand",
          "event.delete",
          "event.get",
          "event.patch",
          "events.get",
          "events.mostRecentBySeverity",
          "events.patch",
          "events.post",
          "flow.delete",
          "flow.get",
          "flow.getStorageEntries",
          "flow.log",
          "flow.patch",
          "flow.pressVirtualButton",
          "flow.setStorageEntry",
          "flows.create",
          "flows.get",
          "webhook.delete",
          "webhook.get",
          "webhook.patch",
          "webhooks.get",
          "webhooks.post"
        ]
      }
    },
    "status": {
      "type": "string",
      "enum": [
        "active",
        "inactive"
      ]
    }
  },
  "additionalProperties": false,
  "required": [
    "name"
  ]
}
```
### <a name="application-api-token-post-example"></a> Example

```json
{
  "name": "My New API Token",
  "expirationDate": "2017-06-13T04:00:00.000Z",
  "scope": [
    "all.Application"
  ],
  "status": "active"
}
```

<br/>

## Application Key

Schema for a single Application Key

### <a name="application-key-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "applicationKeyId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "applicationId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "creationDate": {
      "type": "string",
      "format": "date-time"
    },
    "lastUpdated": {
      "type": "string",
      "format": "date-time"
    },
    "key": {
      "type": "string"
    },
    "status": {
      "type": "string",
      "enum": [
        "active",
        "inactive"
      ]
    },
    "secret": {
      "type": "string"
    },
    "deviceIds": {
      "type": "array",
      "items": {
        "type": "string",
        "pattern": "^[A-Fa-f\\d]{24}$"
      }
    },
    "deviceTags": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "key": {
            "type": "string",
            "pattern": "^[0-9a-zA-Z_-]{1,255}$"
          },
          "value": {
            "type": "string",
            "minLength": 1,
            "maxLength": 255
          }
        },
        "additionalProperties": false
      }
    },
    "description": {
      "type": "string",
      "maxLength": 32767
    }
  }
}
```
### <a name="application-key-example"></a> Example

```json
{
  "id": "575ec76c7ae143cd83dc4a96",
  "applicationKeyId": "575ec76c7ae143cd83dc4a96",
  "applicationId": "575ec8687ae143cd83dc4a97",
  "creationDate": "2016-06-13T04:00:00.000Z",
  "lastUpdated": "2016-06-13T04:00:00.000Z",
  "key": "this_would_be_the_key",
  "status": "active",
  "description": "An example key description"
}
```

<br/>

## Application Key Patch

Schema for the body of an Application Key modification request

### <a name="application-key-patch-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string",
      "enum": [
        "active",
        "inactive"
      ]
    },
    "description": {
      "type": "string",
      "maxLength": 32767
    }
  },
  "additionalProperties": false
}
```
### <a name="application-key-patch-example"></a> Example

```json
{
  "status": "active",
  "description": "An example updated key description"
}
```

<br/>

## Application Key Post

Schema for the body of an Application Key creation request

### <a name="application-key-post-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "deviceIds": {
      "type": "array",
      "items": {
        "type": "string",
        "pattern": "^[A-Fa-f\\d]{24}$"
      }
    },
    "deviceTags": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "key": {
            "type": "string",
            "pattern": "^[0-9a-zA-Z_-]{1,255}$"
          },
          "value": {
            "type": "string",
            "minLength": 1,
            "maxLength": 255
          }
        },
        "additionalProperties": false
      }
    },
    "description": {
      "type": "string",
      "maxLength": 32767
    }
  },
  "additionalProperties": false
}
```
### <a name="application-key-post-example"></a> Example

```json
{
  "description": "An example new key description"
}
```

<br/>

## Application Keys

Schema for a collection of Application Keys

### <a name="application-keys-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "items": {
      "type": "array",
      "items": {
        "title": "Application Key",
        "description": "Schema for a single Application Key",
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "applicationKeyId": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "applicationId": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "creationDate": {
            "type": "string",
            "format": "date-time"
          },
          "lastUpdated": {
            "type": "string",
            "format": "date-time"
          },
          "key": {
            "type": "string"
          },
          "status": {
            "type": "string",
            "enum": [
              "active",
              "inactive"
            ]
          },
          "secret": {
            "type": "string"
          },
          "deviceIds": {
            "type": "array",
            "items": {
              "type": "string",
              "pattern": "^[A-Fa-f\\d]{24}$"
            }
          },
          "deviceTags": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "key": {
                  "type": "string",
                  "pattern": "^[0-9a-zA-Z_-]{1,255}$"
                },
                "value": {
                  "type": "string",
                  "minLength": 1,
                  "maxLength": 255
                }
              },
              "additionalProperties": false
            }
          },
          "description": {
            "type": "string",
            "maxLength": 32767
          }
        }
      }
    },
    "count": {
      "type": "integer"
    },
    "totalCount": {
      "type": "integer"
    },
    "perPage": {
      "type": "integer"
    },
    "page": {
      "type": "integer"
    },
    "filter": {
      "type": "string"
    },
    "filterField": {
      "type": "string"
    },
    "sortField": {
      "type": "string"
    },
    "sortDirection": {
      "type": "string",
      "enum": [
        "asc",
        "desc"
      ]
    },
    "applicationId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    }
  }
}
```
### <a name="application-keys-example"></a> Example

```json
{
  "items": [
    {
      "id": "575ec76c7ae143cd83dc4a96",
      "applicationKeyId": "575ec76c7ae143cd83dc4a96",
      "applicationId": "575ec8687ae143cd83dc4a97",
      "creationDate": "2016-06-13T04:00:00.000Z",
      "lastUpdated": "2016-06-13T04:00:00.000Z",
      "key": "this_would_be_the_key",
      "status": "active",
      "description": "An example key description"
    }
  ],
  "count": 1,
  "totalCount": 4,
  "perPage": 1,
  "page": 0,
  "sortField": "key",
  "sortDirection": "asc",
  "applicationId": "575ec8687ae143cd83dc4a97"
}
```

<br/>

## Application Patch

Schema for the body of an Application modification request

### <a name="application-patch-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "minLength": 1,
      "maxLength": 255
    },
    "description": {
      "type": "string",
      "maxLength": 32767
    }
  },
  "additionalProperties": false
}
```
### <a name="application-patch-example"></a> Example

```json
{
  "name": "My Updated Application",
  "description": "Description of my updated application"
}
```

<br/>

## Application Post

Schema for the body of an Application creation request

### <a name="application-post-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "orgId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "name": {
      "type": "string",
      "minLength": 1,
      "maxLength": 255
    },
    "description": {
      "type": "string",
      "maxLength": 32767
    }
  },
  "additionalProperties": false,
  "required": [
    "name"
  ]
}
```
### <a name="application-post-example"></a> Example

```json
{
  "name": "My New Application",
  "description": "Description of my new application"
}
```

<br/>

## Applications

Schema for a collection of Applications

### <a name="applications-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "items": {
      "type": "array",
      "items": {
        "title": "Application",
        "description": "Schema for a single Application",
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "applicationId": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "creationDate": {
            "type": "string",
            "format": "date-time"
          },
          "lastUpdated": {
            "type": "string",
            "format": "date-time"
          },
          "ownerId": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "ownerType": {
            "type": "string",
            "enum": [
              "user",
              "organization"
            ]
          },
          "name": {
            "type": "string",
            "minLength": 1,
            "maxLength": 255
          },
          "description": {
            "type": "string",
            "maxLength": 32767
          },
          "summary": {
            "type": "object",
            "properties": {
              "deviceCount": {
                "type": "number"
              },
              "flowCount": {
                "type": "number"
              },
              "webhookCount": {
                "type": "number"
              },
              "eventCount": {
                "type": "number"
              },
              "keyCount": {
                "type": "number"
              },
              "deviceRecipeCount": {
                "type": "number"
              }
            }
          }
        }
      }
    },
    "count": {
      "type": "integer"
    },
    "totalCount": {
      "type": "integer"
    },
    "perPage": {
      "type": "integer"
    },
    "page": {
      "type": "integer"
    },
    "filter": {
      "type": "string"
    },
    "filterField": {
      "type": "string"
    },
    "sortField": {
      "type": "string"
    },
    "sortDirection": {
      "type": "string",
      "enum": [
        "asc",
        "desc"
      ]
    }
  }
}
```
### <a name="applications-example"></a> Example

```json
{
  "items": [
    {
      "id": "575ec8687ae143cd83dc4a97",
      "applicationId": "575ec8687ae143cd83dc4a97",
      "creationDate": "2016-06-13T04:00:00.000Z",
      "lastUpdated": "2016-06-13T04:00:00.000Z",
      "ownerId": "575ed70c7ae143cd83dc4aa9",
      "ownerType": "user",
      "name": "My Application",
      "description": "The is the best application description",
      "summary": {
        "deviceCount": 5,
        "flowCount": 2,
        "webhookCount": 0,
        "eventCount": 0,
        "keyCount": 1,
        "deviceRecipeCount": 0
      }
    }
  ],
  "count": 1,
  "totalCount": 8,
  "perPage": 1,
  "page": 0,
  "sortField": "name",
  "sortDirection": "asc"
}
```

<br/>

## Audit Log

Schema for a single Audit Log entry

### <a name="audit-log-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "auditLogId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "creationDate": {
      "type": "string",
      "format": "date-time"
    },
    "orgId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "primaryTargetId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "primaryTargetType": {
      "type": "string",
      "enum": [
        "Application",
        "Dashboard",
        "Solution",
        "OrgInvite"
      ]
    },
    "primaryTargetName": {
      "type": "string",
      "maxLength": 1024
    },
    "secondaryTargetId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "secondaryTargetType": {
      "type": "string",
      "enum": [
        "ApiToken",
        "ApplicationKey",
        "Device",
        "DeviceRecipe",
        "Event",
        "Flow",
        "SolutionUser",
        "Webhook"
      ]
    },
    "secondaryTargetName": {
      "type": "string",
      "maxLength": 1024
    },
    "actorId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "actorType": {
      "type": "string",
      "enum": [
        "Application",
        "Device",
        "Flow",
        "SolutionUser",
        "User",
        "ApiToken"
      ]
    },
    "actorName": {
      "type": "string",
      "maxLength": 1024
    },
    "requestResource": {
      "type": "string",
      "maxLength": 1024
    },
    "requestAction": {
      "type": "string",
      "maxLength": 1024
    },
    "requestQueryParams": {
      "type": "object"
    },
    "requestBody": {
      "type": "object"
    },
    "requestPathParams": {
      "type": "object"
    },
    "responseBody": {
      "type": "object"
    },
    "responseStatus": {
      "type": "integer",
      "minimum": 100,
      "maximum": 599
    }
  }
}
```
### <a name="audit-log-example"></a> Example

```json
{
  "id": "586e9d5151265cb9d72f6ec6",
  "auditLogId": "586e9d5151265cb9d72f6ec6",
  "creationDate": "2016-06-13T04:00:00.000Z",
  "orgId": "575ed6e87ae143cd83dc4aa8",
  "primaryTargetId": "575ec8687ae143cd83dc4a97",
  "primaryTargetType": "Application",
  "primaryTargetName": "My Application",
  "actorId": "575ed70c7ae143cd83dc4aa9",
  "actorType": "User",
  "actorName": "example@losant.com",
  "requestResource": "application",
  "requestAction": "delete",
  "requestQueryParams": {},
  "requestBody": {},
  "requestPathParams": {
    "applicationId": "575ec8687ae143cd83dc4a97"
  },
  "responseBody": {
    "success": true
  },
  "responseStatus": 200
}
```

<br/>

## Audit Log Filter

Schema for the filter of an audit log query

### <a name="audit-log-filter-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "primaryTarget": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "type": {
            "type": "string",
            "enum": [
              "Application",
              "Dashboard",
              "Solution",
              "OrgInvite"
            ]
          },
          "name": {
            "type": "string",
            "maxLength": 1024
          }
        },
        "additionalProperties": false
      }
    },
    "secondaryTarget": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "type": {
            "type": "string",
            "enum": [
              "ApiToken",
              "ApplicationKey",
              "Device",
              "DeviceRecipe",
              "Event",
              "Flow",
              "SolutionUser",
              "Webhook"
            ]
          },
          "name": {
            "type": "string",
            "maxLength": 1024
          }
        },
        "additionalProperties": false
      }
    },
    "actor": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "type": {
            "type": "string",
            "enum": [
              "Application",
              "Device",
              "Flow",
              "SolutionUser",
              "User",
              "ApiToken"
            ]
          },
          "name": {
            "type": "string",
            "maxLength": 1024
          }
        },
        "additionalProperties": false
      }
    },
    "request": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "resource": {
            "type": "string",
            "maxLength": 1024
          },
          "action": {
            "type": "string",
            "maxLength": 1024
          }
        },
        "additionalProperties": false
      }
    },
    "responseCode": {
      "type": "array",
      "items": {
        "type": "integer",
        "minimum": 100,
        "maximum": 599
      }
    }
  },
  "additionalProperties": false
}
```
### <a name="audit-log-filter-example"></a> Example

```json
{
  "primaryTarget": [
    {
      "type": "Dashboard"
    },
    {
      "type": "Application",
      "id": "575ec8687ae143cd83dc4a97"
    }
  ],
  "actor": [
    {
      "type": "User",
      "id": "575ed70c7ae143cd83dc4aa9"
    }
  ]
}
```

<br/>

## Audit Logs

Schema for a collection of Audit Logs

### <a name="audit-logs-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "items": {
      "type": "array",
      "items": {
        "title": "Audit Log",
        "description": "Schema for a single Audit Log entry",
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "auditLogId": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "creationDate": {
            "type": "string",
            "format": "date-time"
          },
          "orgId": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "primaryTargetId": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "primaryTargetType": {
            "type": "string",
            "enum": [
              "Application",
              "Dashboard",
              "Solution",
              "OrgInvite"
            ]
          },
          "primaryTargetName": {
            "type": "string",
            "maxLength": 1024
          },
          "secondaryTargetId": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "secondaryTargetType": {
            "type": "string",
            "enum": [
              "ApiToken",
              "ApplicationKey",
              "Device",
              "DeviceRecipe",
              "Event",
              "Flow",
              "SolutionUser",
              "Webhook"
            ]
          },
          "secondaryTargetName": {
            "type": "string",
            "maxLength": 1024
          },
          "actorId": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "actorType": {
            "type": "string",
            "enum": [
              "Application",
              "Device",
              "Flow",
              "SolutionUser",
              "User",
              "ApiToken"
            ]
          },
          "actorName": {
            "type": "string",
            "maxLength": 1024
          },
          "requestResource": {
            "type": "string",
            "maxLength": 1024
          },
          "requestAction": {
            "type": "string",
            "maxLength": 1024
          },
          "requestQueryParams": {
            "type": "object"
          },
          "requestBody": {
            "type": "object"
          },
          "requestPathParams": {
            "type": "object"
          },
          "responseBody": {
            "type": "object"
          },
          "responseStatus": {
            "type": "integer",
            "minimum": 100,
            "maximum": 599
          }
        }
      }
    },
    "count": {
      "type": "integer"
    },
    "totalCount": {
      "type": "integer"
    },
    "perPage": {
      "type": "integer"
    },
    "page": {
      "type": "integer"
    },
    "sortField": {
      "type": "string"
    },
    "sortDirection": {
      "type": "string",
      "enum": [
        "asc",
        "desc"
      ]
    },
    "orgId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    }
  }
}
```
### <a name="audit-logs-example"></a> Example

```json
{
  "items": [
    {
      "id": "586e9d5151265cb9d72f6ec6",
      "auditLogId": "586e9d5151265cb9d72f6ec6",
      "creationDate": "2016-06-13T04:00:00.000Z",
      "orgId": "575ed6e87ae143cd83dc4aa8",
      "primaryTargetId": "575ec8687ae143cd83dc4a97",
      "primaryTargetType": "Application",
      "primaryTargetName": "My Application",
      "actorId": "575ed70c7ae143cd83dc4aa9",
      "actorType": "User",
      "actorName": "example@losant.com",
      "requestResource": "application",
      "requestAction": "delete",
      "requestQueryParams": {},
      "requestBody": {},
      "requestPathParams": {
        "applicationId": "575ec8687ae143cd83dc4a97"
      },
      "responseBody": {
        "success": true
      },
      "responseStatus": 200
    }
  ],
  "count": 1,
  "totalCount": 4,
  "perPage": 1,
  "page": 0,
  "sortField": "creationDate",
  "sortDirection": "desc",
  "orgId": "575ed6e87ae143cd83dc4aa8"
}
```

<br/>

## Authenticated Device

Schema for the successful response when authenticating a Device

### <a name="authenticated-device-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "applicationId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "deviceId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "deviceClass": {
      "type": "string",
      "enum": [
        "standalone",
        "gateway",
        "peripheral",
        "floating",
        "virtual"
      ]
    },
    "token": {
      "type": "string",
      "minLength": 1
    }
  },
  "required": [
    "applicationId",
    "deviceId",
    "deviceClass",
    "token"
  ]
}
```
### <a name="authenticated-device-example"></a> Example

```json
{
  "applicationId": "575ec8687ae143cd83dc4a97",
  "deviceId": "575ecf887ae143cd83dc4aa2",
  "deviceClass": "standalone",
  "token": "token_to_use_for_authenticating_subsequent_requests"
}
```

<br/>

## Authenticated Solution User

Schema for the successful response when authenticating a Solution User

### <a name="authenticated-solution-user-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "solutionUserId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "token": {
      "type": "string",
      "minLength": 1
    }
  },
  "required": [
    "solutionUserId",
    "token"
  ]
}
```
### <a name="authenticated-solution-user-example"></a> Example

```json
{
  "solutionUserId": "566116085df4b701000258e3",
  "token": "token_to_use_for_authenticating_subsequent_requests"
}
```

<br/>

## Authenticated User

Schema for the successful response when authenticating a User

### <a name="authenticated-user-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "userId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "token": {
      "type": "string",
      "minLength": 1
    }
  },
  "required": [
    "userId",
    "token"
  ]
}
```
### <a name="authenticated-user-example"></a> Example

```json
{
  "userId": "575ed70c7ae143cd83dc4aa9",
  "token": "token_to_use_for_authenticating_subsequent_requests"
}
```

<br/>

## Composite Device State

Schema for a composite Device state

### <a name="composite-device-state-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "patternProperties": {
    "^[0-9a-zA-Z_-]{1,255}$": {
      "type": "object",
      "properties": {
        "value": {
          "type": [
            "number",
            "string",
            "boolean"
          ]
        },
        "time": {
          "oneOf": [
            {
              "type": "string"
            },
            {
              "type": "number"
            },
            {
              "type": "object",
              "properties": {
                "$date": {
                  "type": "string"
                }
              },
              "additionalProperties": false,
              "required": [
                "$date"
              ]
            }
          ]
        },
        "relayId": {
          "type": "string"
        }
      }
    }
  },
  "additionalProperties": false
}
```
### <a name="composite-device-state-example"></a> Example

```json
{
  "voltage": {
    "time": "2016-06-13T04:00:00.000Z",
    "value": 22.4
  },
  "loaded": {
    "time": "2016-06-13T03:00:00.000Z",
    "value": false
  }
}
```

<br/>

## Dashboard

Schema for a single Dashboard

### <a name="dashboard-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "dashboardId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "creationDate": {
      "type": "string",
      "format": "date-time"
    },
    "lastUpdated": {
      "type": "string",
      "format": "date-time"
    },
    "ownerId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "ownerType": {
      "type": "string",
      "enum": [
        "user",
        "organization"
      ]
    },
    "name": {
      "type": "string",
      "minLength": 1,
      "maxLength": 255
    },
    "description": {
      "type": "string",
      "maxLength": 32767
    },
    "refreshRate": {
      "type": "number",
      "minimum": 5,
      "maximum": 600
    },
    "isPasswordProtected": {
      "type": "boolean"
    },
    "public": {
      "type": "boolean"
    },
    "blocks": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "blockType": {
            "type": "string"
          },
          "title": {
            "type": "string",
            "maxLength": 255
          },
          "applicationId": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "startX": {
            "type": "integer"
          },
          "startY": {
            "type": "integer"
          },
          "width": {
            "type": "integer"
          },
          "height": {
            "type": "integer"
          },
          "config": {
            "type": "object"
          }
        },
        "required": [
          "blockType",
          "startX",
          "startY",
          "width",
          "height"
        ],
        "additionalProperties": false
      }
    },
    "contextConfiguration": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "pattern": "^[0-9a-zA-Z_-]{1,255}$"
          },
          "type": {
            "type": "string",
            "enum": [
              "deviceId",
              "deviceAttribute",
              "string",
              "number"
            ]
          },
          "applicationId": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "defaultValue": {
            "type": [
              "string",
              "number"
            ]
          },
          "validationEnabled": {
            "type": "boolean"
          },
          "validationConfig": {
            "type": "object",
            "properties": {
              "min": {
                "type": "number"
              },
              "max": {
                "type": "number"
              },
              "regExp": {
                "type": "string",
                "maxLength": 1024
              },
              "attributes": {
                "type": "array",
                "items": {
                  "type": "string",
                  "pattern": "^[0-9a-zA-Z_-]{1,255}$"
                }
              },
              "deviceIds": {
                "type": "array",
                "items": {
                  "type": "string",
                  "pattern": "^[A-Fa-f\\d]{24}$"
                }
              },
              "deviceTags": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "key": {
                      "type": "string",
                      "pattern": "^[0-9a-zA-Z_-]{1,255}$"
                    },
                    "value": {
                      "type": "string",
                      "minLength": 1,
                      "maxLength": 255
                    }
                  },
                  "additionalProperties": false
                }
              }
            },
            "additionalProperties": false
          }
        },
        "required": [
          "name",
          "type",
          "defaultValue"
        ],
        "additionalProperties": false
      }
    }
  }
}
```
### <a name="dashboard-example"></a> Example

```json
{
  "id": "575ece2b7ae143cd83dc4a9b",
  "dashboardId": "575ece2b7ae143cd83dc4a9b",
  "creationDate": "2016-06-13T04:00:00.000Z",
  "lastUpdated": "2016-06-13T04:00:00.000Z",
  "ownerId": "575ed70c7ae143cd83dc4aa9",
  "ownerType": "user",
  "name": "My Dashboard",
  "description": "The best dashboard description",
  "refreshRate": 60,
  "public": false,
  "blocks": []
}
```

<br/>

## Dashboard Context Instance

Schema for a dashboard context instance

### <a name="dashboard-context-instance-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "patternProperties": {
    "^[0-9a-zA-Z_-]{1,255}$": {
      "type": [
        "string",
        "number"
      ]
    }
  },
  "additionalProperties": false
}
```
### <a name="dashboard-context-instance-example"></a> Example

```json
{
  "myContextVariable": "myValue",
  "myOtherVariable": "575ecf887ae143cd83dc4aa2"
}
```

<br/>

## Dashboard Patch

Schema for the body of a Dashboard modification request

### <a name="dashboard-patch-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "minLength": 1,
      "maxLength": 255
    },
    "blocks": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "blockType": {
            "type": "string"
          },
          "title": {
            "type": "string",
            "maxLength": 255
          },
          "applicationId": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "startX": {
            "type": "integer"
          },
          "startY": {
            "type": "integer"
          },
          "width": {
            "type": "integer"
          },
          "height": {
            "type": "integer"
          },
          "config": {
            "type": "object"
          }
        },
        "required": [
          "blockType",
          "startX",
          "startY",
          "width",
          "height"
        ],
        "additionalProperties": false
      }
    },
    "description": {
      "type": "string",
      "maxLength": 32767
    },
    "refreshRate": {
      "type": "number",
      "minimum": 5,
      "maximum": 600
    },
    "public": {
      "type": "boolean"
    },
    "password": {
      "type": [
        "string",
        "null"
      ]
    },
    "contextConfiguration": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "pattern": "^[0-9a-zA-Z_-]{1,255}$"
          },
          "type": {
            "type": "string",
            "enum": [
              "deviceId",
              "deviceAttribute",
              "string",
              "number"
            ]
          },
          "applicationId": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "defaultValue": {
            "type": [
              "string",
              "number"
            ]
          },
          "validationEnabled": {
            "type": "boolean"
          },
          "validationConfig": {
            "type": "object",
            "properties": {
              "min": {
                "type": "number"
              },
              "max": {
                "type": "number"
              },
              "regExp": {
                "type": "string",
                "maxLength": 1024
              },
              "attributes": {
                "type": "array",
                "items": {
                  "type": "string",
                  "pattern": "^[0-9a-zA-Z_-]{1,255}$"
                }
              },
              "deviceIds": {
                "type": "array",
                "items": {
                  "type": "string",
                  "pattern": "^[A-Fa-f\\d]{24}$"
                }
              },
              "deviceTags": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "key": {
                      "type": "string",
                      "pattern": "^[0-9a-zA-Z_-]{1,255}$"
                    },
                    "value": {
                      "type": "string",
                      "minLength": 1,
                      "maxLength": 255
                    }
                  },
                  "additionalProperties": false
                }
              }
            },
            "additionalProperties": false
          }
        },
        "required": [
          "name",
          "type",
          "defaultValue"
        ],
        "additionalProperties": false
      }
    }
  },
  "additionalProperties": false
}
```
### <a name="dashboard-patch-example"></a> Example

```json
{
  "name": "My Updated Dashboard",
  "description": "Description of my updated dashboard",
  "refreshRate": 300,
  "public": true
}
```

<br/>

## Dashboard Post

Schema for the body of a Dashboard creation request

### <a name="dashboard-post-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "orgId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "name": {
      "type": "string",
      "minLength": 1,
      "maxLength": 255
    },
    "blocks": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "blockType": {
            "type": "string"
          },
          "title": {
            "type": "string",
            "maxLength": 255
          },
          "applicationId": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "startX": {
            "type": "integer"
          },
          "startY": {
            "type": "integer"
          },
          "width": {
            "type": "integer"
          },
          "height": {
            "type": "integer"
          },
          "config": {
            "type": "object"
          }
        },
        "required": [
          "blockType",
          "startX",
          "startY",
          "width",
          "height"
        ],
        "additionalProperties": false
      }
    },
    "description": {
      "type": "string",
      "maxLength": 32767
    },
    "refreshRate": {
      "type": "number",
      "minimum": 5,
      "maximum": 600
    },
    "public": {
      "type": "boolean"
    },
    "password": {
      "type": [
        "string",
        "null"
      ]
    },
    "contextConfiguration": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "pattern": "^[0-9a-zA-Z_-]{1,255}$"
          },
          "type": {
            "type": "string",
            "enum": [
              "deviceId",
              "deviceAttribute",
              "string",
              "number"
            ]
          },
          "applicationId": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "defaultValue": {
            "type": [
              "string",
              "number"
            ]
          },
          "validationEnabled": {
            "type": "boolean"
          },
          "validationConfig": {
            "type": "object",
            "properties": {
              "min": {
                "type": "number"
              },
              "max": {
                "type": "number"
              },
              "regExp": {
                "type": "string",
                "maxLength": 1024
              },
              "attributes": {
                "type": "array",
                "items": {
                  "type": "string",
                  "pattern": "^[0-9a-zA-Z_-]{1,255}$"
                }
              },
              "deviceIds": {
                "type": "array",
                "items": {
                  "type": "string",
                  "pattern": "^[A-Fa-f\\d]{24}$"
                }
              },
              "deviceTags": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "key": {
                      "type": "string",
                      "pattern": "^[0-9a-zA-Z_-]{1,255}$"
                    },
                    "value": {
                      "type": "string",
                      "minLength": 1,
                      "maxLength": 255
                    }
                  },
                  "additionalProperties": false
                }
              }
            },
            "additionalProperties": false
          }
        },
        "required": [
          "name",
          "type",
          "defaultValue"
        ],
        "additionalProperties": false
      }
    }
  },
  "additionalProperties": false,
  "required": [
    "name"
  ]
}
```
### <a name="dashboard-post-example"></a> Example

```json
{
  "name": "My New Dashboard",
  "public": false
}
```

<br/>

## Dashboards

Schema for a collection of Dashboards

### <a name="dashboards-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "items": {
      "type": "array",
      "items": {
        "title": "Dashboard",
        "description": "Schema for a single Dashboard",
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "dashboardId": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "creationDate": {
            "type": "string",
            "format": "date-time"
          },
          "lastUpdated": {
            "type": "string",
            "format": "date-time"
          },
          "ownerId": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "ownerType": {
            "type": "string",
            "enum": [
              "user",
              "organization"
            ]
          },
          "name": {
            "type": "string",
            "minLength": 1,
            "maxLength": 255
          },
          "description": {
            "type": "string",
            "maxLength": 32767
          },
          "refreshRate": {
            "type": "number",
            "minimum": 5,
            "maximum": 600
          },
          "isPasswordProtected": {
            "type": "boolean"
          },
          "public": {
            "type": "boolean"
          },
          "blocks": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "id": {
                  "type": "string"
                },
                "blockType": {
                  "type": "string"
                },
                "title": {
                  "type": "string",
                  "maxLength": 255
                },
                "applicationId": {
                  "type": "string",
                  "pattern": "^[A-Fa-f\\d]{24}$"
                },
                "startX": {
                  "type": "integer"
                },
                "startY": {
                  "type": "integer"
                },
                "width": {
                  "type": "integer"
                },
                "height": {
                  "type": "integer"
                },
                "config": {
                  "type": "object"
                }
              },
              "required": [
                "blockType",
                "startX",
                "startY",
                "width",
                "height"
              ],
              "additionalProperties": false
            }
          },
          "contextConfiguration": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "name": {
                  "type": "string",
                  "pattern": "^[0-9a-zA-Z_-]{1,255}$"
                },
                "type": {
                  "type": "string",
                  "enum": [
                    "deviceId",
                    "deviceAttribute",
                    "string",
                    "number"
                  ]
                },
                "applicationId": {
                  "type": "string",
                  "pattern": "^[A-Fa-f\\d]{24}$"
                },
                "defaultValue": {
                  "type": [
                    "string",
                    "number"
                  ]
                },
                "validationEnabled": {
                  "type": "boolean"
                },
                "validationConfig": {
                  "type": "object",
                  "properties": {
                    "min": {
                      "type": "number"
                    },
                    "max": {
                      "type": "number"
                    },
                    "regExp": {
                      "type": "string",
                      "maxLength": 1024
                    },
                    "attributes": {
                      "type": "array",
                      "items": {
                        "type": "string",
                        "pattern": "^[0-9a-zA-Z_-]{1,255}$"
                      }
                    },
                    "deviceIds": {
                      "type": "array",
                      "items": {
                        "type": "string",
                        "pattern": "^[A-Fa-f\\d]{24}$"
                      }
                    },
                    "deviceTags": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "key": {
                            "type": "string",
                            "pattern": "^[0-9a-zA-Z_-]{1,255}$"
                          },
                          "value": {
                            "type": "string",
                            "minLength": 1,
                            "maxLength": 255
                          }
                        },
                        "additionalProperties": false
                      }
                    }
                  },
                  "additionalProperties": false
                }
              },
              "required": [
                "name",
                "type",
                "defaultValue"
              ],
              "additionalProperties": false
            }
          }
        }
      }
    },
    "count": {
      "type": "integer"
    },
    "totalCount": {
      "type": "integer"
    },
    "perPage": {
      "type": "integer"
    },
    "page": {
      "type": "integer"
    },
    "filter": {
      "type": "string"
    },
    "filterField": {
      "type": "string"
    },
    "sortField": {
      "type": "string"
    },
    "sortDirection": {
      "type": "string",
      "enum": [
        "asc",
        "desc"
      ]
    }
  }
}
```
### <a name="dashboards-example"></a> Example

```json
{
  "items": [
    {
      "id": "575ece2b7ae143cd83dc4a9b",
      "dashboardId": "575ece2b7ae143cd83dc4a9b",
      "creationDate": "2016-06-13T04:00:00.000Z",
      "lastUpdated": "2016-06-13T04:00:00.000Z",
      "ownerId": "575ed70c7ae143cd83dc4aa9",
      "ownerType": "user",
      "name": "My Dashboard",
      "description": "The best dashboard description",
      "refreshRate": 60,
      "public": false,
      "blocks": []
    }
  ],
  "count": 1,
  "totalCount": 5,
  "perPage": 1,
  "page": 0,
  "sortField": "name",
  "sortDirection": "asc"
}
```

<br/>

## Device

Schema for a single Device

### <a name="device-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "deviceId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "applicationId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "creationDate": {
      "type": "string",
      "format": "date-time"
    },
    "lastUpdated": {
      "type": "string",
      "format": "date-time"
    },
    "name": {
      "type": "string",
      "minLength": 1,
      "maxLength": 255
    },
    "description": {
      "type": "string",
      "maxLength": 32767
    },
    "tags": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "key": {
            "type": "string",
            "pattern": "^[0-9a-zA-Z_-]{1,255}$"
          },
          "value": {
            "type": "string",
            "minLength": 1,
            "maxLength": 255
          }
        },
        "required": [
          "key",
          "value"
        ],
        "additionalProperties": false
      }
    },
    "attributes": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "pattern": "^[0-9a-zA-Z_-]{1,255}$"
          },
          "dataType": {
            "type": "string",
            "enum": [
              "string",
              "number",
              "gps",
              "boolean"
            ]
          }
        },
        "required": [
          "name",
          "dataType"
        ],
        "additionalProperties": false
      }
    },
    "deviceClass": {
      "type": "string",
      "enum": [
        "standalone",
        "gateway",
        "peripheral",
        "floating",
        "virtual"
      ]
    },
    "gatewayId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "connectionInfo": {
      "type": "object",
      "properties": {
        "time": {
          "type": "string",
          "format": "date-time"
        },
        "connected": {
          "enum": [
            1,
            0,
            null
          ]
        }
      }
    }
  }
}
```
### <a name="device-example"></a> Example

```json
{
  "id": "575ecf887ae143cd83dc4aa2",
  "deviceId": "575ecf887ae143cd83dc4aa2",
  "applicationId": "575ec8687ae143cd83dc4a97",
  "creationDate": "2016-06-13T04:00:00.000Z",
  "lastUpdated": "2016-06-13T04:00:00.000Z",
  "name": "My Device",
  "description": "A device description",
  "tags": [
    {
      "key": "TagKey",
      "value": "TagValue"
    },
    {
      "key": "floor",
      "value": "8"
    }
  ],
  "attributes": [
    {
      "name": "voltage",
      "dataType": "number"
    }
  ],
  "deviceClass": "standalone",
  "connectionInfo": {
    "time": "2016-06-14T08:15:00.000Z",
    "connected": 1
  }
}
```

<br/>

## Device Command

Schema for a command for a single Device

### <a name="device-command-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "time": {
      "oneOf": [
        {
          "type": "string"
        },
        {
          "type": "number"
        },
        {
          "type": "object",
          "properties": {
            "$date": {
              "type": "string"
            }
          },
          "additionalProperties": false,
          "required": [
            "$date"
          ]
        }
      ]
    },
    "name": {
      "type": "string",
      "minLength": 1,
      "maxLength": 255
    },
    "payload": {}
  },
  "required": [
    "name"
  ],
  "additionalProperties": false
}
```
### <a name="device-command-example"></a> Example

```json
{
  "time": "2016-06-13T04:00:00.000Z",
  "name": "myCommand",
  "payload": [
    1,
    1,
    2,
    3,
    5
  ]
}
```

<br/>

## Device Commands

Schema for an array of Device Commands

### <a name="device-commands-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "array",
  "items": {
    "title": "Device Command",
    "description": "Schema for a command for a single Device",
    "type": "object",
    "properties": {
      "time": {
        "oneOf": [
          {
            "type": "string"
          },
          {
            "type": "number"
          },
          {
            "type": "object",
            "properties": {
              "$date": {
                "type": "string"
              }
            },
            "additionalProperties": false,
            "required": [
              "$date"
            ]
          }
        ]
      },
      "name": {
        "type": "string",
        "minLength": 1,
        "maxLength": 255
      },
      "payload": {}
    },
    "required": [
      "name"
    ],
    "additionalProperties": false
  }
}
```
### <a name="device-commands-example"></a> Example

```json
[
  {
    "time": "2016-06-13T04:00:00.000Z",
    "name": "myCommand",
    "payload": [
      1,
      1,
      2,
      3,
      5
    ]
  },
  {
    "time": "2016-06-13T04:00:00.000Z",
    "name": "myCommand",
    "payload": [
      1,
      1,
      2,
      3,
      5
    ]
  }
]
```

<br/>

## Device Credentials

Schema for the body of a Device authentication request

### <a name="device-credentials-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "deviceId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "key": {
      "type": "string"
    },
    "secret": {
      "type": "string"
    }
  },
  "required": [
    "deviceId",
    "key",
    "secret"
  ],
  "additionalProperties": false
}
```
### <a name="device-credentials-example"></a> Example

```json
{
  "deviceId": "575ecf887ae143cd83dc4aa2",
  "key": "this_would_be_the_key",
  "secret": "this_would_be_the_secret"
}
```

<br/>

## Device Log

Log of connection information for a Device

### <a name="device-log-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "connected": {
        "enum": [
          1,
          0
        ]
      },
      "time": {
        "type": "string",
        "format": "date-time"
      },
      "disconnectReason": {
        "type": "string"
      },
      "messagesFromClient": {
        "type": "number"
      },
      "messagesToClient": {
        "type": "number"
      }
    }
  }
}
```
### <a name="device-log-example"></a> Example

```json
[
  {
    "connected": 1,
    "time": "2016-06-03T00:56:22.447Z"
  },
  {
    "connected": 0,
    "disconnectReason": "Connection Lost",
    "messagesFromClient": 2548,
    "messagesToClient": 0,
    "time": "2016-06-03T00:56:21.028Z"
  },
  {
    "connected": 1,
    "time": "2016-06-01T06:24:39.190Z"
  },
  {
    "connected": 0,
    "disconnectReason": "Connection Lost",
    "messagesFromClient": 479,
    "messagesToClient": 0,
    "time": "2016-06-01T06:24:37.925Z"
  },
  {
    "connected": 1,
    "time": "2016-05-31T22:24:48.777Z"
  }
]
```

<br/>

## Device Patch

Schema for the body of a Device modification request

### <a name="device-patch-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "minLength": 1,
      "maxLength": 255
    },
    "description": {
      "type": "string",
      "maxLength": 32767
    },
    "tags": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "key": {
            "type": "string",
            "pattern": "^[0-9a-zA-Z_-]{1,255}$"
          },
          "value": {
            "type": "string",
            "minLength": 1,
            "maxLength": 255
          }
        },
        "required": [
          "key",
          "value"
        ],
        "additionalProperties": false
      }
    },
    "attributes": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "pattern": "^[0-9a-zA-Z_-]{1,255}$"
          },
          "dataType": {
            "type": "string",
            "enum": [
              "string",
              "number",
              "gps",
              "boolean"
            ]
          }
        },
        "required": [
          "name",
          "dataType"
        ],
        "additionalProperties": false
      }
    },
    "deviceClass": {
      "type": "string",
      "enum": [
        "standalone",
        "gateway",
        "peripheral",
        "floating",
        "virtual"
      ]
    },
    "gatewayId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    }
  },
  "additionalProperties": false
}
```
### <a name="device-patch-example"></a> Example

```json
{
  "name": "My Updated Device",
  "description": "Description of my updated device",
  "tags": [
    {
      "key": "TagKey",
      "value": "TagValue"
    }
  ],
  "attributes": [
    {
      "name": "voltage",
      "dataType": "number"
    }
  ],
  "deviceClass": "standalone"
}
```

<br/>

## Device Post

Schema for the body of a Device creation request

### <a name="device-post-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "minLength": 1,
      "maxLength": 255
    },
    "description": {
      "type": "string",
      "maxLength": 32767
    },
    "tags": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "key": {
            "type": "string",
            "pattern": "^[0-9a-zA-Z_-]{1,255}$"
          },
          "value": {
            "type": "string",
            "minLength": 1,
            "maxLength": 255
          }
        },
        "required": [
          "key",
          "value"
        ],
        "additionalProperties": false
      }
    },
    "attributes": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "pattern": "^[0-9a-zA-Z_-]{1,255}$"
          },
          "dataType": {
            "type": "string",
            "enum": [
              "string",
              "number",
              "gps",
              "boolean"
            ]
          }
        },
        "required": [
          "name",
          "dataType"
        ],
        "additionalProperties": false
      }
    },
    "deviceClass": {
      "type": "string",
      "enum": [
        "standalone",
        "gateway",
        "peripheral",
        "floating",
        "virtual"
      ]
    },
    "gatewayId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    }
  },
  "additionalProperties": false,
  "required": [
    "name"
  ]
}
```
### <a name="device-post-example"></a> Example

```json
{
  "name": "My New Device",
  "description": "Description of my new device",
  "tags": [
    {
      "key": "TagKey",
      "value": "TagValue"
    }
  ],
  "attributes": [
    {
      "name": "voltage",
      "dataType": "number"
    }
  ],
  "deviceClass": "standalone"
}
```

<br/>

## Device Recipe

Schema for a single Device Recipe

### <a name="device-recipe-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "deviceRecipeId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "applicationId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "creationDate": {
      "type": "string",
      "format": "date-time"
    },
    "lastUpdated": {
      "type": "string",
      "format": "date-time"
    },
    "name": {
      "type": "string",
      "minLength": 1,
      "maxLength": 255
    },
    "deviceName": {
      "type": "string",
      "minLength": 1,
      "maxLength": 255
    },
    "description": {
      "type": "string",
      "maxLength": 32767
    },
    "deviceDescription": {
      "type": "string",
      "maxLength": 32767
    },
    "tags": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "key": {
            "type": "string",
            "pattern": "^[0-9a-zA-Z_-]{1,255}$"
          },
          "value": {
            "type": "string",
            "minLength": 1,
            "maxLength": 255
          }
        },
        "required": [
          "key",
          "value"
        ],
        "additionalProperties": false
      }
    },
    "attributes": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "pattern": "^[0-9a-zA-Z_-]{1,255}$"
          },
          "dataType": {
            "type": "string",
            "enum": [
              "string",
              "number",
              "gps",
              "boolean"
            ]
          }
        },
        "required": [
          "name",
          "dataType"
        ],
        "additionalProperties": false
      }
    },
    "deviceClass": {
      "type": "string",
      "enum": [
        "standalone",
        "gateway",
        "peripheral",
        "floating",
        "virtual"
      ]
    },
    "gatewayId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    }
  }
}
```
### <a name="device-recipe-example"></a> Example

```json
{
  "id": "575ecec57ae143cd83dc4a9f",
  "deviceRecipeId": "575ecec57ae143cd83dc4a9f",
  "applicationId": "575ec8687ae143cd83dc4a97",
  "creationDate": "2016-06-13T04:00:00.000Z",
  "lastUpdated": "2016-06-13T04:00:00.000Z",
  "name": "Actual recipe name",
  "deviceName": "Future device name",
  "description": "My recipe description",
  "deviceDescription": "Future device description",
  "tags": [
    {
      "key": "TagKey",
      "value": "TagValue"
    }
  ],
  "attributes": [
    {
      "name": "voltage",
      "dataType": "number"
    }
  ],
  "deviceClass": "standalone"
}
```

<br/>

## Device Recipe Bulk Create

Schema for the result of a bulk Device creation request

### <a name="device-recipe-bulk-create-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "created": {
      "type": "number"
    },
    "failed": {
      "type": "number"
    },
    "csvResult": {
      "type": "string"
    }
  }
}
```
### <a name="device-recipe-bulk-create-example"></a> Example

```json
{
  "created": 10,
  "failed": 0,
  "csvResult": "a,comma,separated,string,of,results"
}
```

<br/>

## Device Recipe Bulk Create Post

Schema for the body of a bulk Device creation request

### <a name="device-recipe-bulk-create-post-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "nameColumn": {
      "type": "string"
    },
    "descriptionColumn": {
      "type": "string"
    },
    "csv": {
      "type": "string"
    }
  },
  "additionalProperties": false,
  "required": [
    "csv"
  ]
}
```
### <a name="device-recipe-bulk-create-post-example"></a> Example

```json
{
  "nameColumn": "myNameColumn",
  "descriptionColumn": "column2",
  "csv": "a,comma,separated,string,of,input,data"
}
```

<br/>

## Device Recipe Patch

Schema for the body of a Device Recipe modification request

### <a name="device-recipe-patch-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "minLength": 1,
      "maxLength": 255
    },
    "deviceName": {
      "type": "string",
      "minLength": 1,
      "maxLength": 255
    },
    "description": {
      "type": "string",
      "maxLength": 32767
    },
    "deviceDescription": {
      "type": "string",
      "maxLength": 32767
    },
    "tags": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "key": {
            "type": "string",
            "pattern": "^[0-9a-zA-Z_-]{1,255}$"
          },
          "value": {
            "type": "string",
            "minLength": 1,
            "maxLength": 255
          }
        },
        "required": [
          "key",
          "value"
        ],
        "additionalProperties": false
      }
    },
    "attributes": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "pattern": "^[0-9a-zA-Z_-]{1,255}$"
          },
          "dataType": {
            "type": "string",
            "enum": [
              "string",
              "number",
              "gps",
              "boolean"
            ]
          }
        },
        "required": [
          "name",
          "dataType"
        ],
        "additionalProperties": false
      }
    },
    "deviceClass": {
      "type": "string",
      "enum": [
        "standalone",
        "gateway",
        "peripheral",
        "floating",
        "virtual"
      ]
    },
    "gatewayId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    }
  },
  "additionalProperties": false
}
```
### <a name="device-recipe-patch-example"></a> Example

```json
{
  "name": "My Updated Device Recipe",
  "deviceName": "Future device name",
  "description": "Description of my updated device recipe",
  "deviceDescription": "Future device description",
  "tags": [
    {
      "key": "TagKey",
      "value": "TagValue"
    }
  ],
  "attributes": [
    {
      "name": "voltage",
      "dataType": "number"
    }
  ],
  "deviceClass": "standalone"
}
```

<br/>

## Device Recipe Post

Schema for the body of a Device Recipe creation request

### <a name="device-recipe-post-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "minLength": 1,
      "maxLength": 255
    },
    "deviceName": {
      "type": "string",
      "minLength": 1,
      "maxLength": 255
    },
    "description": {
      "type": "string",
      "maxLength": 32767
    },
    "deviceDescription": {
      "type": "string",
      "maxLength": 32767
    },
    "tags": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "key": {
            "type": "string",
            "pattern": "^[0-9a-zA-Z_-]{1,255}$"
          },
          "value": {
            "type": "string",
            "minLength": 1,
            "maxLength": 255
          }
        },
        "required": [
          "key",
          "value"
        ],
        "additionalProperties": false
      }
    },
    "attributes": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "pattern": "^[0-9a-zA-Z_-]{1,255}$"
          },
          "dataType": {
            "type": "string",
            "enum": [
              "string",
              "number",
              "gps",
              "boolean"
            ]
          }
        },
        "required": [
          "name",
          "dataType"
        ],
        "additionalProperties": false
      }
    },
    "deviceClass": {
      "type": "string",
      "enum": [
        "standalone",
        "gateway",
        "peripheral",
        "floating",
        "virtual"
      ]
    },
    "gatewayId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    }
  },
  "additionalProperties": false,
  "required": [
    "name"
  ]
}
```
### <a name="device-recipe-post-example"></a> Example

```json
{
  "name": "My New Device Recipe",
  "deviceName": "Future device name",
  "description": "Description of my new device recipe",
  "deviceDescription": "Future device description",
  "tags": [
    {
      "key": "TagKey",
      "value": "TagValue"
    }
  ],
  "attributes": [
    {
      "name": "voltage",
      "dataType": "number"
    }
  ],
  "deviceClass": "standalone"
}
```

<br/>

## Device Recipes

Schema for a collection of Device Recipes

### <a name="device-recipes-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "items": {
      "type": "array",
      "items": {
        "title": "Device Recipe",
        "description": "Schema for a single Device Recipe",
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "deviceRecipeId": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "applicationId": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "creationDate": {
            "type": "string",
            "format": "date-time"
          },
          "lastUpdated": {
            "type": "string",
            "format": "date-time"
          },
          "name": {
            "type": "string",
            "minLength": 1,
            "maxLength": 255
          },
          "deviceName": {
            "type": "string",
            "minLength": 1,
            "maxLength": 255
          },
          "description": {
            "type": "string",
            "maxLength": 32767
          },
          "deviceDescription": {
            "type": "string",
            "maxLength": 32767
          },
          "tags": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "key": {
                  "type": "string",
                  "pattern": "^[0-9a-zA-Z_-]{1,255}$"
                },
                "value": {
                  "type": "string",
                  "minLength": 1,
                  "maxLength": 255
                }
              },
              "required": [
                "key",
                "value"
              ],
              "additionalProperties": false
            }
          },
          "attributes": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "name": {
                  "type": "string",
                  "pattern": "^[0-9a-zA-Z_-]{1,255}$"
                },
                "dataType": {
                  "type": "string",
                  "enum": [
                    "string",
                    "number",
                    "gps",
                    "boolean"
                  ]
                }
              },
              "required": [
                "name",
                "dataType"
              ],
              "additionalProperties": false
            }
          },
          "deviceClass": {
            "type": "string",
            "enum": [
              "standalone",
              "gateway",
              "peripheral",
              "floating",
              "virtual"
            ]
          },
          "gatewayId": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          }
        }
      }
    },
    "count": {
      "type": "integer"
    },
    "totalCount": {
      "type": "integer"
    },
    "perPage": {
      "type": "integer"
    },
    "page": {
      "type": "integer"
    },
    "filter": {
      "type": "string"
    },
    "filterField": {
      "type": "string"
    },
    "sortField": {
      "type": "string"
    },
    "sortDirection": {
      "type": "string",
      "enum": [
        "asc",
        "desc"
      ]
    },
    "applicationId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    }
  }
}
```
### <a name="device-recipes-example"></a> Example

```json
{
  "items": [
    {
      "id": "575ecec57ae143cd83dc4a9f",
      "deviceRecipeId": "575ecec57ae143cd83dc4a9f",
      "applicationId": "575ec8687ae143cd83dc4a97",
      "creationDate": "2016-06-13T04:00:00.000Z",
      "lastUpdated": "2016-06-13T04:00:00.000Z",
      "name": "Actual recipe name",
      "deviceName": "Future device name",
      "description": "My recipe description",
      "deviceDescription": "Future device description",
      "tags": [
        {
          "key": "TagKey",
          "value": "TagValue"
        }
      ],
      "attributes": [
        {
          "name": "voltage",
          "dataType": "number"
        }
      ],
      "deviceClass": "standalone"
    }
  ],
  "count": 1,
  "totalCount": 4,
  "perPage": 1,
  "page": 0,
  "sortField": "name",
  "sortDirection": "asc",
  "applicationId": "575ec8687ae143cd83dc4a97"
}
```

<br/>

## Single or Multiple Device States

Schema for a single device state or an array of device states

### <a name="single-or-multiple-device-states-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "oneOf": [
    {
      "title": "Device State",
      "description": "Schema for a single Device state",
      "type": "object",
      "properties": {
        "time": {
          "oneOf": [
            {
              "type": "string"
            },
            {
              "type": "number"
            },
            {
              "type": "object",
              "properties": {
                "$date": {
                  "type": "string"
                }
              },
              "additionalProperties": false,
              "required": [
                "$date"
              ]
            }
          ]
        },
        "relayId": {
          "type": "string"
        },
        "meta": {},
        "data": {
          "type": "object",
          "patternProperties": {
            "^[0-9a-zA-Z_-]{1,255}$": {
              "type": [
                "number",
                "string",
                "boolean"
              ]
            }
          },
          "additionalProperties": false
        }
      },
      "required": [
        "data"
      ],
      "additionalProperties": false
    },
    {
      "title": "Device States",
      "description": "Schema for an array of Device states",
      "type": "array",
      "items": {
        "title": "Device State",
        "description": "Schema for a single Device state",
        "type": "object",
        "properties": {
          "time": {
            "oneOf": [
              {
                "type": "string"
              },
              {
                "type": "number"
              },
              {
                "type": "object",
                "properties": {
                  "$date": {
                    "type": "string"
                  }
                },
                "additionalProperties": false,
                "required": [
                  "$date"
                ]
              }
            ]
          },
          "relayId": {
            "type": "string"
          },
          "meta": {},
          "data": {
            "type": "object",
            "patternProperties": {
              "^[0-9a-zA-Z_-]{1,255}$": {
                "type": [
                  "number",
                  "string",
                  "boolean"
                ]
              }
            },
            "additionalProperties": false
          }
        },
        "required": [
          "data"
        ],
        "additionalProperties": false
      }
    }
  ]
}
```
### <a name="single-or-multiple-device-states-example"></a> Example

```json
{
  "time": "2016-06-13T04:00:00.000Z",
  "data": {
    "voltage": 22.4
  }
}
```

<br/>

## Device States

Schema for an array of Device states

### <a name="device-states-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "array",
  "items": {
    "title": "Device State",
    "description": "Schema for a single Device state",
    "type": "object",
    "properties": {
      "time": {
        "oneOf": [
          {
            "type": "string"
          },
          {
            "type": "number"
          },
          {
            "type": "object",
            "properties": {
              "$date": {
                "type": "string"
              }
            },
            "additionalProperties": false,
            "required": [
              "$date"
            ]
          }
        ]
      },
      "relayId": {
        "type": "string"
      },
      "meta": {},
      "data": {
        "type": "object",
        "patternProperties": {
          "^[0-9a-zA-Z_-]{1,255}$": {
            "type": [
              "number",
              "string",
              "boolean"
            ]
          }
        },
        "additionalProperties": false
      }
    },
    "required": [
      "data"
    ],
    "additionalProperties": false
  }
}
```
### <a name="device-states-example"></a> Example

```json
[
  {
    "time": "2016-06-13T04:00:00.000Z",
    "data": {
      "voltage": 22.4
    }
  },
  {
    "time": "2016-06-13T04:00:00.000Z",
    "data": {
      "voltage": 22.4
    }
  }
]
```

<br/>

## Device Tag Filter

Array of Tags for filtering devices. Tag keys and tag values are optional.

### <a name="device-tag-filter-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "key": {
        "type": "string",
        "pattern": "^[0-9a-zA-Z_-]{1,255}$"
      },
      "value": {
        "type": "string",
        "minLength": 1,
        "maxLength": 255
      }
    },
    "additionalProperties": false
  }
}
```
### <a name="device-tag-filter-example"></a> Example

```json
[
  {
    "value": "red"
  },
  {
    "key": "floor",
    "value": 2
  }
]
```

<br/>

## Devices

Schema for a collection of Devices

### <a name="devices-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "items": {
      "type": "array",
      "items": {
        "title": "Device",
        "description": "Schema for a single Device",
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "deviceId": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "applicationId": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "creationDate": {
            "type": "string",
            "format": "date-time"
          },
          "lastUpdated": {
            "type": "string",
            "format": "date-time"
          },
          "name": {
            "type": "string",
            "minLength": 1,
            "maxLength": 255
          },
          "description": {
            "type": "string",
            "maxLength": 32767
          },
          "tags": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "key": {
                  "type": "string",
                  "pattern": "^[0-9a-zA-Z_-]{1,255}$"
                },
                "value": {
                  "type": "string",
                  "minLength": 1,
                  "maxLength": 255
                }
              },
              "required": [
                "key",
                "value"
              ],
              "additionalProperties": false
            }
          },
          "attributes": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "name": {
                  "type": "string",
                  "pattern": "^[0-9a-zA-Z_-]{1,255}$"
                },
                "dataType": {
                  "type": "string",
                  "enum": [
                    "string",
                    "number",
                    "gps",
                    "boolean"
                  ]
                }
              },
              "required": [
                "name",
                "dataType"
              ],
              "additionalProperties": false
            }
          },
          "deviceClass": {
            "type": "string",
            "enum": [
              "standalone",
              "gateway",
              "peripheral",
              "floating",
              "virtual"
            ]
          },
          "gatewayId": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "connectionInfo": {
            "type": "object",
            "properties": {
              "time": {
                "type": "string",
                "format": "date-time"
              },
              "connected": {
                "enum": [
                  1,
                  0,
                  null
                ]
              }
            }
          }
        }
      }
    },
    "count": {
      "type": "integer"
    },
    "totalCount": {
      "type": "integer"
    },
    "perPage": {
      "type": "integer"
    },
    "page": {
      "type": "integer"
    },
    "filter": {
      "type": "string"
    },
    "filterField": {
      "type": "string"
    },
    "sortField": {
      "type": "string"
    },
    "sortDirection": {
      "type": "string",
      "enum": [
        "asc",
        "desc"
      ]
    },
    "applicationId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    }
  }
}
```
### <a name="devices-example"></a> Example

```json
{
  "items": [
    {
      "id": "575ecf887ae143cd83dc4aa2",
      "deviceId": "575ecf887ae143cd83dc4aa2",
      "applicationId": "575ec8687ae143cd83dc4a97",
      "creationDate": "2016-06-13T04:00:00.000Z",
      "lastUpdated": "2016-06-13T04:00:00.000Z",
      "name": "My Device",
      "description": "A device description",
      "tags": [
        {
          "key": "TagKey",
          "value": "TagValue"
        },
        {
          "key": "floor",
          "value": "8"
        }
      ],
      "attributes": [
        {
          "name": "voltage",
          "dataType": "number"
        }
      ],
      "deviceClass": "standalone",
      "connectionInfo": {
        "time": "2016-06-14T08:15:00.000Z",
        "connected": 1
      }
    }
  ],
  "count": 1,
  "totalCount": 4,
  "perPage": 1,
  "page": 0,
  "sortField": "name",
  "sortDirection": "asc",
  "applicationId": "575ec8687ae143cd83dc4a97"
}
```

<br/>

## Disable Two Factor Auth

Schema for the body of a request to disable two factor auth

### <a name="disable-two-factor-auth-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "twoFactorCode": {
      "type": "string",
      "maxLength": 2048
    },
    "password": {
      "type": "string",
      "minLength": 8,
      "maxLength": 2048
    }
  },
  "required": [
    "password",
    "twoFactorCode"
  ],
  "additionalProperties": false
}
```
### <a name="disable-two-factor-auth-example"></a> Example

```json
{
  "twoFactorCode": "123123",
  "password": "this would be your password"
}
```

<br/>

## Enable Two Factor Auth

Schema for the body of a request to enable two factor auth

### <a name="enable-two-factor-auth-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "twoFactorAuthKey": {
      "type": "string",
      "minLength": 52,
      "maxLength": 52
    },
    "password": {
      "type": "string",
      "minLength": 8,
      "maxLength": 2048
    }
  },
  "required": [
    "password",
    "twoFactorAuthKey"
  ],
  "additionalProperties": false
}
```
### <a name="enable-two-factor-auth-example"></a> Example

```json
{
  "twoFactorAuthKey": "HBBGWJJVOVLXS4ZGNRTDOUKTMESFUR3BMRWVQND2HJYT44TOMVJA",
  "password": "this would be your password"
}
```

<br/>

## Error

Schema for errors returned by the API

### <a name="error-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "type": {
      "type": "string"
    },
    "message": {
      "type": "string"
    }
  }
}
```
### <a name="error-example"></a> Example

```json
{
  "type": "NotFound",
  "message": "Application was not found"
}
```

<br/>

## Event

Schema for a single Event

### <a name="event-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "eventId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "applicationId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "creationDate": {
      "type": "string",
      "format": "date-time"
    },
    "lastUpdated": {
      "type": "string",
      "format": "date-time"
    },
    "sourceType": {
      "type": "string",
      "enum": [
        "flow",
        "user",
        "device",
        "apiToken"
      ]
    },
    "sourceId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "level": {
      "type": "string",
      "enum": [
        "info",
        "warning",
        "error",
        "critical"
      ]
    },
    "state": {
      "type": "string",
      "enum": [
        "new",
        "acknowledged",
        "resolved"
      ]
    },
    "subject": {
      "type": "string",
      "minLength": 1,
      "maxLength": 255
    },
    "message": {
      "type": "string",
      "maxLength": 32767
    },
    "data": {},
    "updates": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "sourceType": {
            "type": "string",
            "enum": [
              "flow",
              "user",
              "device",
              "apiToken"
            ]
          },
          "sourceId": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "creationDate": {
            "type": "string",
            "format": "date-time"
          },
          "comment": {
            "type": "string",
            "maxLength": 32767
          },
          "data": {},
          "stateChange": {
            "type": "object",
            "properties": {
              "old": {
                "type": "string",
                "enum": [
                  "new",
                  "acknowledged",
                  "resolved"
                ]
              },
              "new": {
                "type": "string",
                "enum": [
                  "new",
                  "acknowledged",
                  "resolved"
                ]
              }
            }
          }
        }
      }
    }
  }
}
```
### <a name="event-example"></a> Example

```json
{
  "id": "575ed0de7ae143cd83dc4aa5",
  "eventId": "575ed0de7ae143cd83dc4aa5",
  "applicationId": "575ec8687ae143cd83dc4a97",
  "creationDate": "2016-06-13T04:00:00.000Z",
  "lastUpdated": "2016-06-13T04:00:00.000Z",
  "sourceType": "user",
  "sourceId": "575ed70c7ae143cd83dc4aa9",
  "level": "info",
  "state": "new",
  "subject": "Power levels critical",
  "message": "Power levels on device 432 have surpassed critical thresholds",
  "updates": []
}
```

<br/>

## Event Patch

Schema for the body of an Event modification request

### <a name="event-patch-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "state": {
      "type": "string",
      "enum": [
        "new",
        "acknowledged",
        "resolved"
      ]
    },
    "comment": {
      "type": "string",
      "maxLength": 32767
    },
    "data": {}
  },
  "additionalProperties": false
}
```
### <a name="event-patch-example"></a> Example

```json
{
  "state": "acknowledged",
  "comment": "Looking into this issue"
}
```

<br/>

## Event Post

Schema for the body of an Event creation request

### <a name="event-post-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "level": {
      "type": "string",
      "enum": [
        "info",
        "warning",
        "error",
        "critical"
      ]
    },
    "state": {
      "type": "string",
      "enum": [
        "new",
        "acknowledged",
        "resolved"
      ]
    },
    "subject": {
      "type": "string",
      "minLength": 1,
      "maxLength": 255
    },
    "message": {
      "type": "string",
      "maxLength": 32767
    },
    "data": {}
  },
  "required": [
    "level",
    "state",
    "subject"
  ],
  "additionalProperties": false
}
```
### <a name="event-post-example"></a> Example

```json
{
  "level": "info",
  "state": "new",
  "subject": "Power levels critical",
  "message": "Power levels on device 432 have surpassed critical thresholds"
}
```

<br/>

## Events

Schema for a collection of Events

### <a name="events-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "items": {
      "type": "array",
      "items": {
        "title": "Event",
        "description": "Schema for a single Event",
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "eventId": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "applicationId": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "creationDate": {
            "type": "string",
            "format": "date-time"
          },
          "lastUpdated": {
            "type": "string",
            "format": "date-time"
          },
          "sourceType": {
            "type": "string",
            "enum": [
              "flow",
              "user",
              "device",
              "apiToken"
            ]
          },
          "sourceId": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "level": {
            "type": "string",
            "enum": [
              "info",
              "warning",
              "error",
              "critical"
            ]
          },
          "state": {
            "type": "string",
            "enum": [
              "new",
              "acknowledged",
              "resolved"
            ]
          },
          "subject": {
            "type": "string",
            "minLength": 1,
            "maxLength": 255
          },
          "message": {
            "type": "string",
            "maxLength": 32767
          },
          "data": {},
          "updates": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "sourceType": {
                  "type": "string",
                  "enum": [
                    "flow",
                    "user",
                    "device",
                    "apiToken"
                  ]
                },
                "sourceId": {
                  "type": "string",
                  "pattern": "^[A-Fa-f\\d]{24}$"
                },
                "creationDate": {
                  "type": "string",
                  "format": "date-time"
                },
                "comment": {
                  "type": "string",
                  "maxLength": 32767
                },
                "data": {},
                "stateChange": {
                  "type": "object",
                  "properties": {
                    "old": {
                      "type": "string",
                      "enum": [
                        "new",
                        "acknowledged",
                        "resolved"
                      ]
                    },
                    "new": {
                      "type": "string",
                      "enum": [
                        "new",
                        "acknowledged",
                        "resolved"
                      ]
                    }
                  }
                }
              }
            }
          }
        }
      }
    },
    "count": {
      "type": "integer"
    },
    "totalCount": {
      "type": "integer"
    },
    "perPage": {
      "type": "integer"
    },
    "page": {
      "type": "integer"
    },
    "filter": {
      "type": "string"
    },
    "filterField": {
      "type": "string"
    },
    "sortField": {
      "type": "string"
    },
    "sortDirection": {
      "type": "string",
      "enum": [
        "asc",
        "desc"
      ]
    },
    "state": {
      "type": "string",
      "enum": [
        "new",
        "acknowledged",
        "resolved"
      ]
    },
    "applicationId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    }
  }
}
```
### <a name="events-example"></a> Example

```json
{
  "items": [
    {
      "id": "575ed0de7ae143cd83dc4aa5",
      "eventId": "575ed0de7ae143cd83dc4aa5",
      "applicationId": "575ec8687ae143cd83dc4a97",
      "creationDate": "2016-06-13T04:00:00.000Z",
      "lastUpdated": "2016-06-13T04:00:00.000Z",
      "sourceType": "user",
      "sourceId": "575ed70c7ae143cd83dc4aa9",
      "level": "info",
      "state": "new",
      "subject": "Power levels critical",
      "message": "Power levels on device 432 have surpassed critical thresholds",
      "updates": []
    }
  ],
  "count": 1,
  "totalCount": 4,
  "perPage": 1,
  "page": 0,
  "sortField": "subject",
  "sortDirection": "asc",
  "applicationId": "575ec8687ae143cd83dc4a97",
  "state": "new"
}
```

<br/>

## Workflow

Schema for a single Workflow

### <a name="workflow-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "flowId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "applicationId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "creationDate": {
      "type": "string",
      "format": "date-time"
    },
    "lastUpdated": {
      "type": "string",
      "format": "date-time"
    },
    "name": {
      "type": "string",
      "minLength": 1,
      "maxLength": 255
    },
    "description": {
      "type": "string",
      "maxLength": 32767
    },
    "enabled": {
      "type": "boolean"
    },
    "triggers": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "key": {
            "type": "string"
          },
          "type": {
            "type": "string"
          },
          "config": {
            "type": "object"
          },
          "meta": {
            "type": "object"
          },
          "outputIds": {
            "type": "array",
            "items": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          }
        },
        "additionalProperties": false,
        "required": [
          "type"
        ]
      }
    },
    "nodes": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "type": {
            "type": "string"
          },
          "config": {
            "type": "object"
          },
          "meta": {
            "type": "object"
          },
          "outputIds": {
            "type": "array",
            "items": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          }
        },
        "additionalProperties": false,
        "required": [
          "type"
        ]
      }
    },
    "globals": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "key": {
            "type": "string",
            "pattern": "^[0-9a-zA-Z_-]{1,255}$"
          },
          "json": {
            "type": "string",
            "minLength": 1
          }
        },
        "additionalProperties": false,
        "required": [
          "key",
          "json"
        ]
      }
    },
    "stats": {
      "type": "object",
      "properties": {
        "runCount": {
          "type": "number"
        },
        "errorCount": {
          "type": "number"
        }
      }
    }
  }
}
```
### <a name="workflow-example"></a> Example

```json
{
  "id": "575ed18f7ae143cd83dc4aa6",
  "flowId": "575ed18f7ae143cd83dc4aa6",
  "applicationId": "575ec8687ae143cd83dc4a97",
  "creationDate": "2016-06-13T04:00:00.000Z",
  "lastUpdated": "2016-06-13T04:00:00.000Z",
  "name": "My Workflow",
  "description": "Description of my empty workflow",
  "enabled": true,
  "triggers": [],
  "nodes": [],
  "globals": [],
  "stats": {
    "runCount": 0,
    "errorCount": 0
  }
}
```

<br/>

## Workflow Log

Log of workflow run information

### <a name="workflow-log-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "time": {
        "type": "string",
        "format": "date-time"
      },
      "errorCount": {
        "type": "number"
      },
      "pathsCompleted": {
        "type": "number"
      },
      "totalCount": {
        "type": "number"
      },
      "totalTime": {
        "type": "number"
      },
      "wallTime": {
        "type": "number"
      },
      "nodes": {
        "type": "object",
        "additionalProperties": {
          "type": "object",
          "properties": {
            "time": {
              "type": "number"
            },
            "count": {
              "type": "number"
            }
          }
        }
      },
      "errors": {
        "type": "array",
        "items": {}
      }
    }
  }
}
```
### <a name="workflow-log-example"></a> Example

```json
[
  {
    "time": "2016-06-03T00:56:22.447Z",
    "errorCount": 0,
    "pathsCompleted": 1,
    "totalCount": 1,
    "totalTime": 24,
    "wallTime": 450,
    "errors": [],
    "nodes": {
      "SJaEw_dV": {
        "time": 22,
        "count": 1
      }
    }
  },
  {
    "time": "2016-06-03T00:57:22.447Z",
    "errorCount": 0,
    "pathsCompleted": 1,
    "totalCount": 3,
    "totalTime": 58,
    "wallTime": 152,
    "errors": [],
    "nodes": {
      "SJaEw_dV": {
        "time": 18,
        "count": 3
      }
    }
  }
]
```

<br/>

## Workflow Patch

Schema for the body of a Workflow modification request

### <a name="workflow-patch-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "minLength": 1,
      "maxLength": 255
    },
    "description": {
      "type": "string",
      "maxLength": 32767
    },
    "enabled": {
      "type": "boolean"
    },
    "triggers": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "key": {
            "type": "string"
          },
          "type": {
            "type": "string"
          },
          "config": {
            "type": "object"
          },
          "meta": {
            "type": "object"
          },
          "outputIds": {
            "type": "array",
            "items": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          }
        },
        "additionalProperties": false,
        "required": [
          "type"
        ]
      }
    },
    "nodes": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "type": {
            "type": "string"
          },
          "config": {
            "type": "object"
          },
          "meta": {
            "type": "object"
          },
          "outputIds": {
            "type": "array",
            "items": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          }
        },
        "additionalProperties": false,
        "required": [
          "type"
        ]
      }
    },
    "globals": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "key": {
            "type": "string",
            "pattern": "^[0-9a-zA-Z_-]{1,255}$"
          },
          "json": {
            "type": "string",
            "minLength": 1
          }
        },
        "additionalProperties": false,
        "required": [
          "key",
          "json"
        ]
      }
    }
  },
  "additionalProperties": false
}
```
### <a name="workflow-patch-example"></a> Example

```json
{
  "name": "My Updated Workflow",
  "description": "Description of my updated workflow",
  "enabled": false
}
```

<br/>

## Workflow Post

Schema for the body of a Workflow creation request

### <a name="workflow-post-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "minLength": 1,
      "maxLength": 255
    },
    "description": {
      "type": "string",
      "maxLength": 32767
    },
    "enabled": {
      "type": "boolean"
    },
    "triggers": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "key": {
            "type": "string"
          },
          "type": {
            "type": "string"
          },
          "config": {
            "type": "object"
          },
          "meta": {
            "type": "object"
          },
          "outputIds": {
            "type": "array",
            "items": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          }
        },
        "additionalProperties": false,
        "required": [
          "type"
        ]
      }
    },
    "nodes": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "type": {
            "type": "string"
          },
          "config": {
            "type": "object"
          },
          "meta": {
            "type": "object"
          },
          "outputIds": {
            "type": "array",
            "items": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          }
        },
        "additionalProperties": false,
        "required": [
          "type"
        ]
      }
    },
    "globals": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "key": {
            "type": "string",
            "pattern": "^[0-9a-zA-Z_-]{1,255}$"
          },
          "json": {
            "type": "string",
            "minLength": 1
          }
        },
        "additionalProperties": false,
        "required": [
          "key",
          "json"
        ]
      }
    }
  },
  "additionalProperties": false,
  "required": [
    "name"
  ]
}
```
### <a name="workflow-post-example"></a> Example

```json
{
  "name": "My New Workflow",
  "description": "Description of my new workflow"
}
```

<br/>

## Workflow Storage Entries

Set of persistent workflow storage values

### <a name="workflow-storage-entries-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "patternProperties": {
    "^.{1,255}$": {}
  }
}
```
### <a name="workflow-storage-entries-example"></a> Example

```json
{
  "myStorageKey": "hello",
  "other key": [
    13,
    21,
    34
  ]
}
```

<br/>

## Workflow Storage Entry

Schema for the body of a request to set a Workflow storage entry

### <a name="workflow-storage-entry-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "key": {
      "type": "string",
      "minLength": 1,
      "maxLength": 255
    },
    "value": {}
  },
  "additionalProperties": false,
  "required": [
    "key"
  ]
}
```
### <a name="workflow-storage-entry-example"></a> Example

```json
{
  "key": "myStorageKey",
  "value": 12
}
```

<br/>

## Workflows

Schema for a collection of Workflows

### <a name="workflows-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "items": {
      "type": "array",
      "items": {
        "title": "Workflow",
        "description": "Schema for a single Workflow",
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "flowId": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "applicationId": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "creationDate": {
            "type": "string",
            "format": "date-time"
          },
          "lastUpdated": {
            "type": "string",
            "format": "date-time"
          },
          "name": {
            "type": "string",
            "minLength": 1,
            "maxLength": 255
          },
          "description": {
            "type": "string",
            "maxLength": 32767
          },
          "enabled": {
            "type": "boolean"
          },
          "triggers": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "key": {
                  "type": "string"
                },
                "type": {
                  "type": "string"
                },
                "config": {
                  "type": "object"
                },
                "meta": {
                  "type": "object"
                },
                "outputIds": {
                  "type": "array",
                  "items": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    }
                  }
                }
              },
              "additionalProperties": false,
              "required": [
                "type"
              ]
            }
          },
          "nodes": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "id": {
                  "type": "string"
                },
                "type": {
                  "type": "string"
                },
                "config": {
                  "type": "object"
                },
                "meta": {
                  "type": "object"
                },
                "outputIds": {
                  "type": "array",
                  "items": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    }
                  }
                }
              },
              "additionalProperties": false,
              "required": [
                "type"
              ]
            }
          },
          "globals": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "key": {
                  "type": "string",
                  "pattern": "^[0-9a-zA-Z_-]{1,255}$"
                },
                "json": {
                  "type": "string",
                  "minLength": 1
                }
              },
              "additionalProperties": false,
              "required": [
                "key",
                "json"
              ]
            }
          },
          "stats": {
            "type": "object",
            "properties": {
              "runCount": {
                "type": "number"
              },
              "errorCount": {
                "type": "number"
              }
            }
          }
        }
      }
    },
    "count": {
      "type": "integer"
    },
    "totalCount": {
      "type": "integer"
    },
    "perPage": {
      "type": "integer"
    },
    "page": {
      "type": "integer"
    },
    "filter": {
      "type": "string"
    },
    "filterField": {
      "type": "string"
    },
    "sortField": {
      "type": "string"
    },
    "sortDirection": {
      "type": "string",
      "enum": [
        "asc",
        "desc"
      ]
    },
    "applicationId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    }
  }
}
```
### <a name="workflows-example"></a> Example

```json
{
  "items": [
    {
      "id": "575ed18f7ae143cd83dc4aa6",
      "flowId": "575ed18f7ae143cd83dc4aa6",
      "applicationId": "575ec8687ae143cd83dc4a97",
      "creationDate": "2016-06-13T04:00:00.000Z",
      "lastUpdated": "2016-06-13T04:00:00.000Z",
      "name": "My Workflow",
      "description": "Description of my empty workflow",
      "enabled": true,
      "triggers": [],
      "nodes": [],
      "globals": [],
      "stats": {
        "runCount": 0,
        "errorCount": 0
      }
    }
  ],
  "count": 1,
  "totalCount": 4,
  "perPage": 1,
  "page": 0,
  "sortField": "name",
  "sortDirection": "asc",
  "applicationId": "575ec8687ae143cd83dc4a97"
}
```

<br/>

## Github Login

Schema for the body of a Github login request

### <a name="github-login-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "accessToken": {
      "type": "string",
      "minLength": 1
    }
  },
  "required": [
    "accessToken"
  ],
  "additionalProperties": false
}
```
### <a name="github-login-example"></a> Example

```json
{
  "accessToken": "the github access token"
}
```

<br/>

## Last Value Data

Schema for the result of a last value query

### <a name="last-value-data-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "patternProperties": {
    "^[A-Fa-f\\d]{24}$": {
      "type": "object",
      "properties": {
        "time": {
          "type": "string",
          "format": "date-time"
        },
        "data": {
          "type": "object",
          "patternProperties": {
            "^[0-9a-zA-Z_-]{1,255}$": {
              "type": [
                "number",
                "string",
                "boolean"
              ]
            }
          },
          "additionalProperties": false
        }
      },
      "additionalProperties": false,
      "required": [
        "data",
        "time"
      ]
    }
  },
  "additionalProperties": false
}
```
### <a name="last-value-data-example"></a> Example

```json
{
  "575ecf887ae143cd83dc4aa2": {
    "time": "2016-06-13T04:00:00.000Z",
    "data": {
      "voltage": 12
    }
  },
  "575ef5c97ae143cd83dc4aac": {
    "time": "2016-06-12T08:30:00.000Z",
    "data": {
      "voltage": 19
    }
  }
}
```

<br/>

## Last Value Query

Schema for the body of a last value query request

### <a name="last-value-query-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "attribute": {
      "type": "string",
      "pattern": "^[0-9a-zA-Z_-]{1,255}$"
    },
    "deviceTags": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "key": {
            "type": "string",
            "pattern": "^[0-9a-zA-Z_-]{1,255}$"
          },
          "value": {
            "type": "string",
            "minLength": 1,
            "maxLength": 255
          }
        },
        "additionalProperties": false
      }
    },
    "deviceIds": {
      "type": "array",
      "items": {
        "type": "string",
        "pattern": "^[A-Fa-f\\d]{24}$"
      }
    }
  },
  "additionalProperties": false
}
```
### <a name="last-value-query-example"></a> Example

```json
{
  "deviceIds": [
    "575ecf887ae143cd83dc4aa2",
    "575ef5c97ae143cd83dc4aac"
  ],
  "attribute": "voltage"
}
```

<br/>

## Me

Schema for information about the currently authenticated user

### <a name="me-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "userId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "creationDate": {
      "type": "string",
      "format": "date-time"
    },
    "lastUpdated": {
      "type": "string",
      "format": "date-time"
    },
    "passwordLastUpdated": {
      "type": "string",
      "format": "date-time"
    },
    "email": {
      "type": "string",
      "format": "email",
      "maxLength": 1024
    },
    "firstName": {
      "type": "string",
      "minLength": 1,
      "maxLength": 1024
    },
    "lastName": {
      "type": "string",
      "minLength": 1,
      "maxLength": 1024
    },
    "companyName": {
      "type": "string",
      "maxLength": 1024
    },
    "phoneNumber": {
      "type": "string",
      "maxLength": 1024
    },
    "location": {
      "type": "string",
      "maxLength": 1024
    },
    "url": {
      "type": "string",
      "maxLength": 1024
    },
    "emailVerified": {
      "type": "boolean"
    },
    "twoFactorAuthEnabled": {
      "type": "boolean"
    },
    "fullName": {
      "type": "string"
    },
    "githubName": {
      "type": "string"
    },
    "twitterName": {
      "type": "string"
    },
    "avatarUrl": {
      "type": "string",
      "format": "url"
    },
    "limits": {
      "application": {
        "type": "number"
      },
      "applicationkey": {
        "type": "number"
      },
      "dashboard": {
        "type": "number"
      },
      "device": {
        "type": "number"
      },
      "devicerecipe": {
        "type": "number"
      },
      "flow": {
        "type": "number"
      },
      "webhook": {
        "type": "number"
      },
      "dataTTL": {
        "type": "number"
      },
      "payload": {
        "type": "number"
      }
    },
    "recentDashboards": {
      "title": "Recent Item List",
      "description": "Schema for an array of recent items",
      "type": "object",
      "properties": {
        "itemType": {
          "type": "string",
          "enum": [
            "application",
            "device",
            "flow",
            "dashboard",
            "organization"
          ]
        },
        "parentId": {
          "type": "string",
          "pattern": "^[A-Fa-f\\d]{24}$"
        },
        "items": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "pattern": "^[A-Fa-f\\d]{24}$"
              },
              "name": {
                "type": "string",
                "minLength": 1,
                "maxLength": 255
              }
            }
          }
        }
      }
    },
    "recentApplications": {
      "title": "Recent Item List",
      "description": "Schema for an array of recent items",
      "type": "object",
      "properties": {
        "itemType": {
          "type": "string",
          "enum": [
            "application",
            "device",
            "flow",
            "dashboard",
            "organization"
          ]
        },
        "parentId": {
          "type": "string",
          "pattern": "^[A-Fa-f\\d]{24}$"
        },
        "items": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "pattern": "^[A-Fa-f\\d]{24}$"
              },
              "name": {
                "type": "string",
                "minLength": 1,
                "maxLength": 255
              }
            }
          }
        }
      }
    },
    "recentOrganizations": {
      "title": "Recent Item List",
      "description": "Schema for an array of recent items",
      "type": "object",
      "properties": {
        "itemType": {
          "type": "string",
          "enum": [
            "application",
            "device",
            "flow",
            "dashboard",
            "organization"
          ]
        },
        "parentId": {
          "type": "string",
          "pattern": "^[A-Fa-f\\d]{24}$"
        },
        "items": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "pattern": "^[A-Fa-f\\d]{24}$"
              },
              "name": {
                "type": "string",
                "minLength": 1,
                "maxLength": 255
              }
            }
          }
        }
      }
    },
    "summary": {
      "type": "object",
      "properties": {
        "appCount": {
          "type": "number"
        },
        "dashCount": {
          "type": "number"
        },
        "orgCount": {
          "type": "number"
        },
        "deviceCount": {
          "type": "number"
        },
        "flowCount": {
          "type": "number"
        },
        "webhookCount": {
          "type": "number"
        },
        "keyCount": {
          "type": "number"
        },
        "deviceRecipeCount": {
          "type": "number"
        },
        "payloadCount": {
          "title": "Payload Counts",
          "description": "Schema the result of a payload count request",
          "type": "object",
          "properties": {
            "mqttOut": {
              "type": "object",
              "patternProperties": {
                ".*": {
                  "type": "number"
                }
              }
            },
            "mqttIn": {
              "type": "object",
              "patternProperties": {
                ".*": {
                  "type": "number"
                }
              }
            },
            "deviceState": {
              "type": "object",
              "patternProperties": {
                ".*": {
                  "type": "number"
                }
              }
            },
            "deviceCommand": {
              "type": "object",
              "patternProperties": {
                ".*": {
                  "type": "number"
                }
              }
            },
            "webhook": {
              "type": "object",
              "patternProperties": {
                ".*": {
                  "type": "number"
                }
              }
            },
            "timer": {
              "type": "object",
              "patternProperties": {
                ".*": {
                  "type": "number"
                }
              }
            },
            "event": {
              "type": "object",
              "patternProperties": {
                ".*": {
                  "type": "number"
                }
              }
            },
            "virtualButton": {
              "type": "object",
              "patternProperties": {
                ".*": {
                  "type": "number"
                }
              }
            },
            "deviceConnect": {
              "type": "object",
              "patternProperties": {
                ".*": {
                  "type": "number"
                }
              }
            },
            "deviceDisconnect": {
              "type": "object",
              "patternProperties": {
                ".*": {
                  "type": "number"
                }
              }
            }
          }
        }
      }
    },
    "currentPeriodStart": {
      "type": "string",
      "format": "date-time"
    },
    "currentPeriodEnd": {
      "type": "string",
      "format": "date-time"
    }
  }
}
```
### <a name="me-example"></a> Example

```json
{
  "id": "575ed70c7ae143cd83dc4aa9",
  "userId": "575ed70c7ae143cd83dc4aa9",
  "creationDate": "2016-06-13T04:00:00.000Z",
  "lastUpdated": "2016-06-13T04:00:00.000Z",
  "passwordLastUpdated": "2016-06-13T04:00:00.000Z",
  "email": "example@losant.com",
  "firstName": "Example",
  "lastName": "Name",
  "companyName": "Losant IoT, Inc.",
  "url": "https://www.losant.com",
  "emailVerified": true,
  "twoFactorAuthEnabled": false,
  "fullName": "Example Name",
  "summary": {
    "appCount": 8,
    "dashCount": 5,
    "orgCount": 2,
    "deviceCount": 12,
    "flowCount": 3,
    "webhookCount": 0,
    "keyCount": 2,
    "deviceRecipeCount": 0
  }
}
```

<br/>

## Me Patch

Schema for the body of request to modify the current user

### <a name="me-patch-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "email": {
      "type": "string",
      "format": "email",
      "maxLength": 1024
    },
    "firstName": {
      "type": "string",
      "minLength": 1,
      "maxLength": 1024
    },
    "lastName": {
      "type": "string",
      "minLength": 1,
      "maxLength": 1024
    },
    "companyName": {
      "type": "string",
      "maxLength": 1024
    },
    "phoneNumber": {
      "type": "string",
      "maxLength": 1024
    },
    "location": {
      "type": "string",
      "maxLength": 1024
    },
    "url": {
      "type": "string",
      "maxLength": 1024
    },
    "password": {
      "type": "string",
      "minLength": 8,
      "maxLength": 2048
    }
  },
  "additionalProperties": false
}
```
### <a name="me-patch-example"></a> Example

```json
{
  "email": "example@losant.com",
  "firstName": "Example",
  "lastName": "Name",
  "companyName": "Losant IoT, Inc.",
  "url": "https://www.losant.com",
  "password": "my new password"
}
```

<br/>

## Multi Device Command

Schema for the body of a request to send a command to multiple Devices

### <a name="multi-device-command-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "time": {
      "oneOf": [
        {
          "type": "string"
        },
        {
          "type": "number"
        },
        {
          "type": "object",
          "properties": {
            "$date": {
              "type": "string"
            }
          },
          "additionalProperties": false,
          "required": [
            "$date"
          ]
        }
      ]
    },
    "name": {
      "type": "string",
      "minLength": 1,
      "maxLength": 255
    },
    "payload": {},
    "deviceTags": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "key": {
            "type": "string",
            "pattern": "^[0-9a-zA-Z_-]{1,255}$"
          },
          "value": {
            "type": "string",
            "minLength": 1,
            "maxLength": 255
          }
        },
        "additionalProperties": false
      }
    },
    "deviceIds": {
      "type": "array",
      "items": {
        "type": "string",
        "pattern": "^[A-Fa-f\\d]{24}$"
      }
    }
  },
  "required": [
    "name"
  ],
  "additionalProperties": false
}
```
### <a name="multi-device-command-example"></a> Example

```json
{
  "time": "2016-06-13T04:00:00.000Z",
  "name": "myCommand",
  "payload": [
    1,
    1,
    2,
    3,
    5
  ],
  "deviceTags": [
    {
      "key": "floor",
      "value": 8
    }
  ]
}
```

<br/>

## Organization

Schema for a single Organization

### <a name="organization-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "orgId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "creationDate": {
      "type": "string",
      "format": "date-time"
    },
    "lastUpdated": {
      "type": "string",
      "format": "date-time"
    },
    "name": {
      "type": "string",
      "minLength": 1,
      "maxLength": 255
    },
    "description": {
      "type": "string",
      "maxLength": 32767
    },
    "solutionsEnabled": {
      "type": "boolean"
    },
    "members": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "userId": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "firstName": {
            "type": "string",
            "minLength": 1,
            "maxLength": 1024
          },
          "lastName": {
            "type": "string",
            "minLength": 1,
            "maxLength": 1024
          },
          "email": {
            "type": "string",
            "format": "email",
            "maxLength": 1024
          },
          "avatarUrl": {
            "type": "string",
            "format": "url"
          },
          "role": {
            "type": "string",
            "enum": [
              "admin",
              "edit",
              "view"
            ]
          }
        }
      }
    },
    "limits": {
      "application": {
        "type": "number"
      },
      "applicationkey": {
        "type": "number"
      },
      "dashboard": {
        "type": "number"
      },
      "device": {
        "type": "number"
      },
      "devicerecipe": {
        "type": "number"
      },
      "flow": {
        "type": "number"
      },
      "solution": {
        "type": "number"
      },
      "webhook": {
        "type": "number"
      },
      "dataTTL": {
        "type": "number"
      },
      "member": {
        "type": "number"
      },
      "payload": {
        "type": "number"
      }
    },
    "summary": {
      "type": "object",
      "properties": {
        "appCount": {
          "type": "number"
        },
        "dashCount": {
          "type": "number"
        },
        "solutionCount": {
          "type": "number"
        },
        "deviceCount": {
          "type": "number"
        },
        "flowCount": {
          "type": "number"
        },
        "webhookCount": {
          "type": "number"
        },
        "keyCount": {
          "type": "number"
        },
        "deviceRecipeCount": {
          "type": "number"
        },
        "payloadCount": {
          "title": "Payload Counts",
          "description": "Schema the result of a payload count request",
          "type": "object",
          "properties": {
            "mqttOut": {
              "type": "object",
              "patternProperties": {
                ".*": {
                  "type": "number"
                }
              }
            },
            "mqttIn": {
              "type": "object",
              "patternProperties": {
                ".*": {
                  "type": "number"
                }
              }
            },
            "deviceState": {
              "type": "object",
              "patternProperties": {
                ".*": {
                  "type": "number"
                }
              }
            },
            "deviceCommand": {
              "type": "object",
              "patternProperties": {
                ".*": {
                  "type": "number"
                }
              }
            },
            "webhook": {
              "type": "object",
              "patternProperties": {
                ".*": {
                  "type": "number"
                }
              }
            },
            "timer": {
              "type": "object",
              "patternProperties": {
                ".*": {
                  "type": "number"
                }
              }
            },
            "event": {
              "type": "object",
              "patternProperties": {
                ".*": {
                  "type": "number"
                }
              }
            },
            "virtualButton": {
              "type": "object",
              "patternProperties": {
                ".*": {
                  "type": "number"
                }
              }
            },
            "deviceConnect": {
              "type": "object",
              "patternProperties": {
                ".*": {
                  "type": "number"
                }
              }
            },
            "deviceDisconnect": {
              "type": "object",
              "patternProperties": {
                ".*": {
                  "type": "number"
                }
              }
            }
          }
        },
        "pendingInviteCount": {
          "type": "number"
        },
        "memberCount": {
          "type": "number"
        }
      }
    },
    "planId": {
      "type": "string",
      "maxLength": 1024
    },
    "billingEmail": {
      "type": "string",
      "format": "email",
      "maxLength": 1024
    },
    "subscriptionStatus": {
      "type": "string",
      "enum": [
        "trialing",
        "active",
        "past_due",
        "canceled",
        "unpaid"
      ]
    },
    "currentPeriodStart": {
      "type": "string",
      "format": "date-time"
    },
    "currentPeriodEnd": {
      "type": "string",
      "format": "date-time"
    },
    "isEnterprise": {
      "type": "boolean"
    },
    "iconColor": {
      "type": "string"
    }
  }
}
```
### <a name="organization-example"></a> Example

```json
{
  "id": "575ed6e87ae143cd83dc4aa8",
  "orgId": "575ed6e87ae143cd83dc4aa8",
  "creationDate": "2016-06-13T04:00:00.000Z",
  "lastUpdated": "2016-06-13T04:00:00.000Z",
  "name": "My Organization",
  "description": "My organization description",
  "members": [
    {
      "userId": "575ed70c7ae143cd83dc4aa9",
      "firstName": "Example",
      "lastName": "Name",
      "email": "example@losant.com",
      "role": "admin"
    },
    {
      "userId": "575ef90f7ae143cd83dc4aad",
      "firstName": "Other View",
      "lastName": "Only User",
      "email": "viewer@losant.com",
      "role": "view"
    }
  ],
  "summary": {
    "appCount": 2,
    "dashCount": 1,
    "solutionCount": 0,
    "deviceCount": 12,
    "flowCount": 3,
    "webhookCount": 0,
    "keyCount": 2,
    "deviceRecipeCount": 0
  }
}
```

<br/>

## Organization Invitation Action

Schema for the body of a request to accept or reject an invitation

### <a name="organization-invitation-action-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "email": {
      "type": "string",
      "format": "email",
      "maxLength": 1024
    },
    "token": {
      "type": "string",
      "minLength": 1
    },
    "accept": {
      "type": "boolean"
    }
  },
  "additionalProperties": false,
  "required": [
    "email",
    "token",
    "accept"
  ]
}
```
### <a name="organization-invitation-action-example"></a> Example

```json
{
  "email": "invitedUser@losant.com",
  "token": "the_invitation_token",
  "accept": true
}
```

<br/>

## Organization Invitation Information

Schema for information about an invitation

### <a name="organization-invitation-information-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "orgName": {
      "type": "string",
      "minLength": 1,
      "maxLength": 255
    },
    "email": {
      "type": "string",
      "format": "email",
      "maxLength": 1024
    },
    "role": {
      "type": "string",
      "enum": [
        "admin",
        "edit",
        "view"
      ]
    },
    "inviteDate": {
      "type": "string",
      "format": "date-time"
    },
    "ttl": {
      "type": "number"
    }
  }
}
```
### <a name="organization-invitation-information-example"></a> Example

```json
{
  "orgName": "My Organization",
  "email": "invitedUser@losant.com",
  "role": "edit",
  "inviteDate": "2016-05-13T04:00:00.000Z",
  "ttl": 4233600000
}
```

<br/>

## Organization Invitation Post

Schema for the body of a request to send an invitation

### <a name="organization-invitation-post-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "email": {
      "type": "string",
      "format": "email",
      "maxLength": 1024
    },
    "role": {
      "type": "string",
      "enum": [
        "admin",
        "edit",
        "view"
      ]
    }
  },
  "additionalProperties": false,
  "required": [
    "email",
    "role"
  ]
}
```
### <a name="organization-invitation-post-example"></a> Example

```json
{
  "email": "invitedUser@losant.com",
  "role": "edit"
}
```

<br/>

## Organization Invitation Result

Schema for the result of accepting/rejecting an invitation

### <a name="organization-invitation-result-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "accepted": {
      "type": "boolean"
    },
    "orgId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    }
  }
}
```
### <a name="organization-invitation-result-example"></a> Example

```json
{
  "accepted": true,
  "orgId": "575ed6e87ae143cd83dc4aa8"
}
```

<br/>

## Organization Invitations

Schema for an array of pending invitations to an Organization

### <a name="organization-invitations-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "id": {
        "type": "string",
        "pattern": "^[A-Fa-f\\d]{24}$"
      },
      "email": {
        "type": "string",
        "format": "email",
        "maxLength": 1024
      },
      "role": {
        "type": "string",
        "enum": [
          "admin",
          "edit",
          "view"
        ]
      },
      "inviteDate": {
        "type": "string",
        "format": "date-time"
      },
      "ttl": {
        "type": "number"
      },
      "hasExpired": {
        "type": "boolean"
      }
    }
  }
}
```
### <a name="organization-invitations-example"></a> Example

```json
[
  {
    "id": "575ed71e7ae143cd83dc4aaa",
    "email": "invitedUser@losant.com",
    "role": "edit",
    "inviteDate": "2016-05-13T04:00:00.000Z",
    "ttl": 4233600000,
    "hasExpired": true
  }
]
```

<br/>

## Organization Member Patch

Schema for the body of a request to modify an Organization member

### <a name="organization-member-patch-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "userId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "role": {
      "type": "string",
      "enum": [
        "admin",
        "edit",
        "view"
      ]
    }
  },
  "additionalProperties": false,
  "required": [
    "userId",
    "role"
  ]
}
```
### <a name="organization-member-patch-example"></a> Example

```json
{
  "userId": "575ef90f7ae143cd83dc4aad",
  "role": "view"
}
```

<br/>

## Organization Patch

Schema for the body of an Organization modification request

### <a name="organization-patch-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "minLength": 1,
      "maxLength": 255
    },
    "description": {
      "type": "string",
      "maxLength": 32767
    },
    "planId": {
      "type": "string",
      "maxLength": 1024
    },
    "billingEmail": {
      "type": "string",
      "format": "email",
      "maxLength": 1024
    },
    "cardToken": {
      "type": "string",
      "maxLength": 1024
    },
    "iconColor": {
      "type": "string"
    }
  },
  "additionalProperties": false
}
```
### <a name="organization-patch-example"></a> Example

```json
{
  "name": "My Updated Organization",
  "description": "Description of my updated organization"
}
```

<br/>

## Organization Post

Schema for the body of an Organization creation request

### <a name="organization-post-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "minLength": 1,
      "maxLength": 255
    },
    "description": {
      "type": "string",
      "maxLength": 32767
    },
    "planId": {
      "type": "string",
      "maxLength": 1024
    },
    "billingEmail": {
      "type": "string",
      "format": "email",
      "maxLength": 1024
    },
    "cardToken": {
      "type": "string",
      "maxLength": 1024
    },
    "iconColor": {
      "type": "string"
    }
  },
  "additionalProperties": false,
  "required": [
    "name"
  ]
}
```
### <a name="organization-post-example"></a> Example

```json
{
  "name": "My New Organization",
  "description": "Description of my new organization"
}
```

<br/>

## Organizations

Schema for a collection of Organizations

### <a name="organizations-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "items": {
      "type": "array",
      "items": {
        "title": "Organization",
        "description": "Schema for a single Organization",
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "orgId": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "creationDate": {
            "type": "string",
            "format": "date-time"
          },
          "lastUpdated": {
            "type": "string",
            "format": "date-time"
          },
          "name": {
            "type": "string",
            "minLength": 1,
            "maxLength": 255
          },
          "description": {
            "type": "string",
            "maxLength": 32767
          },
          "solutionsEnabled": {
            "type": "boolean"
          },
          "members": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "userId": {
                  "type": "string",
                  "pattern": "^[A-Fa-f\\d]{24}$"
                },
                "firstName": {
                  "type": "string",
                  "minLength": 1,
                  "maxLength": 1024
                },
                "lastName": {
                  "type": "string",
                  "minLength": 1,
                  "maxLength": 1024
                },
                "email": {
                  "type": "string",
                  "format": "email",
                  "maxLength": 1024
                },
                "avatarUrl": {
                  "type": "string",
                  "format": "url"
                },
                "role": {
                  "type": "string",
                  "enum": [
                    "admin",
                    "edit",
                    "view"
                  ]
                }
              }
            }
          },
          "limits": {
            "application": {
              "type": "number"
            },
            "applicationkey": {
              "type": "number"
            },
            "dashboard": {
              "type": "number"
            },
            "device": {
              "type": "number"
            },
            "devicerecipe": {
              "type": "number"
            },
            "flow": {
              "type": "number"
            },
            "solution": {
              "type": "number"
            },
            "webhook": {
              "type": "number"
            },
            "dataTTL": {
              "type": "number"
            },
            "member": {
              "type": "number"
            },
            "payload": {
              "type": "number"
            }
          },
          "summary": {
            "type": "object",
            "properties": {
              "appCount": {
                "type": "number"
              },
              "dashCount": {
                "type": "number"
              },
              "solutionCount": {
                "type": "number"
              },
              "deviceCount": {
                "type": "number"
              },
              "flowCount": {
                "type": "number"
              },
              "webhookCount": {
                "type": "number"
              },
              "keyCount": {
                "type": "number"
              },
              "deviceRecipeCount": {
                "type": "number"
              },
              "payloadCount": {
                "title": "Payload Counts",
                "description": "Schema the result of a payload count request",
                "type": "object",
                "properties": {
                  "mqttOut": {
                    "type": "object",
                    "patternProperties": {
                      ".*": {
                        "type": "number"
                      }
                    }
                  },
                  "mqttIn": {
                    "type": "object",
                    "patternProperties": {
                      ".*": {
                        "type": "number"
                      }
                    }
                  },
                  "deviceState": {
                    "type": "object",
                    "patternProperties": {
                      ".*": {
                        "type": "number"
                      }
                    }
                  },
                  "deviceCommand": {
                    "type": "object",
                    "patternProperties": {
                      ".*": {
                        "type": "number"
                      }
                    }
                  },
                  "webhook": {
                    "type": "object",
                    "patternProperties": {
                      ".*": {
                        "type": "number"
                      }
                    }
                  },
                  "timer": {
                    "type": "object",
                    "patternProperties": {
                      ".*": {
                        "type": "number"
                      }
                    }
                  },
                  "event": {
                    "type": "object",
                    "patternProperties": {
                      ".*": {
                        "type": "number"
                      }
                    }
                  },
                  "virtualButton": {
                    "type": "object",
                    "patternProperties": {
                      ".*": {
                        "type": "number"
                      }
                    }
                  },
                  "deviceConnect": {
                    "type": "object",
                    "patternProperties": {
                      ".*": {
                        "type": "number"
                      }
                    }
                  },
                  "deviceDisconnect": {
                    "type": "object",
                    "patternProperties": {
                      ".*": {
                        "type": "number"
                      }
                    }
                  }
                }
              },
              "pendingInviteCount": {
                "type": "number"
              },
              "memberCount": {
                "type": "number"
              }
            }
          },
          "planId": {
            "type": "string",
            "maxLength": 1024
          },
          "billingEmail": {
            "type": "string",
            "format": "email",
            "maxLength": 1024
          },
          "subscriptionStatus": {
            "type": "string",
            "enum": [
              "trialing",
              "active",
              "past_due",
              "canceled",
              "unpaid"
            ]
          },
          "currentPeriodStart": {
            "type": "string",
            "format": "date-time"
          },
          "currentPeriodEnd": {
            "type": "string",
            "format": "date-time"
          },
          "isEnterprise": {
            "type": "boolean"
          },
          "iconColor": {
            "type": "string"
          }
        }
      }
    },
    "count": {
      "type": "integer"
    },
    "totalCount": {
      "type": "integer"
    },
    "perPage": {
      "type": "integer"
    },
    "page": {
      "type": "integer"
    },
    "filter": {
      "type": "string"
    },
    "filterField": {
      "type": "string"
    },
    "sortField": {
      "type": "string"
    },
    "sortDirection": {
      "type": "string",
      "enum": [
        "asc",
        "desc"
      ]
    }
  }
}
```
### <a name="organizations-example"></a> Example

```json
{
  "items": [
    {
      "id": "575ed6e87ae143cd83dc4aa8",
      "orgId": "575ed6e87ae143cd83dc4aa8",
      "creationDate": "2016-06-13T04:00:00.000Z",
      "lastUpdated": "2016-06-13T04:00:00.000Z",
      "name": "My Organization",
      "description": "My organization description",
      "members": [
        {
          "userId": "575ed70c7ae143cd83dc4aa9",
          "firstName": "Example",
          "lastName": "Name",
          "email": "example@losant.com",
          "role": "admin"
        },
        {
          "userId": "575ef90f7ae143cd83dc4aad",
          "firstName": "Other View",
          "lastName": "Only User",
          "email": "viewer@losant.com",
          "role": "view"
        }
      ],
      "summary": {
        "appCount": 2,
        "dashCount": 1,
        "solutionCount": 0,
        "deviceCount": 12,
        "flowCount": 3,
        "webhookCount": 0,
        "keyCount": 2,
        "deviceRecipeCount": 0
      }
    }
  ],
  "count": 1,
  "totalCount": 2,
  "perPage": 1,
  "page": 0,
  "sortField": "name",
  "sortDirection": "asc"
}
```

<br/>

## Payload Counts

Schema the result of a payload count request

### <a name="payload-counts-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "mqttOut": {
      "type": "object",
      "patternProperties": {
        ".*": {
          "type": "number"
        }
      }
    },
    "mqttIn": {
      "type": "object",
      "patternProperties": {
        ".*": {
          "type": "number"
        }
      }
    },
    "deviceState": {
      "type": "object",
      "patternProperties": {
        ".*": {
          "type": "number"
        }
      }
    },
    "deviceCommand": {
      "type": "object",
      "patternProperties": {
        ".*": {
          "type": "number"
        }
      }
    },
    "webhook": {
      "type": "object",
      "patternProperties": {
        ".*": {
          "type": "number"
        }
      }
    },
    "timer": {
      "type": "object",
      "patternProperties": {
        ".*": {
          "type": "number"
        }
      }
    },
    "event": {
      "type": "object",
      "patternProperties": {
        ".*": {
          "type": "number"
        }
      }
    },
    "virtualButton": {
      "type": "object",
      "patternProperties": {
        ".*": {
          "type": "number"
        }
      }
    },
    "deviceConnect": {
      "type": "object",
      "patternProperties": {
        ".*": {
          "type": "number"
        }
      }
    },
    "deviceDisconnect": {
      "type": "object",
      "patternProperties": {
        ".*": {
          "type": "number"
        }
      }
    }
  }
}
```
### <a name="payload-counts-example"></a> Example

```json
{
  "timer": {
    "timer.flow": 19772
  },
  "deviceState": {
    "flow.flow": 5215,
    "device.mqtt": 1244049
  },
  "mqttOut": {
    "device.mqtt": 12
  },
  "webhook": {
    "public.rest": 1713284
  },
  "deviceConnect": {
    "device.mqtt": 1016
  },
  "deviceDisconnect": {
    "device.mqtt": 1016
  }
}
```

<br/>

## Recent Item

Schema for the body of a request to add a recent item

### <a name="recent-item-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "itemType": {
      "type": "string",
      "enum": [
        "application",
        "device",
        "flow",
        "dashboard",
        "organization"
      ]
    },
    "parentId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "itemId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    }
  },
  "required": [
    "itemType",
    "itemId"
  ]
}
```
### <a name="recent-item-example"></a> Example

```json
{
  "itemType": "device",
  "parentId": "575ec8687ae143cd83dc4a97",
  "itemId": "575ecf887ae143cd83dc4aa2"
}
```

<br/>

## Recent Item List

Schema for an array of recent items

### <a name="recent-item-list-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "itemType": {
      "type": "string",
      "enum": [
        "application",
        "device",
        "flow",
        "dashboard",
        "organization"
      ]
    },
    "parentId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "name": {
            "type": "string",
            "minLength": 1,
            "maxLength": 255
          }
        }
      }
    }
  }
}
```
### <a name="recent-item-list-example"></a> Example

```json
{
  "itemType": "application",
  "items": [
    {
      "id": "575ec8687ae143cd83dc4a97",
      "name": "My Application"
    },
    {
      "id": "575efbcc7ae143cd83dc4aae",
      "name": "My Other Application"
    }
  ]
}
```

<br/>

## Resource Transfer

Schema for the body of a resource transfer request

### <a name="resource-transfer-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "destinationId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "destinationType": {
      "type": "string",
      "enum": [
        "user",
        "organization"
      ]
    },
    "applicationIds": {
      "type": "array",
      "items": {
        "type": "string",
        "pattern": "^[A-Fa-f\\d]{24}$"
      }
    },
    "dashboardIds": {
      "type": "array",
      "items": {
        "type": "string",
        "pattern": "^[A-Fa-f\\d]{24}$"
      }
    },
    "solutionIds": {
      "type": "array",
      "items": {
        "type": "string",
        "pattern": "^[A-Fa-f\\d]{24}$"
      }
    },
    "strict": {
      "type": "boolean"
    }
  },
  "additionalProperties": false,
  "required": [
    "destinationId",
    "destinationType"
  ]
}
```
### <a name="resource-transfer-example"></a> Example

```json
{
  "destinationId": "575ed6e87ae143cd83dc4aa8",
  "destinationType": "organization",
  "applicationIds": [
    "575ec8687ae143cd83dc4a97"
  ]
}
```

<br/>

## Solution

Schema for a single Solution

### <a name="solution-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "solutionId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "orgId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "creationDate": {
      "type": "string",
      "format": "date-time"
    },
    "lastUpdated": {
      "type": "string",
      "format": "date-time"
    },
    "name": {
      "type": "string",
      "minLength": 1,
      "maxLength": 255
    },
    "description": {
      "type": "string",
      "maxLength": 32767
    },
    "slug": {
      "type": "string",
      "pattern": "^[0-9a-z_-]{1,255}$"
    },
    "allowSelfDeletion": {
      "type": "boolean"
    },
    "allowSelfEmailChange": {
      "type": "boolean"
    },
    "passwordReset": {
      "type": "object",
      "properties": {
        "allowPasswordReset": {
          "type": "boolean"
        },
        "emailSubject": {
          "type": "string",
          "maxLength": 255
        },
        "emailBody": {
          "type": "string",
          "maxLength": 32767
        },
        "emailFrom": {
          "type": "string",
          "format": "email",
          "maxLength": 1024
        }
      }
    },
    "summary": {
      "type": "object",
      "properties": {
        "solutionUserCount": {
          "type": "number"
        }
      }
    }
  }
}
```
### <a name="solution-example"></a> Example

```json
{
  "id": "57955788124b37010084c053",
  "solutionId": "57955788124b37010084c053",
  "orgId": "575ed6e87ae143cd83dc4aa8",
  "creationDate": "2016-06-13T04:00:00.000Z",
  "lastUpdated": "2016-06-13T04:00:00.000Z",
  "name": "My Solution",
  "slug": "my_solution",
  "allowSelfDeletion": false,
  "allowSelfEmailChange": false,
  "summary": {
    "solutionUserCount": 0
  }
}
```

<br/>

## Solution Patch

Schema for the body of a Solution modification request

### <a name="solution-patch-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "minLength": 1,
      "maxLength": 255
    },
    "description": {
      "type": "string",
      "maxLength": 32767
    },
    "slug": {
      "type": "string",
      "pattern": "^[0-9a-z_-]{1,255}$"
    },
    "allowSelfDeletion": {
      "type": "boolean"
    },
    "allowSelfEmailChange": {
      "type": "boolean"
    },
    "passwordReset": {
      "type": "object",
      "properties": {
        "allowPasswordReset": {
          "type": "boolean"
        },
        "emailSubject": {
          "type": "string",
          "maxLength": 255
        },
        "emailBody": {
          "type": "string",
          "maxLength": 32767
        },
        "emailFrom": {
          "type": "string",
          "format": "email",
          "maxLength": 1024
        }
      },
      "additionalProperties": false
    },
    "additionalProperties": false
  }
}
```
### <a name="solution-patch-example"></a> Example

```json
{
  "name": "My Updated Solution",
  "allowSelfDeletion": true
}
```

<br/>

## Solution Post

Schema for the body of a Solution creation request

### <a name="solution-post-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "minLength": 1,
      "maxLength": 255
    },
    "description": {
      "type": "string",
      "maxLength": 32767
    },
    "slug": {
      "type": "string",
      "pattern": "^[0-9a-z_-]{1,255}$"
    },
    "allowSelfDeletion": {
      "type": "boolean"
    },
    "allowSelfEmailChange": {
      "type": "boolean"
    },
    "passwordReset": {
      "type": "object",
      "properties": {
        "allowPasswordReset": {
          "type": "boolean"
        },
        "emailSubject": {
          "type": "string",
          "maxLength": 255
        },
        "emailBody": {
          "type": "string",
          "maxLength": 32767
        },
        "emailFrom": {
          "type": "string",
          "format": "email",
          "maxLength": 1024
        }
      },
      "additionalProperties": false
    },
    "required": [
      "name",
      "slug"
    ],
    "additionalProperties": false
  }
}
```
### <a name="solution-post-example"></a> Example

```json
{
  "name": "My New Solution",
  "slug": "my_new_solution"
}
```

<br/>

## Solution User

Schema for a single Solution User

### <a name="solution-user-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "solutionUserId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "solutionId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "orgId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "creationDate": {
      "type": "string",
      "format": "date-time"
    },
    "lastUpdated": {
      "type": "string",
      "format": "date-time"
    },
    "passwordLastUpdated": {
      "type": "string",
      "format": "date-time"
    },
    "lastLogin": {
      "type": "string",
      "format": "date-time"
    },
    "email": {
      "type": "string",
      "format": "email",
      "maxLength": 1024
    },
    "firstName": {
      "type": "string",
      "minLength": 1,
      "maxLength": 1024
    },
    "lastName": {
      "type": "string",
      "minLength": 1,
      "maxLength": 1024
    },
    "companyName": {
      "type": "string",
      "maxLength": 1024
    },
    "phoneNumber": {
      "type": "string",
      "maxLength": 1024
    },
    "location": {
      "type": "string",
      "maxLength": 1024
    },
    "url": {
      "type": "string",
      "maxLength": 1024
    },
    "forcePasswordResetOnNextLogin": {
      "type": "boolean"
    },
    "fullName": {
      "type": "string"
    },
    "twoFactorAuthEnabled": {
      "type": "boolean"
    },
    "avatarUrl": {
      "type": "string",
      "format": "url"
    },
    "accessRestrictions": {
      "type": "object",
      "properties": {
        "dashboardIds": {
          "type": "array",
          "items": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          }
        }
      }
    }
  }
}
```
### <a name="solution-user-example"></a> Example

```json
{
  "id": "566116085df4b701000258e3",
  "solutionUserId": "566116085df4b701000258e3",
  "solutionId": "57955788124b37010084c053",
  "orgId": "575ed6e87ae143cd83dc4aa8",
  "creationDate": "2016-06-13T04:00:00.000Z",
  "lastUpdated": "2016-06-13T04:00:00.000Z",
  "passwordLastUpdated": "2016-06-13T04:00:00.000Z",
  "lastLogin": "2016-06-13T04:00:00.000Z",
  "email": "example@solutionuser.com",
  "firstName": "Example",
  "lastName": "Name",
  "forcePasswordResetOnNextLogin": false,
  "fullName": "Example Name",
  "twoFactorAuthEnabled": false,
  "avatarUrl": "https://example.avatar.url/is_here.png",
  "accessRestrictions": {
    "dashboardIds": [
      "575ece2b7ae143cd83dc4a9b",
      "575ece2b7ae143cd83dc4a9c"
    ]
  }
}
```

<br/>

## User Credentials

Schema for the body of a Solution User authentication request

### <a name="user-credentials-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "solutionId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "email": {
      "type": "string",
      "format": "email",
      "maxLength": 1024
    },
    "password": {
      "type": "string",
      "minLength": 8,
      "maxLength": 2048
    },
    "twoFactorCode": {
      "type": "string",
      "maxLength": 2048
    }
  },
  "required": [
    "solutionId",
    "email",
    "password"
  ],
  "additionalProperties": false
}
```
### <a name="user-credentials-example"></a> Example

```json
{
  "solutionId": "57955788124b37010084c053",
  "email": "example@solutionuser.com",
  "password": "this is the password"
}
```

<br/>

## Solution User Patch

Schema for the body of a Solution User modification request

### <a name="solution-user-patch-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "email": {
      "type": "string",
      "format": "email",
      "maxLength": 1024
    },
    "firstName": {
      "type": "string",
      "minLength": 1,
      "maxLength": 1024
    },
    "lastName": {
      "type": "string",
      "minLength": 1,
      "maxLength": 1024
    },
    "companyName": {
      "type": "string",
      "maxLength": 1024
    },
    "phoneNumber": {
      "type": "string",
      "maxLength": 1024
    },
    "location": {
      "type": "string",
      "maxLength": 1024
    },
    "url": {
      "type": "string",
      "maxLength": 1024
    },
    "forcePasswordResetOnNextLogin": {
      "type": "boolean"
    },
    "password": {
      "type": "string",
      "minLength": 8,
      "maxLength": 2048
    },
    "twoFactorAuthKey": {
      "type": "string",
      "minLength": 52,
      "maxLength": 52
    },
    "accessRestrictions": {
      "type": "object",
      "properties": {
        "dashboardIds": {
          "type": "array",
          "items": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          }
        },
        "additionalProperties": false
      }
    }
  },
  "additionalProperties": false
}
```
### <a name="solution-user-patch-example"></a> Example

```json
{
  "password": "aNewUserPassword",
  "forcePasswordResetOnNextLogin": true
}
```

<br/>

## Solution User Post

Schema for the body of a Solution User creation request

### <a name="solution-user-post-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "email": {
      "type": "string",
      "format": "email",
      "maxLength": 1024
    },
    "firstName": {
      "type": "string",
      "minLength": 1,
      "maxLength": 1024
    },
    "lastName": {
      "type": "string",
      "minLength": 1,
      "maxLength": 1024
    },
    "companyName": {
      "type": "string",
      "maxLength": 1024
    },
    "phoneNumber": {
      "type": "string",
      "maxLength": 1024
    },
    "location": {
      "type": "string",
      "maxLength": 1024
    },
    "url": {
      "type": "string",
      "maxLength": 1024
    },
    "forcePasswordResetOnNextLogin": {
      "type": "boolean"
    },
    "password": {
      "type": "string",
      "minLength": 8,
      "maxLength": 2048
    },
    "twoFactorAuthKey": {
      "type": "string",
      "minLength": 52,
      "maxLength": 52
    },
    "accessRestrictions": {
      "type": "object",
      "properties": {
        "dashboardIds": {
          "type": "array",
          "items": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          }
        },
        "additionalProperties": false
      }
    }
  },
  "required": [
    "email",
    "firstName",
    "lastName",
    "password"
  ],
  "additionalProperties": false
}
```
### <a name="solution-user-post-example"></a> Example

```json
{
  "email": "example@solutionuser.com",
  "firstName": "Example",
  "lastName": "Name",
  "password": "aUserPassword",
  "accessRestrictions": {
    "dashboardIds": [
      "575ece2b7ae143cd83dc4a9b",
      "575ece2b7ae143cd83dc4a9c"
    ]
  }
}
```

<br/>

## Solution Users

Schema for a collection of Solution Users

### <a name="solution-users-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "items": {
      "type": "array",
      "items": {
        "title": "Solution User",
        "description": "Schema for a single Solution User",
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "solutionUserId": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "solutionId": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "orgId": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "creationDate": {
            "type": "string",
            "format": "date-time"
          },
          "lastUpdated": {
            "type": "string",
            "format": "date-time"
          },
          "passwordLastUpdated": {
            "type": "string",
            "format": "date-time"
          },
          "lastLogin": {
            "type": "string",
            "format": "date-time"
          },
          "email": {
            "type": "string",
            "format": "email",
            "maxLength": 1024
          },
          "firstName": {
            "type": "string",
            "minLength": 1,
            "maxLength": 1024
          },
          "lastName": {
            "type": "string",
            "minLength": 1,
            "maxLength": 1024
          },
          "companyName": {
            "type": "string",
            "maxLength": 1024
          },
          "phoneNumber": {
            "type": "string",
            "maxLength": 1024
          },
          "location": {
            "type": "string",
            "maxLength": 1024
          },
          "url": {
            "type": "string",
            "maxLength": 1024
          },
          "forcePasswordResetOnNextLogin": {
            "type": "boolean"
          },
          "fullName": {
            "type": "string"
          },
          "twoFactorAuthEnabled": {
            "type": "boolean"
          },
          "avatarUrl": {
            "type": "string",
            "format": "url"
          },
          "accessRestrictions": {
            "type": "object",
            "properties": {
              "dashboardIds": {
                "type": "array",
                "items": {
                  "type": "string",
                  "pattern": "^[A-Fa-f\\d]{24}$"
                }
              }
            }
          }
        }
      }
    },
    "count": {
      "type": "integer"
    },
    "totalCount": {
      "type": "integer"
    },
    "perPage": {
      "type": "integer"
    },
    "page": {
      "type": "integer"
    },
    "filter": {
      "type": "string"
    },
    "filterField": {
      "type": "string"
    },
    "sortField": {
      "type": "string"
    },
    "sortDirection": {
      "type": "string",
      "enum": [
        "asc",
        "desc"
      ]
    },
    "orgId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "solutionId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    }
  }
}
```
### <a name="solution-users-example"></a> Example

```json
{
  "items": [
    {
      "id": "566116085df4b701000258e3",
      "solutionUserId": "566116085df4b701000258e3",
      "solutionId": "57955788124b37010084c053",
      "orgId": "575ed6e87ae143cd83dc4aa8",
      "creationDate": "2016-06-13T04:00:00.000Z",
      "lastUpdated": "2016-06-13T04:00:00.000Z",
      "passwordLastUpdated": "2016-06-13T04:00:00.000Z",
      "lastLogin": "2016-06-13T04:00:00.000Z",
      "email": "example@solutionuser.com",
      "firstName": "Example",
      "lastName": "Name",
      "forcePasswordResetOnNextLogin": false,
      "fullName": "Example Name",
      "twoFactorAuthEnabled": false,
      "avatarUrl": "https://example.avatar.url/is_here.png",
      "accessRestrictions": {
        "dashboardIds": [
          "575ece2b7ae143cd83dc4a9b",
          "575ece2b7ae143cd83dc4a9c"
        ]
      }
    }
  ],
  "count": 1,
  "totalCount": 4,
  "perPage": 1,
  "page": 0,
  "sortField": "name",
  "sortDirection": "asc",
  "solutionId": "57955788124b37010084c053",
  "orgId": "575ed6e87ae143cd83dc4aa8"
}
```

<br/>

## Solutions

Schema for a collection of Solutions

### <a name="solutions-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "items": {
      "type": "array",
      "items": {
        "title": "Solution",
        "description": "Schema for a single Solution",
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "solutionId": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "orgId": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "creationDate": {
            "type": "string",
            "format": "date-time"
          },
          "lastUpdated": {
            "type": "string",
            "format": "date-time"
          },
          "name": {
            "type": "string",
            "minLength": 1,
            "maxLength": 255
          },
          "description": {
            "type": "string",
            "maxLength": 32767
          },
          "slug": {
            "type": "string",
            "pattern": "^[0-9a-z_-]{1,255}$"
          },
          "allowSelfDeletion": {
            "type": "boolean"
          },
          "allowSelfEmailChange": {
            "type": "boolean"
          },
          "passwordReset": {
            "type": "object",
            "properties": {
              "allowPasswordReset": {
                "type": "boolean"
              },
              "emailSubject": {
                "type": "string",
                "maxLength": 255
              },
              "emailBody": {
                "type": "string",
                "maxLength": 32767
              },
              "emailFrom": {
                "type": "string",
                "format": "email",
                "maxLength": 1024
              }
            }
          },
          "summary": {
            "type": "object",
            "properties": {
              "solutionUserCount": {
                "type": "number"
              }
            }
          }
        }
      }
    },
    "count": {
      "type": "integer"
    },
    "totalCount": {
      "type": "integer"
    },
    "perPage": {
      "type": "integer"
    },
    "page": {
      "type": "integer"
    },
    "filter": {
      "type": "string"
    },
    "filterField": {
      "type": "string"
    },
    "sortField": {
      "type": "string"
    },
    "sortDirection": {
      "type": "string",
      "enum": [
        "asc",
        "desc"
      ]
    },
    "orgId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    }
  }
}
```
### <a name="solutions-example"></a> Example

```json
{
  "items": [
    {
      "id": "57955788124b37010084c053",
      "solutionId": "57955788124b37010084c053",
      "orgId": "575ed6e87ae143cd83dc4aa8",
      "creationDate": "2016-06-13T04:00:00.000Z",
      "lastUpdated": "2016-06-13T04:00:00.000Z",
      "name": "My Solution",
      "slug": "my_solution",
      "allowSelfDeletion": false,
      "allowSelfEmailChange": false,
      "summary": {
        "solutionUserCount": 0
      }
    }
  ],
  "count": 1,
  "totalCount": 4,
  "perPage": 1,
  "page": 0,
  "sortField": "name",
  "sortDirection": "asc",
  "orgId": "575ed6e87ae143cd83dc4aa8"
}
```

<br/>

## Success

Schema for reporting a successful operation

### <a name="success-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "success": {
      "type": "boolean",
      "enum": [
        true
      ]
    }
  }
}
```
### <a name="success-example"></a> Example

```json
{
  "success": true
}
```

<br/>

## Time Series Data

Schema for the result of a time series query

### <a name="time-series-data-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "start": {
      "type": "string",
      "format": "date-time"
    },
    "end": {
      "type": "string",
      "format": "date-time"
    },
    "resolution": {
      "type": "number"
    },
    "aggregation": {
      "type": "string",
      "enum": [
        "FIRST",
        "LAST",
        "COUNT",
        "MAX",
        "MIN",
        "MEDIAN",
        "MEAN",
        "SUM"
      ]
    },
    "devices": {
      "type": "object",
      "patternProperties": {
        "^[A-Fa-f\\d]{24}$": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "minLength": 1,
              "maxLength": 255
            },
            "points": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "time": {
                    "type": "string",
                    "format": "date-time"
                  },
                  "data": {
                    "type": "object",
                    "patternProperties": {
                      "^[0-9a-zA-Z_-]{1,255}$": {
                        "type": [
                          "number",
                          "string",
                          "boolean"
                        ]
                      }
                    },
                    "additionalProperties": false
                  }
                },
                "additionalProperties": false,
                "required": [
                  "data",
                  "time"
                ]
              }
            }
          },
          "additionalProperties": false,
          "required": [
            "name",
            "points"
          ]
        }
      },
      "additionalProperties": false
    }
  },
  "additionalProperties": false,
  "required": [
    "start",
    "end",
    "resolution",
    "aggregation",
    "devices"
  ]
}
```
### <a name="time-series-data-example"></a> Example

```json
{
  "start": "2016-06-15T03:50:00.000Z",
  "end": "2016-06-15T04:00:00.000Z",
  "resolution": 300000,
  "aggregation": "MEAN",
  "devices": {
    "575ecf887ae143cd83dc4aa2": {
      "name": "My Device",
      "points": [
        {
          "time": "2016-06-15T03:50:00.000Z",
          "data": {
            "voltage": 10.3
          }
        },
        {
          "time": "2016-06-15T03:55:00.000Z",
          "data": {
            "voltage": 12.7
          }
        }
      ]
    },
    "575ef5c97ae143cd83dc4aac": {
      "name": "My Other Device",
      "points": [
        {
          "time": "2016-06-15T03:50:00.000Z",
          "data": {
            "voltage": 10.3
          }
        },
        {
          "time": "2016-06-15T03:55:00.000Z",
          "data": {
            "voltage": 12.7
          }
        }
      ]
    }
  }
}
```

<br/>

## Time Series Query

Schema for the body of a time series query request

### <a name="time-series-query-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "start": {
      "type": "number"
    },
    "end": {
      "type": "number"
    },
    "duration": {
      "type": "number"
    },
    "resolution": {
      "type": "number"
    },
    "aggregation": {
      "type": "string",
      "enum": [
        "FIRST",
        "LAST",
        "COUNT",
        "MAX",
        "MIN",
        "MEDIAN",
        "MEAN",
        "SUM"
      ]
    },
    "attributes": {
      "type": "array",
      "items": {
        "type": "string",
        "pattern": "^[0-9a-zA-Z_-]{1,255}$"
      }
    },
    "deviceTags": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "key": {
            "type": "string",
            "pattern": "^[0-9a-zA-Z_-]{1,255}$"
          },
          "value": {
            "type": "string",
            "minLength": 1,
            "maxLength": 255
          }
        },
        "additionalProperties": false
      }
    },
    "deviceIds": {
      "type": "array",
      "items": {
        "type": "string",
        "pattern": "^[A-Fa-f\\d]{24}$"
      }
    },
    "limit": {
      "type": "number"
    }
  },
  "additionalProperties": false
}
```
### <a name="time-series-query-example"></a> Example

```json
{
  "end": 0,
  "duration": 600000,
  "resolution": 300000,
  "aggregation": "MEAN",
  "attributes": [
    "voltage"
  ],
  "deviceTags": {
    "key": "floor",
    "value": "8"
  }
}
```

<br/>

## User Credentials

Schema for the body of a User authentication request

### <a name="user-credentials-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "email": {
      "type": "string",
      "format": "email",
      "maxLength": 1024
    },
    "password": {
      "type": "string",
      "minLength": 8,
      "maxLength": 2048
    },
    "twoFactorCode": {
      "type": "string",
      "maxLength": 2048
    }
  },
  "required": [
    "email",
    "password"
  ],
  "additionalProperties": false
}
```
### <a name="user-credentials-example"></a> Example

```json
{
  "email": "example@losant.com",
  "password": "this is the password"
}
```

<br/>

## Virtual Button Press

Schema for the body of a request to press a Workflow virtual button

### <a name="virtual-button-press-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "key": {
      "type": "string"
    },
    "payload": {},
    "meta": {}
  },
  "required": [
    "key"
  ],
  "additionalProperties": false
}
```
### <a name="virtual-button-press-example"></a> Example

```json
{
  "key": "575ed18f7ae143cd83dc4aa6-SJaEw_dV",
  "payload": {
    "some": "data"
  }
}
```

<br/>

## Webhook

Schema for a single Webhook

### <a name="webhook-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "webhookId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "applicationId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    },
    "creationDate": {
      "type": "string",
      "format": "date-time"
    },
    "lastUpdated": {
      "type": "string",
      "format": "date-time"
    },
    "name": {
      "type": "string",
      "minLength": 1,
      "maxLength": 255
    },
    "token": {
      "type": "string",
      "minLength": 1
    },
    "responseCode": {
      "type": "integer",
      "minimum": 100,
      "maximum": 599
    },
    "verificationType": {
      "type": "string",
      "enum": [
        "facebook",
        "fitbit",
        "none",
        "twilio"
      ]
    },
    "verificationCode": {
      "type": "string",
      "maxLength": 32767
    },
    "waitForReply": {
      "type": "boolean"
    },
    "basicAuthUsername": {
      "type": "string",
      "maxLength": 255
    },
    "basicAuthPassword": {
      "type": "string",
      "maxLength": 255
    }
  }
}
```
### <a name="webhook-example"></a> Example

```json
{
  "id": "575ed78e7ae143cd83dc4aab",
  "webhookId": "575ed78e7ae143cd83dc4aab",
  "applicationId": "575ec8687ae143cd83dc4a97",
  "creationDate": "2016-06-13T04:00:00.000Z",
  "lastUpdated": "2016-06-13T04:00:00.000Z",
  "name": "My Webhook",
  "token": "the_webhook_token",
  "responseCode": 200
}
```

<br/>

## Webhook Patch

Schema for the body of a Webhook modification request

### <a name="webhook-patch-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "minLength": 1,
      "maxLength": 255
    },
    "responseCode": {
      "type": "integer",
      "minimum": 100,
      "maximum": 599
    },
    "verificationType": {
      "type": "string",
      "enum": [
        "facebook",
        "fitbit",
        "none",
        "twilio"
      ]
    },
    "verificationCode": {
      "type": "string",
      "maxLength": 32767
    },
    "waitForReply": {
      "type": "boolean"
    },
    "basicAuthUsername": {
      "type": "string",
      "maxLength": 255
    },
    "basicAuthPassword": {
      "type": "string",
      "maxLength": 255
    }
  },
  "additionalProperties": false
}
```
### <a name="webhook-patch-example"></a> Example

```json
{
  "name": "My Updated Webhook",
  "responseCode": 201
}
```

<br/>

## Webhook Post

Schema for the body of a Webhook creation request

### <a name="webhook-post-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "minLength": 1,
      "maxLength": 255
    },
    "responseCode": {
      "type": "integer",
      "minimum": 100,
      "maximum": 599
    },
    "verificationType": {
      "type": "string",
      "enum": [
        "facebook",
        "fitbit",
        "none",
        "twilio"
      ]
    },
    "verificationCode": {
      "type": "string",
      "maxLength": 32767
    },
    "waitForReply": {
      "type": "boolean"
    },
    "basicAuthUsername": {
      "type": "string",
      "maxLength": 255
    },
    "basicAuthPassword": {
      "type": "string",
      "maxLength": 255
    }
  },
  "required": [
    "name"
  ],
  "additionalProperties": false
}
```
### <a name="webhook-post-example"></a> Example

```json
{
  "name": "My New Webhook"
}
```

<br/>

## Webhooks

Schema for a collection of Webhooks

### <a name="webhooks-schema"></a> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "items": {
      "type": "array",
      "items": {
        "title": "Webhook",
        "description": "Schema for a single Webhook",
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "webhookId": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "applicationId": {
            "type": "string",
            "pattern": "^[A-Fa-f\\d]{24}$"
          },
          "creationDate": {
            "type": "string",
            "format": "date-time"
          },
          "lastUpdated": {
            "type": "string",
            "format": "date-time"
          },
          "name": {
            "type": "string",
            "minLength": 1,
            "maxLength": 255
          },
          "token": {
            "type": "string",
            "minLength": 1
          },
          "responseCode": {
            "type": "integer",
            "minimum": 100,
            "maximum": 599
          },
          "verificationType": {
            "type": "string",
            "enum": [
              "facebook",
              "fitbit",
              "none",
              "twilio"
            ]
          },
          "verificationCode": {
            "type": "string",
            "maxLength": 32767
          },
          "waitForReply": {
            "type": "boolean"
          },
          "basicAuthUsername": {
            "type": "string",
            "maxLength": 255
          },
          "basicAuthPassword": {
            "type": "string",
            "maxLength": 255
          }
        }
      }
    },
    "count": {
      "type": "integer"
    },
    "totalCount": {
      "type": "integer"
    },
    "perPage": {
      "type": "integer"
    },
    "page": {
      "type": "integer"
    },
    "filter": {
      "type": "string"
    },
    "filterField": {
      "type": "string"
    },
    "sortField": {
      "type": "string"
    },
    "sortDirection": {
      "type": "string",
      "enum": [
        "asc",
        "desc"
      ]
    },
    "applicationId": {
      "type": "string",
      "pattern": "^[A-Fa-f\\d]{24}$"
    }
  }
}
```
### <a name="webhooks-example"></a> Example

```json
{
  "items": [
    {
      "id": "575ed78e7ae143cd83dc4aab",
      "webhookId": "575ed78e7ae143cd83dc4aab",
      "applicationId": "575ec8687ae143cd83dc4a97",
      "creationDate": "2016-06-13T04:00:00.000Z",
      "lastUpdated": "2016-06-13T04:00:00.000Z",
      "name": "My Webhook",
      "token": "the_webhook_token",
      "responseCode": 200
    }
  ],
  "count": 1,
  "totalCount": 4,
  "perPage": 1,
  "page": 0,
  "sortField": "name",
  "sortDirection": "asc",
  "applicationId": "575ec8687ae143cd83dc4a97"
}
```

<br/>
