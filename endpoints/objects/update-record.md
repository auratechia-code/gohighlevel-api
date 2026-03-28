---
title: "Update Record"
source: "https://marketplace.gohighlevel.com/docs/ghl/objects/update-object-record"
generated_at: "2026-03-28T17:50:27.617023"
tags: ["api", "endpoint", "PUT"]
---

# Update Record

Update a Custom Object Record by Id. Supported Objects are business and custom objects. Documentation Link -https://doc.clickup.com/8631005/d/h/87cpx-277156/93bf0c2e23177b0/87cpx-376296

## Endpoint Information

> [!IMPORTANT]
> **Method:** `PUT`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "record": {    "id": "661c06b4ffde146bdb469442",    "owner": [      "sx6wyHhbFdRXh302Lunr"    ],    "followers": [      "sx6wyHhbFdRXh302Lunr",      "v5cEPM428h8vShlRW1KT"    ],    "properties": {      "customer_number": 1424,      "ticket_name": "Customer not able login",      "phone_number": "+917000000000",      "money": {        "currency": "default",        "value": 100      },      "type_of_ticket": "doubt",      "section_of_app": [        "contacts",        "smartlist"      ],      "recieved_on": "2024-07-11",      "my_files": [        {          "url": "---url_of_file---"        }      ],      "my_textbox_list.option_a": "Value 1",      "my_textbox_list.option_b": "Value 2"    },    "dateAdded": "2024-07-29T15:51:28.071Z",    "dateUpdated": "2024-07-29T15:51:28.071Z"  }}
```

#### NODEJS
```javascript
{  "record": {    "id": "661c06b4ffde146bdb469442",    "owner": [      "sx6wyHhbFdRXh302Lunr"    ],    "followers": [      "sx6wyHhbFdRXh302Lunr",      "v5cEPM428h8vShlRW1KT"    ],    "properties": {      "customer_number": 1424,      "ticket_name": "Customer not able login",      "phone_number": "+917000000000",      "money": {        "currency": "default",        "value": 100      },      "type_of_ticket": "doubt",      "section_of_app": [        "contacts",        "smartlist"      ],      "recieved_on": "2024-07-11",      "my_files": [        {          "url": "---url_of_file---"        }      ],      "my_textbox_list.option_a": "Value 1",      "my_textbox_list.option_b": "Value 2"    },    "dateAdded": "2024-07-29T15:51:28.071Z",    "dateUpdated": "2024-07-29T15:51:28.071Z"  }}
```

#### PYTHON
```python
{  "record": {    "id": "661c06b4ffde146bdb469442",    "owner": [      "sx6wyHhbFdRXh302Lunr"    ],    "followers": [      "sx6wyHhbFdRXh302Lunr",      "v5cEPM428h8vShlRW1KT"    ],    "properties": {      "customer_number": 1424,      "ticket_name": "Customer not able login",      "phone_number": "+917000000000",      "money": {        "currency": "default",        "value": 100      },      "type_of_ticket": "doubt",      "section_of_app": [        "contacts",        "smartlist"      ],      "recieved_on": "2024-07-11",      "my_files": [        {          "url": "---url_of_file---"        }      ],      "my_textbox_list.option_a": "Value 1",      "my_textbox_list.option_b": "Value 2"    },    "dateAdded": "2024-07-29T15:51:28.071Z",    "dateUpdated": "2024-07-29T15:51:28.071Z"  }}
```

#### PHP
```php
{  "record": {    "id": "661c06b4ffde146bdb469442",    "owner": [      "sx6wyHhbFdRXh302Lunr"    ],    "followers": [      "sx6wyHhbFdRXh302Lunr",      "v5cEPM428h8vShlRW1KT"    ],    "properties": {      "customer_number": 1424,      "ticket_name": "Customer not able login",      "phone_number": "+917000000000",      "money": {        "currency": "default",        "value": 100      },      "type_of_ticket": "doubt",      "section_of_app": [        "contacts",        "smartlist"      ],      "recieved_on": "2024-07-11",      "my_files": [        {          "url": "---url_of_file---"        }      ],      "my_textbox_list.option_a": "Value 1",      "my_textbox_list.option_b": "Value 2"    },    "dateAdded": "2024-07-29T15:51:28.071Z",    "dateUpdated": "2024-07-29T15:51:28.071Z"  }}
```

#### JAVA
```java
{  "record": {    "id": "661c06b4ffde146bdb469442",    "owner": [      "sx6wyHhbFdRXh302Lunr"    ],    "followers": [      "sx6wyHhbFdRXh302Lunr",      "v5cEPM428h8vShlRW1KT"    ],    "properties": {      "customer_number": 1424,      "ticket_name": "Customer not able login",      "phone_number": "+917000000000",      "money": {        "currency": "default",        "value": 100      },      "type_of_ticket": "doubt",      "section_of_app": [        "contacts",        "smartlist"      ],      "recieved_on": "2024-07-11",      "my_files": [        {          "url": "---url_of_file---"        }      ],      "my_textbox_list.option_a": "Value 1",      "my_textbox_list.option_b": "Value 2"    },    "dateAdded": "2024-07-29T15:51:28.071Z",    "dateUpdated": "2024-07-29T15:51:28.071Z"  }}
```

#### GO
```go
{  "record": {    "id": "661c06b4ffde146bdb469442",    "owner": [      "sx6wyHhbFdRXh302Lunr"    ],    "followers": [      "sx6wyHhbFdRXh302Lunr",      "v5cEPM428h8vShlRW1KT"    ],    "properties": {      "customer_number": 1424,      "ticket_name": "Customer not able login",      "phone_number": "+917000000000",      "money": {        "currency": "default",        "value": 100      },      "type_of_ticket": "doubt",      "section_of_app": [        "contacts",        "smartlist"      ],      "recieved_on": "2024-07-11",      "my_files": [        {          "url": "---url_of_file---"        }      ],      "my_textbox_list.option_a": "Value 1",      "my_textbox_list.option_b": "Value 2"    },    "dateAdded": "2024-07-29T15:51:28.071Z",    "dateUpdated": "2024-07-29T15:51:28.071Z"  }}
```

#### RUBY
```ruby
{  "record": {    "id": "661c06b4ffde146bdb469442",    "owner": [      "sx6wyHhbFdRXh302Lunr"    ],    "followers": [      "sx6wyHhbFdRXh302Lunr",      "v5cEPM428h8vShlRW1KT"    ],    "properties": {      "customer_number": 1424,      "ticket_name": "Customer not able login",      "phone_number": "+917000000000",      "money": {        "currency": "default",        "value": 100      },      "type_of_ticket": "doubt",      "section_of_app": [        "contacts",        "smartlist"      ],      "recieved_on": "2024-07-11",      "my_files": [        {          "url": "---url_of_file---"        }      ],      "my_textbox_list.option_a": "Value 1",      "my_textbox_list.option_b": "Value 2"    },    "dateAdded": "2024-07-29T15:51:28.071Z",    "dateUpdated": "2024-07-29T15:51:28.071Z"  }}
```

#### POWERSHELL
```powershell
{  "record": {    "id": "661c06b4ffde146bdb469442",    "owner": [      "sx6wyHhbFdRXh302Lunr"    ],    "followers": [      "sx6wyHhbFdRXh302Lunr",      "v5cEPM428h8vShlRW1KT"    ],    "properties": {      "customer_number": 1424,      "ticket_name": "Customer not able login",      "phone_number": "+917000000000",      "money": {        "currency": "default",        "value": 100      },      "type_of_ticket": "doubt",      "section_of_app": [        "contacts",        "smartlist"      ],      "recieved_on": "2024-07-11",      "my_files": [        {          "url": "---url_of_file---"        }      ],      "my_textbox_list.option_a": "Value 1",      "my_textbox_list.option_b": "Value 2"    },    "dateAdded": "2024-07-29T15:51:28.071Z",    "dateUpdated": "2024-07-29T15:51:28.071Z"  }}
```

