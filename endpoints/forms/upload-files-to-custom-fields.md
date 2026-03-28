---
title: "Upload files to custom fields"
source: "https://marketplace.gohighlevel.com/docs/ghl/forms/upload-to-custom-fields"
generated_at: "2026-03-28T17:50:27.520392"
tags: ["api", "endpoint", "POST"]
---

# Upload files to custom fields

Post the necessary fields for the API to upload files. The files need to be a buffer with the key "< custom_field_id >_< file_id >".Here custom field id is the ID of your custom field and file id is a randomly generated id (or uuid)There is support for multiple file uploads as well. Have multiple fields in the format mentioned.File size is limited to 50 MB.The allowed file types are:PDFDOCXDOCJPGJPEGPNGGIFCSVXLSXXLSMP4MPEGZIPRARTXTSVGThe API will return the updated contact object.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `POST`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "statusCode": 400,  "message": "Bad Request"}
```

#### NODEJS
```javascript
{  "statusCode": 400,  "message": "Bad Request"}
```

#### PYTHON
```python
{  "statusCode": 400,  "message": "Bad Request"}
```

#### PHP
```php
{  "statusCode": 400,  "message": "Bad Request"}
```

#### JAVA
```java
{  "statusCode": 400,  "message": "Bad Request"}
```

#### GO
```go
{  "statusCode": 400,  "message": "Bad Request"}
```

#### RUBY
```ruby
{  "statusCode": 400,  "message": "Bad Request"}
```

#### POWERSHELL
```powershell
{  "statusCode": 400,  "message": "Bad Request"}
```

