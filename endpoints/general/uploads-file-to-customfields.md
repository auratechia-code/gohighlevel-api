---
title: "Uploads File to customFields"
source: "https://marketplace.gohighlevel.com/docs/ghl/locations/upload-file-custom-fields"
generated_at: "2026-03-28T17:50:27.593797"
tags: ["api", "endpoint", "POST"]
---

# Uploads File to customFields

Uploads File to customFields

## Endpoint Information

> [!IMPORTANT]
> **Method:** `POST`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "uploadedFiles": {    "FileName.csv": "https://highlevel-private-staging.storage.googleapis.com/location/Ar4JQgIyuzRsVuwD9RSK/custom-Field/UpZLmohmKEQYn0ymqplY/56e0d7fc-085c-4a07-9e1d-6d8fdac7e710.csv"  },  "meta": [    {      "fieldname": "FileName.csv",      "originalname": "FileName.csv",      "encoding": "7bit",      "mimetype": "text/csv",      "size": 2061,      "url": "https://highlevel-private-staging.storage.googleapis.com/location/Ar4JQgIyuzRsVuwD9RSK/custom-Field/UpZLmohmKEQYn0ymqplY/56e0d7fc-085c-4a07-9e1d-6d8fdac7e710.csv"    }  ]}
```

#### NODEJS
```javascript
{  "uploadedFiles": {    "FileName.csv": "https://highlevel-private-staging.storage.googleapis.com/location/Ar4JQgIyuzRsVuwD9RSK/custom-Field/UpZLmohmKEQYn0ymqplY/56e0d7fc-085c-4a07-9e1d-6d8fdac7e710.csv"  },  "meta": [    {      "fieldname": "FileName.csv",      "originalname": "FileName.csv",      "encoding": "7bit",      "mimetype": "text/csv",      "size": 2061,      "url": "https://highlevel-private-staging.storage.googleapis.com/location/Ar4JQgIyuzRsVuwD9RSK/custom-Field/UpZLmohmKEQYn0ymqplY/56e0d7fc-085c-4a07-9e1d-6d8fdac7e710.csv"    }  ]}
```

#### PYTHON
```python
{  "uploadedFiles": {    "FileName.csv": "https://highlevel-private-staging.storage.googleapis.com/location/Ar4JQgIyuzRsVuwD9RSK/custom-Field/UpZLmohmKEQYn0ymqplY/56e0d7fc-085c-4a07-9e1d-6d8fdac7e710.csv"  },  "meta": [    {      "fieldname": "FileName.csv",      "originalname": "FileName.csv",      "encoding": "7bit",      "mimetype": "text/csv",      "size": 2061,      "url": "https://highlevel-private-staging.storage.googleapis.com/location/Ar4JQgIyuzRsVuwD9RSK/custom-Field/UpZLmohmKEQYn0ymqplY/56e0d7fc-085c-4a07-9e1d-6d8fdac7e710.csv"    }  ]}
```

#### PHP
```php
{  "uploadedFiles": {    "FileName.csv": "https://highlevel-private-staging.storage.googleapis.com/location/Ar4JQgIyuzRsVuwD9RSK/custom-Field/UpZLmohmKEQYn0ymqplY/56e0d7fc-085c-4a07-9e1d-6d8fdac7e710.csv"  },  "meta": [    {      "fieldname": "FileName.csv",      "originalname": "FileName.csv",      "encoding": "7bit",      "mimetype": "text/csv",      "size": 2061,      "url": "https://highlevel-private-staging.storage.googleapis.com/location/Ar4JQgIyuzRsVuwD9RSK/custom-Field/UpZLmohmKEQYn0ymqplY/56e0d7fc-085c-4a07-9e1d-6d8fdac7e710.csv"    }  ]}
```

#### JAVA
```java
{  "uploadedFiles": {    "FileName.csv": "https://highlevel-private-staging.storage.googleapis.com/location/Ar4JQgIyuzRsVuwD9RSK/custom-Field/UpZLmohmKEQYn0ymqplY/56e0d7fc-085c-4a07-9e1d-6d8fdac7e710.csv"  },  "meta": [    {      "fieldname": "FileName.csv",      "originalname": "FileName.csv",      "encoding": "7bit",      "mimetype": "text/csv",      "size": 2061,      "url": "https://highlevel-private-staging.storage.googleapis.com/location/Ar4JQgIyuzRsVuwD9RSK/custom-Field/UpZLmohmKEQYn0ymqplY/56e0d7fc-085c-4a07-9e1d-6d8fdac7e710.csv"    }  ]}
```

#### GO
```go
{  "uploadedFiles": {    "FileName.csv": "https://highlevel-private-staging.storage.googleapis.com/location/Ar4JQgIyuzRsVuwD9RSK/custom-Field/UpZLmohmKEQYn0ymqplY/56e0d7fc-085c-4a07-9e1d-6d8fdac7e710.csv"  },  "meta": [    {      "fieldname": "FileName.csv",      "originalname": "FileName.csv",      "encoding": "7bit",      "mimetype": "text/csv",      "size": 2061,      "url": "https://highlevel-private-staging.storage.googleapis.com/location/Ar4JQgIyuzRsVuwD9RSK/custom-Field/UpZLmohmKEQYn0ymqplY/56e0d7fc-085c-4a07-9e1d-6d8fdac7e710.csv"    }  ]}
```

#### RUBY
```ruby
{  "uploadedFiles": {    "FileName.csv": "https://highlevel-private-staging.storage.googleapis.com/location/Ar4JQgIyuzRsVuwD9RSK/custom-Field/UpZLmohmKEQYn0ymqplY/56e0d7fc-085c-4a07-9e1d-6d8fdac7e710.csv"  },  "meta": [    {      "fieldname": "FileName.csv",      "originalname": "FileName.csv",      "encoding": "7bit",      "mimetype": "text/csv",      "size": 2061,      "url": "https://highlevel-private-staging.storage.googleapis.com/location/Ar4JQgIyuzRsVuwD9RSK/custom-Field/UpZLmohmKEQYn0ymqplY/56e0d7fc-085c-4a07-9e1d-6d8fdac7e710.csv"    }  ]}
```

#### POWERSHELL
```powershell
{  "uploadedFiles": {    "FileName.csv": "https://highlevel-private-staging.storage.googleapis.com/location/Ar4JQgIyuzRsVuwD9RSK/custom-Field/UpZLmohmKEQYn0ymqplY/56e0d7fc-085c-4a07-9e1d-6d8fdac7e710.csv"  },  "meta": [    {      "fieldname": "FileName.csv",      "originalname": "FileName.csv",      "encoding": "7bit",      "mimetype": "text/csv",      "size": 2061,      "url": "https://highlevel-private-staging.storage.googleapis.com/location/Ar4JQgIyuzRsVuwD9RSK/custom-Field/UpZLmohmKEQYn0ymqplY/56e0d7fc-085c-4a07-9e1d-6d8fdac7e710.csv"    }  ]}
```

