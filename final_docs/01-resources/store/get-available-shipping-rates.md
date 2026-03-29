# Get available shipping rates

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | POST |
| **Endpoint URL** | `https://services.leadconnectorhq.com/store/shipping-zone/shipping-rates` |
| **Scopes Required** | `N/A` |
| **Authentication** | OAuth Access Token / Private Integration Token |
| **Token Type** | Sub-Account Token |

---

## 2. REQUEST

### Header Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **Version** | `string` | Yes | API version. Use `2021-07-28`. |

### Path Parameters

N/A
### Query Parameters

N/A
### Body Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **altId** | `string` | No |  |
| **altType** | `string` | No |  |
| **country** | `string` | No |  |
| **address** | `object` | Yes | Address of the customer name string Name of the customer Example: John Doe companyName string Name of the Company Example: ABC Company addressLine1 string Address line 1 of the customer Example: 123 Main St. country string required Country code of the customer Possible values: [ US , CA , AF , AX , AL , DZ , AS , AD , AO , AI , AQ , AG , AR , AM , AW , AU , AT , AZ , BS , BH , BD , BB , BY , BE , BZ , BJ , BM , BT , BO , BA , BW , BV , BR , IO , BN , BG , BF , BI , KH , CM , CV , KY , CF , TD , CL , CN , CX , CC , CO , KM , CG , CD , CK , CR , CI , HR , CU , CY , CZ , DK , DJ , DM , DO , EC , EG , SV , GQ , ER , EE , ET , FK , FO , FJ , FI , FR , GF , PF , TF , GA , GM , GE , DE , GH , GI , GR , GL , GD , GP , GU , GT , GG , GN , GW , GY , HT , HM , VA , HN , HK , HU , IS , IN , ID , IR , IQ , IE , IM , IL , IT , JM , JP , JE , JO , KZ , KE , KI , KP , XK , KW , KG , LA , LV , LB , LS , LR , LY , LI , LT , LU , MO , MK , MG , MW , MY , MV , ML , MT , MH , MQ , MR , MU , YT , MX , FM , MD , MC , MN , ME , MS , MA , MZ , MM , NA , NR , NP , NL , AN , NC , NZ , NI , NE , NG , NU , NF , MP , NO , OM , PK , PW , PS , PA , PG , PY , PE , PH , PN , PL , PT , PR , QA , RE , RO , RU , RW , SH , KN , LC , MF , PM , VC , WS , SM , ST , SA , SN , RS , SC , SL , SG , SX , SK , SI , SB , SO , ZA , GS , KR , ES , LK , SD , SR , SJ , SZ , SE , CH , SY , TW , TJ , TZ , TH , TL , TG , TK , TO , TT , TN , TR , TM , TC , TV , UG , UA , AE , GB , UM , UY , UZ , VU , VE , VN , VG , VI , WF , EH , YE , ZM , ZW ] Example: US state string State code of the customer Possible values: [ AL , AK , AS , AZ , AR , AA , AE , AP , CA , CO , CT , DE , DC , FM , FL , GA , GU , HI , ID , IL , IN , IA , KS , KY , LA , ME , MH , MD , MA , MI , MN , MS , MO , MT , NE , NV , NH , NJ , NM , NY , NC , ND , MP , OH , OK , OR , PW , PA , PR , RI , SC , SD , TN , TX , UT , VT , VI , VA , WA , WV , WI , WY , AB , BC , MB , NB , NL , NT , NS , NU , ON , PE , QC , SK , YT , BA , CT , CC , CH , CB , CN , ER , FO , JY , LP , LR , MZ , MN , NQ , RN , SA , SJ , SL , SC , SF , SE , TF , TU , ACT , NSW , NT , QLD , SA , TAS , VIC , WA , AC , AL , AM , AP , BA , CE , DF , ES , GO , MA , MG , MS , MT , PA , PB , PE , PI , PR , RJ , RN , RO , RR , RS , SC , SE , SP , TO , AI , AN , AP , AT , BI , CO , AR , LI , LL , LR , MA , ML , RM , TA , VS , NB , AMA , ANT , ARA , ATL , BOL , BOY , CAL , CAQ , CAS , CAU , CES , CHO , CUN , COR , GUA , GUV , HUI , LAG , MAG , MET , NAR , NSA , PUT , QUI , RIS , SAP , SAN , SUC , TOL , VAC , VAU , VID , CR-A , CR-C , CR-G , CR-H , CR-L , CR-P , CR-SJ , GT-16 , GT-15 , GT-04 , GT-20 , GT-02 , GT-05 , GT-01 , GT-13 , GT-18 , GT-21 , GT-22 , GT-17 , GT-09 , GT-14 , GT-11 , GT-03 , GT-12 , GT-06 , GT-07 , GT-10 , GT-08 , GT-19 , HK , KL , NT , AN , AP , AR , AS , BR , CH , CG , DN , DD , DL , GA , GJ , HR , HP , JK , JH , KA , KL , LA , LD , MP , MH , MN , ML , MZ , NL , OR , PY , PB , RJ , SK , TN , TS , TR , UP , UK , WB , CW , CN , CE , CO , DL , D , G , KY , KE , KK , LS , LM , LK , LD , LH , MO , MH , MN , OY , RN , SO , TA , WD , WH , WX , WW , AG , AL , AN , AO , AR , AP , AT , AV , BA , BT , BL , BN , BG , BI , BO , BZ , BS , BR , CA , CL , CB , CI , CE , CT , CZ , CH , CO , CS , CR , KR , CN , EN , FM , FE , FI , FG , FC , FR , GE , GO , GR , IM , IS , AQ , SP , LT , LE , LC , LI , LO , LU , MC , MN , MS , MT , VS , ME , MI , MO , MB , NA , NO , NU , OG , OT , OR , PD , PA , PR , PV , PG , PU , PE , PC , PI , PT , PN , PZ , PO , RG , RA , RC , RE , RI , RN , RM , RO , SA , SS , SV , SI , SR , SO , TA , TE , TR , TO , TP , TN , TV , TS , UD , VA , VE , VB , VC , VR , VV , VI , VT , JP-23 , JP-05 , JP-02 , JP-12 , JP-38 , JP-18 , JP-40 , JP-07 , JP-21 , JP-10 , JP-34 , JP-01 , JP-28 , JP-08 , JP-17 , JP-03 , JP-37 , JP-46 , JP-14 , JP-39 , JP-43 , JP-26 , JP-24 , JP-04 , JP-45 , JP-20 , JP-42 , JP-29 , JP-15 , JP-44 , JP-33 , JP-47 , JP-27 , JP-41 , JP-11 , JP-25 , JP-32 , JP-22 , JP-09 , JP-36 , JP-13 , JP-31 , JP-16 , JP-30 , JP-06 , JP-35 , JP-19 , JHR , KDH , KTN , KUL , LBN , MLK , NSN , PHG , PNG , PRK , PLS , PJY , SBH , SWK , SGR , TRG , AGU , BCN , BCS , CAM , CHP , CHH , CMX , COA , COL , DUR , GUA , GRO , HID , JAL , MIC , MOR , MEX , NAY , NLE , OAX , PUE , QUE , ROO , SLP , SIN , SON , TAB , TAM , TLA , VER , YUC , ZAC , AUK , BOP , CAN , CIT , GIS , HKB , MWT , MBH , NSN , NTL , OTA , STL , TKI , TAS , WKO , WGN , WTC , JK , BA , GB , IS , KP , PB , SD , AMA , ANC , APU , ARE , AYA , CAJ , CAL , CUS , HUV , HUC , ICA , JUN , LAL , LAM , LIM , LOR , MDD , MOQ , PAS , PIU , PUN , SAM , TAC , TUM , UCA , PH-ABR , PH-AGN , PH-AGS , PH-AKL , PH-ALB , PH-ANT , PH-APA , PH-AUR , PH-BAS , PH-BAN , PH-BTN , PH-BTG , PH-BEN , PH-BIL , PH-BOH , PH-BUK , PH-BUL , PH-CAG , PH-CAN , PH-CAS , PH-CAM , PH-CAP , PH-CAT , PH-CAV , PH-CEB , PH-NCO , PH-DAO , PH-DAV , PH-DAS , PH-EAS , PH-GUI , PH-IFU , PH-ILN , PH-ILS , PH-ILI , PH-ISA , PH-KAL , PH-LUN , PH-LAG , PH-LAN , PH-LAS , PH-LEY , PH-MAG , PH-MAD , PH-MAS , PH-00 , PH-MSC , PH-MSR , PH-MOU , PH-NEC , PH-NER , PH-NSA , PH-NUE , PH-NUV , PH-MDC , PH-MDR , PH-PLW , PH-PAM , PH-PAN , PH-QUE , PH-QUI , PH-RIZ , PH-ROM , PH-WSA , PH-SAR , PH-SIG , PH-SOR , PH-SCO , PH-SLE , PH-SUK , PH-SLU , PH-SUN , PH-SUR , PH-TAR , PH-TAW , PH-ZMB , PH-ZAN , PH-ZAS , PH-ZSI , PT-20 , PT-01 , PT-02 , PT-03 , PT-04 , PT-05 , PT-06 , PT-07 , PT-08 , PT-09 , PT-10 , PT-11 , PT-30 , PT-12 , PT-13 , PT-14 , PT-15 , PT-16 , PT-17 , PT-18 , AB , AR , AG , BC , BH , BN , BT , BR , BV , B , BZ , CL , CS , CJ , CT , CV , DB , DJ , GL , GR , GJ , HR , HD , IL , IS , IF , MM , MH , MS , NT , OT , PH , SJ , SM , SB , SV , TR , TM , TL , VL , VS , VN , KR-26 , KR-43 , KR-44 , KR-27 , KR-30 , KR-42 , KR-29 , KR-47 , KR-41 , KR-48 , KR-28 , KR-49 , KR-45 , KR-46 , KR-50 , KR-11 , KR-31 , C , VI , AB , A , AL , O , AV , BA , PM , B , BU , CC , CA , S , CS , CE , CR , CO , CU , GI , GR , GU , SS , H , HU , J , LO , GC , LE , L , LU , M , MA , ML , MU , NA , OR , P , PO , SA , TF , SG , SE , SO , T , TE , TO , V , VA , BI , ZA , Z , AZ , AJ , DU , FU , RK , SH , UQ , BFP , ENG , NIR , SCT , WLS , AR , CA , CL , CO , DU , FS , FD , LA , MA , MO , PA , RN , RV , RO , SA , SJ , SO , TA , TT ] Example: US city string City of the customer Example: New York zip string Zip code of the customer Example: 12345 phone string Phone number of the customer Example: 1234567890 email string Email of the customer Example: abu@example.com |
| **name** | `string` | No |  |
| **companyName** | `string` | No |  |
| **addressLine1** | `string` | No |  |
| **country** | `string` | No |  |
| **state** | `string` | No |  |
| **city** | `string` | No |  |
| **zip** | `string` | No |  |
| **phone** | `string` | No |  |
| **email** | `string` | No |  |
| **amountAvailable** | `string` | No |  |
| **totalOrderAmount** | `number` | No |  |
| **weightAvailable** | `boolean` | No |  |
| **totalOrderWeight** | `number` | No |  |
| **source** | `object` | Yes | Source of the order type string required Source of order Possible values: [ funnel , website , invoice , calendar , text2Pay , document_contracts , membership , mobile_app , communities , point_of_sale , manual , form , survey , payment_link , external ] Example: website subType string Source subtype of order Possible values: [ one_step_order_form , two_step_order_form , upsell , tap_to_pay , card_payment , store , contact_view , email_campaign , payments_dashboard , shopify , subscription_view , store_upsell , woocommerce , service , meeting , imported_csv , qr_code ] Example: store |
| **type** | `string` | No |  |
| **subType** | `string` | No |  |
| **products** | `object[]` | Yes | An array of price IDs and quantity Array [ id string required id of product qty number required No of quantities ] |
| **id** | `string` | No |  |
| **qty** | `number` | No |  |
| **couponCode** | `string` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "status": true,
  "message": "Successfully created",
  "data": [
    {
      "name": "North zone",
      "description": "Ships next day",
      "currency": "USD",
      "amount": 99.99,
      "isCarrierRate": true,
      "shippingCarrierId": "655b33a82209e60b6adb87a5",
      "percentageOfRateFee": 10.99,
      "shippingCarrierServices": [
        {
          "name": "Priority Mail Express International",
          "value": "PriorityMailExpressInternational"
        }
      ],
      "_id": "655b33a82209e60b6adb87a5",
      "shippingZoneId": "655b33a82209e60b6adb87a5"
    }
  ]
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **status** | `bool` |  |
| **message** | `str` |  |
| **data** | `list` |  |

### Error Codes

| Status Code | Description |
| :--- | :--- |
| **400 Bad Request** | Invalid input parameters. |
| **401 Unauthorized** | Invalid Token. |

---

## 4. CODE EXAMPLES

### 1. CURL

```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/store/shipping-zone/shipping-rates \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "altId": "string",
  "altType": "string",
  "country": "string",
  "address": "string",
  "name": "string",
  "companyName": "string",
  "addressLine1": "string",
  "state": "string",
  "city": "string",
  "zip": "string",
  "phone": "string",
  "email": "string",
  "amountAvailable": "string",
  "totalOrderAmount": 123,
  "weightAvailable": true,
  "totalOrderWeight": 123,
  "source": "string",
  "type": "string",
  "subType": "string",
  "products": "string",
  "id": "string",
  "qty": 123,
  "couponCode": "string"
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
    const response = await ghl.api.request('POST', 'https://services.leadconnectorhq.com/store/shipping-zone/shipping-rates', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "altId": "string",
  "altType": "string",
  "country": "string",
  "address": "string",
  "name": "string",
  "companyName": "string",
  "addressLine1": "string",
  "state": "string",
  "city": "string",
  "zip": "string",
  "phone": "string",
  "email": "string",
  "amountAvailable": "string",
  "totalOrderAmount": 123,
  "weightAvailable": true,
  "totalOrderWeight": 123,
  "source": "string",
  "type": "string",
  "subType": "string",
  "products": "string",
  "id": "string",
  "qty": 123,
  "couponCode": "string"
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
  method: 'post',
  url: 'https://services.leadconnectorhq.com/store/shipping-zone/shipping-rates',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "altId": "string",
  "altType": "string",
  "country": "string",
  "address": "string",
  "name": "string",
  "companyName": "string",
  "addressLine1": "string",
  "state": "string",
  "city": "string",
  "zip": "string",
  "phone": "string",
  "email": "string",
  "amountAvailable": "string",
  "totalOrderAmount": 123,
  "weightAvailable": true,
  "totalOrderWeight": 123,
  "source": "string",
  "type": "string",
  "subType": "string",
  "products": "string",
  "id": "string",
  "qty": 123,
  "couponCode": "string"
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
  'method': 'POST',
  'hostname': 'services.leadconnectorhq.com',
  'path': '/store/shipping-zone/shipping-rates',
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
  "altId": "string",
  "altType": "string",
  "country": "string",
  "address": "string",
  "name": "string",
  "companyName": "string",
  "addressLine1": "string",
  "state": "string",
  "city": "string",
  "zip": "string",
  "phone": "string",
  "email": "string",
  "amountAvailable": "string",
  "totalOrderAmount": 123,
  "weightAvailable": true,
  "totalOrderWeight": 123,
  "source": "string",
  "type": "string",
  "subType": "string",
  "products": "string",
  "id": "string",
  "qty": 123,
  "couponCode": "string"
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'POST',
  'url': 'https://services.leadconnectorhq.com/store/shipping-zone/shipping-rates',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "altId": "string",
  "altType": "string",
  "country": "string",
  "address": "string",
  "name": "string",
  "companyName": "string",
  "addressLine1": "string",
  "state": "string",
  "city": "string",
  "zip": "string",
  "phone": "string",
  "email": "string",
  "amountAvailable": "string",
  "totalOrderAmount": 123,
  "weightAvailable": true,
  "totalOrderWeight": 123,
  "source": "string",
  "type": "string",
  "subType": "string",
  "products": "string",
  "id": "string",
  "qty": 123,
  "couponCode": "string"
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

unirest('POST', 'https://services.leadconnectorhq.com/store/shipping-zone/shipping-rates')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "altId": "string",
  "altType": "string",
  "country": "string",
  "address": "string",
  "name": "string",
  "companyName": "string",
  "addressLine1": "string",
  "state": "string",
  "city": "string",
  "zip": "string",
  "phone": "string",
  "email": "string",
  "amountAvailable": "string",
  "totalOrderAmount": 123,
  "weightAvailable": true,
  "totalOrderWeight": 123,
  "source": "string",
  "type": "string",
  "subType": "string",
  "products": "string",
  "id": "string",
  "qty": 123,
  "couponCode": "string"
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/store/shipping-zone/shipping-rates"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=json.dumps({
  "altId": "string",
  "altType": "string",
  "country": "string",
  "address": "string",
  "name": "string",
  "companyName": "string",
  "addressLine1": "string",
  "state": "string",
  "city": "string",
  "zip": "string",
  "phone": "string",
  "email": "string",
  "amountAvailable": "string",
  "totalOrderAmount": 123,
  "weightAvailable": true,
  "totalOrderWeight": 123,
  "source": "string",
  "type": "string",
  "subType": "string",
  "products": "string",
  "id": "string",
  "qty": 123,
  "couponCode": "string"
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
$response = $client->request('POST', 'https://services.leadconnectorhq.com/store/shipping-zone/shipping-rates', [
  'headers' => $headers,
  'body' => '{
  "altId": "string",
  "altType": "string",
  "country": "string",
  "address": "string",
  "name": "string",
  "companyName": "string",
  "addressLine1": "string",
  "state": "string",
  "city": "string",
  "zip": "string",
  "phone": "string",
  "email": "string",
  "amountAvailable": "string",
  "totalOrderAmount": 123,
  "weightAvailable": true,
  "totalOrderWeight": 123,
  "source": "string",
  "type": "string",
  "subType": "string",
  "products": "string",
  "id": "string",
  "qty": 123,
  "couponCode": "string"
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
    .uri(URI.create("https://services.leadconnectorhq.com/store/shipping-zone/shipping-rates"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("POST", HttpRequest.BodyPublishers.ofString("{
  \"altId\": \"string\",
  \"altType\": \"string\",
  \"country\": \"string\",
  \"address\": \"string\",
  \"name\": \"string\",
  \"companyName\": \"string\",
  \"addressLine1\": \"string\",
  \"state\": \"string\",
  \"city\": \"string\",
  \"zip\": \"string\",
  \"phone\": \"string\",
  \"email\": \"string\",
  \"amountAvailable\": \"string\",
  \"totalOrderAmount\": 123,
  \"weightAvailable\": true,
  \"totalOrderWeight\": 123,
  \"source\": \"string\",
  \"type\": \"string\",
  \"subType\": \"string\",
  \"products\": \"string\",
  \"id\": \"string\",
  \"qty\": 123,
  \"couponCode\": \"string\"
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
  url := "https://services.leadconnectorhq.com/store/shipping-zone/shipping-rates"
  payload := strings.NewReader(`{
  "altId": "string",
  "altType": "string",
  "country": "string",
  "address": "string",
  "name": "string",
  "companyName": "string",
  "addressLine1": "string",
  "state": "string",
  "city": "string",
  "zip": "string",
  "phone": "string",
  "email": "string",
  "amountAvailable": "string",
  "totalOrderAmount": 123,
  "weightAvailable": true,
  "totalOrderWeight": 123,
  "source": "string",
  "type": "string",
  "subType": "string",
  "products": "string",
  "id": "string",
  "qty": 123,
  "couponCode": "string"
}`)
  req, _ := http.NewRequest("POST", url, payload)
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

url = URI("https://services.leadconnectorhq.com/store/shipping-zone/shipping-rates")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "altId": "string",
  "altType": "string",
  "country": "string",
  "address": "string",
  "name": "string",
  "companyName": "string",
  "addressLine1": "string",
  "state": "string",
  "city": "string",
  "zip": "string",
  "phone": "string",
  "email": "string",
  "amountAvailable": "string",
  "totalOrderAmount": 123,
  "weightAvailable": true,
  "totalOrderWeight": 123,
  "source": "string",
  "type": "string",
  "subType": "string",
  "products": "string",
  "id": "string",
  "qty": 123,
  "couponCode": "string"
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
  "altId": "string",
  "altType": "string",
  "country": "string",
  "address": "string",
  "name": "string",
  "companyName": "string",
  "addressLine1": "string",
  "state": "string",
  "city": "string",
  "zip": "string",
  "phone": "string",
  "email": "string",
  "amountAvailable": "string",
  "totalOrderAmount": 123,
  "weightAvailable": true,
  "totalOrderWeight": 123,
  "source": "string",
  "type": "string",
  "subType": "string",
  "products": "string",
  "id": "string",
  "qty": 123,
  "couponCode": "string"
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/store/shipping-zone/shipping-rates' -Method 'POST' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
