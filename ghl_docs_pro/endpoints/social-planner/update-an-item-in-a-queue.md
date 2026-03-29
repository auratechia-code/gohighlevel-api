# Update an item in a queue

**Method:** `PUT` | **URL:** `https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/items/:itemId`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
name: Authorization
type: http
scopes: socialplanner/category.write
scheme: bearer
bearerFormat: JWT
in: header
description: Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.
```

## 📥 Parameters
### Path Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `queueId` | ✅ | itemId string required |
| `itemId` | ❌ |  |

### Header Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `Version` | ❌ |  |

## 📤 Responses
<details>
<summary>Response 200</summary>

```json
{
  "success": true,
  "statusCode": 200,
  "results": {
    "message": "Queue item updated successfully",
    "queueItem": {
      "_id": "60af88475f1b2c001f5d5f4b",
      "order": 1000,
      "variations": [
        {
          "_id": "60af88475f1b2c001f5d5f4c",
          "content": "Check out our latest blog post! #marketing #socialmedia",
          "mentions": [
            {
              "platform": "instagram",
              "username": "example_user",
              "offset": 10,
              "length": 12
            }
          ],
          "ogTags": {
            "metaLink": "https://example.com",
            "metaImage": "https://example.com/image.png",
            "ogTitle": "Example Title"
          }
        }
      ],
      "primaryImage": "https://example.com/images/post-image.png",
      "lastScheduledTime": null,
      "queueId": "60af88475f1b2c001f5d5f4a",
      "postId": "60af88475f1b2c001f5d5f4d",
      "modifiedPostPayload": {
        "_id": "61bb16833b3f2791f9715be2",
        "source": "composer",
        "locationId": "ve9EPM428h8vShlRW1KT",
        "displayDate": "2023-08-02T00:00:00.000Z",
        "createdAt": "2023-08-02T00:00:00.000Z",
        "updatedAt": "2023-08-02T00:00:00.000Z",
        "accountId": "w37swmmLbA02zgqKPpxITe",
        "error": "Failed due to auth token",
        "postId": "323534534435",
        "publishedAt": "2021-06-22T05:32:49.463Z",
        "accountIds": [
          "aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496"
        ],
        "summary": "Sample Summary",
        "media": [
          {
            "url": "https://example.com/image.jpg",
            "type": "image/jpeg",
            "caption": "Sample caption"
          }
        ],
        "status": "published",
        "createdBy": "Lx1EI6YIgQYMQi0ytFXv",
        "type": "post",
        "tags": [
          "aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496"
        ],
        "ogTagsDetails": {
          "metaImage": "https://example.com/image.jpg",
          "metaLink": "https://www.yahoo.com/",
          "ogTitle": "Page Title",
          "ogDescription": "Page Description"
        },
        "postApprovalDetails": {
          "approver": "iVrVJ2uoXNF0wzcBzgl5",
          "approvalStatus": "approved"
        },
        "tiktokPostDetails": {
          "privacyLevel": "PUBLIC_TO_EVERYONE",
          "enableComment": true
        },
        "gmbPostDetails": {
          "gmbEventType": "STANDARD",
          "actionType": "BOOK"
        },
        "user": {
          "id": "6284c43d519161e96cc09c13",
          "firstName": "Harry",
          "lastName": "Spencer",
          "email": "abc@xyc.com"
        },
        "linkedinPostDetails": {
          "pdfTitle": "Q4 Marketing Strategy Presentation",
          "postAsPdf": true
        },
        "pinterestPostDetails": {
          "title": "10 Easy Home Decor Ideas for 2024",
          "link": "https://yoursite.com/blog/home-decor-ideas",
          "boardIds": {
            "6887d6de1d8175813d50dab8": "987654321098765432",
            "682c7d1710a2fe3d805a3513": "123456789012345678"
          },
          "shortenedLinks": [
            "string"
          ]
        },
        "facebookPostDetails": {
          "type": "post"
        },
        "instagramPostDetails": {
          "type": "post",
          "collaborators": {
            "accountId1": [
              "username1",
              "username2"
            ],
            "accountId2": [
              "username3",
              "username4"
            ]
          },
          "showOnFeed": true,
          "publishViaPushNotification": true,
          "publisherNote": "When publishing, add swipe up link to the landing page so that we can direct them to the sales page"
        },
        "youtubePostDetails": {
          "title": "How to Build a Successful Marketing Strategy in 2024",
          "privacyLevel": "public",
          "type": "video"
        },
        "communityPostDetails": {
          "title": "Welcome to Our New Community Feature!",
          "notifyAllGroupMembers": true,
          "postAsUser": {
            "xMQswA02zgqKPpxITe": {
              "avatar": "https://lh3.googleusercontent.com/a/user-avatar.jpg",
              "id": "snCr14eeYkSppD04rkNW",
              "name": "John Smith"
            }
          }
        },
        "mediaOptimization": true
      },
      "parentPostId": "60af88475f1b2c001f5d5f4e",
      "errors": [
        "INVALID_USER_ID",
        "PIXABAY_MEDIA"
      ],
      "currentVariation": 0,
      "createdAt": "2024-12-09T13:41:21.385Z",
      "updatedAt": "2024-12-09T13:41:21.385Z",
      "deleted": false,
      "locationId": "fvg1TXIiVxGcdOaL0riG"
    },
    "updatedSlots": [
      {
        "itemId": "60af88475f1b2c001f5d5f4b",
        "scheduledDateTime": "2023-10-15T10:00:00.000Z",
        "isSkipped": false
      }
    ],
    "totalPostsChanged": 5
  },
  "traceId": "string"
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "success": true,  "statusCode": 200,  "results": {    "message": "Queue item updated successfully",    "queueItem": {      "_id": "60af88475f1b2c001f5d5f4b",      "order": 1000,      "variations": [        {          "_id": "60af88475f1b2c001f5d5f4c",          "content": "Check out our latest blog post! #marketing #socialmedia",          "mentions": [            {              "platform": "instagram",              "username": "example_user",              "offset": 10,              "length": 12            }          ],          "ogTags": {            "metaLink": "https://example.com",            "metaImage": "https://example.com/image.png",            "ogTitle": "Example Title"          }        }      ],      "primaryImage": "https://example.com/images/post-image.png",      "lastScheduledTime": null,      "queueId": "60af88475f1b2c001f5d5f4a",      "postId": "60af88475f1b2c001f5d5f4d",      "modifiedPostPayload": {        "_id": "61bb16833b3f2791f9715be2",        "source": "composer",        "locationId": "ve9EPM428h8vShlRW1KT",        "displayDate": "2023-08-02T00:00:00.000Z",        "createdAt": "2023-08-02T00:00:00.000Z",        "updatedAt": "2023-08-02T00:00:00.000Z",        "accountId": "w37swmmLbA02zgqKPpxITe",        "error": "Failed due to auth token",        "postId": "323534534435",        "publishedAt": "2021-06-22T05:32:49.463Z",        "accountIds": [          "aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496"        ],        "summary": "Sample Summary",        "media": [          {            "url": "https://example.com/image.jpg",            "type": "image/jpeg",            "caption": "Sample caption"          }        ],        "status": "published",        "createdBy": "Lx1EI6YIgQYMQi0ytFXv",        "type": "post",        "tags": [          "aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496"        ],        "ogTagsDetails": {          "metaImage": "https://example.com/image.jpg",          "metaLink": "https://www.yahoo.com/",          "ogTitle": "Page Title",          "ogDescription": "Page Description"        },        "postApprovalDetails": {          "approver": "iVrVJ2uoXNF0wzcBzgl5",          "approvalStatus": "approved"        },        "tiktokPostDetails": {          "privacyLevel": "PUBLIC_TO_EVERYONE",          "enableComment": true        },        "gmbPostDetails": {          "gmbEventType": "STANDARD",          "actionType": "BOOK"        },        "user": {          "id": "6284c43d519161e96cc09c13",          "firstName": "Harry",          "lastName": "Spencer",          "email": "abc@xyc.com"        },        "linkedinPostDetails": {          "pdfTitle": "Q4 Marketing Strategy Presentation",          "postAsPdf": true        },        "pinterestPostDetails": {          "title": "10 Easy Home Decor Ideas for 2024",          "link": "https://yoursite.com/blog/home-decor-ideas",          "boardIds": {            "6887d6de1d8175813d50dab8": "987654321098765432",            "682c7d1710a2fe3d805a3513": "123456789012345678"          },          "shortenedLinks": [            "string"          ]        },        "facebookPostDetails": {          "type": "post"        },        "instagramPostDetails": {          "type": "post",          "collaborators": {            "accountId1": [              "username1",              "username2"            ],            "accountId2": [              "username3",              "username4"            ]          },          "showOnFeed": true,          "publishViaPushNotification": true,          "publisherNote": "When publishing, add swipe up link to the landing page so that we can direct them to the sales page"        },        "youtubePostDetails": {          "title": "How to Build a Successful Marketing Strategy in 2024",          "privacyLevel": "public",          "type": "video"        },        "communityPostDetails": {          "title": "Welcome to Our New Community Feature!",          "notifyAllGroupMembers": true,          "postAsUser": {            "xMQswA02zgqKPpxITe": {              "avatar": "https://lh3.googleusercontent.com/a/user-avatar.jpg",              "id": "snCr14eeYkSppD04rkNW",              "name": "John Smith"            }          }        },        "mediaOptimization": true      },      "parentPostId": "60af88475f1b2c001f5d5f4e",      "errors": [        "INVALID_USER_ID",        "PIXABAY_MEDIA"      ],      "currentVariation": 0,      "createdAt": "2024-12-09T13:41:21.385Z",      "updatedAt": "2024-12-09T13:41:21.385Z",      "deleted": false,      "locationId": "fvg1TXIiVxGcdOaL0riG"    },    "updatedSlots": [      {        "itemId": "60af88475f1b2c001f5d5f4b",        "scheduledDateTime": "2023-10-15T10:00:00.000Z",        "isSkipped": false      }    ],    "totalPostsChanged": 5  },  "traceId": "string"}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "success": true,  "statusCode": 200,  "results": {    "message": "Queue item updated successfully",    "queueItem": {      "_id": "60af88475f1b2c001f5d5f4b",      "order": 1000,      "variations": [        {          "_id": "60af88475f1b2c001f5d5f4c",          "content": "Check out our latest blog post! #marketing #socialmedia",          "mentions": [            {              "platform": "instagram",              "username": "example_user",              "offset": 10,              "length": 12            }          ],          "ogTags": {            "metaLink": "https://example.com",            "metaImage": "https://example.com/image.png",            "ogTitle": "Example Title"          }        }      ],      "primaryImage": "https://example.com/images/post-image.png",      "lastScheduledTime": null,      "queueId": "60af88475f1b2c001f5d5f4a",      "postId": "60af88475f1b2c001f5d5f4d",      "modifiedPostPayload": {        "_id": "61bb16833b3f2791f9715be2",        "source": "composer",        "locationId": "ve9EPM428h8vShlRW1KT",        "displayDate": "2023-08-02T00:00:00.000Z",        "createdAt": "2023-08-02T00:00:00.000Z",        "updatedAt": "2023-08-02T00:00:00.000Z",        "accountId": "w37swmmLbA02zgqKPpxITe",        "error": "Failed due to auth token",        "postId": "323534534435",        "publishedAt": "2021-06-22T05:32:49.463Z",        "accountIds": [          "aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496"        ],        "summary": "Sample Summary",        "media": [          {            "url": "https://example.com/image.jpg",            "type": "image/jpeg",            "caption": "Sample caption"          }        ],        "status": "published",        "createdBy": "Lx1EI6YIgQYMQi0ytFXv",        "type": "post",        "tags": [          "aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496"        ],        "ogTagsDetails": {          "metaImage": "https://example.com/image.jpg",          "metaLink": "https://www.yahoo.com/",          "ogTitle": "Page Title",          "ogDescription": "Page Description"        },        "postApprovalDetails": {          "approver": "iVrVJ2uoXNF0wzcBzgl5",          "approvalStatus": "approved"        },        "tiktokPostDetails": {          "privacyLevel": "PUBLIC_TO_EVERYONE",          "enableComment": true        },        "gmbPostDetails": {          "gmbEventType": "STANDARD",          "actionType": "BOOK"        },        "user": {          "id": "6284c43d519161e96cc09c13",          "firstName": "Harry",          "lastName": "Spencer",          "email": "abc@xyc.com"        },        "linkedinPostDetails": {          "pdfTitle": "Q4 Marketing Strategy Presentation",          "postAsPdf": true        },        "pinterestPostDetails": {          "title": "10 Easy Home Decor Ideas for 2024",          "link": "https://yoursite.com/blog/home-decor-ideas",          "boardIds": {            "6887d6de1d8175813d50dab8": "987654321098765432",            "682c7d1710a2fe3d805a3513": "123456789012345678"          },          "shortenedLinks": [            "string"          ]        },        "facebookPostDetails": {          "type": "post"        },        "instagramPostDetails": {          "type": "post",          "collaborators": {            "accountId1": [              "username1",              "username2"            ],            "accountId2": [              "username3",              "username4"            ]          },          "showOnFeed": true,          "publishViaPushNotification": true,          "publisherNote": "When publishing, add swipe up link to the landing page so that we can direct them to the sales page"        },        "youtubePostDetails": {          "title": "How to Build a Successful Marketing Strategy in 2024",          "privacyLevel": "public",          "type": "video"        },        "communityPostDetails": {          "title": "Welcome to Our New Community Feature!",          "notifyAllGroupMembers": true,          "postAsUser": {            "xMQswA02zgqKPpxITe": {              "avatar": "https://lh3.googleusercontent.com/a/user-avatar.jpg",              "id": "snCr14eeYkSppD04rkNW",              "name": "John Smith"            }          }        },        "mediaOptimization": true      },      "parentPostId": "60af88475f1b2c001f5d5f4e",      "errors": [        "INVALID_USER_ID",        "PIXABAY_MEDIA"      ],      "currentVariation": 0,      "createdAt": "2024-12-09T13:41:21.385Z",      "updatedAt": "2024-12-09T13:41:21.385Z",      "deleted": false,      "locationId": "fvg1TXIiVxGcdOaL0riG"    },    "updatedSlots": [      {        "itemId": "60af88475f1b2c001f5d5f4b",        "scheduledDateTime": "2023-10-15T10:00:00.000Z",        "isSkipped": false      }    ],    "totalPostsChanged": 5  },  "traceId": "string"}
```
</details>

<details>
<summary>Response 422</summary>

```json
{  "success": true,  "statusCode": 200,  "results": {    "message": "Queue item updated successfully",    "queueItem": {      "_id": "60af88475f1b2c001f5d5f4b",      "order": 1000,      "variations": [        {          "_id": "60af88475f1b2c001f5d5f4c",          "content": "Check out our latest blog post! #marketing #socialmedia",          "mentions": [            {              "platform": "instagram",              "username": "example_user",              "offset": 10,              "length": 12            }          ],          "ogTags": {            "metaLink": "https://example.com",            "metaImage": "https://example.com/image.png",            "ogTitle": "Example Title"          }        }      ],      "primaryImage": "https://example.com/images/post-image.png",      "lastScheduledTime": null,      "queueId": "60af88475f1b2c001f5d5f4a",      "postId": "60af88475f1b2c001f5d5f4d",      "modifiedPostPayload": {        "_id": "61bb16833b3f2791f9715be2",        "source": "composer",        "locationId": "ve9EPM428h8vShlRW1KT",        "displayDate": "2023-08-02T00:00:00.000Z",        "createdAt": "2023-08-02T00:00:00.000Z",        "updatedAt": "2023-08-02T00:00:00.000Z",        "accountId": "w37swmmLbA02zgqKPpxITe",        "error": "Failed due to auth token",        "postId": "323534534435",        "publishedAt": "2021-06-22T05:32:49.463Z",        "accountIds": [          "aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496"        ],        "summary": "Sample Summary",        "media": [          {            "url": "https://example.com/image.jpg",            "type": "image/jpeg",            "caption": "Sample caption"          }        ],        "status": "published",        "createdBy": "Lx1EI6YIgQYMQi0ytFXv",        "type": "post",        "tags": [          "aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496"        ],        "ogTagsDetails": {          "metaImage": "https://example.com/image.jpg",          "metaLink": "https://www.yahoo.com/",          "ogTitle": "Page Title",          "ogDescription": "Page Description"        },        "postApprovalDetails": {          "approver": "iVrVJ2uoXNF0wzcBzgl5",          "approvalStatus": "approved"        },        "tiktokPostDetails": {          "privacyLevel": "PUBLIC_TO_EVERYONE",          "enableComment": true        },        "gmbPostDetails": {          "gmbEventType": "STANDARD",          "actionType": "BOOK"        },        "user": {          "id": "6284c43d519161e96cc09c13",          "firstName": "Harry",          "lastName": "Spencer",          "email": "abc@xyc.com"        },        "linkedinPostDetails": {          "pdfTitle": "Q4 Marketing Strategy Presentation",          "postAsPdf": true        },        "pinterestPostDetails": {          "title": "10 Easy Home Decor Ideas for 2024",          "link": "https://yoursite.com/blog/home-decor-ideas",          "boardIds": {            "6887d6de1d8175813d50dab8": "987654321098765432",            "682c7d1710a2fe3d805a3513": "123456789012345678"          },          "shortenedLinks": [            "string"          ]        },        "facebookPostDetails": {          "type": "post"        },        "instagramPostDetails": {          "type": "post",          "collaborators": {            "accountId1": [              "username1",              "username2"            ],            "accountId2": [              "username3",              "username4"            ]          },          "showOnFeed": true,          "publishViaPushNotification": true,          "publisherNote": "When publishing, add swipe up link to the landing page so that we can direct them to the sales page"        },        "youtubePostDetails": {          "title": "How to Build a Successful Marketing Strategy in 2024",          "privacyLevel": "public",          "type": "video"        },        "communityPostDetails": {          "title": "Welcome to Our New Community Feature!",          "notifyAllGroupMembers": true,          "postAsUser": {            "xMQswA02zgqKPpxITe": {              "avatar": "https://lh3.googleusercontent.com/a/user-avatar.jpg",              "id": "snCr14eeYkSppD04rkNW",              "name": "John Smith"            }          }        },        "mediaOptimization": true      },      "parentPostId": "60af88475f1b2c001f5d5f4e",      "errors": [        "INVALID_USER_ID",        "PIXABAY_MEDIA"      ],      "currentVariation": 0,      "createdAt": "2024-12-09T13:41:21.385Z",      "updatedAt": "2024-12-09T13:41:21.385Z",      "deleted": false,      "locationId": "fvg1TXIiVxGcdOaL0riG"    },    "updatedSlots": [      {        "itemId": "60af88475f1b2c001f5d5f4b",        "scheduledDateTime": "2023-10-15T10:00:00.000Z",        "isSkipped": false      }    ],    "totalPostsChanged": 5  },  "traceId": "string"}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L -X PUT 'https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/items/:itemId' \

	-H 'Content-Type: application/json' \

	-H 'Accept: application/json' \

	-H 'Authorization: Bearer <TOKEN>' \

	-d '{

	  "locationId": "609e126a1c4ae1001291e1b5",

	  "sessionId": "60af88475f1b2c001f5d5f4b",

	  "modifiedPostPayload": {

	    "accountIds": [

	      "aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496"

	    ],

	    "summary": "Hello World",

	    "media": [

	      {

	        "url": "https://example.com/image.jpg",

	        "type": "image/jpeg",

	        "caption": "Sample caption"

	      }

	    ],

	    "status": "scheduled",

	    "scheduleDate": "2024-01-15T10:00:00Z",

	    "selectedBestTime": "2024-01-15T10:00:00Z",

	    "createdBy": "Lx1EI6YIgQYMQi0ytFXv",

	    "followUpComment": "What do you think? Let us know in the comments!",

	    "ogTagsDetails": {

	      "metaImage": "https://example.com/image.jpg",

	      "metaLink": "https://www.yahoo.com/",

	      "ogTitle": "Page Title",

	      "ogDescription": "Page Description"

	    },

	    "type": "post",

	    "postApprovalDetails": {

	      "approver": "iVrVJ2uoXNF0wzcBzgl5",

	      "approvalStatus": "pending"

	    },

	    "scheduleTimeUpdated": true,

	    "tags": [

	      "65f151c99bc2bf3aaf970d72",

	      "65f151c99bc2bf3aaf970d73"

	    ],

	    "categoryId": "65f151c99bc2bf3aaf970d72",

	    "applyWatermark": true,

	    "tiktokPostDetails": {

	      "privacyLevel": "PUBLIC_TO_EVERYONE",

	      "enableComment": true,

	      "enableDuet": false

	    },

	    "gmbPostDetails": {

	      "gmbEventType": "STANDARD",

	      "actionType": "BOOK",

	      "url": "https://example.com"

	    },

	    "userId": "sdfdsfdsfEWEsdfsdsW32dd",

	    "linkedinPostDetails": {

	      "pdfTitle": "Q4 Marketing Strategy Presentation",

	      "postAsPdf": true

	    },

	    "pinterestPostDetails": {

	      "title": "10 Easy Home Decor Ideas for 2024",

	      "link": "https://yoursite.com/blog/home-decor-ideas",

	      "boardIds": {

	        "6887d6de1d8175813d50dab8": "987654321098765432",

	        "682c7d1710a2fe3d805a3513": "123456789012345678"

	      },

	      "shortenedLinks": [

	        "string"

	      ]

	    },

	    "facebookPostDetails": {

	      "type": "post"

	    },

	    "instagramPostDetails": {

	      "type": "post",

	      "collaborators": {

	        "accountId1": [

	          "username1",

	          "username2"

	        ],

	        "accountId2": [

	          "username3",

	          "username4"

	        ]

	      },

	      "showOnFeed": true,

	      "publishViaPushNotification": true,

	      "publisherNote": "When publishing, add swipe up link to the landing page so that we can direct them to the sales page"

	    },

	    "youtubePostDetails": {

	      "title": "How to Build a Successful Marketing Strategy in 2024",

	      "privacyLevel": "public",

	      "type": "video"

	    },

	    "communityPostDetails": {

	      "title": "Welcome to Our New Community Feature!",

	      "notifyAllGroupMembers": true,

	      "postAsUser": {

	        "xMQswA02zgqKPpxITe": {

	          "avatar": "https://lh3.googleusercontent.com/a/user-avatar.jpg",

	          "id": "snCr14eeYkSppD04rkNW",

	          "name": "John Smith"

	        }

	      }

	    },

	    "locationId": "ve9EPM428h8vShlRW1KT"

	  },

	  "newOrder": 0,

	  "variations": [

	    {

	      "content": "Check out our latest blog post! #marketing #socialmedia",

	      "mentions": [

	        {

	          "platform": "instagram",

	          "username": "example_user",

	          "offset": 10,

	          "length": 12

	        }

	      ],

	      "ogTags": {

	        "metaLink": "https://example.com/blog/post-title",

	        "metaImage": "https://example.com/images/preview.png",

	        "ogTitle": "Check out our latest blog post!"

	      }

	    }

	  ],

	  "primaryImage": "http://example.com/media.png"

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

	  const response = await highLevel.socialPlanner.updateQueueItem({

	    'queueId': 'queueId_value',

	    'itemId': 'itemId_value'

	  },

	  {

	    'locationId': '609e126a1c4ae1001291e1b5',

	    'sessionId': '60af88475f1b2c001f5d5f4b',

	    'modifiedPostPayload': {

	      'accountIds': [

	        'aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496'

	      ],

	      'summary': 'Hello World',

	      'media': [

	        {

	          'url': 'https://example.com/image.jpg',

	          'type': 'image/jpeg',

	          'caption': 'Sample caption'

	        }

	      ],

	      'status': 'scheduled',

	      'scheduleDate': '2024-01-15T10:00:00Z',

	      'selectedBestTime': '2024-01-15T10:00:00Z',

	      'createdBy': 'Lx1EI6YIgQYMQi0ytFXv',

	      'followUpComment': 'What do you think? Let us know in the comments!',

	      'ogTagsDetails': {

	        'metaImage': 'https://example.com/image.jpg',

	        'metaLink': 'https://www.yahoo.com/',

	        'ogTitle': 'Page Title',

	        'ogDescription': 'Page Description'

	      },

	      'type': 'post',

	      'postApprovalDetails': {

	        'approver': 'iVrVJ2uoXNF0wzcBzgl5',

	        'approvalStatus': 'pending'

	      },

	      'scheduleTimeUpdated': true,

	      'tags': [

	        '65f151c99bc2bf3aaf970d72',

	        '65f151c99bc2bf3aaf970d73'

	      ],

	      'categoryId': '65f151c99bc2bf3aaf970d72',

	      'applyWatermark': true,

	      'tiktokPostDetails': {

	        'privacyLevel': 'PUBLIC_TO_EVERYONE',

	        'enableComment': true,

	        'enableDuet': false

	      },

	      'gmbPostDetails': {

	        'gmbEventType': 'STANDARD',

	        'actionType': 'BOOK',

	        'url': 'https://example.com'

	      },

	      'userId': 'sdfdsfdsfEWEsdfsdsW32dd',

	      'linkedinPostDetails': {

	        'pdfTitle': 'Q4 Marketing Strategy Presentation',

	        'postAsPdf': true

	      },

	      'pinterestPostDetails': {

	        'title': '10 Easy Home Decor Ideas for 2024',

	        'link': 'https://yoursite.com/blog/home-decor-ideas',

	        'boardIds': {

	          '6887d6de1d8175813d50dab8': '987654321098765432',

	          '682c7d1710a2fe3d805a3513': '123456789012345678'

	        },

	        'shortenedLinks': [

	          'string'

	        ]

	      },

	      'facebookPostDetails': {

	        'type': 'post'

	      },

	      'instagramPostDetails': {

	        'type': 'post',

	        'collaborators': {

	          'accountId1': [

	            'username1',

	            'username2'

	          ],

	          'accountId2': [

	            'username3',

	            'username4'

	          ]

	        },

	        'showOnFeed': true,

	        'publishViaPushNotification': true,

	        'publisherNote': 'When publishing, add swipe up link to the landing page so that we can direct them to the sales page'

	      },

	      'youtubePostDetails': {

	        'title': 'How to Build a Successful Marketing Strategy in 2024',

	        'privacyLevel': 'public',

	        'type': 'video'

	      },

	      'communityPostDetails': {

	        'title': 'Welcome to Our New Community Feature!',

	        'notifyAllGroupMembers': true,

	        'postAsUser': {

	          'xMQswA02zgqKPpxITe': {

	            'avatar': 'https://lh3.googleusercontent.com/a/user-avatar.jpg',

	            'id': 'snCr14eeYkSppD04rkNW',

	            'name': 'John Smith'

	          }

	        }

	      },

	      'locationId': 've9EPM428h8vShlRW1KT'

	    },

	    'newOrder': 0,

	    'variations': [

	      {

	        'content': 'Check out our latest blog post! #marketing #socialmedia',

	        'mentions': [

	          {

	            'platform': 'instagram',

	            'username': 'example_user',

	            'offset': 10,

	            'length': 12

	          }

	        ],

	        'ogTags': {

	          'metaLink': 'https://example.com/blog/post-title',

	          'metaImage': 'https://example.com/images/preview.png',

	          'ogTitle': 'Check out our latest blog post!'

	        }

	      }

	    ],

	    'primaryImage': 'http://example.com/media.png'

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

	  "locationId": "609e126a1c4ae1001291e1b5",

	  "sessionId": "60af88475f1b2c001f5d5f4b",

	  "modifiedPostPayload": {

	    "accountIds": [

	      "aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496"

	    ],

	    "summary": "Hello World",

	    "media": [

	      {

	        "url": "https://example.com/image.jpg",

	        "type": "image/jpeg",

	        "caption": "Sample caption"

	      }

	    ],

	    "status": "scheduled",

	    "scheduleDate": "2024-01-15T10:00:00Z",

	    "selectedBestTime": "2024-01-15T10:00:00Z",

	    "createdBy": "Lx1EI6YIgQYMQi0ytFXv",

	    "followUpComment": "What do you think? Let us know in the comments!",

	    "ogTagsDetails": {

	      "metaImage": "https://example.com/image.jpg",

	      "metaLink": "https://www.yahoo.com/",

	      "ogTitle": "Page Title",

	      "ogDescription": "Page Description"

	    },

	    "type": "post",

	    "postApprovalDetails": {

	      "approver": "iVrVJ2uoXNF0wzcBzgl5",

	      "approvalStatus": "pending"

	    },

	    "scheduleTimeUpdated": true,

	    "tags": [

	      "65f151c99bc2bf3aaf970d72",

	      "65f151c99bc2bf3aaf970d73"

	    ],

	    "categoryId": "65f151c99bc2bf3aaf970d72",

	    "applyWatermark": true,

	    "tiktokPostDetails": {

	      "privacyLevel": "PUBLIC_TO_EVERYONE",

	      "enableComment": true,

	      "enableDuet": false

	    },

	    "gmbPostDetails": {

	      "gmbEventType": "STANDARD",

	      "actionType": "BOOK",

	      "url": "https://example.com"

	    },

	    "userId": "sdfdsfdsfEWEsdfsdsW32dd",

	    "linkedinPostDetails": {

	      "pdfTitle": "Q4 Marketing Strategy Presentation",

	      "postAsPdf": true

	    },

	    "pinterestPostDetails": {

	      "title": "10 Easy Home Decor Ideas for 2024",

	      "link": "https://yoursite.com/blog/home-decor-ideas",

	      "boardIds": {

	        "6887d6de1d8175813d50dab8": "987654321098765432",

	        "682c7d1710a2fe3d805a3513": "123456789012345678"

	      },

	      "shortenedLinks": [

	        "string"

	      ]

	    },

	    "facebookPostDetails": {

	      "type": "post"

	    },

	    "instagramPostDetails": {

	      "type": "post",

	      "collaborators": {

	        "accountId1": [

	          "username1",

	          "username2"

	        ],

	        "accountId2": [

	          "username3",

	          "username4"

	        ]

	      },

	      "showOnFeed": true,

	      "publishViaPushNotification": true,

	      "publisherNote": "When publishing, add swipe up link to the landing page so that we can direct them to the sales page"

	    },

	    "youtubePostDetails": {

	      "title": "How to Build a Successful Marketing Strategy in 2024",

	      "privacyLevel": "public",

	      "type": "video"

	    },

	    "communityPostDetails": {

	      "title": "Welcome to Our New Community Feature!",

	      "notifyAllGroupMembers": true,

	      "postAsUser": {

	        "xMQswA02zgqKPpxITe": {

	          "avatar": "https://lh3.googleusercontent.com/a/user-avatar.jpg",

	          "id": "snCr14eeYkSppD04rkNW",

	          "name": "John Smith"

	        }

	      }

	    },

	    "locationId": "ve9EPM428h8vShlRW1KT"

	  },

	  "newOrder": 0,

	  "variations": [

	    {

	      "content": "Check out our latest blog post! #marketing #socialmedia",

	      "mentions": [

	        {

	          "platform": "instagram",

	          "username": "example_user",

	          "offset": 10,

	          "length": 12

	        }

	      ],

	      "ogTags": {

	        "metaLink": "https://example.com/blog/post-title",

	        "metaImage": "https://example.com/images/preview.png",

	        "ogTitle": "Check out our latest blog post!"

	      }

	    }

	  ],

	  "primaryImage": "http://example.com/media.png"

	});

	

	let config = {

	  method: 'put',

	  maxBodyLength: Infinity,

	  url: 'https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/items/:itemId',

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

	  'path': '/social-media-posting/category/queues/:queueId/items/:itemId',

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

	  "locationId": "609e126a1c4ae1001291e1b5",

	  "sessionId": "60af88475f1b2c001f5d5f4b",

	  "modifiedPostPayload": {

	    "accountIds": [

	      "aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496"

	    ],

	    "summary": "Hello World",

	    "media": [

	      {

	        "url": "https://example.com/image.jpg",

	        "type": "image/jpeg",

	        "caption": "Sample caption"

	      }

	    ],

	    "status": "scheduled",

	    "scheduleDate": "2024-01-15T10:00:00Z",

	    "selectedBestTime": "2024-01-15T10:00:00Z",

	    "createdBy": "Lx1EI6YIgQYMQi0ytFXv",

	    "followUpComment": "What do you think? Let us know in the comments!",

	    "ogTagsDetails": {

	      "metaImage": "https://example.com/image.jpg",

	      "metaLink": "https://www.yahoo.com/",

	      "ogTitle": "Page Title",

	      "ogDescription": "Page Description"

	    },

	    "type": "post",

	    "postApprovalDetails": {

	      "approver": "iVrVJ2uoXNF0wzcBzgl5",

	      "approvalStatus": "pending"

	    },

	    "scheduleTimeUpdated": true,

	    "tags": [

	      "65f151c99bc2bf3aaf970d72",

	      "65f151c99bc2bf3aaf970d73"

	    ],

	    "categoryId": "65f151c99bc2bf3aaf970d72",

	    "applyWatermark": true,

	    "tiktokPostDetails": {

	      "privacyLevel": "PUBLIC_TO_EVERYONE",

	      "enableComment": true,

	      "enableDuet": false

	    },

	    "gmbPostDetails": {

	      "gmbEventType": "STANDARD",

	      "actionType": "BOOK",

	      "url": "https://example.com"

	    },

	    "userId": "sdfdsfdsfEWEsdfsdsW32dd",

	    "linkedinPostDetails": {

	      "pdfTitle": "Q4 Marketing Strategy Presentation",

	      "postAsPdf": true

	    },

	    "pinterestPostDetails": {

	      "title": "10 Easy Home Decor Ideas for 2024",

	      "link": "https://yoursite.com/blog/home-decor-ideas",

	      "boardIds": {

	        "6887d6de1d8175813d50dab8": "987654321098765432",

	        "682c7d1710a2fe3d805a3513": "123456789012345678"

	      },

	      "shortenedLinks": [

	        "string"

	      ]

	    },

	    "facebookPostDetails": {

	      "type": "post"

	    },

	    "instagramPostDetails": {

	      "type": "post",

	      "collaborators": {

	        "accountId1": [

	          "username1",

	          "username2"

	        ],

	        "accountId2": [

	          "username3",

	          "username4"

	        ]

	      },

	      "showOnFeed": true,

	      "publishViaPushNotification": true,

	      "publisherNote": "When publishing, add swipe up link to the landing page so that we can direct them to the sales page"

	    },

	    "youtubePostDetails": {

	      "title": "How to Build a Successful Marketing Strategy in 2024",

	      "privacyLevel": "public",

	      "type": "video"

	    },

	    "communityPostDetails": {

	      "title": "Welcome to Our New Community Feature!",

	      "notifyAllGroupMembers": true,

	      "postAsUser": {

	        "xMQswA02zgqKPpxITe": {

	          "avatar": "https://lh3.googleusercontent.com/a/user-avatar.jpg",

	          "id": "snCr14eeYkSppD04rkNW",

	          "name": "John Smith"

	        }

	      }

	    },

	    "locationId": "ve9EPM428h8vShlRW1KT"

	  },

	  "newOrder": 0,

	  "variations": [

	    {

	      "content": "Check out our latest blog post! #marketing #socialmedia",

	      "mentions": [

	        {

	          "platform": "instagram",

	          "username": "example_user",

	          "offset": 10,

	          "length": 12

	        }

	      ],

	      "ogTags": {

	        "metaLink": "https://example.com/blog/post-title",

	        "metaImage": "https://example.com/images/preview.png",

	        "ogTitle": "Check out our latest blog post!"

	      }

	    }

	  ],

	  "primaryImage": "http://example.com/media.png"

	});

	

	req.write(postData);

	

	req.end();

```

#### REQUEST
```nodejs
	var request = require('request');

	var options = {

	  'method': 'PUT',

	  'url': 'https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/items/:itemId',

	  'headers': {

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  },

	  body: JSON.stringify({

	    "locationId": "609e126a1c4ae1001291e1b5",

	    "sessionId": "60af88475f1b2c001f5d5f4b",

	    "modifiedPostPayload": {

	      "accountIds": [

	        "aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496"

	      ],

	      "summary": "Hello World",

	      "media": [

	        {

	          "url": "https://example.com/image.jpg",

	          "type": "image/jpeg",

	          "caption": "Sample caption"

	        }

	      ],

	      "status": "scheduled",

	      "scheduleDate": "2024-01-15T10:00:00Z",

	      "selectedBestTime": "2024-01-15T10:00:00Z",

	      "createdBy": "Lx1EI6YIgQYMQi0ytFXv",

	      "followUpComment": "What do you think? Let us know in the comments!",

	      "ogTagsDetails": {

	        "metaImage": "https://example.com/image.jpg",

	        "metaLink": "https://www.yahoo.com/",

	        "ogTitle": "Page Title",

	        "ogDescription": "Page Description"

	      },

	      "type": "post",

	      "postApprovalDetails": {

	        "approver": "iVrVJ2uoXNF0wzcBzgl5",

	        "approvalStatus": "pending"

	      },

	      "scheduleTimeUpdated": true,

	      "tags": [

	        "65f151c99bc2bf3aaf970d72",

	        "65f151c99bc2bf3aaf970d73"

	      ],

	      "categoryId": "65f151c99bc2bf3aaf970d72",

	      "applyWatermark": true,

	      "tiktokPostDetails": {

	        "privacyLevel": "PUBLIC_TO_EVERYONE",

	        "enableComment": true,

	        "enableDuet": false

	      },

	      "gmbPostDetails": {

	        "gmbEventType": "STANDARD",

	        "actionType": "BOOK",

	        "url": "https://example.com"

	      },

	      "userId": "sdfdsfdsfEWEsdfsdsW32dd",

	      "linkedinPostDetails": {

	        "pdfTitle": "Q4 Marketing Strategy Presentation",

	        "postAsPdf": true

	      },

	      "pinterestPostDetails": {

	        "title": "10 Easy Home Decor Ideas for 2024",

	        "link": "https://yoursite.com/blog/home-decor-ideas",

	        "boardIds": {

	          "6887d6de1d8175813d50dab8": "987654321098765432",

	          "682c7d1710a2fe3d805a3513": "123456789012345678"

	        },

	        "shortenedLinks": [

	          "string"

	        ]

	      },

	      "facebookPostDetails": {

	        "type": "post"

	      },

	      "instagramPostDetails": {

	        "type": "post",

	        "collaborators": {

	          "accountId1": [

	            "username1",

	            "username2"

	          ],

	          "accountId2": [

	            "username3",

	            "username4"

	          ]

	        },

	        "showOnFeed": true,

	        "publishViaPushNotification": true,

	        "publisherNote": "When publishing, add swipe up link to the landing page so that we can direct them to the sales page"

	      },

	      "youtubePostDetails": {

	        "title": "How to Build a Successful Marketing Strategy in 2024",

	        "privacyLevel": "public",

	        "type": "video"

	      },

	      "communityPostDetails": {

	        "title": "Welcome to Our New Community Feature!",

	        "notifyAllGroupMembers": true,

	        "postAsUser": {

	          "xMQswA02zgqKPpxITe": {

	            "avatar": "https://lh3.googleusercontent.com/a/user-avatar.jpg",

	            "id": "snCr14eeYkSppD04rkNW",

	            "name": "John Smith"

	          }

	        }

	      },

	      "locationId": "ve9EPM428h8vShlRW1KT"

	    },

	    "newOrder": 0,

	    "variations": [

	      {

	        "content": "Check out our latest blog post! #marketing #socialmedia",

	        "mentions": [

	          {

	            "platform": "instagram",

	            "username": "example_user",

	            "offset": 10,

	            "length": 12

	          }

	        ],

	        "ogTags": {

	          "metaLink": "https://example.com/blog/post-title",

	          "metaImage": "https://example.com/images/preview.png",

	          "ogTitle": "Check out our latest blog post!"

	        }

	      }

	    ],

	    "primaryImage": "http://example.com/media.png"

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

	var req = unirest('PUT', 'https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/items/:itemId')

	  .headers({

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  })

	  .send(JSON.stringify({

	    "locationId": "609e126a1c4ae1001291e1b5",

	    "sessionId": "60af88475f1b2c001f5d5f4b",

	    "modifiedPostPayload": {

	      "accountIds": [

	        "aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496"

	      ],

	      "summary": "Hello World",

	      "media": [

	        {

	          "url": "https://example.com/image.jpg",

	          "type": "image/jpeg",

	          "caption": "Sample caption"

	        }

	      ],

	      "status": "scheduled",

	      "scheduleDate": "2024-01-15T10:00:00Z",

	      "selectedBestTime": "2024-01-15T10:00:00Z",

	      "createdBy": "Lx1EI6YIgQYMQi0ytFXv",

	      "followUpComment": "What do you think? Let us know in the comments!",

	      "ogTagsDetails": {

	        "metaImage": "https://example.com/image.jpg",

	        "metaLink": "https://www.yahoo.com/",

	        "ogTitle": "Page Title",

	        "ogDescription": "Page Description"

	      },

	      "type": "post",

	      "postApprovalDetails": {

	        "approver": "iVrVJ2uoXNF0wzcBzgl5",

	        "approvalStatus": "pending"

	      },

	      "scheduleTimeUpdated": true,

	      "tags": [

	        "65f151c99bc2bf3aaf970d72",

	        "65f151c99bc2bf3aaf970d73"

	      ],

	      "categoryId": "65f151c99bc2bf3aaf970d72",

	      "applyWatermark": true,

	      "tiktokPostDetails": {

	        "privacyLevel": "PUBLIC_TO_EVERYONE",

	        "enableComment": true,

	        "enableDuet": false

	      },

	      "gmbPostDetails": {

	        "gmbEventType": "STANDARD",

	        "actionType": "BOOK",

	        "url": "https://example.com"

	      },

	      "userId": "sdfdsfdsfEWEsdfsdsW32dd",

	      "linkedinPostDetails": {

	        "pdfTitle": "Q4 Marketing Strategy Presentation",

	        "postAsPdf": true

	      },

	      "pinterestPostDetails": {

	        "title": "10 Easy Home Decor Ideas for 2024",

	        "link": "https://yoursite.com/blog/home-decor-ideas",

	        "boardIds": {

	          "6887d6de1d8175813d50dab8": "987654321098765432",

	          "682c7d1710a2fe3d805a3513": "123456789012345678"

	        },

	        "shortenedLinks": [

	          "string"

	        ]

	      },

	      "facebookPostDetails": {

	        "type": "post"

	      },

	      "instagramPostDetails": {

	        "type": "post",

	        "collaborators": {

	          "accountId1": [

	            "username1",

	            "username2"

	          ],

	          "accountId2": [

	            "username3",

	            "username4"

	          ]

	        },

	        "showOnFeed": true,

	        "publishViaPushNotification": true,

	        "publisherNote": "When publishing, add swipe up link to the landing page so that we can direct them to the sales page"

	      },

	      "youtubePostDetails": {

	        "title": "How to Build a Successful Marketing Strategy in 2024",

	        "privacyLevel": "public",

	        "type": "video"

	      },

	      "communityPostDetails": {

	        "title": "Welcome to Our New Community Feature!",

	        "notifyAllGroupMembers": true,

	        "postAsUser": {

	          "xMQswA02zgqKPpxITe": {

	            "avatar": "https://lh3.googleusercontent.com/a/user-avatar.jpg",

	            "id": "snCr14eeYkSppD04rkNW",

	            "name": "John Smith"

	          }

	        }

	      },

	      "locationId": "ve9EPM428h8vShlRW1KT"

	    },

	    "newOrder": 0,

	    "variations": [

	      {

	        "content": "Check out our latest blog post! #marketing #socialmedia",

	        "mentions": [

	          {

	            "platform": "instagram",

	            "username": "example_user",

	            "offset": 10,

	            "length": 12

	          }

	        ],

	        "ogTags": {

	          "metaLink": "https://example.com/blog/post-title",

	          "metaImage": "https://example.com/images/preview.png",

	          "ogTitle": "Check out our latest blog post!"

	        }

	      }

	    ],

	    "primaryImage": "http://example.com/media.png"

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

	  "locationId": "609e126a1c4ae1001291e1b5",

	  "sessionId": "60af88475f1b2c001f5d5f4b",

	  "modifiedPostPayload": {

	    "accountIds": [

	      "aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496"

	    ],

	    "summary": "Hello World",

	    "media": [

	      {

	        "url": "https://example.com/image.jpg",

	        "type": "image/jpeg",

	        "caption": "Sample caption"

	      }

	    ],

	    "status": "scheduled",

	    "scheduleDate": "2024-01-15T10:00:00Z",

	    "selectedBestTime": "2024-01-15T10:00:00Z",

	    "createdBy": "Lx1EI6YIgQYMQi0ytFXv",

	    "followUpComment": "What do you think? Let us know in the comments!",

	    "ogTagsDetails": {

	      "metaImage": "https://example.com/image.jpg",

	      "metaLink": "https://www.yahoo.com/",

	      "ogTitle": "Page Title",

	      "ogDescription": "Page Description"

	    },

	    "type": "post",

	    "postApprovalDetails": {

	      "approver": "iVrVJ2uoXNF0wzcBzgl5",

	      "approvalStatus": "pending"

	    },

	    "scheduleTimeUpdated": True,

	    "tags": [

	      "65f151c99bc2bf3aaf970d72",

	      "65f151c99bc2bf3aaf970d73"

	    ],

	    "categoryId": "65f151c99bc2bf3aaf970d72",

	    "applyWatermark": True,

	    "tiktokPostDetails": {

	      "privacyLevel": "PUBLIC_TO_EVERYONE",

	      "enableComment": True,

	      "enableDuet": False

	    },

	    "gmbPostDetails": {

	      "gmbEventType": "STANDARD",

	      "actionType": "BOOK",

	      "url": "https://example.com"

	    },

	    "userId": "sdfdsfdsfEWEsdfsdsW32dd",

	    "linkedinPostDetails": {

	      "pdfTitle": "Q4 Marketing Strategy Presentation",

	      "postAsPdf": True

	    },

	    "pinterestPostDetails": {

	      "title": "10 Easy Home Decor Ideas for 2024",

	      "link": "https://yoursite.com/blog/home-decor-ideas",

	      "boardIds": {

	        "6887d6de1d8175813d50dab8": "987654321098765432",

	        "682c7d1710a2fe3d805a3513": "123456789012345678"

	      },

	      "shortenedLinks": [

	        "string"

	      ]

	    },

	    "facebookPostDetails": {

	      "type": "post"

	    },

	    "instagramPostDetails": {

	      "type": "post",

	      "collaborators": {

	        "accountId1": [

	          "username1",

	          "username2"

	        ],

	        "accountId2": [

	          "username3",

	          "username4"

	        ]

	      },

	      "showOnFeed": True,

	      "publishViaPushNotification": True,

	      "publisherNote": "When publishing, add swipe up link to the landing page so that we can direct them to the sales page"

	    },

	    "youtubePostDetails": {

	      "title": "How to Build a Successful Marketing Strategy in 2024",

	      "privacyLevel": "public",

	      "type": "video"

	    },

	    "communityPostDetails": {

	      "title": "Welcome to Our New Community Feature!",

	      "notifyAllGroupMembers": True,

	      "postAsUser": {

	        "xMQswA02zgqKPpxITe": {

	          "avatar": "https://lh3.googleusercontent.com/a/user-avatar.jpg",

	          "id": "snCr14eeYkSppD04rkNW",

	          "name": "John Smith"

	        }

	      }

	    },

	    "locationId": "ve9EPM428h8vShlRW1KT"

	  },

	  "newOrder": 0,

	  "variations": [

	    {

	      "content": "Check out our latest blog post! #marketing #socialmedia",

	      "mentions": [

	        {

	          "platform": "instagram",

	          "username": "example_user",

	          "offset": 10,

	          "length": 12

	        }

	      ],

	      "ogTags": {

	        "metaLink": "https://example.com/blog/post-title",

	        "metaImage": "https://example.com/images/preview.png",

	        "ogTitle": "Check out our latest blog post!"

	      }

	    }

	  ],

	  "primaryImage": "http://example.com/media.png"

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json',

	  'Authorization': 'Bearer <TOKEN>'

	}

	conn.request("PUT", "/social-media-posting/category/queues/:queueId/items/:itemId", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	import json

	

	url = "https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/items/:itemId"

	

	payload = json.dumps({

	  "locationId": "609e126a1c4ae1001291e1b5",

	  "sessionId": "60af88475f1b2c001f5d5f4b",

	  "modifiedPostPayload": {

	    "accountIds": [

	      "aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496"

	    ],

	    "summary": "Hello World",

	    "media": [

	      {

	        "url": "https://example.com/image.jpg",

	        "type": "image/jpeg",

	        "caption": "Sample caption"

	      }

	    ],

	    "status": "scheduled",

	    "scheduleDate": "2024-01-15T10:00:00Z",

	    "selectedBestTime": "2024-01-15T10:00:00Z",

	    "createdBy": "Lx1EI6YIgQYMQi0ytFXv",

	    "followUpComment": "What do you think? Let us know in the comments!",

	    "ogTagsDetails": {

	      "metaImage": "https://example.com/image.jpg",

	      "metaLink": "https://www.yahoo.com/",

	      "ogTitle": "Page Title",

	      "ogDescription": "Page Description"

	    },

	    "type": "post",

	    "postApprovalDetails": {

	      "approver": "iVrVJ2uoXNF0wzcBzgl5",

	      "approvalStatus": "pending"

	    },

	    "scheduleTimeUpdated": True,

	    "tags": [

	      "65f151c99bc2bf3aaf970d72",

	      "65f151c99bc2bf3aaf970d73"

	    ],

	    "categoryId": "65f151c99bc2bf3aaf970d72",

	    "applyWatermark": True,

	    "tiktokPostDetails": {

	      "privacyLevel": "PUBLIC_TO_EVERYONE",

	      "enableComment": True,

	      "enableDuet": False

	    },

	    "gmbPostDetails": {

	      "gmbEventType": "STANDARD",

	      "actionType": "BOOK",

	      "url": "https://example.com"

	    },

	    "userId": "sdfdsfdsfEWEsdfsdsW32dd",

	    "linkedinPostDetails": {

	      "pdfTitle": "Q4 Marketing Strategy Presentation",

	      "postAsPdf": True

	    },

	    "pinterestPostDetails": {

	      "title": "10 Easy Home Decor Ideas for 2024",

	      "link": "https://yoursite.com/blog/home-decor-ideas",

	      "boardIds": {

	        "6887d6de1d8175813d50dab8": "987654321098765432",

	        "682c7d1710a2fe3d805a3513": "123456789012345678"

	      },

	      "shortenedLinks": [

	        "string"

	      ]

	    },

	    "facebookPostDetails": {

	      "type": "post"

	    },

	    "instagramPostDetails": {

	      "type": "post",

	      "collaborators": {

	        "accountId1": [

	          "username1",

	          "username2"

	        ],

	        "accountId2": [

	          "username3",

	          "username4"

	        ]

	      },

	      "showOnFeed": True,

	      "publishViaPushNotification": True,

	      "publisherNote": "When publishing, add swipe up link to the landing page so that we can direct them to the sales page"

	    },

	    "youtubePostDetails": {

	      "title": "How to Build a Successful Marketing Strategy in 2024",

	      "privacyLevel": "public",

	      "type": "video"

	    },

	    "communityPostDetails": {

	      "title": "Welcome to Our New Community Feature!",

	      "notifyAllGroupMembers": True,

	      "postAsUser": {

	        "xMQswA02zgqKPpxITe": {

	          "avatar": "https://lh3.googleusercontent.com/a/user-avatar.jpg",

	          "id": "snCr14eeYkSppD04rkNW",

	          "name": "John Smith"

	        }

	      }

	    },

	    "locationId": "ve9EPM428h8vShlRW1KT"

	  },

	  "newOrder": 0,

	  "variations": [

	    {

	      "content": "Check out our latest blog post! #marketing #socialmedia",

	      "mentions": [

	        {

	          "platform": "instagram",

	          "username": "example_user",

	          "offset": 10,

	          "length": 12

	        }

	      ],

	      "ogTags": {

	        "metaLink": "https://example.com/blog/post-title",

	        "metaImage": "https://example.com/images/preview.png",

	        "ogTitle": "Check out our latest blog post!"

	      }

	    }

	  ],

	  "primaryImage": "http://example.com/media.png"

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/items/:itemId',

	  CURLOPT_RETURNTRANSFER => true,

	  CURLOPT_ENCODING => '',

	  CURLOPT_MAXREDIRS => 10,

	  CURLOPT_TIMEOUT => 0,

	  CURLOPT_FOLLOWLOCATION => true,

	  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,

	  CURLOPT_CUSTOMREQUEST => 'PUT',

	  CURLOPT_POSTFIELDS =>'{

	  "locationId": "609e126a1c4ae1001291e1b5",

	  "sessionId": "60af88475f1b2c001f5d5f4b",

	  "modifiedPostPayload": {

	    "accountIds": [

	      "aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496"

	    ],

	    "summary": "Hello World",

	    "media": [

	      {

	        "url": "https://example.com/image.jpg",

	        "type": "image/jpeg",

	        "caption": "Sample caption"

	      }

	    ],

	    "status": "scheduled",

	    "scheduleDate": "2024-01-15T10:00:00Z",

	    "selectedBestTime": "2024-01-15T10:00:00Z",

	    "createdBy": "Lx1EI6YIgQYMQi0ytFXv",

	    "followUpComment": "What do you think? Let us know in the comments!",

	    "ogTagsDetails": {

	      "metaImage": "https://example.com/image.jpg",

	      "metaLink": "https://www.yahoo.com/",

	      "ogTitle": "Page Title",

	      "ogDescription": "Page Description"

	    },

	    "type": "post",

	    "postApprovalDetails": {

	      "approver": "iVrVJ2uoXNF0wzcBzgl5",

	      "approvalStatus": "pending"

	    },

	    "scheduleTimeUpdated": true,

	    "tags": [

	      "65f151c99bc2bf3aaf970d72",

	      "65f151c99bc2bf3aaf970d73"

	    ],

	    "categoryId": "65f151c99bc2bf3aaf970d72",

	    "applyWatermark": true,

	    "tiktokPostDetails": {

	      "privacyLevel": "PUBLIC_TO_EVERYONE",

	      "enableComment": true,

	      "enableDuet": false

	    },

	    "gmbPostDetails": {

	      "gmbEventType": "STANDARD",

	      "actionType": "BOOK",

	      "url": "https://example.com"

	    },

	    "userId": "sdfdsfdsfEWEsdfsdsW32dd",

	    "linkedinPostDetails": {

	      "pdfTitle": "Q4 Marketing Strategy Presentation",

	      "postAsPdf": true

	    },

	    "pinterestPostDetails": {

	      "title": "10 Easy Home Decor Ideas for 2024",

	      "link": "https://yoursite.com/blog/home-decor-ideas",

	      "boardIds": {

	        "6887d6de1d8175813d50dab8": "987654321098765432",

	        "682c7d1710a2fe3d805a3513": "123456789012345678"

	      },

	      "shortenedLinks": [

	        "string"

	      ]

	    },

	    "facebookPostDetails": {

	      "type": "post"

	    },

	    "instagramPostDetails": {

	      "type": "post",

	      "collaborators": {

	        "accountId1": [

	          "username1",

	          "username2"

	        ],

	        "accountId2": [

	          "username3",

	          "username4"

	        ]

	      },

	      "showOnFeed": true,

	      "publishViaPushNotification": true,

	      "publisherNote": "When publishing, add swipe up link to the landing page so that we can direct them to the sales page"

	    },

	    "youtubePostDetails": {

	      "title": "How to Build a Successful Marketing Strategy in 2024",

	      "privacyLevel": "public",

	      "type": "video"

	    },

	    "communityPostDetails": {

	      "title": "Welcome to Our New Community Feature!",

	      "notifyAllGroupMembers": true,

	      "postAsUser": {

	        "xMQswA02zgqKPpxITe": {

	          "avatar": "https://lh3.googleusercontent.com/a/user-avatar.jpg",

	          "id": "snCr14eeYkSppD04rkNW",

	          "name": "John Smith"

	        }

	      }

	    },

	    "locationId": "ve9EPM428h8vShlRW1KT"

	  },

	  "newOrder": 0,

	  "variations": [

	    {

	      "content": "Check out our latest blog post! #marketing #socialmedia",

	      "mentions": [

	        {

	          "platform": "instagram",

	          "username": "example_user",

	          "offset": 10,

	          "length": 12

	        }

	      ],

	      "ogTags": {

	        "metaLink": "https://example.com/blog/post-title",

	        "metaImage": "https://example.com/images/preview.png",

	        "ogTitle": "Check out our latest blog post!"

	      }

	    }

	  ],

	  "primaryImage": "http://example.com/media.png"

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

	  "locationId": "609e126a1c4ae1001291e1b5",

	  "sessionId": "60af88475f1b2c001f5d5f4b",

	  "modifiedPostPayload": {

	    "accountIds": [

	      "aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496"

	    ],

	    "summary": "Hello World",

	    "media": [

	      {

	        "url": "https://example.com/image.jpg",

	        "type": "image/jpeg",

	        "caption": "Sample caption"

	      }

	    ],

	    "status": "scheduled",

	    "scheduleDate": "2024-01-15T10:00:00Z",

	    "selectedBestTime": "2024-01-15T10:00:00Z",

	    "createdBy": "Lx1EI6YIgQYMQi0ytFXv",

	    "followUpComment": "What do you think? Let us know in the comments!",

	    "ogTagsDetails": {

	      "metaImage": "https://example.com/image.jpg",

	      "metaLink": "https://www.yahoo.com/",

	      "ogTitle": "Page Title",

	      "ogDescription": "Page Description"

	    },

	    "type": "post",

	    "postApprovalDetails": {

	      "approver": "iVrVJ2uoXNF0wzcBzgl5",

	      "approvalStatus": "pending"

	    },

	    "scheduleTimeUpdated": true,

	    "tags": [

	      "65f151c99bc2bf3aaf970d72",

	      "65f151c99bc2bf3aaf970d73"

	    ],

	    "categoryId": "65f151c99bc2bf3aaf970d72",

	    "applyWatermark": true,

	    "tiktokPostDetails": {

	      "privacyLevel": "PUBLIC_TO_EVERYONE",

	      "enableComment": true,

	      "enableDuet": false

	    },

	    "gmbPostDetails": {

	      "gmbEventType": "STANDARD",

	      "actionType": "BOOK",

	      "url": "https://example.com"

	    },

	    "userId": "sdfdsfdsfEWEsdfsdsW32dd",

	    "linkedinPostDetails": {

	      "pdfTitle": "Q4 Marketing Strategy Presentation",

	      "postAsPdf": true

	    },

	    "pinterestPostDetails": {

	      "title": "10 Easy Home Decor Ideas for 2024",

	      "link": "https://yoursite.com/blog/home-decor-ideas",

	      "boardIds": {

	        "6887d6de1d8175813d50dab8": "987654321098765432",

	        "682c7d1710a2fe3d805a3513": "123456789012345678"

	      },

	      "shortenedLinks": [

	        "string"

	      ]

	    },

	    "facebookPostDetails": {

	      "type": "post"

	    },

	    "instagramPostDetails": {

	      "type": "post",

	      "collaborators": {

	        "accountId1": [

	          "username1",

	          "username2"

	        ],

	        "accountId2": [

	          "username3",

	          "username4"

	        ]

	      },

	      "showOnFeed": true,

	      "publishViaPushNotification": true,

	      "publisherNote": "When publishing, add swipe up link to the landing page so that we can direct them to the sales page"

	    },

	    "youtubePostDetails": {

	      "title": "How to Build a Successful Marketing Strategy in 2024",

	      "privacyLevel": "public",

	      "type": "video"

	    },

	    "communityPostDetails": {

	      "title": "Welcome to Our New Community Feature!",

	      "notifyAllGroupMembers": true,

	      "postAsUser": {

	        "xMQswA02zgqKPpxITe": {

	          "avatar": "https://lh3.googleusercontent.com/a/user-avatar.jpg",

	          "id": "snCr14eeYkSppD04rkNW",

	          "name": "John Smith"

	        }

	      }

	    },

	    "locationId": "ve9EPM428h8vShlRW1KT"

	  },

	  "newOrder": 0,

	  "variations": [

	    {

	      "content": "Check out our latest blog post! #marketing #socialmedia",

	      "mentions": [

	        {

	          "platform": "instagram",

	          "username": "example_user",

	          "offset": 10,

	          "length": 12

	        }

	      ],

	      "ogTags": {

	        "metaLink": "https://example.com/blog/post-title",

	        "metaImage": "https://example.com/images/preview.png",

	        "ogTitle": "Check out our latest blog post!"

	      }

	    }

	  ],

	  "primaryImage": "http://example.com/media.png"

	}';

	$request = new Request('PUT', 'https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/items/:itemId', $headers, $body);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/items/:itemId');

	$request->setMethod(HTTP_Request2::METHOD_PUT);

	$request->setConfig(array(

	  'follow_redirects' => TRUE

	));

	$request->setHeader(array(

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json',

	  'Authorization' => 'Bearer <TOKEN>'

	));

	$request->setBody('{\n  "locationId": "609e126a1c4ae1001291e1b5",\n  "sessionId": "60af88475f1b2c001f5d5f4b",\n  "modifiedPostPayload": {\n    "accountIds": [\n      "aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496"\n    ],\n    "summary": "Hello World",\n    "media": [\n      {\n        "url": "https://example.com/image.jpg",\n        "type": "image/jpeg",\n        "caption": "Sample caption"\n      }\n    ],\n    "status": "scheduled",\n    "scheduleDate": "2024-01-15T10:00:00Z",\n    "selectedBestTime": "2024-01-15T10:00:00Z",\n    "createdBy": "Lx1EI6YIgQYMQi0ytFXv",\n    "followUpComment": "What do you think? Let us know in the comments!",\n    "ogTagsDetails": {\n      "metaImage": "https://example.com/image.jpg",\n      "metaLink": "https://www.yahoo.com/",\n      "ogTitle": "Page Title",\n      "ogDescription": "Page Description"\n    },\n    "type": "post",\n    "postApprovalDetails": {\n      "approver": "iVrVJ2uoXNF0wzcBzgl5",\n      "approvalStatus": "pending"\n    },\n    "scheduleTimeUpdated": true,\n    "tags": [\n      "65f151c99bc2bf3aaf970d72",\n      "65f151c99bc2bf3aaf970d73"\n    ],\n    "categoryId": "65f151c99bc2bf3aaf970d72",\n    "applyWatermark": true,\n    "tiktokPostDetails": {\n      "privacyLevel": "PUBLIC_TO_EVERYONE",\n      "enableComment": true,\n      "enableDuet": false\n    },\n    "gmbPostDetails": {\n      "gmbEventType": "STANDARD",\n      "actionType": "BOOK",\n      "url": "https://example.com"\n    },\n    "userId": "sdfdsfdsfEWEsdfsdsW32dd",\n    "linkedinPostDetails": {\n      "pdfTitle": "Q4 Marketing Strategy Presentation",\n      "postAsPdf": true\n    },\n    "pinterestPostDetails": {\n      "title": "10 Easy Home Decor Ideas for 2024",\n      "link": "https://yoursite.com/blog/home-decor-ideas",\n      "boardIds": {\n        "6887d6de1d8175813d50dab8": "987654321098765432",\n        "682c7d1710a2fe3d805a3513": "123456789012345678"\n      },\n      "shortenedLinks": [\n        "string"\n      ]\n    },\n    "facebookPostDetails": {\n      "type": "post"\n    },\n    "instagramPostDetails": {\n      "type": "post",\n      "collaborators": {\n        "accountId1": [\n          "username1",\n          "username2"\n        ],\n        "accountId2": [\n          "username3",\n          "username4"\n        ]\n      },\n      "showOnFeed": true,\n      "publishViaPushNotification": true,\n      "publisherNote": "When publishing, add swipe up link to the landing page so that we can direct them to the sales page"\n    },\n    "youtubePostDetails": {\n      "title": "How to Build a Successful Marketing Strategy in 2024",\n      "privacyLevel": "public",\n      "type": "video"\n    },\n    "communityPostDetails": {\n      "title": "Welcome to Our New Community Feature!",\n      "notifyAllGroupMembers": true,\n      "postAsUser": {\n        "xMQswA02zgqKPpxITe": {\n          "avatar": "https://lh3.googleusercontent.com/a/user-avatar.jpg",\n          "id": "snCr14eeYkSppD04rkNW",\n          "name": "John Smith"\n        }\n      }\n    },\n    "locationId": "ve9EPM428h8vShlRW1KT"\n  },\n  "newOrder": 0,\n  "variations": [\n    {\n      "content": "Check out our latest blog post! #marketing #socialmedia",\n      "mentions": [\n        {\n          "platform": "instagram",\n          "username": "example_user",\n          "offset": 10,\n          "length": 12\n        }\n      ],\n      "ogTags": {\n        "metaLink": "https://example.com/blog/post-title",\n        "metaImage": "https://example.com/images/preview.png",\n        "ogTitle": "Check out our latest blog post!"\n      }\n    }\n  ],\n  "primaryImage": "http://example.com/media.png"\n}');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/items/:itemId');

	$request->setRequestMethod('PUT');

	$body = new http\Message\Body;

	$body->append('{

	  "locationId": "609e126a1c4ae1001291e1b5",

	  "sessionId": "60af88475f1b2c001f5d5f4b",

	  "modifiedPostPayload": {

	    "accountIds": [

	      "aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496"

	    ],

	    "summary": "Hello World",

	    "media": [

	      {

	        "url": "https://example.com/image.jpg",

	        "type": "image/jpeg",

	        "caption": "Sample caption"

	      }

	    ],

	    "status": "scheduled",

	    "scheduleDate": "2024-01-15T10:00:00Z",

	    "selectedBestTime": "2024-01-15T10:00:00Z",

	    "createdBy": "Lx1EI6YIgQYMQi0ytFXv",

	    "followUpComment": "What do you think? Let us know in the comments!",

	    "ogTagsDetails": {

	      "metaImage": "https://example.com/image.jpg",

	      "metaLink": "https://www.yahoo.com/",

	      "ogTitle": "Page Title",

	      "ogDescription": "Page Description"

	    },

	    "type": "post",

	    "postApprovalDetails": {

	      "approver": "iVrVJ2uoXNF0wzcBzgl5",

	      "approvalStatus": "pending"

	    },

	    "scheduleTimeUpdated": true,

	    "tags": [

	      "65f151c99bc2bf3aaf970d72",

	      "65f151c99bc2bf3aaf970d73"

	    ],

	    "categoryId": "65f151c99bc2bf3aaf970d72",

	    "applyWatermark": true,

	    "tiktokPostDetails": {

	      "privacyLevel": "PUBLIC_TO_EVERYONE",

	      "enableComment": true,

	      "enableDuet": false

	    },

	    "gmbPostDetails": {

	      "gmbEventType": "STANDARD",

	      "actionType": "BOOK",

	      "url": "https://example.com"

	    },

	    "userId": "sdfdsfdsfEWEsdfsdsW32dd",

	    "linkedinPostDetails": {

	      "pdfTitle": "Q4 Marketing Strategy Presentation",

	      "postAsPdf": true

	    },

	    "pinterestPostDetails": {

	      "title": "10 Easy Home Decor Ideas for 2024",

	      "link": "https://yoursite.com/blog/home-decor-ideas",

	      "boardIds": {

	        "6887d6de1d8175813d50dab8": "987654321098765432",

	        "682c7d1710a2fe3d805a3513": "123456789012345678"

	      },

	      "shortenedLinks": [

	        "string"

	      ]

	    },

	    "facebookPostDetails": {

	      "type": "post"

	    },

	    "instagramPostDetails": {

	      "type": "post",

	      "collaborators": {

	        "accountId1": [

	          "username1",

	          "username2"

	        ],

	        "accountId2": [

	          "username3",

	          "username4"

	        ]

	      },

	      "showOnFeed": true,

	      "publishViaPushNotification": true,

	      "publisherNote": "When publishing, add swipe up link to the landing page so that we can direct them to the sales page"

	    },

	    "youtubePostDetails": {

	      "title": "How to Build a Successful Marketing Strategy in 2024",

	      "privacyLevel": "public",

	      "type": "video"

	    },

	    "communityPostDetails": {

	      "title": "Welcome to Our New Community Feature!",

	      "notifyAllGroupMembers": true,

	      "postAsUser": {

	        "xMQswA02zgqKPpxITe": {

	          "avatar": "https://lh3.googleusercontent.com/a/user-avatar.jpg",

	          "id": "snCr14eeYkSppD04rkNW",

	          "name": "John Smith"

	        }

	      }

	    },

	    "locationId": "ve9EPM428h8vShlRW1KT"

	  },

	  "newOrder": 0,

	  "variations": [

	    {

	      "content": "Check out our latest blog post! #marketing #socialmedia",

	      "mentions": [

	        {

	          "platform": "instagram",

	          "username": "example_user",

	          "offset": 10,

	          "length": 12

	        }

	      ],

	      "ogTags": {

	        "metaLink": "https://example.com/blog/post-title",

	        "metaImage": "https://example.com/images/preview.png",

	        "ogTitle": "Check out our latest blog post!"

	      }

	    }

	  ],

	  "primaryImage": "http://example.com/media.png"

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

	RequestBody body = RequestBody.create(mediaType, "{\n  \"locationId\": \"609e126a1c4ae1001291e1b5\",\n  \"sessionId\": \"60af88475f1b2c001f5d5f4b\",\n  \"modifiedPostPayload\": {\n    \"accountIds\": [\n      \"aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496\"\n    ],\n    \"summary\": \"Hello World\",\n    \"media\": [\n      {\n        \"url\": \"https://example.com/image.jpg\",\n        \"type\": \"image/jpeg\",\n        \"caption\": \"Sample caption\"\n      }\n    ],\n    \"status\": \"scheduled\",\n    \"scheduleDate\": \"2024-01-15T10:00:00Z\",\n    \"selectedBestTime\": \"2024-01-15T10:00:00Z\",\n    \"createdBy\": \"Lx1EI6YIgQYMQi0ytFXv\",\n    \"followUpComment\": \"What do you think? Let us know in the comments!\",\n    \"ogTagsDetails\": {\n      \"metaImage\": \"https://example.com/image.jpg\",\n      \"metaLink\": \"https://www.yahoo.com/\",\n      \"ogTitle\": \"Page Title\",\n      \"ogDescription\": \"Page Description\"\n    },\n    \"type\": \"post\",\n    \"postApprovalDetails\": {\n      \"approver\": \"iVrVJ2uoXNF0wzcBzgl5\",\n      \"approvalStatus\": \"pending\"\n    },\n    \"scheduleTimeUpdated\": true,\n    \"tags\": [\n      \"65f151c99bc2bf3aaf970d72\",\n      \"65f151c99bc2bf3aaf970d73\"\n    ],\n    \"categoryId\": \"65f151c99bc2bf3aaf970d72\",\n    \"applyWatermark\": true,\n    \"tiktokPostDetails\": {\n      \"privacyLevel\": \"PUBLIC_TO_EVERYONE\",\n      \"enableComment\": true,\n      \"enableDuet\": false\n    },\n    \"gmbPostDetails\": {\n      \"gmbEventType\": \"STANDARD\",\n      \"actionType\": \"BOOK\",\n      \"url\": \"https://example.com\"\n    },\n    \"userId\": \"sdfdsfdsfEWEsdfsdsW32dd\",\n    \"linkedinPostDetails\": {\n      \"pdfTitle\": \"Q4 Marketing Strategy Presentation\",\n      \"postAsPdf\": true\n    },\n    \"pinterestPostDetails\": {\n      \"title\": \"10 Easy Home Decor Ideas for 2024\",\n      \"link\": \"https://yoursite.com/blog/home-decor-ideas\",\n      \"boardIds\": {\n        \"6887d6de1d8175813d50dab8\": \"987654321098765432\",\n        \"682c7d1710a2fe3d805a3513\": \"123456789012345678\"\n      },\n      \"shortenedLinks\": [\n        \"string\"\n      ]\n    },\n    \"facebookPostDetails\": {\n      \"type\": \"post\"\n    },\n    \"instagramPostDetails\": {\n      \"type\": \"post\",\n      \"collaborators\": {\n        \"accountId1\": [\n          \"username1\",\n          \"username2\"\n        ],\n        \"accountId2\": [\n          \"username3\",\n          \"username4\"\n        ]\n      },\n      \"showOnFeed\": true,\n      \"publishViaPushNotification\": true,\n      \"publisherNote\": \"When publishing, add swipe up link to the landing page so that we can direct them to the sales page\"\n    },\n    \"youtubePostDetails\": {\n      \"title\": \"How to Build a Successful Marketing Strategy in 2024\",\n      \"privacyLevel\": \"public\",\n      \"type\": \"video\"\n    },\n    \"communityPostDetails\": {\n      \"title\": \"Welcome to Our New Community Feature!\",\n      \"notifyAllGroupMembers\": true,\n      \"postAsUser\": {\n        \"xMQswA02zgqKPpxITe\": {\n          \"avatar\": \"https://lh3.googleusercontent.com/a/user-avatar.jpg\",\n          \"id\": \"snCr14eeYkSppD04rkNW\",\n          \"name\": \"John Smith\"\n        }\n      }\n    },\n    \"locationId\": \"ve9EPM428h8vShlRW1KT\"\n  },\n  \"newOrder\": 0,\n  \"variations\": [\n    {\n      \"content\": \"Check out our latest blog post! #marketing #socialmedia\",\n      \"mentions\": [\n        {\n          \"platform\": \"instagram\",\n          \"username\": \"example_user\",\n          \"offset\": 10,\n          \"length\": 12\n        }\n      ],\n      \"ogTags\": {\n        \"metaLink\": \"https://example.com/blog/post-title\",\n        \"metaImage\": \"https://example.com/images/preview.png\",\n        \"ogTitle\": \"Check out our latest blog post!\"\n      }\n    }\n  ],\n  \"primaryImage\": \"http://example.com/media.png\"\n}");

	Request request = new Request.Builder()

	  .url("https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/items/:itemId")

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

	HttpResponse<String> response = Unirest.put("https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/items/:itemId")

	  .header("Content-Type", "application/json")

	  .header("Accept", "application/json")

	  .header("Authorization", "Bearer <TOKEN>")

	  .body("{\n  \"locationId\": \"609e126a1c4ae1001291e1b5\",\n  \"sessionId\": \"60af88475f1b2c001f5d5f4b\",\n  \"modifiedPostPayload\": {\n    \"accountIds\": [\n      \"aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496\"\n    ],\n    \"summary\": \"Hello World\",\n    \"media\": [\n      {\n        \"url\": \"https://example.com/image.jpg\",\n        \"type\": \"image/jpeg\",\n        \"caption\": \"Sample caption\"\n      }\n    ],\n    \"status\": \"scheduled\",\n    \"scheduleDate\": \"2024-01-15T10:00:00Z\",\n    \"selectedBestTime\": \"2024-01-15T10:00:00Z\",\n    \"createdBy\": \"Lx1EI6YIgQYMQi0ytFXv\",\n    \"followUpComment\": \"What do you think? Let us know in the comments!\",\n    \"ogTagsDetails\": {\n      \"metaImage\": \"https://example.com/image.jpg\",\n      \"metaLink\": \"https://www.yahoo.com/\",\n      \"ogTitle\": \"Page Title\",\n      \"ogDescription\": \"Page Description\"\n    },\n    \"type\": \"post\",\n    \"postApprovalDetails\": {\n      \"approver\": \"iVrVJ2uoXNF0wzcBzgl5\",\n      \"approvalStatus\": \"pending\"\n    },\n    \"scheduleTimeUpdated\": true,\n    \"tags\": [\n      \"65f151c99bc2bf3aaf970d72\",\n      \"65f151c99bc2bf3aaf970d73\"\n    ],\n    \"categoryId\": \"65f151c99bc2bf3aaf970d72\",\n    \"applyWatermark\": true,\n    \"tiktokPostDetails\": {\n      \"privacyLevel\": \"PUBLIC_TO_EVERYONE\",\n      \"enableComment\": true,\n      \"enableDuet\": false\n    },\n    \"gmbPostDetails\": {\n      \"gmbEventType\": \"STANDARD\",\n      \"actionType\": \"BOOK\",\n      \"url\": \"https://example.com\"\n    },\n    \"userId\": \"sdfdsfdsfEWEsdfsdsW32dd\",\n    \"linkedinPostDetails\": {\n      \"pdfTitle\": \"Q4 Marketing Strategy Presentation\",\n      \"postAsPdf\": true\n    },\n    \"pinterestPostDetails\": {\n      \"title\": \"10 Easy Home Decor Ideas for 2024\",\n      \"link\": \"https://yoursite.com/blog/home-decor-ideas\",\n      \"boardIds\": {\n        \"6887d6de1d8175813d50dab8\": \"987654321098765432\",\n        \"682c7d1710a2fe3d805a3513\": \"123456789012345678\"\n      },\n      \"shortenedLinks\": [\n        \"string\"\n      ]\n    },\n    \"facebookPostDetails\": {\n      \"type\": \"post\"\n    },\n    \"instagramPostDetails\": {\n      \"type\": \"post\",\n      \"collaborators\": {\n        \"accountId1\": [\n          \"username1\",\n          \"username2\"\n        ],\n        \"accountId2\": [\n          \"username3\",\n          \"username4\"\n        ]\n      },\n      \"showOnFeed\": true,\n      \"publishViaPushNotification\": true,\n      \"publisherNote\": \"When publishing, add swipe up link to the landing page so that we can direct them to the sales page\"\n    },\n    \"youtubePostDetails\": {\n      \"title\": \"How to Build a Successful Marketing Strategy in 2024\",\n      \"privacyLevel\": \"public\",\n      \"type\": \"video\"\n    },\n    \"communityPostDetails\": {\n      \"title\": \"Welcome to Our New Community Feature!\",\n      \"notifyAllGroupMembers\": true,\n      \"postAsUser\": {\n        \"xMQswA02zgqKPpxITe\": {\n          \"avatar\": \"https://lh3.googleusercontent.com/a/user-avatar.jpg\",\n          \"id\": \"snCr14eeYkSppD04rkNW\",\n          \"name\": \"John Smith\"\n        }\n      }\n    },\n    \"locationId\": \"ve9EPM428h8vShlRW1KT\"\n  },\n  \"newOrder\": 0,\n  \"variations\": [\n    {\n      \"content\": \"Check out our latest blog post! #marketing #socialmedia\",\n      \"mentions\": [\n        {\n          \"platform\": \"instagram\",\n          \"username\": \"example_user\",\n          \"offset\": 10,\n          \"length\": 12\n        }\n      ],\n      \"ogTags\": {\n        \"metaLink\": \"https://example.com/blog/post-title\",\n        \"metaImage\": \"https://example.com/images/preview.png\",\n        \"ogTitle\": \"Check out our latest blog post!\"\n      }\n    }\n  ],\n  \"primaryImage\": \"http://example.com/media.png\"\n}")

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

	

	  url := "https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/items/:itemId"

	  method := "PUT"

	

	  payload := strings.NewReader(`{

	  "locationId": "609e126a1c4ae1001291e1b5",

	  "sessionId": "60af88475f1b2c001f5d5f4b",

	  "modifiedPostPayload": {

	    "accountIds": [

	      "aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496"

	    ],

	    "summary": "Hello World",

	    "media": [

	      {

	        "url": "https://example.com/image.jpg",

	        "type": "image/jpeg",

	        "caption": "Sample caption"

	      }

	    ],

	    "status": "scheduled",

	    "scheduleDate": "2024-01-15T10:00:00Z",

	    "selectedBestTime": "2024-01-15T10:00:00Z",

	    "createdBy": "Lx1EI6YIgQYMQi0ytFXv",

	    "followUpComment": "What do you think? Let us know in the comments!",

	    "ogTagsDetails": {

	      "metaImage": "https://example.com/image.jpg",

	      "metaLink": "https://www.yahoo.com/",

	      "ogTitle": "Page Title",

	      "ogDescription": "Page Description"

	    },

	    "type": "post",

	    "postApprovalDetails": {

	      "approver": "iVrVJ2uoXNF0wzcBzgl5",

	      "approvalStatus": "pending"

	    },

	    "scheduleTimeUpdated": true,

	    "tags": [

	      "65f151c99bc2bf3aaf970d72",

	      "65f151c99bc2bf3aaf970d73"

	    ],

	    "categoryId": "65f151c99bc2bf3aaf970d72",

	    "applyWatermark": true,

	    "tiktokPostDetails": {

	      "privacyLevel": "PUBLIC_TO_EVERYONE",

	      "enableComment": true,

	      "enableDuet": false

	    },

	    "gmbPostDetails": {

	      "gmbEventType": "STANDARD",

	      "actionType": "BOOK",

	      "url": "https://example.com"

	    },

	    "userId": "sdfdsfdsfEWEsdfsdsW32dd",

	    "linkedinPostDetails": {

	      "pdfTitle": "Q4 Marketing Strategy Presentation",

	      "postAsPdf": true

	    },

	    "pinterestPostDetails": {

	      "title": "10 Easy Home Decor Ideas for 2024",

	      "link": "https://yoursite.com/blog/home-decor-ideas",

	      "boardIds": {

	        "6887d6de1d8175813d50dab8": "987654321098765432",

	        "682c7d1710a2fe3d805a3513": "123456789012345678"

	      },

	      "shortenedLinks": [

	        "string"

	      ]

	    },

	    "facebookPostDetails": {

	      "type": "post"

	    },

	    "instagramPostDetails": {

	      "type": "post",

	      "collaborators": {

	        "accountId1": [

	          "username1",

	          "username2"

	        ],

	        "accountId2": [

	          "username3",

	          "username4"

	        ]

	      },

	      "showOnFeed": true,

	      "publishViaPushNotification": true,

	      "publisherNote": "When publishing, add swipe up link to the landing page so that we can direct them to the sales page"

	    },

	    "youtubePostDetails": {

	      "title": "How to Build a Successful Marketing Strategy in 2024",

	      "privacyLevel": "public",

	      "type": "video"

	    },

	    "communityPostDetails": {

	      "title": "Welcome to Our New Community Feature!",

	      "notifyAllGroupMembers": true,

	      "postAsUser": {

	        "xMQswA02zgqKPpxITe": {

	          "avatar": "https://lh3.googleusercontent.com/a/user-avatar.jpg",

	          "id": "snCr14eeYkSppD04rkNW",

	          "name": "John Smith"

	        }

	      }

	    },

	    "locationId": "ve9EPM428h8vShlRW1KT"

	  },

	  "newOrder": 0,

	  "variations": [

	    {

	      "content": "Check out our latest blog post! #marketing #socialmedia",

	      "mentions": [

	        {

	          "platform": "instagram",

	          "username": "example_user",

	          "offset": 10,

	          "length": 12

	        }

	      ],

	      "ogTags": {

	        "metaLink": "https://example.com/blog/post-title",

	        "metaImage": "https://example.com/images/preview.png",

	        "ogTitle": "Check out our latest blog post!"

	      }

	    }

	  ],

	  "primaryImage": "http://example.com/media.png"

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

	

	url = URI("https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/items/:itemId")

	

	https = Net::HTTP.new(url.host, url.port)

	https.use_ssl = true

	

	request = Net::HTTP::Put.new(url)

	request["Content-Type"] = "application/json"

	request["Accept"] = "application/json"

	request["Authorization"] = "Bearer <TOKEN>"

	request.body = JSON.dump({

	  "locationId": "609e126a1c4ae1001291e1b5",

	  "sessionId": "60af88475f1b2c001f5d5f4b",

	  "modifiedPostPayload": {

	    "accountIds": [

	      "aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496"

	    ],

	    "summary": "Hello World",

	    "media": [

	      {

	        "url": "https://example.com/image.jpg",

	        "type": "image/jpeg",

	        "caption": "Sample caption"

	      }

	    ],

	    "status": "scheduled",

	    "scheduleDate": "2024-01-15T10:00:00Z",

	    "selectedBestTime": "2024-01-15T10:00:00Z",

	    "createdBy": "Lx1EI6YIgQYMQi0ytFXv",

	    "followUpComment": "What do you think? Let us know in the comments\!",

	    "ogTagsDetails": {

	      "metaImage": "https://example.com/image.jpg",

	      "metaLink": "https://www.yahoo.com/",

	      "ogTitle": "Page Title",

	      "ogDescription": "Page Description"

	    },

	    "type": "post",

	    "postApprovalDetails": {

	      "approver": "iVrVJ2uoXNF0wzcBzgl5",

	      "approvalStatus": "pending"

	    },

	    "scheduleTimeUpdated": true,

	    "tags": [

	      "65f151c99bc2bf3aaf970d72",

	      "65f151c99bc2bf3aaf970d73"

	    ],

	    "categoryId": "65f151c99bc2bf3aaf970d72",

	    "applyWatermark": true,

	    "tiktokPostDetails": {

	      "privacyLevel": "PUBLIC_TO_EVERYONE",

	      "enableComment": true,

	      "enableDuet": false

	    },

	    "gmbPostDetails": {

	      "gmbEventType": "STANDARD",

	      "actionType": "BOOK",

	      "url": "https://example.com"

	    },

	    "userId": "sdfdsfdsfEWEsdfsdsW32dd",

	    "linkedinPostDetails": {

	      "pdfTitle": "Q4 Marketing Strategy Presentation",

	      "postAsPdf": true

	    },

	    "pinterestPostDetails": {

	      "title": "10 Easy Home Decor Ideas for 2024",

	      "link": "https://yoursite.com/blog/home-decor-ideas",

	      "boardIds": {

	        "6887d6de1d8175813d50dab8": "987654321098765432",

	        "682c7d1710a2fe3d805a3513": "123456789012345678"

	      },

	      "shortenedLinks": [

	        "string"

	      ]

	    },

	    "facebookPostDetails": {

	      "type": "post"

	    },

	    "instagramPostDetails": {

	      "type": "post",

	      "collaborators": {

	        "accountId1": [

	          "username1",

	          "username2"

	        ],

	        "accountId2": [

	          "username3",

	          "username4"

	        ]

	      },

	      "showOnFeed": true,

	      "publishViaPushNotification": true,

	      "publisherNote": "When publishing, add swipe up link to the landing page so that we can direct them to the sales page"

	    },

	    "youtubePostDetails": {

	      "title": "How to Build a Successful Marketing Strategy in 2024",

	      "privacyLevel": "public",

	      "type": "video"

	    },

	    "communityPostDetails": {

	      "title": "Welcome to Our New Community Feature\!",

	      "notifyAllGroupMembers": true,

	      "postAsUser": {

	        "xMQswA02zgqKPpxITe": {

	          "avatar": "https://lh3.googleusercontent.com/a/user-avatar.jpg",

	          "id": "snCr14eeYkSppD04rkNW",

	          "name": "John Smith"

	        }

	      }

	    },

	    "locationId": "ve9EPM428h8vShlRW1KT"

	  },

	  "newOrder": 0,

	  "variations": [

	    {

	      "content": "Check out our latest blog post\! \#marketing \#socialmedia",

	      "mentions": [

	        {

	          "platform": "instagram",

	          "username": "example_user",

	          "offset": 10,

	          "length": 12

	        }

	      ],

	      "ogTags": {

	        "metaLink": "https://example.com/blog/post-title",

	        "metaImage": "https://example.com/images/preview.png",

	        "ogTitle": "Check out our latest blog post\!"

	      }

	    }

	  ],

	  "primaryImage": "http://example.com/media.png"

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

	  `"locationId`": `"609e126a1c4ae1001291e1b5`",

	  `"sessionId`": `"60af88475f1b2c001f5d5f4b`",

	  `"modifiedPostPayload`": {

	    `"accountIds`": [

	      `"aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496`"

	    ],

	    `"summary`": `"Hello World`",

	    `"media`": [

	      {

	        `"url`": `"https://example.com/image.jpg`",

	        `"type`": `"image/jpeg`",

	        `"caption`": `"Sample caption`"

	      }

	    ],

	    `"status`": `"scheduled`",

	    `"scheduleDate`": `"2024-01-15T10:00:00Z`",

	    `"selectedBestTime`": `"2024-01-15T10:00:00Z`",

	    `"createdBy`": `"Lx1EI6YIgQYMQi0ytFXv`",

	    `"followUpComment`": `"What do you think? Let us know in the comments!`",

	    `"ogTagsDetails`": {

	      `"metaImage`": `"https://example.com/image.jpg`",

	      `"metaLink`": `"https://www.yahoo.com/`",

	      `"ogTitle`": `"Page Title`",

	      `"ogDescription`": `"Page Description`"

	    },

	    `"type`": `"post`",

	    `"postApprovalDetails`": {

	      `"approver`": `"iVrVJ2uoXNF0wzcBzgl5`",

	      `"approvalStatus`": `"pending`"

	    },

	    `"scheduleTimeUpdated`": true,

	    `"tags`": [

	      `"65f151c99bc2bf3aaf970d72`",

	      `"65f151c99bc2bf3aaf970d73`"

	    ],

	    `"categoryId`": `"65f151c99bc2bf3aaf970d72`",

	    `"applyWatermark`": true,

	    `"tiktokPostDetails`": {

	      `"privacyLevel`": `"PUBLIC_TO_EVERYONE`",

	      `"enableComment`": true,

	      `"enableDuet`": false

	    },

	    `"gmbPostDetails`": {

	      `"gmbEventType`": `"STANDARD`",

	      `"actionType`": `"BOOK`",

	      `"url`": `"https://example.com`"

	    },

	    `"userId`": `"sdfdsfdsfEWEsdfsdsW32dd`",

	    `"linkedinPostDetails`": {

	      `"pdfTitle`": `"Q4 Marketing Strategy Presentation`",

	      `"postAsPdf`": true

	    },

	    `"pinterestPostDetails`": {

	      `"title`": `"10 Easy Home Decor Ideas for 2024`",

	      `"link`": `"https://yoursite.com/blog/home-decor-ideas`",

	      `"boardIds`": {

	        `"6887d6de1d8175813d50dab8`": `"987654321098765432`",

	        `"682c7d1710a2fe3d805a3513`": `"123456789012345678`"

	      },

	      `"shortenedLinks`": [

	        `"string`"

	      ]

	    },

	    `"facebookPostDetails`": {

	      `"type`": `"post`"

	    },

	    `"instagramPostDetails`": {

	      `"type`": `"post`",

	      `"collaborators`": {

	        `"accountId1`": [

	          `"username1`",

	          `"username2`"

	        ],

	        `"accountId2`": [

	          `"username3`",

	          `"username4`"

	        ]

	      },

	      `"showOnFeed`": true,

	      `"publishViaPushNotification`": true,

	      `"publisherNote`": `"When publishing, add swipe up link to the landing page so that we can direct them to the sales page`"

	    },

	    `"youtubePostDetails`": {

	      `"title`": `"How to Build a Successful Marketing Strategy in 2024`",

	      `"privacyLevel`": `"public`",

	      `"type`": `"video`"

	    },

	    `"communityPostDetails`": {

	      `"title`": `"Welcome to Our New Community Feature!`",

	      `"notifyAllGroupMembers`": true,

	      `"postAsUser`": {

	        `"xMQswA02zgqKPpxITe`": {

	          `"avatar`": `"https://lh3.googleusercontent.com/a/user-avatar.jpg`",

	          `"id`": `"snCr14eeYkSppD04rkNW`",

	          `"name`": `"John Smith`"

	        }

	      }

	    },

	    `"locationId`": `"ve9EPM428h8vShlRW1KT`"

	  },

	  `"newOrder`": 0,

	  `"variations`": [

	    {

	      `"content`": `"Check out our latest blog post! #marketing #socialmedia`",

	      `"mentions`": [

	        {

	          `"platform`": `"instagram`",

	          `"username`": `"example_user`",

	          `"offset`": 10,

	          `"length`": 12

	        }

	      ],

	      `"ogTags`": {

	        `"metaLink`": `"https://example.com/blog/post-title`",

	        `"metaImage`": `"https://example.com/images/preview.png`",

	        `"ogTitle`": `"Check out our latest blog post!`"

	      }

	    }

	  ],

	  `"primaryImage`": `"http://example.com/media.png`"

	}

	"@

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/items/:itemId' -Method 'PUT' -Headers $headers -Body $body

	$response | ConvertTo-Json

```

