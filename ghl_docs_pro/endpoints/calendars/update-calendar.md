# Update Calendar

**Method:** `PUT` | **URL:** `https://services.leadconnectorhq.com/calendars/:calendarId`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
name: Authorization
type: http
scopes: calendars.write
scheme: bearer
bearerFormat: JWT
in: header
description: Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.
```

## 📥 Parameters
### Path Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `calendarId` | ❌ |  |

### Header Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `Version` | ❌ |  |

## 📤 Responses
<details>
<summary>Response 200</summary>

```json
{
  "calendar": {
    "isActive": true,
    "locationId": "ocQHyuzHvysMo5N5VsXc",
    "groupId": "BqTwX8QFwXzpegMve9EQ",
    "teamMembers": [
      {
        "userId": "ocQHyuzHvysMo5N5VsXc",
        "priority": 0.5,
        "isPrimary": true,
        "locationConfigurations": [
          {
            "kind": "custom",
            "location": "string",
            "meetingId": "my_conference_id"
          }
        ]
      }
    ],
    "eventType": "RoundRobin_OptimizeForAvailability",
    "name": "test calendar",
    "description": "this is used for testing",
    "slug": "test1",
    "widgetSlug": "test1",
    "calendarType": "round_robin",
    "widgetType": "classic",
    "eventTitle": "{{contact.name}}",
    "eventColor": "#039be5",
    "locationConfigurations": [
      {
        "kind": "custom",
        "location": "string",
        "meetingId": "my_conference_id"
      }
    ],
    "slotDuration": 30,
    "slotDurationUnit": "mins",
    "slotInterval": 30,
    "slotIntervalUnit": "mins",
    "slotBuffer": 0,
    "slotBufferUnit": "mins",
    "preBuffer": 0,
    "preBufferUnit": "mins",
    "appoinmentPerSlot": 1,
    "appoinmentPerDay": 0,
    "allowBookingAfter": 0,
    "allowBookingAfterUnit": "days",
    "allowBookingFor": 0,
    "allowBookingForUnit": "days",
    "enableRecurring": false,
    "recurring": {
      "freq": "DAILY",
      "count": 0,
      "bookingOption": "skip",
      "bookingOverlapDefaultStatus": "confirmed"
    },
    "formId": "string",
    "stickyContact": true,
    "isLivePaymentMode": true,
    "autoConfirm": true,
    "shouldSendAlertEmailsToAssignedMember": true,
    "alertEmail": "string",
    "googleInvitationEmails": false,
    "allowReschedule": true,
    "allowCancellation": true,
    "shouldAssignContactToTeamMember": true,
    "shouldSkipAssigningContactForExisting": true,
    "notes": "string",
    "pixelId": "string",
    "formSubmitType": "ThankYouMessage",
    "formSubmitRedirectURL": "string",
    "formSubmitThanksMessage": "string",
    "guestType": "count_only",
    "consentLabel": "string",
    "calendarCoverImage": "https://path-to-image.com",
    "lookBusyConfig": {
      "enabled": true,
      "LookBusyPercentage": 0
    },
    "id": "0TkCdp9PfvLeWKYRRvIz"
  }
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "calendar": {    "isActive": true,    "locationId": "ocQHyuzHvysMo5N5VsXc",    "groupId": "BqTwX8QFwXzpegMve9EQ",    "teamMembers": [      {        "userId": "ocQHyuzHvysMo5N5VsXc",        "priority": 0.5,        "isPrimary": true,        "locationConfigurations": [          {            "kind": "custom",            "location": "string",            "meetingId": "my_conference_id"          }        ]      }    ],    "eventType": "RoundRobin_OptimizeForAvailability",    "name": "test calendar",    "description": "this is used for testing",    "slug": "test1",    "widgetSlug": "test1",    "calendarType": "round_robin",    "widgetType": "classic",    "eventTitle": "{{contact.name}}",    "eventColor": "#039be5",    "locationConfigurations": [      {        "kind": "custom",        "location": "string",        "meetingId": "my_conference_id"      }    ],    "slotDuration": 30,    "slotDurationUnit": "mins",    "slotInterval": 30,    "slotIntervalUnit": "mins",    "slotBuffer": 0,    "slotBufferUnit": "mins",    "preBuffer": 0,    "preBufferUnit": "mins",    "appoinmentPerSlot": 1,    "appoinmentPerDay": 0,    "allowBookingAfter": 0,    "allowBookingAfterUnit": "days",    "allowBookingFor": 0,    "allowBookingForUnit": "days",    "enableRecurring": false,    "recurring": {      "freq": "DAILY",      "count": 0,      "bookingOption": "skip",      "bookingOverlapDefaultStatus": "confirmed"    },    "formId": "string",    "stickyContact": true,    "isLivePaymentMode": true,    "autoConfirm": true,    "shouldSendAlertEmailsToAssignedMember": true,    "alertEmail": "string",    "googleInvitationEmails": false,    "allowReschedule": true,    "allowCancellation": true,    "shouldAssignContactToTeamMember": true,    "shouldSkipAssigningContactForExisting": true,    "notes": "string",    "pixelId": "string",    "formSubmitType": "ThankYouMessage",    "formSubmitRedirectURL": "string",    "formSubmitThanksMessage": "string",    "guestType": "count_only",    "consentLabel": "string",    "calendarCoverImage": "https://path-to-image.com",    "lookBusyConfig": {      "enabled": true,      "LookBusyPercentage": 0    },    "id": "0TkCdp9PfvLeWKYRRvIz"  }}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "calendar": {    "isActive": true,    "locationId": "ocQHyuzHvysMo5N5VsXc",    "groupId": "BqTwX8QFwXzpegMve9EQ",    "teamMembers": [      {        "userId": "ocQHyuzHvysMo5N5VsXc",        "priority": 0.5,        "isPrimary": true,        "locationConfigurations": [          {            "kind": "custom",            "location": "string",            "meetingId": "my_conference_id"          }        ]      }    ],    "eventType": "RoundRobin_OptimizeForAvailability",    "name": "test calendar",    "description": "this is used for testing",    "slug": "test1",    "widgetSlug": "test1",    "calendarType": "round_robin",    "widgetType": "classic",    "eventTitle": "{{contact.name}}",    "eventColor": "#039be5",    "locationConfigurations": [      {        "kind": "custom",        "location": "string",        "meetingId": "my_conference_id"      }    ],    "slotDuration": 30,    "slotDurationUnit": "mins",    "slotInterval": 30,    "slotIntervalUnit": "mins",    "slotBuffer": 0,    "slotBufferUnit": "mins",    "preBuffer": 0,    "preBufferUnit": "mins",    "appoinmentPerSlot": 1,    "appoinmentPerDay": 0,    "allowBookingAfter": 0,    "allowBookingAfterUnit": "days",    "allowBookingFor": 0,    "allowBookingForUnit": "days",    "enableRecurring": false,    "recurring": {      "freq": "DAILY",      "count": 0,      "bookingOption": "skip",      "bookingOverlapDefaultStatus": "confirmed"    },    "formId": "string",    "stickyContact": true,    "isLivePaymentMode": true,    "autoConfirm": true,    "shouldSendAlertEmailsToAssignedMember": true,    "alertEmail": "string",    "googleInvitationEmails": false,    "allowReschedule": true,    "allowCancellation": true,    "shouldAssignContactToTeamMember": true,    "shouldSkipAssigningContactForExisting": true,    "notes": "string",    "pixelId": "string",    "formSubmitType": "ThankYouMessage",    "formSubmitRedirectURL": "string",    "formSubmitThanksMessage": "string",    "guestType": "count_only",    "consentLabel": "string",    "calendarCoverImage": "https://path-to-image.com",    "lookBusyConfig": {      "enabled": true,      "LookBusyPercentage": 0    },    "id": "0TkCdp9PfvLeWKYRRvIz"  }}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L -X PUT 'https://services.leadconnectorhq.com/calendars/:calendarId' \

	-H 'Content-Type: application/json' \

	-H 'Accept: application/json' \

	-H 'Authorization: Bearer <TOKEN>' \

	-d '{

	  "groupId": "BqTwX8QFwXzpegMve9EQ",

	  "teamMembers": [

	    {

	      "userId": "ocQHyuzHvysMo5N5VsXc",

	      "priority": 0.5,

	      "isPrimary": true,

	      "locationConfigurations": [

	        {

	          "kind": "custom",

	          "location": "string"

	        }

	      ]

	    }

	  ],

	  "eventType": "RoundRobin_OptimizeForAvailability",

	  "name": "test calendar",

	  "description": "this is used for testing",

	  "slug": "test1",

	  "widgetSlug": "test1",

	  "widgetType": "classic",

	  "eventTitle": "string",

	  "eventColor": "#039be5",

	  "locationConfigurations": [

	    {

	      "kind": "custom",

	      "location": "string"

	    }

	  ],

	  "slotDuration": 30,

	  "slotDurationUnit": "mins",

	  "preBufferUnit": "mins",

	  "slotInterval": 30,

	  "slotIntervalUnit": "mins",

	  "slotBuffer": 0,

	  "preBuffer": 0,

	  "appoinmentPerSlot": 0,

	  "appoinmentPerDay": 0,

	  "allowBookingAfter": 0,

	  "allowBookingAfterUnit": "days",

	  "allowBookingFor": 0,

	  "allowBookingForUnit": "days",

	  "enableRecurring": false,

	  "recurring": {

	    "freq": "DAILY",

	    "count": 0,

	    "bookingOption": "skip",

	    "bookingOverlapDefaultStatus": "confirmed"

	  },

	  "formId": "string",

	  "stickyContact": true,

	  "isLivePaymentMode": true,

	  "autoConfirm": true,

	  "shouldSendAlertEmailsToAssignedMember": true,

	  "alertEmail": "string",

	  "googleInvitationEmails": true,

	  "allowReschedule": true,

	  "allowCancellation": true,

	  "shouldAssignContactToTeamMember": true,

	  "shouldSkipAssigningContactForExisting": true,

	  "notes": "string",

	  "pixelId": "string",

	  "formSubmitType": "ThankYouMessage",

	  "formSubmitRedirectURL": "string",

	  "formSubmitThanksMessage": "string",

	  "guestType": "count_only",

	  "consentLabel": "string",

	  "calendarCoverImage": "string",

	  "lookBusyConfig": {

	    "enabled": true,

	    "LookBusyPercentage": 0

	  },

	  "isActive": true

	}'

```

### NODEJS
#### SDK
```nodejs
	const { HighLevel } = require('@gohighlevel/api-client');

	

	const highLevel = new HighLevel({

	  clientId: 'your_client_id_here',

	  clientSecret: 'your_client_secret_here',

	});

	

	try {

	  const response = await highLevel.calendars.updateCalendar({

	    'calendarId': 'ocQHyuzHvysMo5N5VsXc'

	  },

	  {

	    'groupId': 'BqTwX8QFwXzpegMve9EQ',

	    'teamMembers': [

	      {

	        'userId': 'ocQHyuzHvysMo5N5VsXc',

	        'priority': 0.5,

	        'isPrimary': true,

	        'locationConfigurations': [

	          {

	            'kind': 'custom',

	            'location': 'string'

	          }

	        ]

	      }

	    ],

	    'eventType': 'RoundRobin_OptimizeForAvailability',

	    'name': 'test calendar',

	    'description': 'this is used for testing',

	    'slug': 'test1',

	    'widgetSlug': 'test1',

	    'widgetType': 'classic',

	    'eventTitle': 'string',

	    'eventColor': '#039be5',

	    'locationConfigurations': [

	      {

	        'kind': 'custom',

	        'location': 'string'

	      }

	    ],

	    'slotDuration': 30,

	    'slotDurationUnit': 'mins',

	    'preBufferUnit': 'mins',

	    'slotInterval': 30,

	    'slotIntervalUnit': 'mins',

	    'slotBuffer': 0,

	    'preBuffer': 0,

	    'appoinmentPerSlot': 0,

	    'appoinmentPerDay': 0,

	    'allowBookingAfter': 0,

	    'allowBookingAfterUnit': 'days',

	    'allowBookingFor': 0,

	    'allowBookingForUnit': 'days',

	    'enableRecurring': false,

	    'recurring': {

	      'freq': 'DAILY',

	      'count': 0,

	      'bookingOption': 'skip',

	      'bookingOverlapDefaultStatus': 'confirmed'

	    },

	    'formId': 'string',

	    'stickyContact': true,

	    'isLivePaymentMode': true,

	    'autoConfirm': true,

	    'shouldSendAlertEmailsToAssignedMember': true,

	    'alertEmail': 'string',

	    'googleInvitationEmails': true,

	    'allowReschedule': true,

	    'allowCancellation': true,

	    'shouldAssignContactToTeamMember': true,

	    'shouldSkipAssigningContactForExisting': true,

	    'notes': 'string',

	    'pixelId': 'string',

	    'formSubmitType': 'ThankYouMessage',

	    'formSubmitRedirectURL': 'string',

	    'formSubmitThanksMessage': 'string',

	    'guestType': 'count_only',

	    'consentLabel': 'string',

	    'calendarCoverImage': 'string',

	    'lookBusyConfig': {

	      'enabled': true,

	      'LookBusyPercentage': 0

	    },

	    'isActive': true

	  });

	  console.log(response);

	} catch (error) {

	  console.error('Error:', error);

	}

```

#### AXIOS
```nodejs
	const axios = require('axios');

	let data = JSON.stringify({

	  "groupId": "BqTwX8QFwXzpegMve9EQ",

	  "teamMembers": [

	    {

	      "userId": "ocQHyuzHvysMo5N5VsXc",

	      "priority": 0.5,

	      "isPrimary": true,

	      "locationConfigurations": [

	        {

	          "kind": "custom",

	          "location": "string"

	        }

	      ]

	    }

	  ],

	  "eventType": "RoundRobin_OptimizeForAvailability",

	  "name": "test calendar",

	  "description": "this is used for testing",

	  "slug": "test1",

	  "widgetSlug": "test1",

	  "widgetType": "classic",

	  "eventTitle": "string",

	  "eventColor": "#039be5",

	  "locationConfigurations": [

	    {

	      "kind": "custom",

	      "location": "string"

	    }

	  ],

	  "slotDuration": 30,

	  "slotDurationUnit": "mins",

	  "preBufferUnit": "mins",

	  "slotInterval": 30,

	  "slotIntervalUnit": "mins",

	  "slotBuffer": 0,

	  "preBuffer": 0,

	  "appoinmentPerSlot": 0,

	  "appoinmentPerDay": 0,

	  "allowBookingAfter": 0,

	  "allowBookingAfterUnit": "days",

	  "allowBookingFor": 0,

	  "allowBookingForUnit": "days",

	  "enableRecurring": false,

	  "recurring": {

	    "freq": "DAILY",

	    "count": 0,

	    "bookingOption": "skip",

	    "bookingOverlapDefaultStatus": "confirmed"

	  },

	  "formId": "string",

	  "stickyContact": true,

	  "isLivePaymentMode": true,

	  "autoConfirm": true,

	  "shouldSendAlertEmailsToAssignedMember": true,

	  "alertEmail": "string",

	  "googleInvitationEmails": true,

	  "allowReschedule": true,

	  "allowCancellation": true,

	  "shouldAssignContactToTeamMember": true,

	  "shouldSkipAssigningContactForExisting": true,

	  "notes": "string",

	  "pixelId": "string",

	  "formSubmitType": "ThankYouMessage",

	  "formSubmitRedirectURL": "string",

	  "formSubmitThanksMessage": "string",

	  "guestType": "count_only",

	  "consentLabel": "string",

	  "calendarCoverImage": "string",

	  "lookBusyConfig": {

	    "enabled": true,

	    "LookBusyPercentage": 0

	  },

	  "isActive": true

	});

	

	let config = {

	  method: 'put',

	  maxBodyLength: Infinity,

	  url: 'https://services.leadconnectorhq.com/calendars/:calendarId',

	  headers: { 

	    'Content-Type': 'application/json', 

	    'Accept': 'application/json', 

	    'Authorization': 'Bearer <TOKEN>'

	  },

	  data : data

	};

	

	axios.request(config)

	.then((response) => {

	  console.log(JSON.stringify(response.data));

	})

	.catch((error) => {

	  console.log(error);

	});

```

#### NATIVE
```nodejs
	var https = require('follow-redirects').https;

	var fs = require('fs');

	

	var options = {

	  'method': 'PUT',

	  'hostname': 'services.leadconnectorhq.com',

	  'path': '/calendars/:calendarId',

	  'headers': {

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  },

	  'maxRedirects': 20

	};

	

	var req = https.request(options, function (res) {

	  var chunks = [];

	

	  res.on("data", function (chunk) {

	    chunks.push(chunk);

	  });

	

	  res.on("end", function (chunk) {

	    var body = Buffer.concat(chunks);

	    console.log(body.toString());

	  });

	

	  res.on("error", function (error) {

	    console.error(error);

	  });

	});

	

	var postData = JSON.stringify({

	  "groupId": "BqTwX8QFwXzpegMve9EQ",

	  "teamMembers": [

	    {

	      "userId": "ocQHyuzHvysMo5N5VsXc",

	      "priority": 0.5,

	      "isPrimary": true,

	      "locationConfigurations": [

	        {

	          "kind": "custom",

	          "location": "string"

	        }

	      ]

	    }

	  ],

	  "eventType": "RoundRobin_OptimizeForAvailability",

	  "name": "test calendar",

	  "description": "this is used for testing",

	  "slug": "test1",

	  "widgetSlug": "test1",

	  "widgetType": "classic",

	  "eventTitle": "string",

	  "eventColor": "#039be5",

	  "locationConfigurations": [

	    {

	      "kind": "custom",

	      "location": "string"

	    }

	  ],

	  "slotDuration": 30,

	  "slotDurationUnit": "mins",

	  "preBufferUnit": "mins",

	  "slotInterval": 30,

	  "slotIntervalUnit": "mins",

	  "slotBuffer": 0,

	  "preBuffer": 0,

	  "appoinmentPerSlot": 0,

	  "appoinmentPerDay": 0,

	  "allowBookingAfter": 0,

	  "allowBookingAfterUnit": "days",

	  "allowBookingFor": 0,

	  "allowBookingForUnit": "days",

	  "enableRecurring": false,

	  "recurring": {

	    "freq": "DAILY",

	    "count": 0,

	    "bookingOption": "skip",

	    "bookingOverlapDefaultStatus": "confirmed"

	  },

	  "formId": "string",

	  "stickyContact": true,

	  "isLivePaymentMode": true,

	  "autoConfirm": true,

	  "shouldSendAlertEmailsToAssignedMember": true,

	  "alertEmail": "string",

	  "googleInvitationEmails": true,

	  "allowReschedule": true,

	  "allowCancellation": true,

	  "shouldAssignContactToTeamMember": true,

	  "shouldSkipAssigningContactForExisting": true,

	  "notes": "string",

	  "pixelId": "string",

	  "formSubmitType": "ThankYouMessage",

	  "formSubmitRedirectURL": "string",

	  "formSubmitThanksMessage": "string",

	  "guestType": "count_only",

	  "consentLabel": "string",

	  "calendarCoverImage": "string",

	  "lookBusyConfig": {

	    "enabled": true,

	    "LookBusyPercentage": 0

	  },

	  "isActive": true

	});

	

	req.write(postData);

	

	req.end();

```

#### REQUEST
```nodejs
	var request = require('request');

	var options = {

	  'method': 'PUT',

	  'url': 'https://services.leadconnectorhq.com/calendars/:calendarId',

	  'headers': {

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  },

	  body: JSON.stringify({

	    "groupId": "BqTwX8QFwXzpegMve9EQ",

	    "teamMembers": [

	      {

	        "userId": "ocQHyuzHvysMo5N5VsXc",

	        "priority": 0.5,

	        "isPrimary": true,

	        "locationConfigurations": [

	          {

	            "kind": "custom",

	            "location": "string"

	          }

	        ]

	      }

	    ],

	    "eventType": "RoundRobin_OptimizeForAvailability",

	    "name": "test calendar",

	    "description": "this is used for testing",

	    "slug": "test1",

	    "widgetSlug": "test1",

	    "widgetType": "classic",

	    "eventTitle": "string",

	    "eventColor": "#039be5",

	    "locationConfigurations": [

	      {

	        "kind": "custom",

	        "location": "string"

	      }

	    ],

	    "slotDuration": 30,

	    "slotDurationUnit": "mins",

	    "preBufferUnit": "mins",

	    "slotInterval": 30,

	    "slotIntervalUnit": "mins",

	    "slotBuffer": 0,

	    "preBuffer": 0,

	    "appoinmentPerSlot": 0,

	    "appoinmentPerDay": 0,

	    "allowBookingAfter": 0,

	    "allowBookingAfterUnit": "days",

	    "allowBookingFor": 0,

	    "allowBookingForUnit": "days",

	    "enableRecurring": false,

	    "recurring": {

	      "freq": "DAILY",

	      "count": 0,

	      "bookingOption": "skip",

	      "bookingOverlapDefaultStatus": "confirmed"

	    },

	    "formId": "string",

	    "stickyContact": true,

	    "isLivePaymentMode": true,

	    "autoConfirm": true,

	    "shouldSendAlertEmailsToAssignedMember": true,

	    "alertEmail": "string",

	    "googleInvitationEmails": true,

	    "allowReschedule": true,

	    "allowCancellation": true,

	    "shouldAssignContactToTeamMember": true,

	    "shouldSkipAssigningContactForExisting": true,

	    "notes": "string",

	    "pixelId": "string",

	    "formSubmitType": "ThankYouMessage",

	    "formSubmitRedirectURL": "string",

	    "formSubmitThanksMessage": "string",

	    "guestType": "count_only",

	    "consentLabel": "string",

	    "calendarCoverImage": "string",

	    "lookBusyConfig": {

	      "enabled": true,

	      "LookBusyPercentage": 0

	    },

	    "isActive": true

	  })

	

	};

	request(options, function (error, response) {

	  if (error) throw new Error(error);

	  console.log(response.body);

	});

```

#### UNIREST
```nodejs
	var unirest = require('unirest');

	var req = unirest('PUT', 'https://services.leadconnectorhq.com/calendars/:calendarId')

	  .headers({

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  })

	  .send(JSON.stringify({

	    "groupId": "BqTwX8QFwXzpegMve9EQ",

	    "teamMembers": [

	      {

	        "userId": "ocQHyuzHvysMo5N5VsXc",

	        "priority": 0.5,

	        "isPrimary": true,

	        "locationConfigurations": [

	          {

	            "kind": "custom",

	            "location": "string"

	          }

	        ]

	      }

	    ],

	    "eventType": "RoundRobin_OptimizeForAvailability",

	    "name": "test calendar",

	    "description": "this is used for testing",

	    "slug": "test1",

	    "widgetSlug": "test1",

	    "widgetType": "classic",

	    "eventTitle": "string",

	    "eventColor": "#039be5",

	    "locationConfigurations": [

	      {

	        "kind": "custom",

	        "location": "string"

	      }

	    ],

	    "slotDuration": 30,

	    "slotDurationUnit": "mins",

	    "preBufferUnit": "mins",

	    "slotInterval": 30,

	    "slotIntervalUnit": "mins",

	    "slotBuffer": 0,

	    "preBuffer": 0,

	    "appoinmentPerSlot": 0,

	    "appoinmentPerDay": 0,

	    "allowBookingAfter": 0,

	    "allowBookingAfterUnit": "days",

	    "allowBookingFor": 0,

	    "allowBookingForUnit": "days",

	    "enableRecurring": false,

	    "recurring": {

	      "freq": "DAILY",

	      "count": 0,

	      "bookingOption": "skip",

	      "bookingOverlapDefaultStatus": "confirmed"

	    },

	    "formId": "string",

	    "stickyContact": true,

	    "isLivePaymentMode": true,

	    "autoConfirm": true,

	    "shouldSendAlertEmailsToAssignedMember": true,

	    "alertEmail": "string",

	    "googleInvitationEmails": true,

	    "allowReschedule": true,

	    "allowCancellation": true,

	    "shouldAssignContactToTeamMember": true,

	    "shouldSkipAssigningContactForExisting": true,

	    "notes": "string",

	    "pixelId": "string",

	    "formSubmitType": "ThankYouMessage",

	    "formSubmitRedirectURL": "string",

	    "formSubmitThanksMessage": "string",

	    "guestType": "count_only",

	    "consentLabel": "string",

	    "calendarCoverImage": "string",

	    "lookBusyConfig": {

	      "enabled": true,

	      "LookBusyPercentage": 0

	    },

	    "isActive": true

	  }))

	  .end(function (res) { 

	    if (res.error) throw new Error(res.error); 

	    console.log(res.raw_body);

	  });

```

### PYTHON
#### HTTP.CLIENT
```python
	import http.client

	import json

	

	conn = http.client.HTTPSConnection("services.leadconnectorhq.com")

	payload = json.dumps({

	  "groupId": "BqTwX8QFwXzpegMve9EQ",

	  "teamMembers": [

	    {

	      "userId": "ocQHyuzHvysMo5N5VsXc",

	      "priority": 0.5,

	      "isPrimary": True,

	      "locationConfigurations": [

	        {

	          "kind": "custom",

	          "location": "string"

	        }

	      ]

	    }

	  ],

	  "eventType": "RoundRobin_OptimizeForAvailability",

	  "name": "test calendar",

	  "description": "this is used for testing",

	  "slug": "test1",

	  "widgetSlug": "test1",

	  "widgetType": "classic",

	  "eventTitle": "string",

	  "eventColor": "#039be5",

	  "locationConfigurations": [

	    {

	      "kind": "custom",

	      "location": "string"

	    }

	  ],

	  "slotDuration": 30,

	  "slotDurationUnit": "mins",

	  "preBufferUnit": "mins",

	  "slotInterval": 30,

	  "slotIntervalUnit": "mins",

	  "slotBuffer": 0,

	  "preBuffer": 0,

	  "appoinmentPerSlot": 0,

	  "appoinmentPerDay": 0,

	  "allowBookingAfter": 0,

	  "allowBookingAfterUnit": "days",

	  "allowBookingFor": 0,

	  "allowBookingForUnit": "days",

	  "enableRecurring": False,

	  "recurring": {

	    "freq": "DAILY",

	    "count": 0,

	    "bookingOption": "skip",

	    "bookingOverlapDefaultStatus": "confirmed"

	  },

	  "formId": "string",

	  "stickyContact": True,

	  "isLivePaymentMode": True,

	  "autoConfirm": True,

	  "shouldSendAlertEmailsToAssignedMember": True,

	  "alertEmail": "string",

	  "googleInvitationEmails": True,

	  "allowReschedule": True,

	  "allowCancellation": True,

	  "shouldAssignContactToTeamMember": True,

	  "shouldSkipAssigningContactForExisting": True,

	  "notes": "string",

	  "pixelId": "string",

	  "formSubmitType": "ThankYouMessage",

	  "formSubmitRedirectURL": "string",

	  "formSubmitThanksMessage": "string",

	  "guestType": "count_only",

	  "consentLabel": "string",

	  "calendarCoverImage": "string",

	  "lookBusyConfig": {

	    "enabled": True,

	    "LookBusyPercentage": 0

	  },

	  "isActive": True

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json',

	  'Authorization': 'Bearer <TOKEN>'

	}

	conn.request("PUT", "/calendars/:calendarId", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	import json

	

	url = "https://services.leadconnectorhq.com/calendars/:calendarId"

	

	payload = json.dumps({

	  "groupId": "BqTwX8QFwXzpegMve9EQ",

	  "teamMembers": [

	    {

	      "userId": "ocQHyuzHvysMo5N5VsXc",

	      "priority": 0.5,

	      "isPrimary": True,

	      "locationConfigurations": [

	        {

	          "kind": "custom",

	          "location": "string"

	        }

	      ]

	    }

	  ],

	  "eventType": "RoundRobin_OptimizeForAvailability",

	  "name": "test calendar",

	  "description": "this is used for testing",

	  "slug": "test1",

	  "widgetSlug": "test1",

	  "widgetType": "classic",

	  "eventTitle": "string",

	  "eventColor": "#039be5",

	  "locationConfigurations": [

	    {

	      "kind": "custom",

	      "location": "string"

	    }

	  ],

	  "slotDuration": 30,

	  "slotDurationUnit": "mins",

	  "preBufferUnit": "mins",

	  "slotInterval": 30,

	  "slotIntervalUnit": "mins",

	  "slotBuffer": 0,

	  "preBuffer": 0,

	  "appoinmentPerSlot": 0,

	  "appoinmentPerDay": 0,

	  "allowBookingAfter": 0,

	  "allowBookingAfterUnit": "days",

	  "allowBookingFor": 0,

	  "allowBookingForUnit": "days",

	  "enableRecurring": False,

	  "recurring": {

	    "freq": "DAILY",

	    "count": 0,

	    "bookingOption": "skip",

	    "bookingOverlapDefaultStatus": "confirmed"

	  },

	  "formId": "string",

	  "stickyContact": True,

	  "isLivePaymentMode": True,

	  "autoConfirm": True,

	  "shouldSendAlertEmailsToAssignedMember": True,

	  "alertEmail": "string",

	  "googleInvitationEmails": True,

	  "allowReschedule": True,

	  "allowCancellation": True,

	  "shouldAssignContactToTeamMember": True,

	  "shouldSkipAssigningContactForExisting": True,

	  "notes": "string",

	  "pixelId": "string",

	  "formSubmitType": "ThankYouMessage",

	  "formSubmitRedirectURL": "string",

	  "formSubmitThanksMessage": "string",

	  "guestType": "count_only",

	  "consentLabel": "string",

	  "calendarCoverImage": "string",

	  "lookBusyConfig": {

	    "enabled": True,

	    "LookBusyPercentage": 0

	  },

	  "isActive": True

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json',

	  'Authorization': 'Bearer <TOKEN>'

	}

	

	response = requests.request("PUT", url, headers=headers, data=payload)

	

	print(response.text)

```

### PHP
#### CURL
```php
	<?php

	

	$curl = curl_init();

	

	curl_setopt_array($curl, array(

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/calendars/:calendarId',

	  CURLOPT_RETURNTRANSFER => true,

	  CURLOPT_ENCODING => '',

	  CURLOPT_MAXREDIRS => 10,

	  CURLOPT_TIMEOUT => 0,

	  CURLOPT_FOLLOWLOCATION => true,

	  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,

	  CURLOPT_CUSTOMREQUEST => 'PUT',

	  CURLOPT_POSTFIELDS =>'{

	  "groupId": "BqTwX8QFwXzpegMve9EQ",

	  "teamMembers": [

	    {

	      "userId": "ocQHyuzHvysMo5N5VsXc",

	      "priority": 0.5,

	      "isPrimary": true,

	      "locationConfigurations": [

	        {

	          "kind": "custom",

	          "location": "string"

	        }

	      ]

	    }

	  ],

	  "eventType": "RoundRobin_OptimizeForAvailability",

	  "name": "test calendar",

	  "description": "this is used for testing",

	  "slug": "test1",

	  "widgetSlug": "test1",

	  "widgetType": "classic",

	  "eventTitle": "string",

	  "eventColor": "#039be5",

	  "locationConfigurations": [

	    {

	      "kind": "custom",

	      "location": "string"

	    }

	  ],

	  "slotDuration": 30,

	  "slotDurationUnit": "mins",

	  "preBufferUnit": "mins",

	  "slotInterval": 30,

	  "slotIntervalUnit": "mins",

	  "slotBuffer": 0,

	  "preBuffer": 0,

	  "appoinmentPerSlot": 0,

	  "appoinmentPerDay": 0,

	  "allowBookingAfter": 0,

	  "allowBookingAfterUnit": "days",

	  "allowBookingFor": 0,

	  "allowBookingForUnit": "days",

	  "enableRecurring": false,

	  "recurring": {

	    "freq": "DAILY",

	    "count": 0,

	    "bookingOption": "skip",

	    "bookingOverlapDefaultStatus": "confirmed"

	  },

	  "formId": "string",

	  "stickyContact": true,

	  "isLivePaymentMode": true,

	  "autoConfirm": true,

	  "shouldSendAlertEmailsToAssignedMember": true,

	  "alertEmail": "string",

	  "googleInvitationEmails": true,

	  "allowReschedule": true,

	  "allowCancellation": true,

	  "shouldAssignContactToTeamMember": true,

	  "shouldSkipAssigningContactForExisting": true,

	  "notes": "string",

	  "pixelId": "string",

	  "formSubmitType": "ThankYouMessage",

	  "formSubmitRedirectURL": "string",

	  "formSubmitThanksMessage": "string",

	  "guestType": "count_only",

	  "consentLabel": "string",

	  "calendarCoverImage": "string",

	  "lookBusyConfig": {

	    "enabled": true,

	    "LookBusyPercentage": 0

	  },

	  "isActive": true

	}',

	  CURLOPT_HTTPHEADER => array(

	    'Content-Type: application/json',

	    'Accept: application/json',

	    'Authorization: Bearer <TOKEN>'

	  ),

	));

	

	$response = curl_exec($curl);

	

	curl_close($curl);

	echo $response;

```

#### GUZZLE
```php
	<?php

	$client = new Client();

	$headers = [

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json',

	  'Authorization' => 'Bearer <TOKEN>'

	];

	$body = '{

	  "groupId": "BqTwX8QFwXzpegMve9EQ",

	  "teamMembers": [

	    {

	      "userId": "ocQHyuzHvysMo5N5VsXc",

	      "priority": 0.5,

	      "isPrimary": true,

	      "locationConfigurations": [

	        {

	          "kind": "custom",

	          "location": "string"

	        }

	      ]

	    }

	  ],

	  "eventType": "RoundRobin_OptimizeForAvailability",

	  "name": "test calendar",

	  "description": "this is used for testing",

	  "slug": "test1",

	  "widgetSlug": "test1",

	  "widgetType": "classic",

	  "eventTitle": "string",

	  "eventColor": "#039be5",

	  "locationConfigurations": [

	    {

	      "kind": "custom",

	      "location": "string"

	    }

	  ],

	  "slotDuration": 30,

	  "slotDurationUnit": "mins",

	  "preBufferUnit": "mins",

	  "slotInterval": 30,

	  "slotIntervalUnit": "mins",

	  "slotBuffer": 0,

	  "preBuffer": 0,

	  "appoinmentPerSlot": 0,

	  "appoinmentPerDay": 0,

	  "allowBookingAfter": 0,

	  "allowBookingAfterUnit": "days",

	  "allowBookingFor": 0,

	  "allowBookingForUnit": "days",

	  "enableRecurring": false,

	  "recurring": {

	    "freq": "DAILY",

	    "count": 0,

	    "bookingOption": "skip",

	    "bookingOverlapDefaultStatus": "confirmed"

	  },

	  "formId": "string",

	  "stickyContact": true,

	  "isLivePaymentMode": true,

	  "autoConfirm": true,

	  "shouldSendAlertEmailsToAssignedMember": true,

	  "alertEmail": "string",

	  "googleInvitationEmails": true,

	  "allowReschedule": true,

	  "allowCancellation": true,

	  "shouldAssignContactToTeamMember": true,

	  "shouldSkipAssigningContactForExisting": true,

	  "notes": "string",

	  "pixelId": "string",

	  "formSubmitType": "ThankYouMessage",

	  "formSubmitRedirectURL": "string",

	  "formSubmitThanksMessage": "string",

	  "guestType": "count_only",

	  "consentLabel": "string",

	  "calendarCoverImage": "string",

	  "lookBusyConfig": {

	    "enabled": true,

	    "LookBusyPercentage": 0

	  },

	  "isActive": true

	}';

	$request = new Request('PUT', 'https://services.leadconnectorhq.com/calendars/:calendarId', $headers, $body);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/calendars/:calendarId');

	$request->setMethod(HTTP_Request2::METHOD_PUT);

	$request->setConfig(array(

	  'follow_redirects' => TRUE

	));

	$request->setHeader(array(

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json',

	  'Authorization' => 'Bearer <TOKEN>'

	));

	$request->setBody('{\n  "groupId": "BqTwX8QFwXzpegMve9EQ",\n  "teamMembers": [\n    {\n      "userId": "ocQHyuzHvysMo5N5VsXc",\n      "priority": 0.5,\n      "isPrimary": true,\n      "locationConfigurations": [\n        {\n          "kind": "custom",\n          "location": "string"\n        }\n      ]\n    }\n  ],\n  "eventType": "RoundRobin_OptimizeForAvailability",\n  "name": "test calendar",\n  "description": "this is used for testing",\n  "slug": "test1",\n  "widgetSlug": "test1",\n  "widgetType": "classic",\n  "eventTitle": "string",\n  "eventColor": "#039be5",\n  "locationConfigurations": [\n    {\n      "kind": "custom",\n      "location": "string"\n    }\n  ],\n  "slotDuration": 30,\n  "slotDurationUnit": "mins",\n  "preBufferUnit": "mins",\n  "slotInterval": 30,\n  "slotIntervalUnit": "mins",\n  "slotBuffer": 0,\n  "preBuffer": 0,\n  "appoinmentPerSlot": 0,\n  "appoinmentPerDay": 0,\n  "allowBookingAfter": 0,\n  "allowBookingAfterUnit": "days",\n  "allowBookingFor": 0,\n  "allowBookingForUnit": "days",\n  "enableRecurring": false,\n  "recurring": {\n    "freq": "DAILY",\n    "count": 0,\n    "bookingOption": "skip",\n    "bookingOverlapDefaultStatus": "confirmed"\n  },\n  "formId": "string",\n  "stickyContact": true,\n  "isLivePaymentMode": true,\n  "autoConfirm": true,\n  "shouldSendAlertEmailsToAssignedMember": true,\n  "alertEmail": "string",\n  "googleInvitationEmails": true,\n  "allowReschedule": true,\n  "allowCancellation": true,\n  "shouldAssignContactToTeamMember": true,\n  "shouldSkipAssigningContactForExisting": true,\n  "notes": "string",\n  "pixelId": "string",\n  "formSubmitType": "ThankYouMessage",\n  "formSubmitRedirectURL": "string",\n  "formSubmitThanksMessage": "string",\n  "guestType": "count_only",\n  "consentLabel": "string",\n  "calendarCoverImage": "string",\n  "lookBusyConfig": {\n    "enabled": true,\n    "LookBusyPercentage": 0\n  },\n  "isActive": true\n}');

	try {

	  $response = $request->send();

	  if ($response->getStatus() == 200) {

	    echo $response->getBody();

	  }

	  else {

	    echo 'Unexpected HTTP status: ' . $response->getStatus() . ' ' .

	    $response->getReasonPhrase();

	  }

	}

	catch(HTTP_Request2_Exception $e) {

	  echo 'Error: ' . $e->getMessage();

	}

```

#### PECL_HTTP
```php
	<?php

	$client = new http\Client;

	$request = new http\Client\Request;

	$request->setRequestUrl('https://services.leadconnectorhq.com/calendars/:calendarId');

	$request->setRequestMethod('PUT');

	$body = new http\Message\Body;

	$body->append('{

	  "groupId": "BqTwX8QFwXzpegMve9EQ",

	  "teamMembers": [

	    {

	      "userId": "ocQHyuzHvysMo5N5VsXc",

	      "priority": 0.5,

	      "isPrimary": true,

	      "locationConfigurations": [

	        {

	          "kind": "custom",

	          "location": "string"

	        }

	      ]

	    }

	  ],

	  "eventType": "RoundRobin_OptimizeForAvailability",

	  "name": "test calendar",

	  "description": "this is used for testing",

	  "slug": "test1",

	  "widgetSlug": "test1",

	  "widgetType": "classic",

	  "eventTitle": "string",

	  "eventColor": "#039be5",

	  "locationConfigurations": [

	    {

	      "kind": "custom",

	      "location": "string"

	    }

	  ],

	  "slotDuration": 30,

	  "slotDurationUnit": "mins",

	  "preBufferUnit": "mins",

	  "slotInterval": 30,

	  "slotIntervalUnit": "mins",

	  "slotBuffer": 0,

	  "preBuffer": 0,

	  "appoinmentPerSlot": 0,

	  "appoinmentPerDay": 0,

	  "allowBookingAfter": 0,

	  "allowBookingAfterUnit": "days",

	  "allowBookingFor": 0,

	  "allowBookingForUnit": "days",

	  "enableRecurring": false,

	  "recurring": {

	    "freq": "DAILY",

	    "count": 0,

	    "bookingOption": "skip",

	    "bookingOverlapDefaultStatus": "confirmed"

	  },

	  "formId": "string",

	  "stickyContact": true,

	  "isLivePaymentMode": true,

	  "autoConfirm": true,

	  "shouldSendAlertEmailsToAssignedMember": true,

	  "alertEmail": "string",

	  "googleInvitationEmails": true,

	  "allowReschedule": true,

	  "allowCancellation": true,

	  "shouldAssignContactToTeamMember": true,

	  "shouldSkipAssigningContactForExisting": true,

	  "notes": "string",

	  "pixelId": "string",

	  "formSubmitType": "ThankYouMessage",

	  "formSubmitRedirectURL": "string",

	  "formSubmitThanksMessage": "string",

	  "guestType": "count_only",

	  "consentLabel": "string",

	  "calendarCoverImage": "string",

	  "lookBusyConfig": {

	    "enabled": true,

	    "LookBusyPercentage": 0

	  },

	  "isActive": true

	}');

	$request->setBody($body);

	$request->setOptions(array());

	$request->setHeaders(array(

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json',

	  'Authorization' => 'Bearer <TOKEN>'

	));

	$client->enqueue($request)->send();

	$response = $client->getResponse();

	echo $response->getBody();

```

### JAVA
#### OKHTTP
```java
	OkHttpClient client = new OkHttpClient().newBuilder()

	  .build();

	MediaType mediaType = MediaType.parse("application/json");

	RequestBody body = RequestBody.create(mediaType, "{\n  \"groupId\": \"BqTwX8QFwXzpegMve9EQ\",\n  \"teamMembers\": [\n    {\n      \"userId\": \"ocQHyuzHvysMo5N5VsXc\",\n      \"priority\": 0.5,\n      \"isPrimary\": true,\n      \"locationConfigurations\": [\n        {\n          \"kind\": \"custom\",\n          \"location\": \"string\"\n        }\n      ]\n    }\n  ],\n  \"eventType\": \"RoundRobin_OptimizeForAvailability\",\n  \"name\": \"test calendar\",\n  \"description\": \"this is used for testing\",\n  \"slug\": \"test1\",\n  \"widgetSlug\": \"test1\",\n  \"widgetType\": \"classic\",\n  \"eventTitle\": \"string\",\n  \"eventColor\": \"#039be5\",\n  \"locationConfigurations\": [\n    {\n      \"kind\": \"custom\",\n      \"location\": \"string\"\n    }\n  ],\n  \"slotDuration\": 30,\n  \"slotDurationUnit\": \"mins\",\n  \"preBufferUnit\": \"mins\",\n  \"slotInterval\": 30,\n  \"slotIntervalUnit\": \"mins\",\n  \"slotBuffer\": 0,\n  \"preBuffer\": 0,\n  \"appoinmentPerSlot\": 0,\n  \"appoinmentPerDay\": 0,\n  \"allowBookingAfter\": 0,\n  \"allowBookingAfterUnit\": \"days\",\n  \"allowBookingFor\": 0,\n  \"allowBookingForUnit\": \"days\",\n  \"enableRecurring\": false,\n  \"recurring\": {\n    \"freq\": \"DAILY\",\n    \"count\": 0,\n    \"bookingOption\": \"skip\",\n    \"bookingOverlapDefaultStatus\": \"confirmed\"\n  },\n  \"formId\": \"string\",\n  \"stickyContact\": true,\n  \"isLivePaymentMode\": true,\n  \"autoConfirm\": true,\n  \"shouldSendAlertEmailsToAssignedMember\": true,\n  \"alertEmail\": \"string\",\n  \"googleInvitationEmails\": true,\n  \"allowReschedule\": true,\n  \"allowCancellation\": true,\n  \"shouldAssignContactToTeamMember\": true,\n  \"shouldSkipAssigningContactForExisting\": true,\n  \"notes\": \"string\",\n  \"pixelId\": \"string\",\n  \"formSubmitType\": \"ThankYouMessage\",\n  \"formSubmitRedirectURL\": \"string\",\n  \"formSubmitThanksMessage\": \"string\",\n  \"guestType\": \"count_only\",\n  \"consentLabel\": \"string\",\n  \"calendarCoverImage\": \"string\",\n  \"lookBusyConfig\": {\n    \"enabled\": true,\n    \"LookBusyPercentage\": 0\n  },\n  \"isActive\": true\n}");

	Request request = new Request.Builder()

	  .url("https://services.leadconnectorhq.com/calendars/:calendarId")

	  .method("PUT", body)

	  .addHeader("Content-Type", "application/json")

	  .addHeader("Accept", "application/json")

	  .addHeader("Authorization", "Bearer <TOKEN>")

	  .build();

	Response response = client.newCall(request).execute();

```

#### UNIREST
```java
	Unirest.setTimeouts(0, 0);

	HttpResponse<String> response = Unirest.put("https://services.leadconnectorhq.com/calendars/:calendarId")

	  .header("Content-Type", "application/json")

	  .header("Accept", "application/json")

	  .header("Authorization", "Bearer <TOKEN>")

	  .body("{\n  \"groupId\": \"BqTwX8QFwXzpegMve9EQ\",\n  \"teamMembers\": [\n    {\n      \"userId\": \"ocQHyuzHvysMo5N5VsXc\",\n      \"priority\": 0.5,\n      \"isPrimary\": true,\n      \"locationConfigurations\": [\n        {\n          \"kind\": \"custom\",\n          \"location\": \"string\"\n        }\n      ]\n    }\n  ],\n  \"eventType\": \"RoundRobin_OptimizeForAvailability\",\n  \"name\": \"test calendar\",\n  \"description\": \"this is used for testing\",\n  \"slug\": \"test1\",\n  \"widgetSlug\": \"test1\",\n  \"widgetType\": \"classic\",\n  \"eventTitle\": \"string\",\n  \"eventColor\": \"#039be5\",\n  \"locationConfigurations\": [\n    {\n      \"kind\": \"custom\",\n      \"location\": \"string\"\n    }\n  ],\n  \"slotDuration\": 30,\n  \"slotDurationUnit\": \"mins\",\n  \"preBufferUnit\": \"mins\",\n  \"slotInterval\": 30,\n  \"slotIntervalUnit\": \"mins\",\n  \"slotBuffer\": 0,\n  \"preBuffer\": 0,\n  \"appoinmentPerSlot\": 0,\n  \"appoinmentPerDay\": 0,\n  \"allowBookingAfter\": 0,\n  \"allowBookingAfterUnit\": \"days\",\n  \"allowBookingFor\": 0,\n  \"allowBookingForUnit\": \"days\",\n  \"enableRecurring\": false,\n  \"recurring\": {\n    \"freq\": \"DAILY\",\n    \"count\": 0,\n    \"bookingOption\": \"skip\",\n    \"bookingOverlapDefaultStatus\": \"confirmed\"\n  },\n  \"formId\": \"string\",\n  \"stickyContact\": true,\n  \"isLivePaymentMode\": true,\n  \"autoConfirm\": true,\n  \"shouldSendAlertEmailsToAssignedMember\": true,\n  \"alertEmail\": \"string\",\n  \"googleInvitationEmails\": true,\n  \"allowReschedule\": true,\n  \"allowCancellation\": true,\n  \"shouldAssignContactToTeamMember\": true,\n  \"shouldSkipAssigningContactForExisting\": true,\n  \"notes\": \"string\",\n  \"pixelId\": \"string\",\n  \"formSubmitType\": \"ThankYouMessage\",\n  \"formSubmitRedirectURL\": \"string\",\n  \"formSubmitThanksMessage\": \"string\",\n  \"guestType\": \"count_only\",\n  \"consentLabel\": \"string\",\n  \"calendarCoverImage\": \"string\",\n  \"lookBusyConfig\": {\n    \"enabled\": true,\n    \"LookBusyPercentage\": 0\n  },\n  \"isActive\": true\n}")

	  .asString();

```

### GO
#### NATIVE
```go
	package main

	

	import (

	  "fmt"

	  "strings"

	  "net/http"

	  "io"

	)

	

	func main() {

	

	  url := "https://services.leadconnectorhq.com/calendars/:calendarId"

	  method := "PUT"

	

	  payload := strings.NewReader(`{

	  "groupId": "BqTwX8QFwXzpegMve9EQ",

	  "teamMembers": [

	    {

	      "userId": "ocQHyuzHvysMo5N5VsXc",

	      "priority": 0.5,

	      "isPrimary": true,

	      "locationConfigurations": [

	        {

	          "kind": "custom",

	          "location": "string"

	        }

	      ]

	    }

	  ],

	  "eventType": "RoundRobin_OptimizeForAvailability",

	  "name": "test calendar",

	  "description": "this is used for testing",

	  "slug": "test1",

	  "widgetSlug": "test1",

	  "widgetType": "classic",

	  "eventTitle": "string",

	  "eventColor": "#039be5",

	  "locationConfigurations": [

	    {

	      "kind": "custom",

	      "location": "string"

	    }

	  ],

	  "slotDuration": 30,

	  "slotDurationUnit": "mins",

	  "preBufferUnit": "mins",

	  "slotInterval": 30,

	  "slotIntervalUnit": "mins",

	  "slotBuffer": 0,

	  "preBuffer": 0,

	  "appoinmentPerSlot": 0,

	  "appoinmentPerDay": 0,

	  "allowBookingAfter": 0,

	  "allowBookingAfterUnit": "days",

	  "allowBookingFor": 0,

	  "allowBookingForUnit": "days",

	  "enableRecurring": false,

	  "recurring": {

	    "freq": "DAILY",

	    "count": 0,

	    "bookingOption": "skip",

	    "bookingOverlapDefaultStatus": "confirmed"

	  },

	  "formId": "string",

	  "stickyContact": true,

	  "isLivePaymentMode": true,

	  "autoConfirm": true,

	  "shouldSendAlertEmailsToAssignedMember": true,

	  "alertEmail": "string",

	  "googleInvitationEmails": true,

	  "allowReschedule": true,

	  "allowCancellation": true,

	  "shouldAssignContactToTeamMember": true,

	  "shouldSkipAssigningContactForExisting": true,

	  "notes": "string",

	  "pixelId": "string",

	  "formSubmitType": "ThankYouMessage",

	  "formSubmitRedirectURL": "string",

	  "formSubmitThanksMessage": "string",

	  "guestType": "count_only",

	  "consentLabel": "string",

	  "calendarCoverImage": "string",

	  "lookBusyConfig": {

	    "enabled": true,

	    "LookBusyPercentage": 0

	  },

	  "isActive": true

	}`)

	

	  client := &http.Client {

	  }

	  req, err := http.NewRequest(method, url, payload)

	

	  if err != nil {

	    fmt.Println(err)

	    return

	  }

	  req.Header.Add("Content-Type", "application/json")

	  req.Header.Add("Accept", "application/json")

	  req.Header.Add("Authorization", "Bearer <TOKEN>")

	

	  res, err := client.Do(req)

	  if err != nil {

	    fmt.Println(err)

	    return

	  }

	  defer res.Body.Close()

	

	  body, err := io.ReadAll(res.Body)

	  if err != nil {

	    fmt.Println(err)

	    return

	  }

	  fmt.Println(string(body))

	}

```

### RUBY
#### NET::HTTP
```ruby
	require "uri"

	require "json"

	require "net/http"

	

	url = URI("https://services.leadconnectorhq.com/calendars/:calendarId")

	

	https = Net::HTTP.new(url.host, url.port)

	https.use_ssl = true

	

	request = Net::HTTP::Put.new(url)

	request["Content-Type"] = "application/json"

	request["Accept"] = "application/json"

	request["Authorization"] = "Bearer <TOKEN>"

	request.body = JSON.dump({

	  "groupId": "BqTwX8QFwXzpegMve9EQ",

	  "teamMembers": [

	    {

	      "userId": "ocQHyuzHvysMo5N5VsXc",

	      "priority": 0.5,

	      "isPrimary": true,

	      "locationConfigurations": [

	        {

	          "kind": "custom",

	          "location": "string"

	        }

	      ]

	    }

	  ],

	  "eventType": "RoundRobin_OptimizeForAvailability",

	  "name": "test calendar",

	  "description": "this is used for testing",

	  "slug": "test1",

	  "widgetSlug": "test1",

	  "widgetType": "classic",

	  "eventTitle": "string",

	  "eventColor": "\#039be5",

	  "locationConfigurations": [

	    {

	      "kind": "custom",

	      "location": "string"

	    }

	  ],

	  "slotDuration": 30,

	  "slotDurationUnit": "mins",

	  "preBufferUnit": "mins",

	  "slotInterval": 30,

	  "slotIntervalUnit": "mins",

	  "slotBuffer": 0,

	  "preBuffer": 0,

	  "appoinmentPerSlot": 0,

	  "appoinmentPerDay": 0,

	  "allowBookingAfter": 0,

	  "allowBookingAfterUnit": "days",

	  "allowBookingFor": 0,

	  "allowBookingForUnit": "days",

	  "enableRecurring": false,

	  "recurring": {

	    "freq": "DAILY",

	    "count": 0,

	    "bookingOption": "skip",

	    "bookingOverlapDefaultStatus": "confirmed"

	  },

	  "formId": "string",

	  "stickyContact": true,

	  "isLivePaymentMode": true,

	  "autoConfirm": true,

	  "shouldSendAlertEmailsToAssignedMember": true,

	  "alertEmail": "string",

	  "googleInvitationEmails": true,

	  "allowReschedule": true,

	  "allowCancellation": true,

	  "shouldAssignContactToTeamMember": true,

	  "shouldSkipAssigningContactForExisting": true,

	  "notes": "string",

	  "pixelId": "string",

	  "formSubmitType": "ThankYouMessage",

	  "formSubmitRedirectURL": "string",

	  "formSubmitThanksMessage": "string",

	  "guestType": "count_only",

	  "consentLabel": "string",

	  "calendarCoverImage": "string",

	  "lookBusyConfig": {

	    "enabled": true,

	    "LookBusyPercentage": 0

	  },

	  "isActive": true

	})

	

	response = https.request(request)

	puts response.read_body

```

### POWERSHELL
#### RESTMETHOD
```powershell
	$headers = New-Object "System.Collections.Generic.Dictionary[[String],[String]]"

	$headers.Add("Content-Type", "application/json")

	$headers.Add("Accept", "application/json")

	$headers.Add("Authorization", "Bearer <TOKEN>")

	

	$body = @"

	{

	  `"groupId`": `"BqTwX8QFwXzpegMve9EQ`",

	  `"teamMembers`": [

	    {

	      `"userId`": `"ocQHyuzHvysMo5N5VsXc`",

	      `"priority`": 0.5,

	      `"isPrimary`": true,

	      `"locationConfigurations`": [

	        {

	          `"kind`": `"custom`",

	          `"location`": `"string`"

	        }

	      ]

	    }

	  ],

	  `"eventType`": `"RoundRobin_OptimizeForAvailability`",

	  `"name`": `"test calendar`",

	  `"description`": `"this is used for testing`",

	  `"slug`": `"test1`",

	  `"widgetSlug`": `"test1`",

	  `"widgetType`": `"classic`",

	  `"eventTitle`": `"string`",

	  `"eventColor`": `"#039be5`",

	  `"locationConfigurations`": [

	    {

	      `"kind`": `"custom`",

	      `"location`": `"string`"

	    }

	  ],

	  `"slotDuration`": 30,

	  `"slotDurationUnit`": `"mins`",

	  `"preBufferUnit`": `"mins`",

	  `"slotInterval`": 30,

	  `"slotIntervalUnit`": `"mins`",

	  `"slotBuffer`": 0,

	  `"preBuffer`": 0,

	  `"appoinmentPerSlot`": 0,

	  `"appoinmentPerDay`": 0,

	  `"allowBookingAfter`": 0,

	  `"allowBookingAfterUnit`": `"days`",

	  `"allowBookingFor`": 0,

	  `"allowBookingForUnit`": `"days`",

	  `"enableRecurring`": false,

	  `"recurring`": {

	    `"freq`": `"DAILY`",

	    `"count`": 0,

	    `"bookingOption`": `"skip`",

	    `"bookingOverlapDefaultStatus`": `"confirmed`"

	  },

	  `"formId`": `"string`",

	  `"stickyContact`": true,

	  `"isLivePaymentMode`": true,

	  `"autoConfirm`": true,

	  `"shouldSendAlertEmailsToAssignedMember`": true,

	  `"alertEmail`": `"string`",

	  `"googleInvitationEmails`": true,

	  `"allowReschedule`": true,

	  `"allowCancellation`": true,

	  `"shouldAssignContactToTeamMember`": true,

	  `"shouldSkipAssigningContactForExisting`": true,

	  `"notes`": `"string`",

	  `"pixelId`": `"string`",

	  `"formSubmitType`": `"ThankYouMessage`",

	  `"formSubmitRedirectURL`": `"string`",

	  `"formSubmitThanksMessage`": `"string`",

	  `"guestType`": `"count_only`",

	  `"consentLabel`": `"string`",

	  `"calendarCoverImage`": `"string`",

	  `"lookBusyConfig`": {

	    `"enabled`": true,

	    `"LookBusyPercentage`": 0

	  },

	  `"isActive`": true

	}

	"@

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/calendars/:calendarId' -Method 'PUT' -Headers $headers -Body $body

	$response | ConvertTo-Json

```

