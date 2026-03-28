---
title: "Get Object Schema by key / id"
source: "https://marketplace.gohighlevel.com/docs/ghl/objects/get-object-schema-by-key"
generated_at: "2026-03-28T17:50:27.613922"
tags: ["api", "endpoint", "GET"]
---

# Get Object Schema by key / id

Retrieve Object Schema by key or ID. This will return the schema of the custom object, including all its fields and properties. Supported objects include contact, opportunity, business and custom objects.To understand objects and records, please have a look the documentation here :https://doc.clickup.com/8631005/d/h/87cpx-277156/93bf0c2e23177b0

## Endpoint Information

> [!IMPORTANT]
> **Method:** `GET`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "object": {    "id": "661c06b4ffde146bdb469442",    "standard": false,    "key": "custom_objects.pet",    "labels": {      "singular": "Pet",      "plural": "Pets"    },    "description": "These are non vaccinated pets",    "locationId": "Q9DT3OAqEXDLYuob1G32",    "primaryDisplayProperty": "custom_objects.pet.name",    "dateAdded": "2024-07-29T15:51:28.071Z",    "dateUpdated": "2024-07-29T15:51:28.071Z",    "type": "The Object type can either USER_DEFINED or SYSTEM_DEFINED"  },  "cache": true,  "fields": [    {      "locationId": "ve9EPM428h8vShlRW1KT",      "name": "Name",      "description": "string",      "placeholder": "string",      "showInForms": true,      "options": [        {          "key": "string",          "label": "string",          "url": "string"        }      ],      "acceptedFormats": ".pdf",      "id": "string",      "objectKey": "custom_object.pet",      "dataType": "TEXT",      "parentId": "3v34PM428h8vShlRW1KT",      "fieldKey": "custom_object.pet.name",      "allowCustomOption": true,      "maxFileLimit": 2,      "dateAdded": "2024-07-29T15:51:28.071Z",      "dateUpdated": "2024-07-29T15:51:28.071Z"    }  ]}
```

#### NODEJS
```javascript
{  "object": {    "id": "661c06b4ffde146bdb469442",    "standard": false,    "key": "custom_objects.pet",    "labels": {      "singular": "Pet",      "plural": "Pets"    },    "description": "These are non vaccinated pets",    "locationId": "Q9DT3OAqEXDLYuob1G32",    "primaryDisplayProperty": "custom_objects.pet.name",    "dateAdded": "2024-07-29T15:51:28.071Z",    "dateUpdated": "2024-07-29T15:51:28.071Z",    "type": "The Object type can either USER_DEFINED or SYSTEM_DEFINED"  },  "cache": true,  "fields": [    {      "locationId": "ve9EPM428h8vShlRW1KT",      "name": "Name",      "description": "string",      "placeholder": "string",      "showInForms": true,      "options": [        {          "key": "string",          "label": "string",          "url": "string"        }      ],      "acceptedFormats": ".pdf",      "id": "string",      "objectKey": "custom_object.pet",      "dataType": "TEXT",      "parentId": "3v34PM428h8vShlRW1KT",      "fieldKey": "custom_object.pet.name",      "allowCustomOption": true,      "maxFileLimit": 2,      "dateAdded": "2024-07-29T15:51:28.071Z",      "dateUpdated": "2024-07-29T15:51:28.071Z"    }  ]}
```

#### PYTHON
```python
{  "object": {    "id": "661c06b4ffde146bdb469442",    "standard": false,    "key": "custom_objects.pet",    "labels": {      "singular": "Pet",      "plural": "Pets"    },    "description": "These are non vaccinated pets",    "locationId": "Q9DT3OAqEXDLYuob1G32",    "primaryDisplayProperty": "custom_objects.pet.name",    "dateAdded": "2024-07-29T15:51:28.071Z",    "dateUpdated": "2024-07-29T15:51:28.071Z",    "type": "The Object type can either USER_DEFINED or SYSTEM_DEFINED"  },  "cache": true,  "fields": [    {      "locationId": "ve9EPM428h8vShlRW1KT",      "name": "Name",      "description": "string",      "placeholder": "string",      "showInForms": true,      "options": [        {          "key": "string",          "label": "string",          "url": "string"        }      ],      "acceptedFormats": ".pdf",      "id": "string",      "objectKey": "custom_object.pet",      "dataType": "TEXT",      "parentId": "3v34PM428h8vShlRW1KT",      "fieldKey": "custom_object.pet.name",      "allowCustomOption": true,      "maxFileLimit": 2,      "dateAdded": "2024-07-29T15:51:28.071Z",      "dateUpdated": "2024-07-29T15:51:28.071Z"    }  ]}
```

#### PHP
```php
{  "object": {    "id": "661c06b4ffde146bdb469442",    "standard": false,    "key": "custom_objects.pet",    "labels": {      "singular": "Pet",      "plural": "Pets"    },    "description": "These are non vaccinated pets",    "locationId": "Q9DT3OAqEXDLYuob1G32",    "primaryDisplayProperty": "custom_objects.pet.name",    "dateAdded": "2024-07-29T15:51:28.071Z",    "dateUpdated": "2024-07-29T15:51:28.071Z",    "type": "The Object type can either USER_DEFINED or SYSTEM_DEFINED"  },  "cache": true,  "fields": [    {      "locationId": "ve9EPM428h8vShlRW1KT",      "name": "Name",      "description": "string",      "placeholder": "string",      "showInForms": true,      "options": [        {          "key": "string",          "label": "string",          "url": "string"        }      ],      "acceptedFormats": ".pdf",      "id": "string",      "objectKey": "custom_object.pet",      "dataType": "TEXT",      "parentId": "3v34PM428h8vShlRW1KT",      "fieldKey": "custom_object.pet.name",      "allowCustomOption": true,      "maxFileLimit": 2,      "dateAdded": "2024-07-29T15:51:28.071Z",      "dateUpdated": "2024-07-29T15:51:28.071Z"    }  ]}
```

#### JAVA
```java
{  "object": {    "id": "661c06b4ffde146bdb469442",    "standard": false,    "key": "custom_objects.pet",    "labels": {      "singular": "Pet",      "plural": "Pets"    },    "description": "These are non vaccinated pets",    "locationId": "Q9DT3OAqEXDLYuob1G32",    "primaryDisplayProperty": "custom_objects.pet.name",    "dateAdded": "2024-07-29T15:51:28.071Z",    "dateUpdated": "2024-07-29T15:51:28.071Z",    "type": "The Object type can either USER_DEFINED or SYSTEM_DEFINED"  },  "cache": true,  "fields": [    {      "locationId": "ve9EPM428h8vShlRW1KT",      "name": "Name",      "description": "string",      "placeholder": "string",      "showInForms": true,      "options": [        {          "key": "string",          "label": "string",          "url": "string"        }      ],      "acceptedFormats": ".pdf",      "id": "string",      "objectKey": "custom_object.pet",      "dataType": "TEXT",      "parentId": "3v34PM428h8vShlRW1KT",      "fieldKey": "custom_object.pet.name",      "allowCustomOption": true,      "maxFileLimit": 2,      "dateAdded": "2024-07-29T15:51:28.071Z",      "dateUpdated": "2024-07-29T15:51:28.071Z"    }  ]}
```

#### GO
```go
{  "object": {    "id": "661c06b4ffde146bdb469442",    "standard": false,    "key": "custom_objects.pet",    "labels": {      "singular": "Pet",      "plural": "Pets"    },    "description": "These are non vaccinated pets",    "locationId": "Q9DT3OAqEXDLYuob1G32",    "primaryDisplayProperty": "custom_objects.pet.name",    "dateAdded": "2024-07-29T15:51:28.071Z",    "dateUpdated": "2024-07-29T15:51:28.071Z",    "type": "The Object type can either USER_DEFINED or SYSTEM_DEFINED"  },  "cache": true,  "fields": [    {      "locationId": "ve9EPM428h8vShlRW1KT",      "name": "Name",      "description": "string",      "placeholder": "string",      "showInForms": true,      "options": [        {          "key": "string",          "label": "string",          "url": "string"        }      ],      "acceptedFormats": ".pdf",      "id": "string",      "objectKey": "custom_object.pet",      "dataType": "TEXT",      "parentId": "3v34PM428h8vShlRW1KT",      "fieldKey": "custom_object.pet.name",      "allowCustomOption": true,      "maxFileLimit": 2,      "dateAdded": "2024-07-29T15:51:28.071Z",      "dateUpdated": "2024-07-29T15:51:28.071Z"    }  ]}
```

#### RUBY
```ruby
{  "object": {    "id": "661c06b4ffde146bdb469442",    "standard": false,    "key": "custom_objects.pet",    "labels": {      "singular": "Pet",      "plural": "Pets"    },    "description": "These are non vaccinated pets",    "locationId": "Q9DT3OAqEXDLYuob1G32",    "primaryDisplayProperty": "custom_objects.pet.name",    "dateAdded": "2024-07-29T15:51:28.071Z",    "dateUpdated": "2024-07-29T15:51:28.071Z",    "type": "The Object type can either USER_DEFINED or SYSTEM_DEFINED"  },  "cache": true,  "fields": [    {      "locationId": "ve9EPM428h8vShlRW1KT",      "name": "Name",      "description": "string",      "placeholder": "string",      "showInForms": true,      "options": [        {          "key": "string",          "label": "string",          "url": "string"        }      ],      "acceptedFormats": ".pdf",      "id": "string",      "objectKey": "custom_object.pet",      "dataType": "TEXT",      "parentId": "3v34PM428h8vShlRW1KT",      "fieldKey": "custom_object.pet.name",      "allowCustomOption": true,      "maxFileLimit": 2,      "dateAdded": "2024-07-29T15:51:28.071Z",      "dateUpdated": "2024-07-29T15:51:28.071Z"    }  ]}
```

#### POWERSHELL
```powershell
{  "object": {    "id": "661c06b4ffde146bdb469442",    "standard": false,    "key": "custom_objects.pet",    "labels": {      "singular": "Pet",      "plural": "Pets"    },    "description": "These are non vaccinated pets",    "locationId": "Q9DT3OAqEXDLYuob1G32",    "primaryDisplayProperty": "custom_objects.pet.name",    "dateAdded": "2024-07-29T15:51:28.071Z",    "dateUpdated": "2024-07-29T15:51:28.071Z",    "type": "The Object type can either USER_DEFINED or SYSTEM_DEFINED"  },  "cache": true,  "fields": [    {      "locationId": "ve9EPM428h8vShlRW1KT",      "name": "Name",      "description": "string",      "placeholder": "string",      "showInForms": true,      "options": [        {          "key": "string",          "label": "string",          "url": "string"        }      ],      "acceptedFormats": ".pdf",      "id": "string",      "objectKey": "custom_object.pet",      "dataType": "TEXT",      "parentId": "3v34PM428h8vShlRW1KT",      "fieldKey": "custom_object.pet.name",      "allowCustomOption": true,      "maxFileLimit": 2,      "dateAdded": "2024-07-29T15:51:28.071Z",      "dateUpdated": "2024-07-29T15:51:28.071Z"    }  ]}
```

