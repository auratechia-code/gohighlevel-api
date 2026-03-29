---
title: "Import Courses"
resource: "courses"
endpoint: "/courses/courses-exporter/public/import"
method: "POST"
version: "2021-07-28"
---

# Import Courses

This endpoint allows for the bulk import of courses (products) into a location. It supports a nested structure including categories, subcategories, lessons (posts), and downloadable materials.

## Endpoint Information

- **Method:** `POST`
- **Path:** `https://services.leadconnectorhq.com/courses/courses-exporter/public/import`
- **Required Scopes:** `courses.write`
- **Mandatory Header:** `Version: 2021-07-28`

## Request Body

| Name | Type | Description |
|------|------|-------------|
| `locationId` | `string` | **Required.** The ID of the location to import courses into. |
| `userId` | `string` | **Required.** The ID of the user performing the import. |
| `products` | `array` | **Required.** List of course products to import. |

### Product Object
| Name | Type | Description |
|------|------|-------------|
| `title` | `string` | Course title. |
| `description` | `string` | Course description. |
| `imageUrl` | `string` | URL for the course thumbnail. |
| `categories` | `array` | List of categories within the course. |
| `instructorDetails`| `object` | Details of the course instructor (`name`, `description`). |

### Category Object
| Name | Type | Description |
|------|------|-------------|
| `title` | `string` | Category title. |
| `visibility` | `string` | `published`, `draft`, or `locked`. |
| `posts` | `array` | List of individual lessons (posts). |
| `subCategories` | `array` | Nested subcategories. |

### Post (Lesson) Object
| Name | Type | Description |
|------|------|-------------|
| `title` | `string` | Lesson title. |
| `visibility` | `string` | `published`, `draft`, or `locked`. |
| `contentType` | `string` | Typically `video`. |
| `description` | `string` | Lesson body content/description. |
| `bucketVideoUrl` | `string` | URL to the video file in GHL bucket. |
| `postMaterials` | `array` | List of attachments (`title`, `type`, `url`). |

## Response Schema (200 OK)

```json
{
  "success": true,
  "message": "Import process started successfully",
  "importId": "uuid-string"
}
```

## Implementation Example

### cURL
```bash
curl --request POST \
  --url 'https://services.leadconnectorhq.com/courses/courses-exporter/public/import' \
  --header 'Authorization: Bearer {YOUR_ACCESS_TOKEN}' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --data '{
    "locationId": "YOUR_LOCATION_ID",
    "userId": "YOUR_USER_ID",
    "products": [
      {
        "title": "Mastering GHL API",
        "description": "Comprehensive guide to GHL API 2.0",
        "categories": [
          {
            "title": "Introduction",
            "posts": [
              {
                "title": "Getting Started",
                "contentType": "video",
                "bucketVideoUrl": "https://link-to-video.mp4"
              }
            ]
          }
        ]
      }
    ]
  }'
```

> [!TIP]
> This endpoint is asynchronous for large imports. You will receive an `importId` to track the progress if the system supports polling (verify via webhooks).
