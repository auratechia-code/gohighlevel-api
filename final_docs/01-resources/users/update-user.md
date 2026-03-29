# Update User

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | PUT |
| **Endpoint URL** | `https://services.leadconnectorhq.com/users/:userId` |
| **Scopes Required** | `users.write` |
| **Authentication** | OAuth Access Token / Private Integration Token |
| **Token Type** | Sub-Account Token |

---

## 2. REQUEST

### Header Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **Version** | `` | No |  |

### Path Parameters

N/A
### Query Parameters

N/A
### Body Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **firstName** | `string` | No |  |
| **lastName** | `string` | No |  |
| **email** | `string` | No |  |
| **password** | `string` | No |  |
| **phone** | `string` | No |  |
| **type** | `string` | No |  |
| **role** | `string` | No |  |
| **companyId** | `string` | No |  |
| **locationIds** | `string[]` | No |  |
| **permissions** | `object` | No | campaignsEnabled boolean Default value: true Example: true campaignsReadOnly boolean Default value: false Example: false contactsEnabled boolean Default value: true Example: true workflowsEnabled boolean Default value: true Example: true workflowsReadOnly boolean Default value: false Example: true triggersEnabled boolean Default value: true Example: true funnelsEnabled boolean Default value: true Example: true websitesEnabled boolean Default value: false Example: false opportunitiesEnabled boolean Default value: true Example: true dashboardStatsEnabled boolean Default value: true Example: true bulkRequestsEnabled boolean Default value: true Example: true appointmentsEnabled boolean Default value: true Example: true reviewsEnabled boolean Default value: true Example: true onlineListingsEnabled boolean Default value: true Example: true phoneCallEnabled boolean Default value: true Example: true conversationsEnabled boolean Default value: true Example: true assignedDataOnly boolean Default value: false Example: false adwordsReportingEnabled boolean Default value: false Example: false membershipEnabled boolean Default value: false Example: false facebookAdsReportingEnabled boolean Default value: false Example: false attributionsReportingEnabled boolean Default value: false Example: false settingsEnabled boolean Default value: true Example: true tagsEnabled boolean Default value: true Example: true leadValueEnabled boolean Default value: true Example: true marketingEnabled boolean Default value: true Example: true agentReportingEnabled boolean Default value: true Example: true botService boolean Default value: false Example: false socialPlanner boolean Default value: true Example: true bloggingEnabled boolean Default value: true Example: true invoiceEnabled boolean Default value: true Example: true affiliateManagerEnabled boolean Default value: true Example: true contentAiEnabled boolean Default value: true Example: true refundsEnabled boolean Default value: true Example: true recordPaymentEnabled boolean Default value: true Example: true cancelSubscriptionEnabled boolean Default value: true Example: true paymentsEnabled boolean Default value: true Example: true communitiesEnabled boolean Default value: true Example: true exportPaymentsEnabled boolean Default value: true Example: true |
| **campaignsEnabled** | `boolean` | No |  |
| **campaignsReadOnly** | `boolean` | No |  |
| **contactsEnabled** | `boolean` | No |  |
| **workflowsEnabled** | `boolean` | No |  |
| **workflowsReadOnly** | `boolean` | No |  |
| **triggersEnabled** | `boolean` | No |  |
| **funnelsEnabled** | `boolean` | No |  |
| **websitesEnabled** | `boolean` | No |  |
| **opportunitiesEnabled** | `boolean` | No |  |
| **dashboardStatsEnabled** | `boolean` | No |  |
| **bulkRequestsEnabled** | `boolean` | No |  |
| **appointmentsEnabled** | `boolean` | No |  |
| **reviewsEnabled** | `boolean` | No |  |
| **onlineListingsEnabled** | `boolean` | No |  |
| **phoneCallEnabled** | `boolean` | No |  |
| **conversationsEnabled** | `boolean` | No |  |
| **assignedDataOnly** | `boolean` | No |  |
| **adwordsReportingEnabled** | `boolean` | No |  |
| **membershipEnabled** | `boolean` | No |  |
| **facebookAdsReportingEnabled** | `boolean` | No |  |
| **attributionsReportingEnabled** | `boolean` | No |  |
| **settingsEnabled** | `boolean` | No |  |
| **tagsEnabled** | `boolean` | No |  |
| **leadValueEnabled** | `boolean` | No |  |
| **marketingEnabled** | `boolean` | No |  |
| **agentReportingEnabled** | `boolean` | No |  |
| **botService** | `boolean` | No |  |
| **socialPlanner** | `boolean` | No |  |
| **bloggingEnabled** | `boolean` | No |  |
| **invoiceEnabled** | `boolean` | No |  |
| **affiliateManagerEnabled** | `boolean` | No |  |
| **contentAiEnabled** | `boolean` | No |  |
| **refundsEnabled** | `boolean` | No |  |
| **recordPaymentEnabled** | `boolean` | No |  |
| **cancelSubscriptionEnabled** | `boolean` | No |  |
| **paymentsEnabled** | `boolean` | No |  |
| **communitiesEnabled** | `boolean` | No |  |
| **exportPaymentsEnabled** | `boolean` | No |  |
| **scopes** | `string[]` | No |  |
| **scopesAssignedToOnly** | `string[]` | No |  |
| **profilePhoto** | `string` | No |  |
| **platformLanguage** | `string` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "id": "0IHuJvc2ofPAAA8GzTRi",
  "name": "John Deo",
  "firstName": "John",
  "lastName": "Deo",
  "email": "john@deo.com",
  "phone": "+1 808-868-8888",
  "extension": "",
  "permissions": {
    "campaignsEnabled": true,
    "campaignsReadOnly": false,
    "contactsEnabled": true,
    "workflowsEnabled": true,
    "workflowsReadOnly": true,
    "triggersEnabled": true,
    "funnelsEnabled": true,
    "websitesEnabled": false,
    "opportunitiesEnabled": true,
    "dashboardStatsEnabled": true,
    "bulkRequestsEnabled": true,
    "appointmentsEnabled": true,
    "reviewsEnabled": true,
    "onlineListingsEnabled": true,
    "phoneCallEnabled": true,
    "conversationsEnabled": true,
    "assignedDataOnly": false,
    "adwordsReportingEnabled": false,
    "membershipEnabled": false,
    "facebookAdsReportingEnabled": false,
    "attributionsReportingEnabled": false,
    "settingsEnabled": true,
    "tagsEnabled": true,
    "leadValueEnabled": true,
    "marketingEnabled": true,
    "agentReportingEnabled": true,
    "botService": false,
    "socialPlanner": true,
    "bloggingEnabled": true,
    "invoiceEnabled": true,
    "affiliateManagerEnabled": true,
    "contentAiEnabled": true,
    "refundsEnabled": true,
    "recordPaymentEnabled": true,
    "cancelSubscriptionEnabled": true,
    "paymentsEnabled": true,
    "communitiesEnabled": true,
    "exportPaymentsEnabled": true
  },
  "scopes": "campaigns.readonly",
  "roles": {
    "type": "account",
    "role": "admin",
    "locationIds": [
      "ve9EPM428h8vShlRW1KT"
    ],
    "restrictSubAccount": true
  },
  "lcPhone": {
    "locationId": "+1234556677"
  },
  "platformLanguage": "en_US"
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **id** | `str` |  |
| **name** | `str` |  |
| **firstName** | `str` |  |
| **lastName** | `str` |  |
| **email** | `str` |  |
| **phone** | `str` |  |
| **extension** | `str` |  |
| **permissions** | `dict` |  |
| **scopes** | `str` |  |
| **roles** | `dict` |  |
| **lcPhone** | `dict` |  |
| **platformLanguage** | `str` |  |

### Error Codes

| Status Code | Description |
| :--- | :--- |
| **400 Bad Request** | Invalid input parameters. |
| **401 Unauthorized** | Invalid Token. |

---

## 4. CODE EXAMPLES

### 1. CURL

```bash
curl --request PUT \
  --url https://services.leadconnectorhq.com/users/:userId \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "type": "string",
  "role": "string",
  "companyId": "string",
  "locationIds": "string",
  "permissions": "string",
  "campaignsEnabled": true,
  "campaignsReadOnly": true,
  "contactsEnabled": true,
  "workflowsEnabled": true,
  "workflowsReadOnly": true,
  "triggersEnabled": true,
  "funnelsEnabled": true,
  "websitesEnabled": true,
  "opportunitiesEnabled": true,
  "dashboardStatsEnabled": true,
  "bulkRequestsEnabled": true,
  "appointmentsEnabled": true,
  "reviewsEnabled": true,
  "onlineListingsEnabled": true,
  "phoneCallEnabled": true,
  "conversationsEnabled": true,
  "assignedDataOnly": true,
  "adwordsReportingEnabled": true,
  "membershipEnabled": true,
  "facebookAdsReportingEnabled": true,
  "attributionsReportingEnabled": true,
  "settingsEnabled": true,
  "tagsEnabled": true,
  "leadValueEnabled": true,
  "marketingEnabled": true,
  "agentReportingEnabled": true,
  "botService": true,
  "socialPlanner": true,
  "bloggingEnabled": true,
  "invoiceEnabled": true,
  "affiliateManagerEnabled": true,
  "contentAiEnabled": true,
  "refundsEnabled": true,
  "recordPaymentEnabled": true,
  "cancelSubscriptionEnabled": true,
  "paymentsEnabled": true,
  "communitiesEnabled": true,
  "exportPaymentsEnabled": true,
  "scopes": "string",
  "scopesAssignedToOnly": "string",
  "profilePhoto": "string",
  "platformLanguage": "string"
}'
```

### 2. NODE SDK

```javascript
const { HighLevel } = require('@gohighlevel/api-client');

const ghl = new HighLevel({
  clientId: 'YOUR_CLIENT_ID',
  clientSecret: 'YOUR_CLIENT_SECRET'
});

async function executeRequest() {
  try {
    const response = await ghl.api.request('PUT', 'https://services.leadconnectorhq.com/users/:userId', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "type": "string",
  "role": "string",
  "companyId": "string",
  "locationIds": "string",
  "permissions": "string",
  "campaignsEnabled": true,
  "campaignsReadOnly": true,
  "contactsEnabled": true,
  "workflowsEnabled": true,
  "workflowsReadOnly": true,
  "triggersEnabled": true,
  "funnelsEnabled": true,
  "websitesEnabled": true,
  "opportunitiesEnabled": true,
  "dashboardStatsEnabled": true,
  "bulkRequestsEnabled": true,
  "appointmentsEnabled": true,
  "reviewsEnabled": true,
  "onlineListingsEnabled": true,
  "phoneCallEnabled": true,
  "conversationsEnabled": true,
  "assignedDataOnly": true,
  "adwordsReportingEnabled": true,
  "membershipEnabled": true,
  "facebookAdsReportingEnabled": true,
  "attributionsReportingEnabled": true,
  "settingsEnabled": true,
  "tagsEnabled": true,
  "leadValueEnabled": true,
  "marketingEnabled": true,
  "agentReportingEnabled": true,
  "botService": true,
  "socialPlanner": true,
  "bloggingEnabled": true,
  "invoiceEnabled": true,
  "affiliateManagerEnabled": true,
  "contentAiEnabled": true,
  "refundsEnabled": true,
  "recordPaymentEnabled": true,
  "cancelSubscriptionEnabled": true,
  "paymentsEnabled": true,
  "communitiesEnabled": true,
  "exportPaymentsEnabled": true,
  "scopes": "string",
  "scopesAssignedToOnly": "string",
  "profilePhoto": "string",
  "platformLanguage": "string"
}
    });
    console.log(response);
  } catch (error) {
    console.error(error);
  }
}
```

### 3. AXIOS

```javascript
const axios = require('axios');

const config = {
  method: 'put',
  url: 'https://services.leadconnectorhq.com/users/:userId',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "type": "string",
  "role": "string",
  "companyId": "string",
  "locationIds": "string",
  "permissions": "string",
  "campaignsEnabled": true,
  "campaignsReadOnly": true,
  "contactsEnabled": true,
  "workflowsEnabled": true,
  "workflowsReadOnly": true,
  "triggersEnabled": true,
  "funnelsEnabled": true,
  "websitesEnabled": true,
  "opportunitiesEnabled": true,
  "dashboardStatsEnabled": true,
  "bulkRequestsEnabled": true,
  "appointmentsEnabled": true,
  "reviewsEnabled": true,
  "onlineListingsEnabled": true,
  "phoneCallEnabled": true,
  "conversationsEnabled": true,
  "assignedDataOnly": true,
  "adwordsReportingEnabled": true,
  "membershipEnabled": true,
  "facebookAdsReportingEnabled": true,
  "attributionsReportingEnabled": true,
  "settingsEnabled": true,
  "tagsEnabled": true,
  "leadValueEnabled": true,
  "marketingEnabled": true,
  "agentReportingEnabled": true,
  "botService": true,
  "socialPlanner": true,
  "bloggingEnabled": true,
  "invoiceEnabled": true,
  "affiliateManagerEnabled": true,
  "contentAiEnabled": true,
  "refundsEnabled": true,
  "recordPaymentEnabled": true,
  "cancelSubscriptionEnabled": true,
  "paymentsEnabled": true,
  "communitiesEnabled": true,
  "exportPaymentsEnabled": true,
  "scopes": "string",
  "scopesAssignedToOnly": "string",
  "profilePhoto": "string",
  "platformLanguage": "string"
}
};

axios(config)
.then(response => console.log(JSON.stringify(response.data)))
.catch(error => console.log(error));
```

### 4. NATIVE NODE

```javascript
const https = require('follow-redirects').https;

const options = {
  'method': 'PUT',
  'hostname': 'services.leadconnectorhq.com',
  'path': '/users/:userId',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
  }
};

const req = https.request(options, (res) => {
  let chunks = [];
  res.on("data", (chunk) => chunks.push(chunk));
  res.on("end", () => console.log(Buffer.concat(chunks).toString()));
});

req.write(JSON.stringify({
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "type": "string",
  "role": "string",
  "companyId": "string",
  "locationIds": "string",
  "permissions": "string",
  "campaignsEnabled": true,
  "campaignsReadOnly": true,
  "contactsEnabled": true,
  "workflowsEnabled": true,
  "workflowsReadOnly": true,
  "triggersEnabled": true,
  "funnelsEnabled": true,
  "websitesEnabled": true,
  "opportunitiesEnabled": true,
  "dashboardStatsEnabled": true,
  "bulkRequestsEnabled": true,
  "appointmentsEnabled": true,
  "reviewsEnabled": true,
  "onlineListingsEnabled": true,
  "phoneCallEnabled": true,
  "conversationsEnabled": true,
  "assignedDataOnly": true,
  "adwordsReportingEnabled": true,
  "membershipEnabled": true,
  "facebookAdsReportingEnabled": true,
  "attributionsReportingEnabled": true,
  "settingsEnabled": true,
  "tagsEnabled": true,
  "leadValueEnabled": true,
  "marketingEnabled": true,
  "agentReportingEnabled": true,
  "botService": true,
  "socialPlanner": true,
  "bloggingEnabled": true,
  "invoiceEnabled": true,
  "affiliateManagerEnabled": true,
  "contentAiEnabled": true,
  "refundsEnabled": true,
  "recordPaymentEnabled": true,
  "cancelSubscriptionEnabled": true,
  "paymentsEnabled": true,
  "communitiesEnabled": true,
  "exportPaymentsEnabled": true,
  "scopes": "string",
  "scopesAssignedToOnly": "string",
  "profilePhoto": "string",
  "platformLanguage": "string"
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'PUT',
  'url': 'https://services.leadconnectorhq.com/users/:userId',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "type": "string",
  "role": "string",
  "companyId": "string",
  "locationIds": "string",
  "permissions": "string",
  "campaignsEnabled": true,
  "campaignsReadOnly": true,
  "contactsEnabled": true,
  "workflowsEnabled": true,
  "workflowsReadOnly": true,
  "triggersEnabled": true,
  "funnelsEnabled": true,
  "websitesEnabled": true,
  "opportunitiesEnabled": true,
  "dashboardStatsEnabled": true,
  "bulkRequestsEnabled": true,
  "appointmentsEnabled": true,
  "reviewsEnabled": true,
  "onlineListingsEnabled": true,
  "phoneCallEnabled": true,
  "conversationsEnabled": true,
  "assignedDataOnly": true,
  "adwordsReportingEnabled": true,
  "membershipEnabled": true,
  "facebookAdsReportingEnabled": true,
  "attributionsReportingEnabled": true,
  "settingsEnabled": true,
  "tagsEnabled": true,
  "leadValueEnabled": true,
  "marketingEnabled": true,
  "agentReportingEnabled": true,
  "botService": true,
  "socialPlanner": true,
  "bloggingEnabled": true,
  "invoiceEnabled": true,
  "affiliateManagerEnabled": true,
  "contentAiEnabled": true,
  "refundsEnabled": true,
  "recordPaymentEnabled": true,
  "cancelSubscriptionEnabled": true,
  "paymentsEnabled": true,
  "communitiesEnabled": true,
  "exportPaymentsEnabled": true,
  "scopes": "string",
  "scopesAssignedToOnly": "string",
  "profilePhoto": "string",
  "platformLanguage": "string"
})
};

request(options, (error, response) => {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

### 6. UNIREST NODE

```javascript
const unirest = require('unirest');

unirest('PUT', 'https://services.leadconnectorhq.com/users/:userId')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "type": "string",
  "role": "string",
  "companyId": "string",
  "locationIds": "string",
  "permissions": "string",
  "campaignsEnabled": true,
  "campaignsReadOnly": true,
  "contactsEnabled": true,
  "workflowsEnabled": true,
  "workflowsReadOnly": true,
  "triggersEnabled": true,
  "funnelsEnabled": true,
  "websitesEnabled": true,
  "opportunitiesEnabled": true,
  "dashboardStatsEnabled": true,
  "bulkRequestsEnabled": true,
  "appointmentsEnabled": true,
  "reviewsEnabled": true,
  "onlineListingsEnabled": true,
  "phoneCallEnabled": true,
  "conversationsEnabled": true,
  "assignedDataOnly": true,
  "adwordsReportingEnabled": true,
  "membershipEnabled": true,
  "facebookAdsReportingEnabled": true,
  "attributionsReportingEnabled": true,
  "settingsEnabled": true,
  "tagsEnabled": true,
  "leadValueEnabled": true,
  "marketingEnabled": true,
  "agentReportingEnabled": true,
  "botService": true,
  "socialPlanner": true,
  "bloggingEnabled": true,
  "invoiceEnabled": true,
  "affiliateManagerEnabled": true,
  "contentAiEnabled": true,
  "refundsEnabled": true,
  "recordPaymentEnabled": true,
  "cancelSubscriptionEnabled": true,
  "paymentsEnabled": true,
  "communitiesEnabled": true,
  "exportPaymentsEnabled": true,
  "scopes": "string",
  "scopesAssignedToOnly": "string",
  "profilePhoto": "string",
  "platformLanguage": "string"
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/users/:userId"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("PUT", url, headers=headers, data=json.dumps({
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "type": "string",
  "role": "string",
  "companyId": "string",
  "locationIds": "string",
  "permissions": "string",
  "campaignsEnabled": true,
  "campaignsReadOnly": true,
  "contactsEnabled": true,
  "workflowsEnabled": true,
  "workflowsReadOnly": true,
  "triggersEnabled": true,
  "funnelsEnabled": true,
  "websitesEnabled": true,
  "opportunitiesEnabled": true,
  "dashboardStatsEnabled": true,
  "bulkRequestsEnabled": true,
  "appointmentsEnabled": true,
  "reviewsEnabled": true,
  "onlineListingsEnabled": true,
  "phoneCallEnabled": true,
  "conversationsEnabled": true,
  "assignedDataOnly": true,
  "adwordsReportingEnabled": true,
  "membershipEnabled": true,
  "facebookAdsReportingEnabled": true,
  "attributionsReportingEnabled": true,
  "settingsEnabled": true,
  "tagsEnabled": true,
  "leadValueEnabled": true,
  "marketingEnabled": true,
  "agentReportingEnabled": true,
  "botService": true,
  "socialPlanner": true,
  "bloggingEnabled": true,
  "invoiceEnabled": true,
  "affiliateManagerEnabled": true,
  "contentAiEnabled": true,
  "refundsEnabled": true,
  "recordPaymentEnabled": true,
  "cancelSubscriptionEnabled": true,
  "paymentsEnabled": true,
  "communitiesEnabled": true,
  "exportPaymentsEnabled": true,
  "scopes": "string",
  "scopesAssignedToOnly": "string",
  "profilePhoto": "string",
  "platformLanguage": "string"
}))
print(response.text)
```

### 8. PHP

```php
<?php
use GuzzleHttp\Client;
$client = new Client();
$headers = [
  'Authorization' => 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version' => '2021-07-28',
  'Content-Type' => 'application/json'
];
$response = $client->request('PUT', 'https://services.leadconnectorhq.com/users/:userId', [
  'headers' => $headers,
  'body' => '{
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "type": "string",
  "role": "string",
  "companyId": "string",
  "locationIds": "string",
  "permissions": "string",
  "campaignsEnabled": true,
  "campaignsReadOnly": true,
  "contactsEnabled": true,
  "workflowsEnabled": true,
  "workflowsReadOnly": true,
  "triggersEnabled": true,
  "funnelsEnabled": true,
  "websitesEnabled": true,
  "opportunitiesEnabled": true,
  "dashboardStatsEnabled": true,
  "bulkRequestsEnabled": true,
  "appointmentsEnabled": true,
  "reviewsEnabled": true,
  "onlineListingsEnabled": true,
  "phoneCallEnabled": true,
  "conversationsEnabled": true,
  "assignedDataOnly": true,
  "adwordsReportingEnabled": true,
  "membershipEnabled": true,
  "facebookAdsReportingEnabled": true,
  "attributionsReportingEnabled": true,
  "settingsEnabled": true,
  "tagsEnabled": true,
  "leadValueEnabled": true,
  "marketingEnabled": true,
  "agentReportingEnabled": true,
  "botService": true,
  "socialPlanner": true,
  "bloggingEnabled": true,
  "invoiceEnabled": true,
  "affiliateManagerEnabled": true,
  "contentAiEnabled": true,
  "refundsEnabled": true,
  "recordPaymentEnabled": true,
  "cancelSubscriptionEnabled": true,
  "paymentsEnabled": true,
  "communitiesEnabled": true,
  "exportPaymentsEnabled": true,
  "scopes": "string",
  "scopesAssignedToOnly": "string",
  "profilePhoto": "string",
  "platformLanguage": "string"
}'
]);
echo $response->getBody();
```

### 9. JAVA

```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

HttpClient client = HttpClient.newHttpClient();
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://services.leadconnectorhq.com/users/:userId"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("PUT", HttpRequest.BodyPublishers.ofString("{
  \"firstName\": \"string\",
  \"lastName\": \"string\",
  \"email\": \"string\",
  \"password\": \"string\",
  \"phone\": \"string\",
  \"type\": \"string\",
  \"role\": \"string\",
  \"companyId\": \"string\",
  \"locationIds\": \"string\",
  \"permissions\": \"string\",
  \"campaignsEnabled\": true,
  \"campaignsReadOnly\": true,
  \"contactsEnabled\": true,
  \"workflowsEnabled\": true,
  \"workflowsReadOnly\": true,
  \"triggersEnabled\": true,
  \"funnelsEnabled\": true,
  \"websitesEnabled\": true,
  \"opportunitiesEnabled\": true,
  \"dashboardStatsEnabled\": true,
  \"bulkRequestsEnabled\": true,
  \"appointmentsEnabled\": true,
  \"reviewsEnabled\": true,
  \"onlineListingsEnabled\": true,
  \"phoneCallEnabled\": true,
  \"conversationsEnabled\": true,
  \"assignedDataOnly\": true,
  \"adwordsReportingEnabled\": true,
  \"membershipEnabled\": true,
  \"facebookAdsReportingEnabled\": true,
  \"attributionsReportingEnabled\": true,
  \"settingsEnabled\": true,
  \"tagsEnabled\": true,
  \"leadValueEnabled\": true,
  \"marketingEnabled\": true,
  \"agentReportingEnabled\": true,
  \"botService\": true,
  \"socialPlanner\": true,
  \"bloggingEnabled\": true,
  \"invoiceEnabled\": true,
  \"affiliateManagerEnabled\": true,
  \"contentAiEnabled\": true,
  \"refundsEnabled\": true,
  \"recordPaymentEnabled\": true,
  \"cancelSubscriptionEnabled\": true,
  \"paymentsEnabled\": true,
  \"communitiesEnabled\": true,
  \"exportPaymentsEnabled\": true,
  \"scopes\": \"string\",
  \"scopesAssignedToOnly\": \"string\",
  \"profilePhoto\": \"string\",
  \"platformLanguage\": \"string\"
}"))
    .build();

HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
System.out.println(response.body());
```

### 10. GO

```go
package main
import (
  "fmt"
  "strings"
  "net/http"
  "io/ioutil"
)
func main() {
  url := "https://services.leadconnectorhq.com/users/:userId"
  payload := strings.NewReader(`{
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "type": "string",
  "role": "string",
  "companyId": "string",
  "locationIds": "string",
  "permissions": "string",
  "campaignsEnabled": true,
  "campaignsReadOnly": true,
  "contactsEnabled": true,
  "workflowsEnabled": true,
  "workflowsReadOnly": true,
  "triggersEnabled": true,
  "funnelsEnabled": true,
  "websitesEnabled": true,
  "opportunitiesEnabled": true,
  "dashboardStatsEnabled": true,
  "bulkRequestsEnabled": true,
  "appointmentsEnabled": true,
  "reviewsEnabled": true,
  "onlineListingsEnabled": true,
  "phoneCallEnabled": true,
  "conversationsEnabled": true,
  "assignedDataOnly": true,
  "adwordsReportingEnabled": true,
  "membershipEnabled": true,
  "facebookAdsReportingEnabled": true,
  "attributionsReportingEnabled": true,
  "settingsEnabled": true,
  "tagsEnabled": true,
  "leadValueEnabled": true,
  "marketingEnabled": true,
  "agentReportingEnabled": true,
  "botService": true,
  "socialPlanner": true,
  "bloggingEnabled": true,
  "invoiceEnabled": true,
  "affiliateManagerEnabled": true,
  "contentAiEnabled": true,
  "refundsEnabled": true,
  "recordPaymentEnabled": true,
  "cancelSubscriptionEnabled": true,
  "paymentsEnabled": true,
  "communitiesEnabled": true,
  "exportPaymentsEnabled": true,
  "scopes": "string",
  "scopesAssignedToOnly": "string",
  "profilePhoto": "string",
  "platformLanguage": "string"
}`)
  req, _ := http.NewRequest("PUT", url, payload)
  req.Header.Add("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
  req.Header.Add("Version", "2021-07-28")
  req.Header.Add("Content-Type", "application/json")
  res, _ := http.DefaultClient.Do(req)
  defer res.Body.Close()
  body, _ := ioutil.ReadAll(res.Body)
  fmt.Println(string(body))
}
```

### 11. RUBY

```ruby
require 'net/http'
require 'uri'
require 'json'

url = URI("https://services.leadconnectorhq.com/users/:userId")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Put.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "type": "string",
  "role": "string",
  "companyId": "string",
  "locationIds": "string",
  "permissions": "string",
  "campaignsEnabled": true,
  "campaignsReadOnly": true,
  "contactsEnabled": true,
  "workflowsEnabled": true,
  "workflowsReadOnly": true,
  "triggersEnabled": true,
  "funnelsEnabled": true,
  "websitesEnabled": true,
  "opportunitiesEnabled": true,
  "dashboardStatsEnabled": true,
  "bulkRequestsEnabled": true,
  "appointmentsEnabled": true,
  "reviewsEnabled": true,
  "onlineListingsEnabled": true,
  "phoneCallEnabled": true,
  "conversationsEnabled": true,
  "assignedDataOnly": true,
  "adwordsReportingEnabled": true,
  "membershipEnabled": true,
  "facebookAdsReportingEnabled": true,
  "attributionsReportingEnabled": true,
  "settingsEnabled": true,
  "tagsEnabled": true,
  "leadValueEnabled": true,
  "marketingEnabled": true,
  "agentReportingEnabled": true,
  "botService": true,
  "socialPlanner": true,
  "bloggingEnabled": true,
  "invoiceEnabled": true,
  "affiliateManagerEnabled": true,
  "contentAiEnabled": true,
  "refundsEnabled": true,
  "recordPaymentEnabled": true,
  "cancelSubscriptionEnabled": true,
  "paymentsEnabled": true,
  "communitiesEnabled": true,
  "exportPaymentsEnabled": true,
  "scopes": "string",
  "scopesAssignedToOnly": "string",
  "profilePhoto": "string",
  "platformLanguage": "string"
})
response = http.request(request)
puts response.read_body
```

### 12. POWERSHELL

```powershell
$headers = New-Object "System.Collections.Generic.Dictionary[[String],[String]]"
$headers.Add("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
$headers.Add("Version", "2021-07-28")
$headers.Add("Content-Type", "application/json")

$body = '{
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "type": "string",
  "role": "string",
  "companyId": "string",
  "locationIds": "string",
  "permissions": "string",
  "campaignsEnabled": true,
  "campaignsReadOnly": true,
  "contactsEnabled": true,
  "workflowsEnabled": true,
  "workflowsReadOnly": true,
  "triggersEnabled": true,
  "funnelsEnabled": true,
  "websitesEnabled": true,
  "opportunitiesEnabled": true,
  "dashboardStatsEnabled": true,
  "bulkRequestsEnabled": true,
  "appointmentsEnabled": true,
  "reviewsEnabled": true,
  "onlineListingsEnabled": true,
  "phoneCallEnabled": true,
  "conversationsEnabled": true,
  "assignedDataOnly": true,
  "adwordsReportingEnabled": true,
  "membershipEnabled": true,
  "facebookAdsReportingEnabled": true,
  "attributionsReportingEnabled": true,
  "settingsEnabled": true,
  "tagsEnabled": true,
  "leadValueEnabled": true,
  "marketingEnabled": true,
  "agentReportingEnabled": true,
  "botService": true,
  "socialPlanner": true,
  "bloggingEnabled": true,
  "invoiceEnabled": true,
  "affiliateManagerEnabled": true,
  "contentAiEnabled": true,
  "refundsEnabled": true,
  "recordPaymentEnabled": true,
  "cancelSubscriptionEnabled": true,
  "paymentsEnabled": true,
  "communitiesEnabled": true,
  "exportPaymentsEnabled": true,
  "scopes": "string",
  "scopesAssignedToOnly": "string",
  "profilePhoto": "string",
  "platformLanguage": "string"
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/users/:userId' -Method 'PUT' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
