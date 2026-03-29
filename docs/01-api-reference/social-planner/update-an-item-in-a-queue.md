# Update an item in a queue

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | PUT |
| **Endpoint URL** | `https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/items/:itemId` |
| **Scopes Required** | `socialplanner/category.write` |
| **Authentication** | OAuth Access Token / Private Integration Token |
| **Token Type** | Sub-Account Token |

---

## 2. REQUEST

### Header Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **Version** | `` | No |  |

### Path Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **queueId** | `` | Yes | itemId string required |
| **itemId** | `` | No |  |

### Query Parameters

N/A
### Body Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **locationId** | `string` | No |  |
| **sessionId** | `string` | No |  |
| **modifiedPostPayload** | `object` | Yes | Modifications to the original post accountIds string[] Account Ids (OAuth only) Example: ["aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496"] summary string Post Content Example: Hello World media object[] Post Media Array [ url string required Public URL of the media file. Must be a valid, accessible HTTPS URL. Example: https://storage.googleapis.com/your-bucket/media/image.jpg caption string Alt text or caption for the media. Used for accessibility and SEO. Example: Team meeting discussing Q4 marketing strategy originalUrl string Original media URL before any processing (watermarking/optimization). Set automatically by the system. Example: https://storage.googleapis.com/test/test/media/original.jpeg watermarkedUrl string URL of the media after watermarking. Set automatically when watermark is applied. Example: https://storage.googleapis.com/test/test/media/watermarked.jpeg type string required MIME type of the media file. See Platform Limitations Guide for platform-specific format support. Possible values: [ image/jpeg , image/jpg , image/png , image/gif , video/mp4 , video/mov , video/webm ] Example: image/jpeg thumbnail string URL of the video thumbnail image. Used for video preview before playback. Tip: For videos, providing a custom thumbnail improves engagement. Example: https://storage.googleapis.com/your-bucket/media/video-thumbnail.jpeg defaultThumb string Default thumbnail URL, auto-generated from video if not provided. Example: https://storage.googleapis.com/test/test/media/default-thumb.jpeg id string Unique identifier for the media item. Used for tracking and referencing. Example: media_abc123xyz optimizedUrl string URL of the optimized/compressed media. Set automatically when media optimization is enabled. Enable Optimization: Set mediaOptimization: true in the post request. Example: https://storage.googleapis.com/your-bucket/media/optimized-image.jpg optimizedType string MIME type of the optimized media. May differ from original if format conversion occurred. Example: image/jpeg isModified boolean Flag indicating if the media was modified (watermarked, optimized, or processed). Example: true ] status object Post status indicating the current state of the post. Available Status Values: draft - Post saved as draft, not yet ready for publishing scheduled - Post scheduled for future publishing (requires scheduleDate ) in_review - Post pending approval (requires scheduleDate and postApprovalDetails ) published - Post has been published in_progress - Post is currently being processed pending - Post is awaiting platform processing for Instagram media container creation failed - Post publishing failed notification_sent - Story notification sent (for manual story posting) deleted - Post has been deleted Validations: scheduled or in_review status requires scheduleDate to be set Draft posts skip most validations (accountIds, media requirements) Example: scheduled scheduleDate string Schedule Date Example: 2024-01-15T10:00:00Z selectedBestTime string Selected Best Time slot for scheduling Example: 2024-01-15T10:00:00Z createdBy string Created By Example: Lx1EI6YIgQYMQi0ytFXv followUpComment string Follow-up comment to be posted immediately after the main post is published. Supported Platforms: Facebook, Instagram, LinkedIn, Pinterest, YouTube NOT Supported: TikTok, Google My Business (GMB) Use Case: Great for adding hashtags, additional context, or engagement prompts without cluttering the main post. Example: What do you think? Let us know in the comments! ogTagsDetails object Og Tags Meta Data metaImage string Preview image URL for the shared link. Best Practices: Use high-quality images (1200x630px recommended) Ensure the image is publicly accessible Auto-fetch: Use the Get Metatags API to fetch OG data from a URL. Example: https://yoursite.com/images/og-image.jpg metaLink string URL of the webpage being shared. This is the destination when users click the link preview. Example: https://yoursite.com/blog/amazing-article ogTitle string Custom title for the link preview. Overrides the page's og:title meta tag. Tip: Keep titles concise (50-60 characters) for best display across platforms. Example: How to Double Your Social Media Engagement ogDescription string Custom description for the link preview. Overrides the page's og:description meta tag. Tip: Keep descriptions under 155 characters for optimal display. Example: Learn proven strategies to boost your social media engagement and grow your audience. type object Post Type must be one of the following values: - post, story, reel Example: post postApprovalDetails object Post Approval Details approver string User ID of the designated approver. Note: The approver will receive a notification when a post is submitted for review. Example: iVrVJ2uoXNF0wzcBzgl5 requesterNote string Note from the post creator to the approver explaining the post or requesting specific feedback. Example: Please review the messaging for our Q4 campaign launch. Let me know if the CTA needs adjustment. approverNote string Note from the approver to the post creator with feedback or approval comments. Example: Approved! Great content. Consider adding more hashtags for visibility. approvalStatus string Current approval status of the post. Available Values: pending - Awaiting approver review approved - Approved and ready for publishing rejected - Rejected by approver (needs revision) not_required - No approval workflow needed Possible values: [ pending , approved , rejected , not_required ] Example: pending scheduleTimeUpdated boolean Flag indicating if the schedule datetime was manually updated. Used for tracking rescheduled posts. Example: true tags string[] Array of Tag IDs to associate with the post for organization and filtering. Get Tag IDs from: Get Tags API — use the _id field from each tag. Validation: All IDs must be valid MongoDB ObjectIds. Example: ["65f151c99bc2bf3aaf970d72","65f151c99bc2bf3aaf970d73"] categoryId string Category ID to organize the post. Categories help group related posts. Get Category IDs from: Get Categories API — use the _id field. Validation: Must be a valid MongoDB ObjectId. Example: 65f151c99bc2bf3aaf970d72 applyWatermark boolean Apply watermark to media in this post. Note: Watermarks are applied to images only. Videos are not watermarked. Example: true tiktokPostDetails object Tiktok Post Details privacyLevel string required Privacy level controlling who can view the video. Available Values: PUBLIC_TO_EVERYONE - Anyone can view (default) MUTUAL_FOLLOW_FRIENDS - Only mutual followers can view SELF_ONLY - Only you can view (private) Note: If set to SELF_ONLY , videoDisclosure must be false . Possible values: [ PUBLIC_TO_EVERYONE , MUTUAL_FOLLOW_FRIENDS , SELF_ONLY ] Example: PUBLIC_TO_EVERYONE promoteOtherBrand boolean Indicates if the video promotes a third-party brand or product. Required: Must be true if videoDisclosure is enabled and you're promoting another brand. Example: false enableComment boolean Allow users to comment on the video. Default is determined by account settings. Example: true enableDuet boolean Allow users to create Duet videos with your content. Duet: Side-by-side video featuring your content and the creator's reaction/addition. Example: true enableStitch boolean Allow users to create Stitch videos with your content. Stitch: Clips up to 5 seconds of your video that creators can use in their own videos. Example: true videoDisclosure boolean Enable branded content disclosure. Required when video is promotional content. Validations: Cannot be true if privacyLevel is SELF_ONLY If enabled, at least one of promoteYourBrand or promoteOtherBrand must be true Example: false promoteYourBrand boolean Indicates if the video promotes your own brand or product. Required: Must be true if videoDisclosure is enabled and you're promoting your own brand. Example: false gmbPostDetails object GMB Post Details gmbEventType string required Google My Business post type. Available Types: STANDARD - Regular update post (What's New) EVENT - Event announcement with dates and title OFFER - Promotional offer with coupon and redemption details Required fields by type: STANDARD: None additional EVENT: title , startDate , endDate OFFER: offerTitle , startDate , endDate , termsConditions , couponCode , redeemOnlineUrl Possible values: [ STANDARD , EVENT , OFFER ] Example: STANDARD title string Event title. Required when gmbEventType is EVENT . Max length: 58 characters Example: Summer Sale Event 2024 offerTitle string Offer title. Required when gmbEventType is OFFER . Example: 50% Off All Products startDate object Start date and time for EVENT or OFFER posts. Required: When gmbEventType is EVENT or OFFER . Structure: startDate : { year, month, day } startTime : { hours, minutes, seconds } startDate object Start Date year number required Year component of the date Example: 2022 month number required Month component of the date (1-12) Example: 1 day number required Day component of the date (1-31) Example: 1 startTime object Start Time hours number required Hour component of the time (0-23) Example: 23 minutes number required Minute component of the time (0-59) Example: 56 seconds number required Second component of the time (0-59) Example: 34 endDate object End date and time for EVENT or OFFER posts. Required: When gmbEventType is EVENT or OFFER . Validation: Must be after startDate . Structure: endDate : { year, month, day } endTime : { hours, minutes, seconds } endDate object End Date year number required Year component of the date Example: 2022 month number required Month component of the date (1-12) Example: 1 day number required Day component of the date (1-31) Example: 1 endTime object End Time hours number required Hour component of the time (0-23) Example: 23 minutes number required Minute component of the time (0-59) Example: 56 seconds number required Second component of the time (0-59) Example: 34 termsConditions string URL to terms and conditions page. Required for OFFER posts. Example: https://yoursite.com/terms-and-conditions url string Call-to-action URL. Required when actionType is set (except none and call ). Required for: STANDARD and EVENT posts with actionType other than none or call . Example: https://yoursite.com/book-now couponCode string Promotional coupon code. Required for OFFER posts. Example: SAVE50 redeemOnlineUrl string URL where customers can redeem the offer online. Required for OFFER posts. Example: https://yoursite.com/redeem-offer actionType string Call-to-action button type for the post. Available Actions: none - No action button order - Order online book - Book appointment shop - Shop now learn_more - Learn more call - Call now (no URL required) sign_up - Sign up Note: All actions except none and call require a url . Possible values: [ none , order , book , shop , learn_more , call , sign_up ] Example: book userId string User ID Example: sdfdsfdsfEWEsdfsdsW32dd linkedinPostDetails object Linkedin Post Details pdfTitle string required Title for the PDF document carousel. Displayed as the document name on LinkedIn. Max length: 100 characters Tip: Use a descriptive title that explains the document content. Example: Q4 Marketing Strategy Presentation postAsPdf boolean required Post images as a PDF document carousel. Limits: Max 300 pages/images Max PDF size: 100 MB Example: true pinterestPostDetails object Pinterest Post Details title string Pin title displayed on Pinterest. Max length: 100 characters Best Practices: Include relevant keywords Be descriptive and engaging Example: 10 Easy Home Decor Ideas for 2024 link string Destination URL for the pin. Users clicking the pin will be directed to this URL. Max length: 2048 characters Best Practices: Use direct links to relevant content Track with UTM parameters for analytics Example: https://yoursite.com/blog/home-decor-ideas boardIds object required Mapping of Pinterest account OAuth IDs to their respective board IDs. Structure: { accountOAuthId: boardId } Get Board IDs from: Get Pinterest Boards API — use the id field from each board. Create Boards: Create Pinterest Board API to create new boards. Required: Each Pinterest account in the post must have a corresponding board ID. property name* string shortenedLinks string[] Shortened links for the post (auto-generated). facebookPostDetails object Facebook Post Details type string required Facebook post format type. Available Types: post - Standard feed post (images, videos, text) story - 24-hour temporary story reel - Short-form vertical video Restrictions: Reels: Require exactly 1 video, not supported on Groups Stories: Captions not supported Possible values: [ post , story , reel ] Example: post instagramPostDetails object Instagram Post Details type string required Instagram post format type. Available Types: post - Standard feed post (images, videos, carousels) story - 24-hour temporary story reel - Short-form vertical video (up to 90 seconds) Restrictions: Media is REQUIRED for all Instagram posts Reels: Require exactly 1 video Stories: Captions not supported, JPEG only for images Possible values: [ post , story , reel ] Example: post collaborators object Object mapping account IDs to arrays of associated usernames for collaboration. Only allowed for type "post" and "reels" Example: {"accountId1":["username1","username2"],"accountId2":["username3","username4"]} showOnFeed boolean Show Reel on profile grid/feed. ✅ Applies to: Reels only true - Reel appears on your profile grid false - Reel only appears in Reels tab Example: true publishViaPushNotification boolean Send Instagram Story via Push  Notification instead of direct posting. Only applicable for Story type. Example: true publisherNote string Note to the publisher for manual posting guidance. Only used when publishViaPushNotification is true. Example: When publishing, add swipe up link to the landing page so that we can direct them to the sales page youtubePostDetails object Youtube Post Details title string Video title displayed on YouTube. Max length: 100 characters Best Practices: Include relevant keywords Be descriptive but concise Avoid clickbait Example: How to Build a Successful Marketing Strategy in 2024 privacyLevel string Video visibility/privacy setting. Available Values: public - Anyone can search and view unlisted - Only people with the link can view private - Only you can view Possible values: [ private , public , unlisted ] Example: public type string required YouTube video format type. Available Types: video - Standard YouTube video (landscape, any duration) short - YouTube Shorts (vertical, up to 60 seconds) Required field. Possible values: [ video , short ] Example: video communityPostDetails object Community Post Details title string required Title of the community post. Displayed as the post headline. Max length: 1,000 characters Required: Yes, for all Community posts. Example: Welcome to Our New Community Feature! notifyAllGroupMembers boolean required Send push notification to all group members when the post is published. Use Case: Enable for important announcements to ensure all members are notified. Example: true postAsUser object required Mapping of Community account OAuth IDs to user details for posting on behalf of users. Structure: { accountOAuthId: { id, name, avatar } } id (required): User ID within the Community group name (optional): Display name for the post author avatar (optional): Profile image URL Get Account OAuth IDs from: Get Accounts API — use the oAuthId field from Community accounts. Required: Yes, each Community account in accountIds must have a corresponding entry here. Example: {"xMQswA02zgqKPpxITe":{"avatar":"https://lh3.googleusercontent.com/a/user-avatar.jpg","id":"snCr14eeYkSppD04rkNW","name":"John Smith"}} locationId string Location Id Example: ve9EPM428h8vShlRW1KT |
| **accountIds** | `string[]` | No |  |
| **summary** | `string` | No |  |
| **media** | `object[]` | Yes | Post Media Array [ url string required Public URL of the media file. Must be a valid, accessible HTTPS URL. Example: https://storage.googleapis.com/your-bucket/media/image.jpg caption string Alt text or caption for the media. Used for accessibility and SEO. Example: Team meeting discussing Q4 marketing strategy originalUrl string Original media URL before any processing (watermarking/optimization). Set automatically by the system. Example: https://storage.googleapis.com/test/test/media/original.jpeg watermarkedUrl string URL of the media after watermarking. Set automatically when watermark is applied. Example: https://storage.googleapis.com/test/test/media/watermarked.jpeg type string required MIME type of the media file. See Platform Limitations Guide for platform-specific format support. Possible values: [ image/jpeg , image/jpg , image/png , image/gif , video/mp4 , video/mov , video/webm ] Example: image/jpeg thumbnail string URL of the video thumbnail image. Used for video preview before playback. Tip: For videos, providing a custom thumbnail improves engagement. Example: https://storage.googleapis.com/your-bucket/media/video-thumbnail.jpeg defaultThumb string Default thumbnail URL, auto-generated from video if not provided. Example: https://storage.googleapis.com/test/test/media/default-thumb.jpeg id string Unique identifier for the media item. Used for tracking and referencing. Example: media_abc123xyz optimizedUrl string URL of the optimized/compressed media. Set automatically when media optimization is enabled. Enable Optimization: Set mediaOptimization: true in the post request. Example: https://storage.googleapis.com/your-bucket/media/optimized-image.jpg optimizedType string MIME type of the optimized media. May differ from original if format conversion occurred. Example: image/jpeg isModified boolean Flag indicating if the media was modified (watermarked, optimized, or processed). Example: true ] |
| **url** | `string` | No |  |
| **caption** | `string` | No |  |
| **originalUrl** | `string` | No |  |
| **watermarkedUrl** | `string` | No |  |
| **type** | `string` | No |  |
| **thumbnail** | `string` | No |  |
| **defaultThumb** | `string` | No |  |
| **id** | `string` | No |  |
| **optimizedUrl** | `string` | No |  |
| **optimizedType** | `string` | No |  |
| **isModified** | `boolean` | No |  |
| **status** | `object` | No |  |
| **scheduleDate** | `string` | No |  |
| **selectedBestTime** | `string` | No |  |
| **createdBy** | `string` | No |  |
| **followUpComment** | `string` | No |  |
| **ogTagsDetails** | `object` | No | Og Tags Meta Data metaImage string Preview image URL for the shared link. Best Practices: Use high-quality images (1200x630px recommended) Ensure the image is publicly accessible Auto-fetch: Use the Get Metatags API to fetch OG data from a URL. Example: https://yoursite.com/images/og-image.jpg metaLink string URL of the webpage being shared. This is the destination when users click the link preview. Example: https://yoursite.com/blog/amazing-article ogTitle string Custom title for the link preview. Overrides the page's og:title meta tag. Tip: Keep titles concise (50-60 characters) for best display across platforms. Example: How to Double Your Social Media Engagement ogDescription string Custom description for the link preview. Overrides the page's og:description meta tag. Tip: Keep descriptions under 155 characters for optimal display. Example: Learn proven strategies to boost your social media engagement and grow your audience. |
| **metaImage** | `string` | No |  |
| **metaLink** | `string` | No |  |
| **ogTitle** | `string` | No |  |
| **ogDescription** | `string` | No |  |
| **type** | `object` | No |  |
| **postApprovalDetails** | `object` | Yes | Post Approval Details approver string User ID of the designated approver. Note: The approver will receive a notification when a post is submitted for review. Example: iVrVJ2uoXNF0wzcBzgl5 requesterNote string Note from the post creator to the approver explaining the post or requesting specific feedback. Example: Please review the messaging for our Q4 campaign launch. Let me know if the CTA needs adjustment. approverNote string Note from the approver to the post creator with feedback or approval comments. Example: Approved! Great content. Consider adding more hashtags for visibility. approvalStatus string Current approval status of the post. Available Values: pending - Awaiting approver review approved - Approved and ready for publishing rejected - Rejected by approver (needs revision) not_required - No approval workflow needed Possible values: [ pending , approved , rejected , not_required ] Example: pending |
| **approver** | `string` | No |  |
| **requesterNote** | `string` | No |  |
| **approverNote** | `string` | No |  |
| **approvalStatus** | `string` | No |  |
| **scheduleTimeUpdated** | `boolean` | No |  |
| **tags** | `string[]` | No |  |
| **categoryId** | `string` | No |  |
| **applyWatermark** | `boolean` | No |  |
| **tiktokPostDetails** | `object` | Yes | Tiktok Post Details privacyLevel string required Privacy level controlling who can view the video. Available Values: PUBLIC_TO_EVERYONE - Anyone can view (default) MUTUAL_FOLLOW_FRIENDS - Only mutual followers can view SELF_ONLY - Only you can view (private) Note: If set to SELF_ONLY , videoDisclosure must be false . Possible values: [ PUBLIC_TO_EVERYONE , MUTUAL_FOLLOW_FRIENDS , SELF_ONLY ] Example: PUBLIC_TO_EVERYONE promoteOtherBrand boolean Indicates if the video promotes a third-party brand or product. Required: Must be true if videoDisclosure is enabled and you're promoting another brand. Example: false enableComment boolean Allow users to comment on the video. Default is determined by account settings. Example: true enableDuet boolean Allow users to create Duet videos with your content. Duet: Side-by-side video featuring your content and the creator's reaction/addition. Example: true enableStitch boolean Allow users to create Stitch videos with your content. Stitch: Clips up to 5 seconds of your video that creators can use in their own videos. Example: true videoDisclosure boolean Enable branded content disclosure. Required when video is promotional content. Validations: Cannot be true if privacyLevel is SELF_ONLY If enabled, at least one of promoteYourBrand or promoteOtherBrand must be true Example: false promoteYourBrand boolean Indicates if the video promotes your own brand or product. Required: Must be true if videoDisclosure is enabled and you're promoting your own brand. Example: false |
| **privacyLevel** | `string` | No |  |
| **promoteOtherBrand** | `boolean` | No |  |
| **enableComment** | `boolean` | No |  |
| **enableDuet** | `boolean` | No |  |
| **enableStitch** | `boolean` | No |  |
| **videoDisclosure** | `boolean` | No |  |
| **promoteYourBrand** | `boolean` | No |  |
| **gmbPostDetails** | `object` | Yes | GMB Post Details gmbEventType string required Google My Business post type. Available Types: STANDARD - Regular update post (What's New) EVENT - Event announcement with dates and title OFFER - Promotional offer with coupon and redemption details Required fields by type: STANDARD: None additional EVENT: title , startDate , endDate OFFER: offerTitle , startDate , endDate , termsConditions , couponCode , redeemOnlineUrl Possible values: [ STANDARD , EVENT , OFFER ] Example: STANDARD title string Event title. Required when gmbEventType is EVENT . Max length: 58 characters Example: Summer Sale Event 2024 offerTitle string Offer title. Required when gmbEventType is OFFER . Example: 50% Off All Products startDate object Start date and time for EVENT or OFFER posts. Required: When gmbEventType is EVENT or OFFER . Structure: startDate : { year, month, day } startTime : { hours, minutes, seconds } startDate object Start Date year number required Year component of the date Example: 2022 month number required Month component of the date (1-12) Example: 1 day number required Day component of the date (1-31) Example: 1 startTime object Start Time hours number required Hour component of the time (0-23) Example: 23 minutes number required Minute component of the time (0-59) Example: 56 seconds number required Second component of the time (0-59) Example: 34 endDate object End date and time for EVENT or OFFER posts. Required: When gmbEventType is EVENT or OFFER . Validation: Must be after startDate . Structure: endDate : { year, month, day } endTime : { hours, minutes, seconds } endDate object End Date year number required Year component of the date Example: 2022 month number required Month component of the date (1-12) Example: 1 day number required Day component of the date (1-31) Example: 1 endTime object End Time hours number required Hour component of the time (0-23) Example: 23 minutes number required Minute component of the time (0-59) Example: 56 seconds number required Second component of the time (0-59) Example: 34 termsConditions string URL to terms and conditions page. Required for OFFER posts. Example: https://yoursite.com/terms-and-conditions url string Call-to-action URL. Required when actionType is set (except none and call ). Required for: STANDARD and EVENT posts with actionType other than none or call . Example: https://yoursite.com/book-now couponCode string Promotional coupon code. Required for OFFER posts. Example: SAVE50 redeemOnlineUrl string URL where customers can redeem the offer online. Required for OFFER posts. Example: https://yoursite.com/redeem-offer actionType string Call-to-action button type for the post. Available Actions: none - No action button order - Order online book - Book appointment shop - Shop now learn_more - Learn more call - Call now (no URL required) sign_up - Sign up Note: All actions except none and call require a url . Possible values: [ none , order , book , shop , learn_more , call , sign_up ] Example: book |
| **gmbEventType** | `string` | No |  |
| **title** | `string` | No |  |
| **offerTitle** | `string` | No |  |
| **startDate** | `object` | Yes | Start date and time for EVENT or OFFER posts. Required: When gmbEventType is EVENT or OFFER . Structure: startDate : { year, month, day } startTime : { hours, minutes, seconds } startDate object Start Date year number required Year component of the date Example: 2022 month number required Month component of the date (1-12) Example: 1 day number required Day component of the date (1-31) Example: 1 startTime object Start Time hours number required Hour component of the time (0-23) Example: 23 minutes number required Minute component of the time (0-59) Example: 56 seconds number required Second component of the time (0-59) Example: 34 |
| **startDate** | `object` | Yes | Start Date year number required Year component of the date Example: 2022 month number required Month component of the date (1-12) Example: 1 day number required Day component of the date (1-31) Example: 1 |
| **year** | `number` | No |  |
| **month** | `number` | No |  |
| **day** | `number` | No |  |
| **startTime** | `object` | Yes | Start Time hours number required Hour component of the time (0-23) Example: 23 minutes number required Minute component of the time (0-59) Example: 56 seconds number required Second component of the time (0-59) Example: 34 |
| **hours** | `number` | No |  |
| **minutes** | `number` | No |  |
| **seconds** | `number` | No |  |
| **endDate** | `object` | Yes | End date and time for EVENT or OFFER posts. Required: When gmbEventType is EVENT or OFFER . Validation: Must be after startDate . Structure: endDate : { year, month, day } endTime : { hours, minutes, seconds } endDate object End Date year number required Year component of the date Example: 2022 month number required Month component of the date (1-12) Example: 1 day number required Day component of the date (1-31) Example: 1 endTime object End Time hours number required Hour component of the time (0-23) Example: 23 minutes number required Minute component of the time (0-59) Example: 56 seconds number required Second component of the time (0-59) Example: 34 |
| **endDate** | `object` | Yes | End Date year number required Year component of the date Example: 2022 month number required Month component of the date (1-12) Example: 1 day number required Day component of the date (1-31) Example: 1 |
| **year** | `number` | No |  |
| **month** | `number` | No |  |
| **day** | `number` | No |  |
| **endTime** | `object` | Yes | End Time hours number required Hour component of the time (0-23) Example: 23 minutes number required Minute component of the time (0-59) Example: 56 seconds number required Second component of the time (0-59) Example: 34 |
| **hours** | `number` | No |  |
| **minutes** | `number` | No |  |
| **seconds** | `number` | No |  |
| **termsConditions** | `string` | No |  |
| **url** | `string` | No |  |
| **couponCode** | `string` | No |  |
| **redeemOnlineUrl** | `string` | No |  |
| **actionType** | `string` | No |  |
| **userId** | `string` | No |  |
| **linkedinPostDetails** | `object` | Yes | Linkedin Post Details pdfTitle string required Title for the PDF document carousel. Displayed as the document name on LinkedIn. Max length: 100 characters Tip: Use a descriptive title that explains the document content. Example: Q4 Marketing Strategy Presentation postAsPdf boolean required Post images as a PDF document carousel. Limits: Max 300 pages/images Max PDF size: 100 MB Example: true |
| **pdfTitle** | `string` | No |  |
| **postAsPdf** | `boolean` | No |  |
| **pinterestPostDetails** | `object` | Yes | Pinterest Post Details title string Pin title displayed on Pinterest. Max length: 100 characters Best Practices: Include relevant keywords Be descriptive and engaging Example: 10 Easy Home Decor Ideas for 2024 link string Destination URL for the pin. Users clicking the pin will be directed to this URL. Max length: 2048 characters Best Practices: Use direct links to relevant content Track with UTM parameters for analytics Example: https://yoursite.com/blog/home-decor-ideas boardIds object required Mapping of Pinterest account OAuth IDs to their respective board IDs. Structure: { accountOAuthId: boardId } Get Board IDs from: Get Pinterest Boards API — use the id field from each board. Create Boards: Create Pinterest Board API to create new boards. Required: Each Pinterest account in the post must have a corresponding board ID. property name* string shortenedLinks string[] Shortened links for the post (auto-generated). |
| **title** | `string` | No |  |
| **link** | `string` | No |  |
| **boardIds** | `object` | Yes | Mapping of Pinterest account OAuth IDs to their respective board IDs. Structure: { accountOAuthId: boardId } Get Board IDs from: Get Pinterest Boards API — use the id field from each board. Create Boards: Create Pinterest Board API to create new boards. Required: Each Pinterest account in the post must have a corresponding board ID. property name* string |
| **property name*** | `string` | No |  |
| **shortenedLinks** | `string[]` | No |  |
| **facebookPostDetails** | `object` | Yes | Facebook Post Details type string required Facebook post format type. Available Types: post - Standard feed post (images, videos, text) story - 24-hour temporary story reel - Short-form vertical video Restrictions: Reels: Require exactly 1 video, not supported on Groups Stories: Captions not supported Possible values: [ post , story , reel ] Example: post |
| **type** | `string` | No |  |
| **instagramPostDetails** | `object` | Yes | Instagram Post Details type string required Instagram post format type. Available Types: post - Standard feed post (images, videos, carousels) story - 24-hour temporary story reel - Short-form vertical video (up to 90 seconds) Restrictions: Media is REQUIRED for all Instagram posts Reels: Require exactly 1 video Stories: Captions not supported, JPEG only for images Possible values: [ post , story , reel ] Example: post collaborators object Object mapping account IDs to arrays of associated usernames for collaboration. Only allowed for type "post" and "reels" Example: {"accountId1":["username1","username2"],"accountId2":["username3","username4"]} showOnFeed boolean Show Reel on profile grid/feed. ✅ Applies to: Reels only true - Reel appears on your profile grid false - Reel only appears in Reels tab Example: true publishViaPushNotification boolean Send Instagram Story via Push  Notification instead of direct posting. Only applicable for Story type. Example: true publisherNote string Note to the publisher for manual posting guidance. Only used when publishViaPushNotification is true. Example: When publishing, add swipe up link to the landing page so that we can direct them to the sales page |
| **type** | `string` | No |  |
| **collaborators** | `object` | No |  |
| **showOnFeed** | `boolean` | No |  |
| **publishViaPushNotification** | `boolean` | No |  |
| **publisherNote** | `string` | No |  |
| **youtubePostDetails** | `object` | Yes | Youtube Post Details title string Video title displayed on YouTube. Max length: 100 characters Best Practices: Include relevant keywords Be descriptive but concise Avoid clickbait Example: How to Build a Successful Marketing Strategy in 2024 privacyLevel string Video visibility/privacy setting. Available Values: public - Anyone can search and view unlisted - Only people with the link can view private - Only you can view Possible values: [ private , public , unlisted ] Example: public type string required YouTube video format type. Available Types: video - Standard YouTube video (landscape, any duration) short - YouTube Shorts (vertical, up to 60 seconds) Required field. Possible values: [ video , short ] Example: video |
| **title** | `string` | No |  |
| **privacyLevel** | `string` | No |  |
| **type** | `string` | No |  |
| **communityPostDetails** | `object` | Yes | Community Post Details title string required Title of the community post. Displayed as the post headline. Max length: 1,000 characters Required: Yes, for all Community posts. Example: Welcome to Our New Community Feature! notifyAllGroupMembers boolean required Send push notification to all group members when the post is published. Use Case: Enable for important announcements to ensure all members are notified. Example: true postAsUser object required Mapping of Community account OAuth IDs to user details for posting on behalf of users. Structure: { accountOAuthId: { id, name, avatar } } id (required): User ID within the Community group name (optional): Display name for the post author avatar (optional): Profile image URL Get Account OAuth IDs from: Get Accounts API — use the oAuthId field from Community accounts. Required: Yes, each Community account in accountIds must have a corresponding entry here. Example: {"xMQswA02zgqKPpxITe":{"avatar":"https://lh3.googleusercontent.com/a/user-avatar.jpg","id":"snCr14eeYkSppD04rkNW","name":"John Smith"}} |
| **title** | `string` | No |  |
| **notifyAllGroupMembers** | `boolean` | No |  |
| **postAsUser** | `object` | No |  |
| **locationId** | `string` | No |  |
| **newOrder** | `object` | No | New order value or position keyword (cyclic-aware). Accepts: A number: explicit order value calculated by FE as midpoint between adjacent items "top": place at cyclic top (first to be scheduled next) "bottom": place at cyclic bottom (last to be scheduled) For positions between items, FE calculates: Math.floor((prevItem.order + nextItem.order) / 2) oneOf MOD1 MOD2 number string |
| **** | `number` | No |  |
| **** | `string` | No |  |
| **variations** | `object[]` | No | Variations Array [ content string The text content of the variation. Example: Check out our latest blog post! #marketing #socialmedia mentions object[] Platform-specific mentions within the content (e.g., @username references). Example: [{"platform":"instagram","username":"example_user","offset":10,"length":12}] ogTags object Open Graph tags for link previews. metaLink object The canonical URL of the content for link preview. Example: https://example.com/blog/post-title metaImage object URL of the image to display in link preview. Example: https://example.com/images/preview.png ogTitle object Title to display in link preview. Example: Check out our latest blog post! ] |
| **content** | `string` | No |  |
| **mentions** | `object[]` | No |  |
| **ogTags** | `object` | No | Open Graph tags for link previews. metaLink object The canonical URL of the content for link preview. Example: https://example.com/blog/post-title metaImage object URL of the image to display in link preview. Example: https://example.com/images/preview.png ogTitle object Title to display in link preview. Example: Check out our latest blog post! |
| **metaLink** | `object` | No |  |
| **metaImage** | `object` | No |  |
| **ogTitle** | `object` | No |  |
| **primaryImage** | `string` | No |  |
| **modifiedPostPayload** | `object` | Yes | Modifications to the original post accountIds string[] Account Ids (OAuth only) Example: ["aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496"] summary string Post Content Example: Hello World media object[] Post Media Array [ url string required Public URL of the media file. Must be a valid, accessible HTTPS URL. Example: https://storage.googleapis.com/your-bucket/media/image.jpg caption string Alt text or caption for the media. Used for accessibility and SEO. Example: Team meeting discussing Q4 marketing strategy originalUrl string Original media URL before any processing (watermarking/optimization). Set automatically by the system. Example: https://storage.googleapis.com/test/test/media/original.jpeg watermarkedUrl string URL of the media after watermarking. Set automatically when watermark is applied. Example: https://storage.googleapis.com/test/test/media/watermarked.jpeg type string required MIME type of the media file. See Platform Limitations Guide for platform-specific format support. Possible values: [ image/jpeg , image/jpg , image/png , image/gif , video/mp4 , video/mov , video/webm ] Example: image/jpeg thumbnail string URL of the video thumbnail image. Used for video preview before playback. Tip: For videos, providing a custom thumbnail improves engagement. Example: https://storage.googleapis.com/your-bucket/media/video-thumbnail.jpeg defaultThumb string Default thumbnail URL, auto-generated from video if not provided. Example: https://storage.googleapis.com/test/test/media/default-thumb.jpeg id string Unique identifier for the media item. Used for tracking and referencing. Example: media_abc123xyz optimizedUrl string URL of the optimized/compressed media. Set automatically when media optimization is enabled. Enable Optimization: Set mediaOptimization: true in the post request. Example: https://storage.googleapis.com/your-bucket/media/optimized-image.jpg optimizedType string MIME type of the optimized media. May differ from original if format conversion occurred. Example: image/jpeg isModified boolean Flag indicating if the media was modified (watermarked, optimized, or processed). Example: true ] status object Post status indicating the current state of the post. Available Status Values: draft - Post saved as draft, not yet ready for publishing scheduled - Post scheduled for future publishing (requires scheduleDate ) in_review - Post pending approval (requires scheduleDate and postApprovalDetails ) published - Post has been published in_progress - Post is currently being processed pending - Post is awaiting platform processing for Instagram media container creation failed - Post publishing failed notification_sent - Story notification sent (for manual story posting) deleted - Post has been deleted Validations: scheduled or in_review status requires scheduleDate to be set Draft posts skip most validations (accountIds, media requirements) Example: scheduled scheduleDate string Schedule Date Example: 2024-01-15T10:00:00Z selectedBestTime string Selected Best Time slot for scheduling Example: 2024-01-15T10:00:00Z createdBy string Created By Example: Lx1EI6YIgQYMQi0ytFXv followUpComment string Follow-up comment to be posted immediately after the main post is published. Supported Platforms: Facebook, Instagram, LinkedIn, Pinterest, YouTube NOT Supported: TikTok, Google My Business (GMB) Use Case: Great for adding hashtags, additional context, or engagement prompts without cluttering the main post. Example: What do you think? Let us know in the comments! ogTagsDetails object Og Tags Meta Data metaImage string Preview image URL for the shared link. Best Practices: Use high-quality images (1200x630px recommended) Ensure the image is publicly accessible Auto-fetch: Use the Get Metatags API to fetch OG data from a URL. Example: https://yoursite.com/images/og-image.jpg metaLink string URL of the webpage being shared. This is the destination when users click the link preview. Example: https://yoursite.com/blog/amazing-article ogTitle string Custom title for the link preview. Overrides the page's og:title meta tag. Tip: Keep titles concise (50-60 characters) for best display across platforms. Example: How to Double Your Social Media Engagement ogDescription string Custom description for the link preview. Overrides the page's og:description meta tag. Tip: Keep descriptions under 155 characters for optimal display. Example: Learn proven strategies to boost your social media engagement and grow your audience. type object Post Type must be one of the following values: - post, story, reel Example: post postApprovalDetails object Post Approval Details approver string User ID of the designated approver. Note: The approver will receive a notification when a post is submitted for review. Example: iVrVJ2uoXNF0wzcBzgl5 requesterNote string Note from the post creator to the approver explaining the post or requesting specific feedback. Example: Please review the messaging for our Q4 campaign launch. Let me know if the CTA needs adjustment. approverNote string Note from the approver to the post creator with feedback or approval comments. Example: Approved! Great content. Consider adding more hashtags for visibility. approvalStatus string Current approval status of the post. Available Values: pending - Awaiting approver review approved - Approved and ready for publishing rejected - Rejected by approver (needs revision) not_required - No approval workflow needed Possible values: [ pending , approved , rejected , not_required ] Example: pending scheduleTimeUpdated boolean Flag indicating if the schedule datetime was manually updated. Used for tracking rescheduled posts. Example: true tags string[] Array of Tag IDs to associate with the post for organization and filtering. Get Tag IDs from: Get Tags API — use the _id field from each tag. Validation: All IDs must be valid MongoDB ObjectIds. Example: ["65f151c99bc2bf3aaf970d72","65f151c99bc2bf3aaf970d73"] categoryId string Category ID to organize the post. Categories help group related posts. Get Category IDs from: Get Categories API — use the _id field. Validation: Must be a valid MongoDB ObjectId. Example: 65f151c99bc2bf3aaf970d72 applyWatermark boolean Apply watermark to media in this post. Note: Watermarks are applied to images only. Videos are not watermarked. Example: true tiktokPostDetails object Tiktok Post Details privacyLevel string required Privacy level controlling who can view the video. Available Values: PUBLIC_TO_EVERYONE - Anyone can view (default) MUTUAL_FOLLOW_FRIENDS - Only mutual followers can view SELF_ONLY - Only you can view (private) Note: If set to SELF_ONLY , videoDisclosure must be false . Possible values: [ PUBLIC_TO_EVERYONE , MUTUAL_FOLLOW_FRIENDS , SELF_ONLY ] Example: PUBLIC_TO_EVERYONE promoteOtherBrand boolean Indicates if the video promotes a third-party brand or product. Required: Must be true if videoDisclosure is enabled and you're promoting another brand. Example: false enableComment boolean Allow users to comment on the video. Default is determined by account settings. Example: true enableDuet boolean Allow users to create Duet videos with your content. Duet: Side-by-side video featuring your content and the creator's reaction/addition. Example: true enableStitch boolean Allow users to create Stitch videos with your content. Stitch: Clips up to 5 seconds of your video that creators can use in their own videos. Example: true videoDisclosure boolean Enable branded content disclosure. Required when video is promotional content. Validations: Cannot be true if privacyLevel is SELF_ONLY If enabled, at least one of promoteYourBrand or promoteOtherBrand must be true Example: false promoteYourBrand boolean Indicates if the video promotes your own brand or product. Required: Must be true if videoDisclosure is enabled and you're promoting your own brand. Example: false gmbPostDetails object GMB Post Details gmbEventType string required Google My Business post type. Available Types: STANDARD - Regular update post (What's New) EVENT - Event announcement with dates and title OFFER - Promotional offer with coupon and redemption details Required fields by type: STANDARD: None additional EVENT: title , startDate , endDate OFFER: offerTitle , startDate , endDate , termsConditions , couponCode , redeemOnlineUrl Possible values: [ STANDARD , EVENT , OFFER ] Example: STANDARD title string Event title. Required when gmbEventType is EVENT . Max length: 58 characters Example: Summer Sale Event 2024 offerTitle string Offer title. Required when gmbEventType is OFFER . Example: 50% Off All Products startDate object Start date and time for EVENT or OFFER posts. Required: When gmbEventType is EVENT or OFFER . Structure: startDate : { year, month, day } startTime : { hours, minutes, seconds } startDate object Start Date year number required Year component of the date Example: 2022 month number required Month component of the date (1-12) Example: 1 day number required Day component of the date (1-31) Example: 1 startTime object Start Time hours number required Hour component of the time (0-23) Example: 23 minutes number required Minute component of the time (0-59) Example: 56 seconds number required Second component of the time (0-59) Example: 34 endDate object End date and time for EVENT or OFFER posts. Required: When gmbEventType is EVENT or OFFER . Validation: Must be after startDate . Structure: endDate : { year, month, day } endTime : { hours, minutes, seconds } endDate object End Date year number required Year component of the date Example: 2022 month number required Month component of the date (1-12) Example: 1 day number required Day component of the date (1-31) Example: 1 endTime object End Time hours number required Hour component of the time (0-23) Example: 23 minutes number required Minute component of the time (0-59) Example: 56 seconds number required Second component of the time (0-59) Example: 34 termsConditions string URL to terms and conditions page. Required for OFFER posts. Example: https://yoursite.com/terms-and-conditions url string Call-to-action URL. Required when actionType is set (except none and call ). Required for: STANDARD and EVENT posts with actionType other than none or call . Example: https://yoursite.com/book-now couponCode string Promotional coupon code. Required for OFFER posts. Example: SAVE50 redeemOnlineUrl string URL where customers can redeem the offer online. Required for OFFER posts. Example: https://yoursite.com/redeem-offer actionType string Call-to-action button type for the post. Available Actions: none - No action button order - Order online book - Book appointment shop - Shop now learn_more - Learn more call - Call now (no URL required) sign_up - Sign up Note: All actions except none and call require a url . Possible values: [ none , order , book , shop , learn_more , call , sign_up ] Example: book userId string User ID Example: sdfdsfdsfEWEsdfsdsW32dd linkedinPostDetails object Linkedin Post Details pdfTitle string required Title for the PDF document carousel. Displayed as the document name on LinkedIn. Max length: 100 characters Tip: Use a descriptive title that explains the document content. Example: Q4 Marketing Strategy Presentation postAsPdf boolean required Post images as a PDF document carousel. Limits: Max 300 pages/images Max PDF size: 100 MB Example: true pinterestPostDetails object Pinterest Post Details title string Pin title displayed on Pinterest. Max length: 100 characters Best Practices: Include relevant keywords Be descriptive and engaging Example: 10 Easy Home Decor Ideas for 2024 link string Destination URL for the pin. Users clicking the pin will be directed to this URL. Max length: 2048 characters Best Practices: Use direct links to relevant content Track with UTM parameters for analytics Example: https://yoursite.com/blog/home-decor-ideas boardIds object required Mapping of Pinterest account OAuth IDs to their respective board IDs. Structure: { accountOAuthId: boardId } Get Board IDs from: Get Pinterest Boards API — use the id field from each board. Create Boards: Create Pinterest Board API to create new boards. Required: Each Pinterest account in the post must have a corresponding board ID. property name* string shortenedLinks string[] Shortened links for the post (auto-generated). facebookPostDetails object Facebook Post Details type string required Facebook post format type. Available Types: post - Standard feed post (images, videos, text) story - 24-hour temporary story reel - Short-form vertical video Restrictions: Reels: Require exactly 1 video, not supported on Groups Stories: Captions not supported Possible values: [ post , story , reel ] Example: post instagramPostDetails object Instagram Post Details type string required Instagram post format type. Available Types: post - Standard feed post (images, videos, carousels) story - 24-hour temporary story reel - Short-form vertical video (up to 90 seconds) Restrictions: Media is REQUIRED for all Instagram posts Reels: Require exactly 1 video Stories: Captions not supported, JPEG only for images Possible values: [ post , story , reel ] Example: post collaborators object Object mapping account IDs to arrays of associated usernames for collaboration. Only allowed for type "post" and "reels" Example: {"accountId1":["username1","username2"],"accountId2":["username3","username4"]} showOnFeed boolean Show Reel on profile grid/feed. ✅ Applies to: Reels only true - Reel appears on your profile grid false - Reel only appears in Reels tab Example: true publishViaPushNotification boolean Send Instagram Story via Push  Notification instead of direct posting. Only applicable for Story type. Example: true publisherNote string Note to the publisher for manual posting guidance. Only used when publishViaPushNotification is true. Example: When publishing, add swipe up link to the landing page so that we can direct them to the sales page youtubePostDetails object Youtube Post Details title string Video title displayed on YouTube. Max length: 100 characters Best Practices: Include relevant keywords Be descriptive but concise Avoid clickbait Example: How to Build a Successful Marketing Strategy in 2024 privacyLevel string Video visibility/privacy setting. Available Values: public - Anyone can search and view unlisted - Only people with the link can view private - Only you can view Possible values: [ private , public , unlisted ] Example: public type string required YouTube video format type. Available Types: video - Standard YouTube video (landscape, any duration) short - YouTube Shorts (vertical, up to 60 seconds) Required field. Possible values: [ video , short ] Example: video communityPostDetails object Community Post Details title string required Title of the community post. Displayed as the post headline. Max length: 1,000 characters Required: Yes, for all Community posts. Example: Welcome to Our New Community Feature! notifyAllGroupMembers boolean required Send push notification to all group members when the post is published. Use Case: Enable for important announcements to ensure all members are notified. Example: true postAsUser object required Mapping of Community account OAuth IDs to user details for posting on behalf of users. Structure: { accountOAuthId: { id, name, avatar } } id (required): User ID within the Community group name (optional): Display name for the post author avatar (optional): Profile image URL Get Account OAuth IDs from: Get Accounts API — use the oAuthId field from Community accounts. Required: Yes, each Community account in accountIds must have a corresponding entry here. Example: {"xMQswA02zgqKPpxITe":{"avatar":"https://lh3.googleusercontent.com/a/user-avatar.jpg","id":"snCr14eeYkSppD04rkNW","name":"John Smith"}} locationId string Location Id Example: ve9EPM428h8vShlRW1KT |
| **accountIds** | `string[]` | No |  |
| **summary** | `string` | No |  |
| **media** | `object[]` | Yes | Post Media Array [ url string required Public URL of the media file. Must be a valid, accessible HTTPS URL. Example: https://storage.googleapis.com/your-bucket/media/image.jpg caption string Alt text or caption for the media. Used for accessibility and SEO. Example: Team meeting discussing Q4 marketing strategy originalUrl string Original media URL before any processing (watermarking/optimization). Set automatically by the system. Example: https://storage.googleapis.com/test/test/media/original.jpeg watermarkedUrl string URL of the media after watermarking. Set automatically when watermark is applied. Example: https://storage.googleapis.com/test/test/media/watermarked.jpeg type string required MIME type of the media file. See Platform Limitations Guide for platform-specific format support. Possible values: [ image/jpeg , image/jpg , image/png , image/gif , video/mp4 , video/mov , video/webm ] Example: image/jpeg thumbnail string URL of the video thumbnail image. Used for video preview before playback. Tip: For videos, providing a custom thumbnail improves engagement. Example: https://storage.googleapis.com/your-bucket/media/video-thumbnail.jpeg defaultThumb string Default thumbnail URL, auto-generated from video if not provided. Example: https://storage.googleapis.com/test/test/media/default-thumb.jpeg id string Unique identifier for the media item. Used for tracking and referencing. Example: media_abc123xyz optimizedUrl string URL of the optimized/compressed media. Set automatically when media optimization is enabled. Enable Optimization: Set mediaOptimization: true in the post request. Example: https://storage.googleapis.com/your-bucket/media/optimized-image.jpg optimizedType string MIME type of the optimized media. May differ from original if format conversion occurred. Example: image/jpeg isModified boolean Flag indicating if the media was modified (watermarked, optimized, or processed). Example: true ] |
| **url** | `string` | No |  |
| **caption** | `string` | No |  |
| **originalUrl** | `string` | No |  |
| **watermarkedUrl** | `string` | No |  |
| **type** | `string` | No |  |
| **thumbnail** | `string` | No |  |
| **defaultThumb** | `string` | No |  |
| **id** | `string` | No |  |
| **optimizedUrl** | `string` | No |  |
| **optimizedType** | `string` | No |  |
| **isModified** | `boolean` | No |  |
| **status** | `object` | No |  |
| **scheduleDate** | `string` | No |  |
| **selectedBestTime** | `string` | No |  |
| **createdBy** | `string` | No |  |
| **followUpComment** | `string` | No |  |
| **ogTagsDetails** | `object` | No | Og Tags Meta Data metaImage string Preview image URL for the shared link. Best Practices: Use high-quality images (1200x630px recommended) Ensure the image is publicly accessible Auto-fetch: Use the Get Metatags API to fetch OG data from a URL. Example: https://yoursite.com/images/og-image.jpg metaLink string URL of the webpage being shared. This is the destination when users click the link preview. Example: https://yoursite.com/blog/amazing-article ogTitle string Custom title for the link preview. Overrides the page's og:title meta tag. Tip: Keep titles concise (50-60 characters) for best display across platforms. Example: How to Double Your Social Media Engagement ogDescription string Custom description for the link preview. Overrides the page's og:description meta tag. Tip: Keep descriptions under 155 characters for optimal display. Example: Learn proven strategies to boost your social media engagement and grow your audience. |
| **metaImage** | `string` | No |  |
| **metaLink** | `string` | No |  |
| **ogTitle** | `string` | No |  |
| **ogDescription** | `string` | No |  |
| **type** | `object` | No |  |
| **postApprovalDetails** | `object` | Yes | Post Approval Details approver string User ID of the designated approver. Note: The approver will receive a notification when a post is submitted for review. Example: iVrVJ2uoXNF0wzcBzgl5 requesterNote string Note from the post creator to the approver explaining the post or requesting specific feedback. Example: Please review the messaging for our Q4 campaign launch. Let me know if the CTA needs adjustment. approverNote string Note from the approver to the post creator with feedback or approval comments. Example: Approved! Great content. Consider adding more hashtags for visibility. approvalStatus string Current approval status of the post. Available Values: pending - Awaiting approver review approved - Approved and ready for publishing rejected - Rejected by approver (needs revision) not_required - No approval workflow needed Possible values: [ pending , approved , rejected , not_required ] Example: pending |
| **approver** | `string` | No |  |
| **requesterNote** | `string` | No |  |
| **approverNote** | `string` | No |  |
| **approvalStatus** | `string` | No |  |
| **scheduleTimeUpdated** | `boolean` | No |  |
| **tags** | `string[]` | No |  |
| **categoryId** | `string` | No |  |
| **applyWatermark** | `boolean` | No |  |
| **tiktokPostDetails** | `object` | Yes | Tiktok Post Details privacyLevel string required Privacy level controlling who can view the video. Available Values: PUBLIC_TO_EVERYONE - Anyone can view (default) MUTUAL_FOLLOW_FRIENDS - Only mutual followers can view SELF_ONLY - Only you can view (private) Note: If set to SELF_ONLY , videoDisclosure must be false . Possible values: [ PUBLIC_TO_EVERYONE , MUTUAL_FOLLOW_FRIENDS , SELF_ONLY ] Example: PUBLIC_TO_EVERYONE promoteOtherBrand boolean Indicates if the video promotes a third-party brand or product. Required: Must be true if videoDisclosure is enabled and you're promoting another brand. Example: false enableComment boolean Allow users to comment on the video. Default is determined by account settings. Example: true enableDuet boolean Allow users to create Duet videos with your content. Duet: Side-by-side video featuring your content and the creator's reaction/addition. Example: true enableStitch boolean Allow users to create Stitch videos with your content. Stitch: Clips up to 5 seconds of your video that creators can use in their own videos. Example: true videoDisclosure boolean Enable branded content disclosure. Required when video is promotional content. Validations: Cannot be true if privacyLevel is SELF_ONLY If enabled, at least one of promoteYourBrand or promoteOtherBrand must be true Example: false promoteYourBrand boolean Indicates if the video promotes your own brand or product. Required: Must be true if videoDisclosure is enabled and you're promoting your own brand. Example: false |
| **privacyLevel** | `string` | No |  |
| **promoteOtherBrand** | `boolean` | No |  |
| **enableComment** | `boolean` | No |  |
| **enableDuet** | `boolean` | No |  |
| **enableStitch** | `boolean` | No |  |
| **videoDisclosure** | `boolean` | No |  |
| **promoteYourBrand** | `boolean` | No |  |
| **gmbPostDetails** | `object` | Yes | GMB Post Details gmbEventType string required Google My Business post type. Available Types: STANDARD - Regular update post (What's New) EVENT - Event announcement with dates and title OFFER - Promotional offer with coupon and redemption details Required fields by type: STANDARD: None additional EVENT: title , startDate , endDate OFFER: offerTitle , startDate , endDate , termsConditions , couponCode , redeemOnlineUrl Possible values: [ STANDARD , EVENT , OFFER ] Example: STANDARD title string Event title. Required when gmbEventType is EVENT . Max length: 58 characters Example: Summer Sale Event 2024 offerTitle string Offer title. Required when gmbEventType is OFFER . Example: 50% Off All Products startDate object Start date and time for EVENT or OFFER posts. Required: When gmbEventType is EVENT or OFFER . Structure: startDate : { year, month, day } startTime : { hours, minutes, seconds } startDate object Start Date year number required Year component of the date Example: 2022 month number required Month component of the date (1-12) Example: 1 day number required Day component of the date (1-31) Example: 1 startTime object Start Time hours number required Hour component of the time (0-23) Example: 23 minutes number required Minute component of the time (0-59) Example: 56 seconds number required Second component of the time (0-59) Example: 34 endDate object End date and time for EVENT or OFFER posts. Required: When gmbEventType is EVENT or OFFER . Validation: Must be after startDate . Structure: endDate : { year, month, day } endTime : { hours, minutes, seconds } endDate object End Date year number required Year component of the date Example: 2022 month number required Month component of the date (1-12) Example: 1 day number required Day component of the date (1-31) Example: 1 endTime object End Time hours number required Hour component of the time (0-23) Example: 23 minutes number required Minute component of the time (0-59) Example: 56 seconds number required Second component of the time (0-59) Example: 34 termsConditions string URL to terms and conditions page. Required for OFFER posts. Example: https://yoursite.com/terms-and-conditions url string Call-to-action URL. Required when actionType is set (except none and call ). Required for: STANDARD and EVENT posts with actionType other than none or call . Example: https://yoursite.com/book-now couponCode string Promotional coupon code. Required for OFFER posts. Example: SAVE50 redeemOnlineUrl string URL where customers can redeem the offer online. Required for OFFER posts. Example: https://yoursite.com/redeem-offer actionType string Call-to-action button type for the post. Available Actions: none - No action button order - Order online book - Book appointment shop - Shop now learn_more - Learn more call - Call now (no URL required) sign_up - Sign up Note: All actions except none and call require a url . Possible values: [ none , order , book , shop , learn_more , call , sign_up ] Example: book |
| **gmbEventType** | `string` | No |  |
| **title** | `string` | No |  |
| **offerTitle** | `string` | No |  |
| **startDate** | `object` | Yes | Start date and time for EVENT or OFFER posts. Required: When gmbEventType is EVENT or OFFER . Structure: startDate : { year, month, day } startTime : { hours, minutes, seconds } startDate object Start Date year number required Year component of the date Example: 2022 month number required Month component of the date (1-12) Example: 1 day number required Day component of the date (1-31) Example: 1 startTime object Start Time hours number required Hour component of the time (0-23) Example: 23 minutes number required Minute component of the time (0-59) Example: 56 seconds number required Second component of the time (0-59) Example: 34 |
| **startDate** | `object` | Yes | Start Date year number required Year component of the date Example: 2022 month number required Month component of the date (1-12) Example: 1 day number required Day component of the date (1-31) Example: 1 |
| **year** | `number` | No |  |
| **month** | `number` | No |  |
| **day** | `number` | No |  |
| **startTime** | `object` | Yes | Start Time hours number required Hour component of the time (0-23) Example: 23 minutes number required Minute component of the time (0-59) Example: 56 seconds number required Second component of the time (0-59) Example: 34 |
| **hours** | `number` | No |  |
| **minutes** | `number` | No |  |
| **seconds** | `number` | No |  |
| **endDate** | `object` | Yes | End date and time for EVENT or OFFER posts. Required: When gmbEventType is EVENT or OFFER . Validation: Must be after startDate . Structure: endDate : { year, month, day } endTime : { hours, minutes, seconds } endDate object End Date year number required Year component of the date Example: 2022 month number required Month component of the date (1-12) Example: 1 day number required Day component of the date (1-31) Example: 1 endTime object End Time hours number required Hour component of the time (0-23) Example: 23 minutes number required Minute component of the time (0-59) Example: 56 seconds number required Second component of the time (0-59) Example: 34 |
| **endDate** | `object` | Yes | End Date year number required Year component of the date Example: 2022 month number required Month component of the date (1-12) Example: 1 day number required Day component of the date (1-31) Example: 1 |
| **year** | `number` | No |  |
| **month** | `number` | No |  |
| **day** | `number` | No |  |
| **endTime** | `object` | Yes | End Time hours number required Hour component of the time (0-23) Example: 23 minutes number required Minute component of the time (0-59) Example: 56 seconds number required Second component of the time (0-59) Example: 34 |
| **hours** | `number` | No |  |
| **minutes** | `number` | No |  |
| **seconds** | `number` | No |  |
| **termsConditions** | `string` | No |  |
| **url** | `string` | No |  |
| **couponCode** | `string` | No |  |
| **redeemOnlineUrl** | `string` | No |  |
| **actionType** | `string` | No |  |
| **userId** | `string` | No |  |
| **linkedinPostDetails** | `object` | Yes | Linkedin Post Details pdfTitle string required Title for the PDF document carousel. Displayed as the document name on LinkedIn. Max length: 100 characters Tip: Use a descriptive title that explains the document content. Example: Q4 Marketing Strategy Presentation postAsPdf boolean required Post images as a PDF document carousel. Limits: Max 300 pages/images Max PDF size: 100 MB Example: true |
| **pdfTitle** | `string` | No |  |
| **postAsPdf** | `boolean` | No |  |
| **pinterestPostDetails** | `object` | Yes | Pinterest Post Details title string Pin title displayed on Pinterest. Max length: 100 characters Best Practices: Include relevant keywords Be descriptive and engaging Example: 10 Easy Home Decor Ideas for 2024 link string Destination URL for the pin. Users clicking the pin will be directed to this URL. Max length: 2048 characters Best Practices: Use direct links to relevant content Track with UTM parameters for analytics Example: https://yoursite.com/blog/home-decor-ideas boardIds object required Mapping of Pinterest account OAuth IDs to their respective board IDs. Structure: { accountOAuthId: boardId } Get Board IDs from: Get Pinterest Boards API — use the id field from each board. Create Boards: Create Pinterest Board API to create new boards. Required: Each Pinterest account in the post must have a corresponding board ID. property name* string shortenedLinks string[] Shortened links for the post (auto-generated). |
| **title** | `string` | No |  |
| **link** | `string` | No |  |
| **boardIds** | `object` | Yes | Mapping of Pinterest account OAuth IDs to their respective board IDs. Structure: { accountOAuthId: boardId } Get Board IDs from: Get Pinterest Boards API — use the id field from each board. Create Boards: Create Pinterest Board API to create new boards. Required: Each Pinterest account in the post must have a corresponding board ID. property name* string |
| **property name*** | `string` | No |  |
| **shortenedLinks** | `string[]` | No |  |
| **facebookPostDetails** | `object` | Yes | Facebook Post Details type string required Facebook post format type. Available Types: post - Standard feed post (images, videos, text) story - 24-hour temporary story reel - Short-form vertical video Restrictions: Reels: Require exactly 1 video, not supported on Groups Stories: Captions not supported Possible values: [ post , story , reel ] Example: post |
| **type** | `string` | No |  |
| **instagramPostDetails** | `object` | Yes | Instagram Post Details type string required Instagram post format type. Available Types: post - Standard feed post (images, videos, carousels) story - 24-hour temporary story reel - Short-form vertical video (up to 90 seconds) Restrictions: Media is REQUIRED for all Instagram posts Reels: Require exactly 1 video Stories: Captions not supported, JPEG only for images Possible values: [ post , story , reel ] Example: post collaborators object Object mapping account IDs to arrays of associated usernames for collaboration. Only allowed for type "post" and "reels" Example: {"accountId1":["username1","username2"],"accountId2":["username3","username4"]} showOnFeed boolean Show Reel on profile grid/feed. ✅ Applies to: Reels only true - Reel appears on your profile grid false - Reel only appears in Reels tab Example: true publishViaPushNotification boolean Send Instagram Story via Push  Notification instead of direct posting. Only applicable for Story type. Example: true publisherNote string Note to the publisher for manual posting guidance. Only used when publishViaPushNotification is true. Example: When publishing, add swipe up link to the landing page so that we can direct them to the sales page |
| **type** | `string` | No |  |
| **collaborators** | `object` | No |  |
| **showOnFeed** | `boolean` | No |  |
| **publishViaPushNotification** | `boolean` | No |  |
| **publisherNote** | `string` | No |  |
| **youtubePostDetails** | `object` | Yes | Youtube Post Details title string Video title displayed on YouTube. Max length: 100 characters Best Practices: Include relevant keywords Be descriptive but concise Avoid clickbait Example: How to Build a Successful Marketing Strategy in 2024 privacyLevel string Video visibility/privacy setting. Available Values: public - Anyone can search and view unlisted - Only people with the link can view private - Only you can view Possible values: [ private , public , unlisted ] Example: public type string required YouTube video format type. Available Types: video - Standard YouTube video (landscape, any duration) short - YouTube Shorts (vertical, up to 60 seconds) Required field. Possible values: [ video , short ] Example: video |
| **title** | `string` | No |  |
| **privacyLevel** | `string` | No |  |
| **type** | `string` | No |  |
| **communityPostDetails** | `object` | Yes | Community Post Details title string required Title of the community post. Displayed as the post headline. Max length: 1,000 characters Required: Yes, for all Community posts. Example: Welcome to Our New Community Feature! notifyAllGroupMembers boolean required Send push notification to all group members when the post is published. Use Case: Enable for important announcements to ensure all members are notified. Example: true postAsUser object required Mapping of Community account OAuth IDs to user details for posting on behalf of users. Structure: { accountOAuthId: { id, name, avatar } } id (required): User ID within the Community group name (optional): Display name for the post author avatar (optional): Profile image URL Get Account OAuth IDs from: Get Accounts API — use the oAuthId field from Community accounts. Required: Yes, each Community account in accountIds must have a corresponding entry here. Example: {"xMQswA02zgqKPpxITe":{"avatar":"https://lh3.googleusercontent.com/a/user-avatar.jpg","id":"snCr14eeYkSppD04rkNW","name":"John Smith"}} |
| **title** | `string` | No |  |
| **notifyAllGroupMembers** | `boolean` | No |  |
| **postAsUser** | `object` | No |  |
| **locationId** | `string` | No |  |
| **modifiedPostPayload** | `object` | Yes | The formatted post data modified from original post. _id string MongoDB document ID of the post Example: 61bb16833b3f2791f9715be2 source string source must be one of the following values: composer, recurring, csv Possible values: [ composer , csv , recurring , review , rss , template-library , category-queue , native ] Example: composer locationId string required Location Id Example: ve9EPM428h8vShlRW1KT displayDate date-time Display date for the post Example: 2023-08-02T00:00:00.000Z createdAt date-time Date when the post was created Example: 2023-08-02T00:00:00.000Z updatedAt date-time Date when the post was last updated Example: 2023-08-02T00:00:00.000Z accountId string Account Id Example: w37swmmLbA02zgqKPpxITe error string required Error Example: Failed due to auth token postId string Platform-specific post identifier Example: 323534534435 publishedAt string Date when the post was published Example: 2021-06-22T05:32:49.463Z accountIds string[] Account Ids Example: ["aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496"] summary string Content text of the post Example: Sample Summary media object[] Post Media Data The limitations of media as per the platforms is provided through the reference link in API description Array [ url string required Public URL of the media file. Must be a valid, accessible HTTPS URL. Example: https://storage.googleapis.com/your-bucket/media/image.jpg caption string Alt text or caption for the media. Used for accessibility and SEO. Example: Team meeting discussing Q4 marketing strategy originalUrl string Original media URL before any processing (watermarking/optimization). Set automatically by the system. Example: https://storage.googleapis.com/test/test/media/original.jpeg watermarkedUrl string URL of the media after watermarking. Set automatically when watermark is applied. Example: https://storage.googleapis.com/test/test/media/watermarked.jpeg type string required MIME type of the media file. See Platform Limitations Guide for platform-specific format support. Possible values: [ image/jpeg , image/jpg , image/png , image/gif , video/mp4 , video/mov , video/webm ] Example: image/jpeg thumbnail string URL of the video thumbnail image. Used for video preview before playback. Tip: For videos, providing a custom thumbnail improves engagement. Example: https://storage.googleapis.com/your-bucket/media/video-thumbnail.jpeg defaultThumb string Default thumbnail URL, auto-generated from video if not provided. Example: https://storage.googleapis.com/test/test/media/default-thumb.jpeg id string Unique identifier for the media item. Used for tracking and referencing. Example: media_abc123xyz optimizedUrl string URL of the optimized/compressed media. Set automatically when media optimization is enabled. Enable Optimization: Set mediaOptimization: true in the post request. Example: https://storage.googleapis.com/your-bucket/media/optimized-image.jpg optimizedType string MIME type of the optimized media. May differ from original if format conversion occurred. Example: image/jpeg isModified boolean Flag indicating if the media was modified (watermarked, optimized, or processed). Example: true ] status object Status must be one of the following values: in_progress, draft, failed, published, scheduled, in_review, notification_sent, deleted Example: published createdBy string User ID who created the post Example: Lx1EI6YIgQYMQi0ytFXv type object required Post Type must be one of the following values: - post, story, reel Example: post tags string[] Tag Ids Example: ["aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496"] ogTagsDetails object Og Tags Meta Data metaImage string Preview image URL for the shared link. Best Practices: Use high-quality images (1200x630px recommended) Ensure the image is publicly accessible Auto-fetch: Use the Get Metatags API to fetch OG data from a URL. Example: https://yoursite.com/images/og-image.jpg metaLink string URL of the webpage being shared. This is the destination when users click the link preview. Example: https://yoursite.com/blog/amazing-article ogTitle string Custom title for the link preview. Overrides the page's og:title meta tag. Tip: Keep titles concise (50-60 characters) for best display across platforms. Example: How to Double Your Social Media Engagement ogDescription string Custom description for the link preview. Overrides the page's og:description meta tag. Tip: Keep descriptions under 155 characters for optimal display. Example: Learn proven strategies to boost your social media engagement and grow your audience. postApprovalDetails object Post Approval Details approver string User ID of the designated approver. Note: The approver will receive a notification when a post is submitted for review. Example: iVrVJ2uoXNF0wzcBzgl5 requesterNote string Note from the post creator to the approver explaining the post or requesting specific feedback. Example: Please review the messaging for our Q4 campaign launch. Let me know if the CTA needs adjustment. approverNote string Note from the approver to the post creator with feedback or approval comments. Example: Approved! Great content. Consider adding more hashtags for visibility. approvalStatus string Current approval status of the post. Available Values: pending - Awaiting approver review approved - Approved and ready for publishing rejected - Rejected by approver (needs revision) not_required - No approval workflow needed Possible values: [ pending , approved , rejected , not_required ] Example: pending approverUser object Approver User Details id string required User Id Example: 6284c43d519161e96cc09c13 title string required Title Example: Mr firstName string required First name Example: Harry lastName string required Last name Example: Spencer profilePhoto string required Profile photo Example: https://storage.googleapis.com/user/kCrjKGHZQ2/profile/1dca8c-61c9-404d-a459-751fbcb.jpeg phone string required Phone number Example: 901111119 email string required Email Id Example: abc@xyc.com tiktokPostDetails object Tiktok Post Details privacyLevel string required Privacy level controlling who can view the video. Available Values: PUBLIC_TO_EVERYONE - Anyone can view (default) MUTUAL_FOLLOW_FRIENDS - Only mutual followers can view SELF_ONLY - Only you can view (private) Note: If set to SELF_ONLY , videoDisclosure must be false . Possible values: [ PUBLIC_TO_EVERYONE , MUTUAL_FOLLOW_FRIENDS , SELF_ONLY ] Example: PUBLIC_TO_EVERYONE promoteOtherBrand boolean Indicates if the video promotes a third-party brand or product. Required: Must be true if videoDisclosure is enabled and you're promoting another brand. Example: false enableComment boolean Allow users to comment on the video. Default is determined by account settings. Example: true enableDuet boolean Allow users to create Duet videos with your content. Duet: Side-by-side video featuring your content and the creator's reaction/addition. Example: true enableStitch boolean Allow users to create Stitch videos with your content. Stitch: Clips up to 5 seconds of your video that creators can use in their own videos. Example: true videoDisclosure boolean Enable branded content disclosure. Required when video is promotional content. Validations: Cannot be true if privacyLevel is SELF_ONLY If enabled, at least one of promoteYourBrand or promoteOtherBrand must be true Example: false promoteYourBrand boolean Indicates if the video promotes your own brand or product. Required: Must be true if videoDisclosure is enabled and you're promoting your own brand. Example: false gmbPostDetails object GMB Post Details gmbEventType string required Google My Business post type. Available Types: STANDARD - Regular update post (What's New) EVENT - Event announcement with dates and title OFFER - Promotional offer with coupon and redemption details Required fields by type: STANDARD: None additional EVENT: title , startDate , endDate OFFER: offerTitle , startDate , endDate , termsConditions , couponCode , redeemOnlineUrl Possible values: [ STANDARD , EVENT , OFFER ] Example: STANDARD title string Event title. Required when gmbEventType is EVENT . Max length: 58 characters Example: Summer Sale Event 2024 offerTitle string Offer title. Required when gmbEventType is OFFER . Example: 50% Off All Products startDate object Start date and time for EVENT or OFFER posts. Required: When gmbEventType is EVENT or OFFER . Structure: startDate : { year, month, day } startTime : { hours, minutes, seconds } startDate object Start Date year number required Year component of the date Example: 2022 month number required Month component of the date (1-12) Example: 1 day number required Day component of the date (1-31) Example: 1 startTime object Start Time hours number required Hour component of the time (0-23) Example: 23 minutes number required Minute component of the time (0-59) Example: 56 seconds number required Second component of the time (0-59) Example: 34 endDate object End date and time for EVENT or OFFER posts. Required: When gmbEventType is EVENT or OFFER . Validation: Must be after startDate . Structure: endDate : { year, month, day } endTime : { hours, minutes, seconds } endDate object End Date year number required Year component of the date Example: 2022 month number required Month component of the date (1-12) Example: 1 day number required Day component of the date (1-31) Example: 1 endTime object End Time hours number required Hour component of the time (0-23) Example: 23 minutes number required Minute component of the time (0-59) Example: 56 seconds number required Second component of the time (0-59) Example: 34 termsConditions string URL to terms and conditions page. Required for OFFER posts. Example: https://yoursite.com/terms-and-conditions url string Call-to-action URL. Required when actionType is set (except none and call ). Required for: STANDARD and EVENT posts with actionType other than none or call . Example: https://yoursite.com/book-now couponCode string Promotional coupon code. Required for OFFER posts. Example: SAVE50 redeemOnlineUrl string URL where customers can redeem the offer online. Required for OFFER posts. Example: https://yoursite.com/redeem-offer actionType string Call-to-action button type for the post. Available Actions: none - No action button order - Order online book - Book appointment shop - Shop now learn_more - Learn more call - Call now (no URL required) sign_up - Sign up Note: All actions except none and call require a url . Possible values: [ none , order , book , shop , learn_more , call , sign_up ] Example: book user object User id string required User Id Example: 6284c43d519161e96cc09c13 title string required Title Example: Mr firstName string required First name Example: Harry lastName string required Last name Example: Spencer profilePhoto string required Profile photo Example: https://storage.googleapis.com/user/kCrjKGHZQ2/profile/1dca8c-61c9-404d-a459-751fbcb.jpeg phone string required Phone number Example: 901111119 email string required Email Id Example: abc@xyc.com linkedinPostDetails object Linkedin Post Details pdfTitle string required Title for the PDF document carousel. Displayed as the document name on LinkedIn. Max length: 100 characters Tip: Use a descriptive title that explains the document content. Example: Q4 Marketing Strategy Presentation postAsPdf boolean required Post images as a PDF document carousel. Limits: Max 300 pages/images Max PDF size: 100 MB Example: true pinterestPostDetails object Pinterest Post Details title string Pin title displayed on Pinterest. Max length: 100 characters Best Practices: Include relevant keywords Be descriptive and engaging Example: 10 Easy Home Decor Ideas for 2024 link string Destination URL for the pin. Users clicking the pin will be directed to this URL. Max length: 2048 characters Best Practices: Use direct links to relevant content Track with UTM parameters for analytics Example: https://yoursite.com/blog/home-decor-ideas boardIds object required Mapping of Pinterest account OAuth IDs to their respective board IDs. Structure: { accountOAuthId: boardId } Get Board IDs from: Get Pinterest Boards API — use the id field from each board. Create Boards: Create Pinterest Board API to create new boards. Required: Each Pinterest account in the post must have a corresponding board ID. property name* string shortenedLinks string[] Shortened links for the post (auto-generated). facebookPostDetails object Facebook Post Details type string required Facebook post format type. Available Types: post - Standard feed post (images, videos, text) story - 24-hour temporary story reel - Short-form vertical video Restrictions: Reels: Require exactly 1 video, not supported on Groups Stories: Captions not supported Possible values: [ post , story , reel ] Example: post instagramPostDetails object Instagram Post Details type string required Instagram post format type. Available Types: post - Standard feed post (images, videos, carousels) story - 24-hour temporary story reel - Short-form vertical video (up to 90 seconds) Restrictions: Media is REQUIRED for all Instagram posts Reels: Require exactly 1 video Stories: Captions not supported, JPEG only for images Possible values: [ post , story , reel ] Example: post collaborators object Object mapping account IDs to arrays of associated usernames for collaboration. Only allowed for type "post" and "reels" Example: {"accountId1":["username1","username2"],"accountId2":["username3","username4"]} showOnFeed boolean Show Reel on profile grid/feed. ✅ Applies to: Reels only true - Reel appears on your profile grid false - Reel only appears in Reels tab Example: true publishViaPushNotification boolean Send Instagram Story via Push  Notification instead of direct posting. Only applicable for Story type. Example: true publisherNote string Note to the publisher for manual posting guidance. Only used when publishViaPushNotification is true. Example: When publishing, add swipe up link to the landing page so that we can direct them to the sales page youtubePostDetails object Youtube Post Details title string Video title displayed on YouTube. Max length: 100 characters Best Practices: Include relevant keywords Be descriptive but concise Avoid clickbait Example: How to Build a Successful Marketing Strategy in 2024 privacyLevel string Video visibility/privacy setting. Available Values: public - Anyone can search and view unlisted - Only people with the link can view private - Only you can view Possible values: [ private , public , unlisted ] Example: public type string required YouTube video format type. Available Types: video - Standard YouTube video (landscape, any duration) short - YouTube Shorts (vertical, up to 60 seconds) Required field. Possible values: [ video , short ] Example: video communityPostDetails object Community Post Details title string required Title of the community post. Displayed as the post headline. Max length: 1,000 characters Required: Yes, for all Community posts. Example: Welcome to Our New Community Feature! notifyAllGroupMembers boolean required Send push notification to all group members when the post is published. Use Case: Enable for important announcements to ensure all members are notified. Example: true postAsUser object required Mapping of Community account OAuth IDs to user details for posting on behalf of users. Structure: { accountOAuthId: { id, name, avatar } } id (required): User ID within the Community group name (optional): Display name for the post author avatar (optional): Profile image URL Get Account OAuth IDs from: Get Accounts API — use the oAuthId field from Community accounts. Required: Yes, each Community account in accountIds must have a corresponding entry here. Example: {"xMQswA02zgqKPpxITe":{"avatar":"https://lh3.googleusercontent.com/a/user-avatar.jpg","id":"snCr14eeYkSppD04rkNW","name":"John Smith"}} mediaOptimization boolean Pass this parameter to optimize the image media Example: true |
| **_id** | `string` | No |  |
| **source** | `string` | No |  |
| **locationId** | `string` | No |  |
| **displayDate** | `date-time` | No |  |
| **createdAt** | `date-time` | No |  |
| **updatedAt** | `date-time` | No |  |
| **accountId** | `string` | No |  |
| **error** | `string` | No |  |
| **postId** | `string` | No |  |
| **publishedAt** | `string` | No |  |
| **accountIds** | `string[]` | No |  |
| **summary** | `string` | No |  |
| **media** | `object[]` | Yes | Post Media Data The limitations of media as per the platforms is provided through the reference link in API description Array [ url string required Public URL of the media file. Must be a valid, accessible HTTPS URL. Example: https://storage.googleapis.com/your-bucket/media/image.jpg caption string Alt text or caption for the media. Used for accessibility and SEO. Example: Team meeting discussing Q4 marketing strategy originalUrl string Original media URL before any processing (watermarking/optimization). Set automatically by the system. Example: https://storage.googleapis.com/test/test/media/original.jpeg watermarkedUrl string URL of the media after watermarking. Set automatically when watermark is applied. Example: https://storage.googleapis.com/test/test/media/watermarked.jpeg type string required MIME type of the media file. See Platform Limitations Guide for platform-specific format support. Possible values: [ image/jpeg , image/jpg , image/png , image/gif , video/mp4 , video/mov , video/webm ] Example: image/jpeg thumbnail string URL of the video thumbnail image. Used for video preview before playback. Tip: For videos, providing a custom thumbnail improves engagement. Example: https://storage.googleapis.com/your-bucket/media/video-thumbnail.jpeg defaultThumb string Default thumbnail URL, auto-generated from video if not provided. Example: https://storage.googleapis.com/test/test/media/default-thumb.jpeg id string Unique identifier for the media item. Used for tracking and referencing. Example: media_abc123xyz optimizedUrl string URL of the optimized/compressed media. Set automatically when media optimization is enabled. Enable Optimization: Set mediaOptimization: true in the post request. Example: https://storage.googleapis.com/your-bucket/media/optimized-image.jpg optimizedType string MIME type of the optimized media. May differ from original if format conversion occurred. Example: image/jpeg isModified boolean Flag indicating if the media was modified (watermarked, optimized, or processed). Example: true ] |
| **url** | `string` | No |  |
| **caption** | `string` | No |  |
| **originalUrl** | `string` | No |  |
| **watermarkedUrl** | `string` | No |  |
| **type** | `string` | No |  |
| **thumbnail** | `string` | No |  |
| **defaultThumb** | `string` | No |  |
| **id** | `string` | No |  |
| **optimizedUrl** | `string` | No |  |
| **optimizedType** | `string` | No |  |
| **isModified** | `boolean` | No |  |
| **status** | `object` | No |  |
| **createdBy** | `string` | No |  |
| **type** | `object` | No |  |
| **tags** | `string[]` | No |  |
| **ogTagsDetails** | `object` | No | Og Tags Meta Data metaImage string Preview image URL for the shared link. Best Practices: Use high-quality images (1200x630px recommended) Ensure the image is publicly accessible Auto-fetch: Use the Get Metatags API to fetch OG data from a URL. Example: https://yoursite.com/images/og-image.jpg metaLink string URL of the webpage being shared. This is the destination when users click the link preview. Example: https://yoursite.com/blog/amazing-article ogTitle string Custom title for the link preview. Overrides the page's og:title meta tag. Tip: Keep titles concise (50-60 characters) for best display across platforms. Example: How to Double Your Social Media Engagement ogDescription string Custom description for the link preview. Overrides the page's og:description meta tag. Tip: Keep descriptions under 155 characters for optimal display. Example: Learn proven strategies to boost your social media engagement and grow your audience. |
| **metaImage** | `string` | No |  |
| **metaLink** | `string` | No |  |
| **ogTitle** | `string` | No |  |
| **ogDescription** | `string` | No |  |
| **postApprovalDetails** | `object` | Yes | Post Approval Details approver string User ID of the designated approver. Note: The approver will receive a notification when a post is submitted for review. Example: iVrVJ2uoXNF0wzcBzgl5 requesterNote string Note from the post creator to the approver explaining the post or requesting specific feedback. Example: Please review the messaging for our Q4 campaign launch. Let me know if the CTA needs adjustment. approverNote string Note from the approver to the post creator with feedback or approval comments. Example: Approved! Great content. Consider adding more hashtags for visibility. approvalStatus string Current approval status of the post. Available Values: pending - Awaiting approver review approved - Approved and ready for publishing rejected - Rejected by approver (needs revision) not_required - No approval workflow needed Possible values: [ pending , approved , rejected , not_required ] Example: pending approverUser object Approver User Details id string required User Id Example: 6284c43d519161e96cc09c13 title string required Title Example: Mr firstName string required First name Example: Harry lastName string required Last name Example: Spencer profilePhoto string required Profile photo Example: https://storage.googleapis.com/user/kCrjKGHZQ2/profile/1dca8c-61c9-404d-a459-751fbcb.jpeg phone string required Phone number Example: 901111119 email string required Email Id Example: abc@xyc.com |
| **approver** | `string` | No |  |
| **requesterNote** | `string` | No |  |
| **approverNote** | `string` | No |  |
| **approvalStatus** | `string` | No |  |
| **approverUser** | `object` | Yes | Approver User Details id string required User Id Example: 6284c43d519161e96cc09c13 title string required Title Example: Mr firstName string required First name Example: Harry lastName string required Last name Example: Spencer profilePhoto string required Profile photo Example: https://storage.googleapis.com/user/kCrjKGHZQ2/profile/1dca8c-61c9-404d-a459-751fbcb.jpeg phone string required Phone number Example: 901111119 email string required Email Id Example: abc@xyc.com |
| **id** | `string` | No |  |
| **title** | `string` | No |  |
| **firstName** | `string` | No |  |
| **lastName** | `string` | No |  |
| **profilePhoto** | `string` | No |  |
| **phone** | `string` | No |  |
| **email** | `string` | No |  |
| **tiktokPostDetails** | `object` | Yes | Tiktok Post Details privacyLevel string required Privacy level controlling who can view the video. Available Values: PUBLIC_TO_EVERYONE - Anyone can view (default) MUTUAL_FOLLOW_FRIENDS - Only mutual followers can view SELF_ONLY - Only you can view (private) Note: If set to SELF_ONLY , videoDisclosure must be false . Possible values: [ PUBLIC_TO_EVERYONE , MUTUAL_FOLLOW_FRIENDS , SELF_ONLY ] Example: PUBLIC_TO_EVERYONE promoteOtherBrand boolean Indicates if the video promotes a third-party brand or product. Required: Must be true if videoDisclosure is enabled and you're promoting another brand. Example: false enableComment boolean Allow users to comment on the video. Default is determined by account settings. Example: true enableDuet boolean Allow users to create Duet videos with your content. Duet: Side-by-side video featuring your content and the creator's reaction/addition. Example: true enableStitch boolean Allow users to create Stitch videos with your content. Stitch: Clips up to 5 seconds of your video that creators can use in their own videos. Example: true videoDisclosure boolean Enable branded content disclosure. Required when video is promotional content. Validations: Cannot be true if privacyLevel is SELF_ONLY If enabled, at least one of promoteYourBrand or promoteOtherBrand must be true Example: false promoteYourBrand boolean Indicates if the video promotes your own brand or product. Required: Must be true if videoDisclosure is enabled and you're promoting your own brand. Example: false |
| **privacyLevel** | `string` | No |  |
| **promoteOtherBrand** | `boolean` | No |  |
| **enableComment** | `boolean` | No |  |
| **enableDuet** | `boolean` | No |  |
| **enableStitch** | `boolean` | No |  |
| **videoDisclosure** | `boolean` | No |  |
| **promoteYourBrand** | `boolean` | No |  |
| **gmbPostDetails** | `object` | Yes | GMB Post Details gmbEventType string required Google My Business post type. Available Types: STANDARD - Regular update post (What's New) EVENT - Event announcement with dates and title OFFER - Promotional offer with coupon and redemption details Required fields by type: STANDARD: None additional EVENT: title , startDate , endDate OFFER: offerTitle , startDate , endDate , termsConditions , couponCode , redeemOnlineUrl Possible values: [ STANDARD , EVENT , OFFER ] Example: STANDARD title string Event title. Required when gmbEventType is EVENT . Max length: 58 characters Example: Summer Sale Event 2024 offerTitle string Offer title. Required when gmbEventType is OFFER . Example: 50% Off All Products startDate object Start date and time for EVENT or OFFER posts. Required: When gmbEventType is EVENT or OFFER . Structure: startDate : { year, month, day } startTime : { hours, minutes, seconds } startDate object Start Date year number required Year component of the date Example: 2022 month number required Month component of the date (1-12) Example: 1 day number required Day component of the date (1-31) Example: 1 startTime object Start Time hours number required Hour component of the time (0-23) Example: 23 minutes number required Minute component of the time (0-59) Example: 56 seconds number required Second component of the time (0-59) Example: 34 endDate object End date and time for EVENT or OFFER posts. Required: When gmbEventType is EVENT or OFFER . Validation: Must be after startDate . Structure: endDate : { year, month, day } endTime : { hours, minutes, seconds } endDate object End Date year number required Year component of the date Example: 2022 month number required Month component of the date (1-12) Example: 1 day number required Day component of the date (1-31) Example: 1 endTime object End Time hours number required Hour component of the time (0-23) Example: 23 minutes number required Minute component of the time (0-59) Example: 56 seconds number required Second component of the time (0-59) Example: 34 termsConditions string URL to terms and conditions page. Required for OFFER posts. Example: https://yoursite.com/terms-and-conditions url string Call-to-action URL. Required when actionType is set (except none and call ). Required for: STANDARD and EVENT posts with actionType other than none or call . Example: https://yoursite.com/book-now couponCode string Promotional coupon code. Required for OFFER posts. Example: SAVE50 redeemOnlineUrl string URL where customers can redeem the offer online. Required for OFFER posts. Example: https://yoursite.com/redeem-offer actionType string Call-to-action button type for the post. Available Actions: none - No action button order - Order online book - Book appointment shop - Shop now learn_more - Learn more call - Call now (no URL required) sign_up - Sign up Note: All actions except none and call require a url . Possible values: [ none , order , book , shop , learn_more , call , sign_up ] Example: book |
| **gmbEventType** | `string` | No |  |
| **title** | `string` | No |  |
| **offerTitle** | `string` | No |  |
| **startDate** | `object` | Yes | Start date and time for EVENT or OFFER posts. Required: When gmbEventType is EVENT or OFFER . Structure: startDate : { year, month, day } startTime : { hours, minutes, seconds } startDate object Start Date year number required Year component of the date Example: 2022 month number required Month component of the date (1-12) Example: 1 day number required Day component of the date (1-31) Example: 1 startTime object Start Time hours number required Hour component of the time (0-23) Example: 23 minutes number required Minute component of the time (0-59) Example: 56 seconds number required Second component of the time (0-59) Example: 34 |
| **startDate** | `object` | Yes | Start Date year number required Year component of the date Example: 2022 month number required Month component of the date (1-12) Example: 1 day number required Day component of the date (1-31) Example: 1 |
| **year** | `number` | No |  |
| **month** | `number` | No |  |
| **day** | `number` | No |  |
| **startTime** | `object` | Yes | Start Time hours number required Hour component of the time (0-23) Example: 23 minutes number required Minute component of the time (0-59) Example: 56 seconds number required Second component of the time (0-59) Example: 34 |
| **hours** | `number` | No |  |
| **minutes** | `number` | No |  |
| **seconds** | `number` | No |  |
| **endDate** | `object` | Yes | End date and time for EVENT or OFFER posts. Required: When gmbEventType is EVENT or OFFER . Validation: Must be after startDate . Structure: endDate : { year, month, day } endTime : { hours, minutes, seconds } endDate object End Date year number required Year component of the date Example: 2022 month number required Month component of the date (1-12) Example: 1 day number required Day component of the date (1-31) Example: 1 endTime object End Time hours number required Hour component of the time (0-23) Example: 23 minutes number required Minute component of the time (0-59) Example: 56 seconds number required Second component of the time (0-59) Example: 34 |
| **endDate** | `object` | Yes | End Date year number required Year component of the date Example: 2022 month number required Month component of the date (1-12) Example: 1 day number required Day component of the date (1-31) Example: 1 |
| **year** | `number` | No |  |
| **month** | `number` | No |  |
| **day** | `number` | No |  |
| **endTime** | `object` | Yes | End Time hours number required Hour component of the time (0-23) Example: 23 minutes number required Minute component of the time (0-59) Example: 56 seconds number required Second component of the time (0-59) Example: 34 |
| **hours** | `number` | No |  |
| **minutes** | `number` | No |  |
| **seconds** | `number` | No |  |
| **termsConditions** | `string` | No |  |
| **url** | `string` | No |  |
| **couponCode** | `string` | No |  |
| **redeemOnlineUrl** | `string` | No |  |
| **actionType** | `string` | No |  |
| **user** | `object` | Yes | User id string required User Id Example: 6284c43d519161e96cc09c13 title string required Title Example: Mr firstName string required First name Example: Harry lastName string required Last name Example: Spencer profilePhoto string required Profile photo Example: https://storage.googleapis.com/user/kCrjKGHZQ2/profile/1dca8c-61c9-404d-a459-751fbcb.jpeg phone string required Phone number Example: 901111119 email string required Email Id Example: abc@xyc.com |
| **id** | `string` | No |  |
| **title** | `string` | No |  |
| **firstName** | `string` | No |  |
| **lastName** | `string` | No |  |
| **profilePhoto** | `string` | No |  |
| **phone** | `string` | No |  |
| **email** | `string` | No |  |
| **linkedinPostDetails** | `object` | Yes | Linkedin Post Details pdfTitle string required Title for the PDF document carousel. Displayed as the document name on LinkedIn. Max length: 100 characters Tip: Use a descriptive title that explains the document content. Example: Q4 Marketing Strategy Presentation postAsPdf boolean required Post images as a PDF document carousel. Limits: Max 300 pages/images Max PDF size: 100 MB Example: true |
| **pdfTitle** | `string` | No |  |
| **postAsPdf** | `boolean` | No |  |
| **pinterestPostDetails** | `object` | Yes | Pinterest Post Details title string Pin title displayed on Pinterest. Max length: 100 characters Best Practices: Include relevant keywords Be descriptive and engaging Example: 10 Easy Home Decor Ideas for 2024 link string Destination URL for the pin. Users clicking the pin will be directed to this URL. Max length: 2048 characters Best Practices: Use direct links to relevant content Track with UTM parameters for analytics Example: https://yoursite.com/blog/home-decor-ideas boardIds object required Mapping of Pinterest account OAuth IDs to their respective board IDs. Structure: { accountOAuthId: boardId } Get Board IDs from: Get Pinterest Boards API — use the id field from each board. Create Boards: Create Pinterest Board API to create new boards. Required: Each Pinterest account in the post must have a corresponding board ID. property name* string shortenedLinks string[] Shortened links for the post (auto-generated). |
| **title** | `string` | No |  |
| **link** | `string` | No |  |
| **boardIds** | `object` | Yes | Mapping of Pinterest account OAuth IDs to their respective board IDs. Structure: { accountOAuthId: boardId } Get Board IDs from: Get Pinterest Boards API — use the id field from each board. Create Boards: Create Pinterest Board API to create new boards. Required: Each Pinterest account in the post must have a corresponding board ID. property name* string |
| **property name*** | `string` | No |  |
| **shortenedLinks** | `string[]` | No |  |
| **facebookPostDetails** | `object` | Yes | Facebook Post Details type string required Facebook post format type. Available Types: post - Standard feed post (images, videos, text) story - 24-hour temporary story reel - Short-form vertical video Restrictions: Reels: Require exactly 1 video, not supported on Groups Stories: Captions not supported Possible values: [ post , story , reel ] Example: post |
| **type** | `string` | No |  |
| **instagramPostDetails** | `object` | Yes | Instagram Post Details type string required Instagram post format type. Available Types: post - Standard feed post (images, videos, carousels) story - 24-hour temporary story reel - Short-form vertical video (up to 90 seconds) Restrictions: Media is REQUIRED for all Instagram posts Reels: Require exactly 1 video Stories: Captions not supported, JPEG only for images Possible values: [ post , story , reel ] Example: post collaborators object Object mapping account IDs to arrays of associated usernames for collaboration. Only allowed for type "post" and "reels" Example: {"accountId1":["username1","username2"],"accountId2":["username3","username4"]} showOnFeed boolean Show Reel on profile grid/feed. ✅ Applies to: Reels only true - Reel appears on your profile grid false - Reel only appears in Reels tab Example: true publishViaPushNotification boolean Send Instagram Story via Push  Notification instead of direct posting. Only applicable for Story type. Example: true publisherNote string Note to the publisher for manual posting guidance. Only used when publishViaPushNotification is true. Example: When publishing, add swipe up link to the landing page so that we can direct them to the sales page |
| **type** | `string` | No |  |
| **collaborators** | `object` | No |  |
| **showOnFeed** | `boolean` | No |  |
| **publishViaPushNotification** | `boolean` | No |  |
| **publisherNote** | `string` | No |  |
| **youtubePostDetails** | `object` | Yes | Youtube Post Details title string Video title displayed on YouTube. Max length: 100 characters Best Practices: Include relevant keywords Be descriptive but concise Avoid clickbait Example: How to Build a Successful Marketing Strategy in 2024 privacyLevel string Video visibility/privacy setting. Available Values: public - Anyone can search and view unlisted - Only people with the link can view private - Only you can view Possible values: [ private , public , unlisted ] Example: public type string required YouTube video format type. Available Types: video - Standard YouTube video (landscape, any duration) short - YouTube Shorts (vertical, up to 60 seconds) Required field. Possible values: [ video , short ] Example: video |
| **title** | `string` | No |  |
| **privacyLevel** | `string` | No |  |
| **type** | `string` | No |  |
| **communityPostDetails** | `object` | Yes | Community Post Details title string required Title of the community post. Displayed as the post headline. Max length: 1,000 characters Required: Yes, for all Community posts. Example: Welcome to Our New Community Feature! notifyAllGroupMembers boolean required Send push notification to all group members when the post is published. Use Case: Enable for important announcements to ensure all members are notified. Example: true postAsUser object required Mapping of Community account OAuth IDs to user details for posting on behalf of users. Structure: { accountOAuthId: { id, name, avatar } } id (required): User ID within the Community group name (optional): Display name for the post author avatar (optional): Profile image URL Get Account OAuth IDs from: Get Accounts API — use the oAuthId field from Community accounts. Required: Yes, each Community account in accountIds must have a corresponding entry here. Example: {"xMQswA02zgqKPpxITe":{"avatar":"https://lh3.googleusercontent.com/a/user-avatar.jpg","id":"snCr14eeYkSppD04rkNW","name":"John Smith"}} |
| **title** | `string` | No |  |
| **notifyAllGroupMembers** | `boolean` | No |  |
| **postAsUser** | `object` | No |  |
| **mediaOptimization** | `boolean` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

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

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **success** | `bool` |  |
| **statusCode** | `int` |  |
| **results** | `dict` |  |
| **traceId** | `str` |  |

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
  --url https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/items/:itemId \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "locationId": "string",
  "sessionId": "string",
  "modifiedPostPayload": "string",
  "accountIds": "string",
  "summary": "string",
  "media": "string",
  "url": "string",
  "caption": "string",
  "originalUrl": "string",
  "watermarkedUrl": "string",
  "type": "string",
  "thumbnail": "string",
  "defaultThumb": "string",
  "id": "string",
  "optimizedUrl": "string",
  "optimizedType": "string",
  "isModified": true,
  "status": "string",
  "scheduleDate": "string",
  "selectedBestTime": "string",
  "createdBy": "string",
  "followUpComment": "string",
  "ogTagsDetails": "string",
  "metaImage": "string",
  "metaLink": "string",
  "ogTitle": "string",
  "ogDescription": "string",
  "postApprovalDetails": "string",
  "approver": "string",
  "requesterNote": "string",
  "approverNote": "string",
  "approvalStatus": "string",
  "scheduleTimeUpdated": true,
  "tags": "string",
  "categoryId": "string",
  "applyWatermark": true,
  "tiktokPostDetails": "string",
  "privacyLevel": "string",
  "promoteOtherBrand": true,
  "enableComment": true,
  "enableDuet": true,
  "enableStitch": true,
  "videoDisclosure": true,
  "promoteYourBrand": true,
  "gmbPostDetails": "string",
  "gmbEventType": "string",
  "title": "string",
  "offerTitle": "string",
  "startDate": "string",
  "year": 123,
  "month": 123,
  "day": 123,
  "startTime": "string",
  "hours": 123,
  "minutes": 123,
  "seconds": 123,
  "endDate": "string",
  "endTime": "string",
  "termsConditions": "string",
  "couponCode": "string",
  "redeemOnlineUrl": "string",
  "actionType": "string",
  "userId": "string",
  "linkedinPostDetails": "string",
  "pdfTitle": "string",
  "postAsPdf": true,
  "pinterestPostDetails": "string",
  "link": "string",
  "boardIds": "string",
  "property name*": "string",
  "shortenedLinks": "string",
  "facebookPostDetails": "string",
  "instagramPostDetails": "string",
  "collaborators": "string",
  "showOnFeed": true,
  "publishViaPushNotification": true,
  "publisherNote": "string",
  "youtubePostDetails": "string",
  "communityPostDetails": "string",
  "notifyAllGroupMembers": true,
  "postAsUser": "string",
  "newOrder": "string",
  "": "string",
  "variations": "string",
  "content": "string",
  "mentions": "string",
  "ogTags": "string",
  "primaryImage": "string",
  "_id": "string",
  "source": "string",
  "displayDate": "string",
  "createdAt": "string",
  "updatedAt": "string",
  "accountId": "string",
  "error": "string",
  "postId": "string",
  "publishedAt": "string",
  "approverUser": "string",
  "firstName": "string",
  "lastName": "string",
  "profilePhoto": "string",
  "phone": "string",
  "email": "string",
  "user": "string",
  "mediaOptimization": true
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
    const response = await ghl.api.request('PUT', 'https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/items/:itemId', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "locationId": "string",
  "sessionId": "string",
  "modifiedPostPayload": "string",
  "accountIds": "string",
  "summary": "string",
  "media": "string",
  "url": "string",
  "caption": "string",
  "originalUrl": "string",
  "watermarkedUrl": "string",
  "type": "string",
  "thumbnail": "string",
  "defaultThumb": "string",
  "id": "string",
  "optimizedUrl": "string",
  "optimizedType": "string",
  "isModified": true,
  "status": "string",
  "scheduleDate": "string",
  "selectedBestTime": "string",
  "createdBy": "string",
  "followUpComment": "string",
  "ogTagsDetails": "string",
  "metaImage": "string",
  "metaLink": "string",
  "ogTitle": "string",
  "ogDescription": "string",
  "postApprovalDetails": "string",
  "approver": "string",
  "requesterNote": "string",
  "approverNote": "string",
  "approvalStatus": "string",
  "scheduleTimeUpdated": true,
  "tags": "string",
  "categoryId": "string",
  "applyWatermark": true,
  "tiktokPostDetails": "string",
  "privacyLevel": "string",
  "promoteOtherBrand": true,
  "enableComment": true,
  "enableDuet": true,
  "enableStitch": true,
  "videoDisclosure": true,
  "promoteYourBrand": true,
  "gmbPostDetails": "string",
  "gmbEventType": "string",
  "title": "string",
  "offerTitle": "string",
  "startDate": "string",
  "year": 123,
  "month": 123,
  "day": 123,
  "startTime": "string",
  "hours": 123,
  "minutes": 123,
  "seconds": 123,
  "endDate": "string",
  "endTime": "string",
  "termsConditions": "string",
  "couponCode": "string",
  "redeemOnlineUrl": "string",
  "actionType": "string",
  "userId": "string",
  "linkedinPostDetails": "string",
  "pdfTitle": "string",
  "postAsPdf": true,
  "pinterestPostDetails": "string",
  "link": "string",
  "boardIds": "string",
  "property name*": "string",
  "shortenedLinks": "string",
  "facebookPostDetails": "string",
  "instagramPostDetails": "string",
  "collaborators": "string",
  "showOnFeed": true,
  "publishViaPushNotification": true,
  "publisherNote": "string",
  "youtubePostDetails": "string",
  "communityPostDetails": "string",
  "notifyAllGroupMembers": true,
  "postAsUser": "string",
  "newOrder": "string",
  "": "string",
  "variations": "string",
  "content": "string",
  "mentions": "string",
  "ogTags": "string",
  "primaryImage": "string",
  "_id": "string",
  "source": "string",
  "displayDate": "string",
  "createdAt": "string",
  "updatedAt": "string",
  "accountId": "string",
  "error": "string",
  "postId": "string",
  "publishedAt": "string",
  "approverUser": "string",
  "firstName": "string",
  "lastName": "string",
  "profilePhoto": "string",
  "phone": "string",
  "email": "string",
  "user": "string",
  "mediaOptimization": true
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
  url: 'https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/items/:itemId',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "locationId": "string",
  "sessionId": "string",
  "modifiedPostPayload": "string",
  "accountIds": "string",
  "summary": "string",
  "media": "string",
  "url": "string",
  "caption": "string",
  "originalUrl": "string",
  "watermarkedUrl": "string",
  "type": "string",
  "thumbnail": "string",
  "defaultThumb": "string",
  "id": "string",
  "optimizedUrl": "string",
  "optimizedType": "string",
  "isModified": true,
  "status": "string",
  "scheduleDate": "string",
  "selectedBestTime": "string",
  "createdBy": "string",
  "followUpComment": "string",
  "ogTagsDetails": "string",
  "metaImage": "string",
  "metaLink": "string",
  "ogTitle": "string",
  "ogDescription": "string",
  "postApprovalDetails": "string",
  "approver": "string",
  "requesterNote": "string",
  "approverNote": "string",
  "approvalStatus": "string",
  "scheduleTimeUpdated": true,
  "tags": "string",
  "categoryId": "string",
  "applyWatermark": true,
  "tiktokPostDetails": "string",
  "privacyLevel": "string",
  "promoteOtherBrand": true,
  "enableComment": true,
  "enableDuet": true,
  "enableStitch": true,
  "videoDisclosure": true,
  "promoteYourBrand": true,
  "gmbPostDetails": "string",
  "gmbEventType": "string",
  "title": "string",
  "offerTitle": "string",
  "startDate": "string",
  "year": 123,
  "month": 123,
  "day": 123,
  "startTime": "string",
  "hours": 123,
  "minutes": 123,
  "seconds": 123,
  "endDate": "string",
  "endTime": "string",
  "termsConditions": "string",
  "couponCode": "string",
  "redeemOnlineUrl": "string",
  "actionType": "string",
  "userId": "string",
  "linkedinPostDetails": "string",
  "pdfTitle": "string",
  "postAsPdf": true,
  "pinterestPostDetails": "string",
  "link": "string",
  "boardIds": "string",
  "property name*": "string",
  "shortenedLinks": "string",
  "facebookPostDetails": "string",
  "instagramPostDetails": "string",
  "collaborators": "string",
  "showOnFeed": true,
  "publishViaPushNotification": true,
  "publisherNote": "string",
  "youtubePostDetails": "string",
  "communityPostDetails": "string",
  "notifyAllGroupMembers": true,
  "postAsUser": "string",
  "newOrder": "string",
  "": "string",
  "variations": "string",
  "content": "string",
  "mentions": "string",
  "ogTags": "string",
  "primaryImage": "string",
  "_id": "string",
  "source": "string",
  "displayDate": "string",
  "createdAt": "string",
  "updatedAt": "string",
  "accountId": "string",
  "error": "string",
  "postId": "string",
  "publishedAt": "string",
  "approverUser": "string",
  "firstName": "string",
  "lastName": "string",
  "profilePhoto": "string",
  "phone": "string",
  "email": "string",
  "user": "string",
  "mediaOptimization": true
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
  'path': '/social-media-posting/category/queues/:queueId/items/:itemId',
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
  "locationId": "string",
  "sessionId": "string",
  "modifiedPostPayload": "string",
  "accountIds": "string",
  "summary": "string",
  "media": "string",
  "url": "string",
  "caption": "string",
  "originalUrl": "string",
  "watermarkedUrl": "string",
  "type": "string",
  "thumbnail": "string",
  "defaultThumb": "string",
  "id": "string",
  "optimizedUrl": "string",
  "optimizedType": "string",
  "isModified": true,
  "status": "string",
  "scheduleDate": "string",
  "selectedBestTime": "string",
  "createdBy": "string",
  "followUpComment": "string",
  "ogTagsDetails": "string",
  "metaImage": "string",
  "metaLink": "string",
  "ogTitle": "string",
  "ogDescription": "string",
  "postApprovalDetails": "string",
  "approver": "string",
  "requesterNote": "string",
  "approverNote": "string",
  "approvalStatus": "string",
  "scheduleTimeUpdated": true,
  "tags": "string",
  "categoryId": "string",
  "applyWatermark": true,
  "tiktokPostDetails": "string",
  "privacyLevel": "string",
  "promoteOtherBrand": true,
  "enableComment": true,
  "enableDuet": true,
  "enableStitch": true,
  "videoDisclosure": true,
  "promoteYourBrand": true,
  "gmbPostDetails": "string",
  "gmbEventType": "string",
  "title": "string",
  "offerTitle": "string",
  "startDate": "string",
  "year": 123,
  "month": 123,
  "day": 123,
  "startTime": "string",
  "hours": 123,
  "minutes": 123,
  "seconds": 123,
  "endDate": "string",
  "endTime": "string",
  "termsConditions": "string",
  "couponCode": "string",
  "redeemOnlineUrl": "string",
  "actionType": "string",
  "userId": "string",
  "linkedinPostDetails": "string",
  "pdfTitle": "string",
  "postAsPdf": true,
  "pinterestPostDetails": "string",
  "link": "string",
  "boardIds": "string",
  "property name*": "string",
  "shortenedLinks": "string",
  "facebookPostDetails": "string",
  "instagramPostDetails": "string",
  "collaborators": "string",
  "showOnFeed": true,
  "publishViaPushNotification": true,
  "publisherNote": "string",
  "youtubePostDetails": "string",
  "communityPostDetails": "string",
  "notifyAllGroupMembers": true,
  "postAsUser": "string",
  "newOrder": "string",
  "": "string",
  "variations": "string",
  "content": "string",
  "mentions": "string",
  "ogTags": "string",
  "primaryImage": "string",
  "_id": "string",
  "source": "string",
  "displayDate": "string",
  "createdAt": "string",
  "updatedAt": "string",
  "accountId": "string",
  "error": "string",
  "postId": "string",
  "publishedAt": "string",
  "approverUser": "string",
  "firstName": "string",
  "lastName": "string",
  "profilePhoto": "string",
  "phone": "string",
  "email": "string",
  "user": "string",
  "mediaOptimization": true
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'PUT',
  'url': 'https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/items/:itemId',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "locationId": "string",
  "sessionId": "string",
  "modifiedPostPayload": "string",
  "accountIds": "string",
  "summary": "string",
  "media": "string",
  "url": "string",
  "caption": "string",
  "originalUrl": "string",
  "watermarkedUrl": "string",
  "type": "string",
  "thumbnail": "string",
  "defaultThumb": "string",
  "id": "string",
  "optimizedUrl": "string",
  "optimizedType": "string",
  "isModified": true,
  "status": "string",
  "scheduleDate": "string",
  "selectedBestTime": "string",
  "createdBy": "string",
  "followUpComment": "string",
  "ogTagsDetails": "string",
  "metaImage": "string",
  "metaLink": "string",
  "ogTitle": "string",
  "ogDescription": "string",
  "postApprovalDetails": "string",
  "approver": "string",
  "requesterNote": "string",
  "approverNote": "string",
  "approvalStatus": "string",
  "scheduleTimeUpdated": true,
  "tags": "string",
  "categoryId": "string",
  "applyWatermark": true,
  "tiktokPostDetails": "string",
  "privacyLevel": "string",
  "promoteOtherBrand": true,
  "enableComment": true,
  "enableDuet": true,
  "enableStitch": true,
  "videoDisclosure": true,
  "promoteYourBrand": true,
  "gmbPostDetails": "string",
  "gmbEventType": "string",
  "title": "string",
  "offerTitle": "string",
  "startDate": "string",
  "year": 123,
  "month": 123,
  "day": 123,
  "startTime": "string",
  "hours": 123,
  "minutes": 123,
  "seconds": 123,
  "endDate": "string",
  "endTime": "string",
  "termsConditions": "string",
  "couponCode": "string",
  "redeemOnlineUrl": "string",
  "actionType": "string",
  "userId": "string",
  "linkedinPostDetails": "string",
  "pdfTitle": "string",
  "postAsPdf": true,
  "pinterestPostDetails": "string",
  "link": "string",
  "boardIds": "string",
  "property name*": "string",
  "shortenedLinks": "string",
  "facebookPostDetails": "string",
  "instagramPostDetails": "string",
  "collaborators": "string",
  "showOnFeed": true,
  "publishViaPushNotification": true,
  "publisherNote": "string",
  "youtubePostDetails": "string",
  "communityPostDetails": "string",
  "notifyAllGroupMembers": true,
  "postAsUser": "string",
  "newOrder": "string",
  "": "string",
  "variations": "string",
  "content": "string",
  "mentions": "string",
  "ogTags": "string",
  "primaryImage": "string",
  "_id": "string",
  "source": "string",
  "displayDate": "string",
  "createdAt": "string",
  "updatedAt": "string",
  "accountId": "string",
  "error": "string",
  "postId": "string",
  "publishedAt": "string",
  "approverUser": "string",
  "firstName": "string",
  "lastName": "string",
  "profilePhoto": "string",
  "phone": "string",
  "email": "string",
  "user": "string",
  "mediaOptimization": true
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

unirest('PUT', 'https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/items/:itemId')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "locationId": "string",
  "sessionId": "string",
  "modifiedPostPayload": "string",
  "accountIds": "string",
  "summary": "string",
  "media": "string",
  "url": "string",
  "caption": "string",
  "originalUrl": "string",
  "watermarkedUrl": "string",
  "type": "string",
  "thumbnail": "string",
  "defaultThumb": "string",
  "id": "string",
  "optimizedUrl": "string",
  "optimizedType": "string",
  "isModified": true,
  "status": "string",
  "scheduleDate": "string",
  "selectedBestTime": "string",
  "createdBy": "string",
  "followUpComment": "string",
  "ogTagsDetails": "string",
  "metaImage": "string",
  "metaLink": "string",
  "ogTitle": "string",
  "ogDescription": "string",
  "postApprovalDetails": "string",
  "approver": "string",
  "requesterNote": "string",
  "approverNote": "string",
  "approvalStatus": "string",
  "scheduleTimeUpdated": true,
  "tags": "string",
  "categoryId": "string",
  "applyWatermark": true,
  "tiktokPostDetails": "string",
  "privacyLevel": "string",
  "promoteOtherBrand": true,
  "enableComment": true,
  "enableDuet": true,
  "enableStitch": true,
  "videoDisclosure": true,
  "promoteYourBrand": true,
  "gmbPostDetails": "string",
  "gmbEventType": "string",
  "title": "string",
  "offerTitle": "string",
  "startDate": "string",
  "year": 123,
  "month": 123,
  "day": 123,
  "startTime": "string",
  "hours": 123,
  "minutes": 123,
  "seconds": 123,
  "endDate": "string",
  "endTime": "string",
  "termsConditions": "string",
  "couponCode": "string",
  "redeemOnlineUrl": "string",
  "actionType": "string",
  "userId": "string",
  "linkedinPostDetails": "string",
  "pdfTitle": "string",
  "postAsPdf": true,
  "pinterestPostDetails": "string",
  "link": "string",
  "boardIds": "string",
  "property name*": "string",
  "shortenedLinks": "string",
  "facebookPostDetails": "string",
  "instagramPostDetails": "string",
  "collaborators": "string",
  "showOnFeed": true,
  "publishViaPushNotification": true,
  "publisherNote": "string",
  "youtubePostDetails": "string",
  "communityPostDetails": "string",
  "notifyAllGroupMembers": true,
  "postAsUser": "string",
  "newOrder": "string",
  "": "string",
  "variations": "string",
  "content": "string",
  "mentions": "string",
  "ogTags": "string",
  "primaryImage": "string",
  "_id": "string",
  "source": "string",
  "displayDate": "string",
  "createdAt": "string",
  "updatedAt": "string",
  "accountId": "string",
  "error": "string",
  "postId": "string",
  "publishedAt": "string",
  "approverUser": "string",
  "firstName": "string",
  "lastName": "string",
  "profilePhoto": "string",
  "phone": "string",
  "email": "string",
  "user": "string",
  "mediaOptimization": true
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/items/:itemId"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("PUT", url, headers=headers, data=json.dumps({
  "locationId": "string",
  "sessionId": "string",
  "modifiedPostPayload": "string",
  "accountIds": "string",
  "summary": "string",
  "media": "string",
  "url": "string",
  "caption": "string",
  "originalUrl": "string",
  "watermarkedUrl": "string",
  "type": "string",
  "thumbnail": "string",
  "defaultThumb": "string",
  "id": "string",
  "optimizedUrl": "string",
  "optimizedType": "string",
  "isModified": true,
  "status": "string",
  "scheduleDate": "string",
  "selectedBestTime": "string",
  "createdBy": "string",
  "followUpComment": "string",
  "ogTagsDetails": "string",
  "metaImage": "string",
  "metaLink": "string",
  "ogTitle": "string",
  "ogDescription": "string",
  "postApprovalDetails": "string",
  "approver": "string",
  "requesterNote": "string",
  "approverNote": "string",
  "approvalStatus": "string",
  "scheduleTimeUpdated": true,
  "tags": "string",
  "categoryId": "string",
  "applyWatermark": true,
  "tiktokPostDetails": "string",
  "privacyLevel": "string",
  "promoteOtherBrand": true,
  "enableComment": true,
  "enableDuet": true,
  "enableStitch": true,
  "videoDisclosure": true,
  "promoteYourBrand": true,
  "gmbPostDetails": "string",
  "gmbEventType": "string",
  "title": "string",
  "offerTitle": "string",
  "startDate": "string",
  "year": 123,
  "month": 123,
  "day": 123,
  "startTime": "string",
  "hours": 123,
  "minutes": 123,
  "seconds": 123,
  "endDate": "string",
  "endTime": "string",
  "termsConditions": "string",
  "couponCode": "string",
  "redeemOnlineUrl": "string",
  "actionType": "string",
  "userId": "string",
  "linkedinPostDetails": "string",
  "pdfTitle": "string",
  "postAsPdf": true,
  "pinterestPostDetails": "string",
  "link": "string",
  "boardIds": "string",
  "property name*": "string",
  "shortenedLinks": "string",
  "facebookPostDetails": "string",
  "instagramPostDetails": "string",
  "collaborators": "string",
  "showOnFeed": true,
  "publishViaPushNotification": true,
  "publisherNote": "string",
  "youtubePostDetails": "string",
  "communityPostDetails": "string",
  "notifyAllGroupMembers": true,
  "postAsUser": "string",
  "newOrder": "string",
  "": "string",
  "variations": "string",
  "content": "string",
  "mentions": "string",
  "ogTags": "string",
  "primaryImage": "string",
  "_id": "string",
  "source": "string",
  "displayDate": "string",
  "createdAt": "string",
  "updatedAt": "string",
  "accountId": "string",
  "error": "string",
  "postId": "string",
  "publishedAt": "string",
  "approverUser": "string",
  "firstName": "string",
  "lastName": "string",
  "profilePhoto": "string",
  "phone": "string",
  "email": "string",
  "user": "string",
  "mediaOptimization": true
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
$response = $client->request('PUT', 'https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/items/:itemId', [
  'headers' => $headers,
  'body' => '{
  "locationId": "string",
  "sessionId": "string",
  "modifiedPostPayload": "string",
  "accountIds": "string",
  "summary": "string",
  "media": "string",
  "url": "string",
  "caption": "string",
  "originalUrl": "string",
  "watermarkedUrl": "string",
  "type": "string",
  "thumbnail": "string",
  "defaultThumb": "string",
  "id": "string",
  "optimizedUrl": "string",
  "optimizedType": "string",
  "isModified": true,
  "status": "string",
  "scheduleDate": "string",
  "selectedBestTime": "string",
  "createdBy": "string",
  "followUpComment": "string",
  "ogTagsDetails": "string",
  "metaImage": "string",
  "metaLink": "string",
  "ogTitle": "string",
  "ogDescription": "string",
  "postApprovalDetails": "string",
  "approver": "string",
  "requesterNote": "string",
  "approverNote": "string",
  "approvalStatus": "string",
  "scheduleTimeUpdated": true,
  "tags": "string",
  "categoryId": "string",
  "applyWatermark": true,
  "tiktokPostDetails": "string",
  "privacyLevel": "string",
  "promoteOtherBrand": true,
  "enableComment": true,
  "enableDuet": true,
  "enableStitch": true,
  "videoDisclosure": true,
  "promoteYourBrand": true,
  "gmbPostDetails": "string",
  "gmbEventType": "string",
  "title": "string",
  "offerTitle": "string",
  "startDate": "string",
  "year": 123,
  "month": 123,
  "day": 123,
  "startTime": "string",
  "hours": 123,
  "minutes": 123,
  "seconds": 123,
  "endDate": "string",
  "endTime": "string",
  "termsConditions": "string",
  "couponCode": "string",
  "redeemOnlineUrl": "string",
  "actionType": "string",
  "userId": "string",
  "linkedinPostDetails": "string",
  "pdfTitle": "string",
  "postAsPdf": true,
  "pinterestPostDetails": "string",
  "link": "string",
  "boardIds": "string",
  "property name*": "string",
  "shortenedLinks": "string",
  "facebookPostDetails": "string",
  "instagramPostDetails": "string",
  "collaborators": "string",
  "showOnFeed": true,
  "publishViaPushNotification": true,
  "publisherNote": "string",
  "youtubePostDetails": "string",
  "communityPostDetails": "string",
  "notifyAllGroupMembers": true,
  "postAsUser": "string",
  "newOrder": "string",
  "": "string",
  "variations": "string",
  "content": "string",
  "mentions": "string",
  "ogTags": "string",
  "primaryImage": "string",
  "_id": "string",
  "source": "string",
  "displayDate": "string",
  "createdAt": "string",
  "updatedAt": "string",
  "accountId": "string",
  "error": "string",
  "postId": "string",
  "publishedAt": "string",
  "approverUser": "string",
  "firstName": "string",
  "lastName": "string",
  "profilePhoto": "string",
  "phone": "string",
  "email": "string",
  "user": "string",
  "mediaOptimization": true
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
    .uri(URI.create("https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/items/:itemId"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("PUT", HttpRequest.BodyPublishers.ofString("{
  \"locationId\": \"string\",
  \"sessionId\": \"string\",
  \"modifiedPostPayload\": \"string\",
  \"accountIds\": \"string\",
  \"summary\": \"string\",
  \"media\": \"string\",
  \"url\": \"string\",
  \"caption\": \"string\",
  \"originalUrl\": \"string\",
  \"watermarkedUrl\": \"string\",
  \"type\": \"string\",
  \"thumbnail\": \"string\",
  \"defaultThumb\": \"string\",
  \"id\": \"string\",
  \"optimizedUrl\": \"string\",
  \"optimizedType\": \"string\",
  \"isModified\": true,
  \"status\": \"string\",
  \"scheduleDate\": \"string\",
  \"selectedBestTime\": \"string\",
  \"createdBy\": \"string\",
  \"followUpComment\": \"string\",
  \"ogTagsDetails\": \"string\",
  \"metaImage\": \"string\",
  \"metaLink\": \"string\",
  \"ogTitle\": \"string\",
  \"ogDescription\": \"string\",
  \"postApprovalDetails\": \"string\",
  \"approver\": \"string\",
  \"requesterNote\": \"string\",
  \"approverNote\": \"string\",
  \"approvalStatus\": \"string\",
  \"scheduleTimeUpdated\": true,
  \"tags\": \"string\",
  \"categoryId\": \"string\",
  \"applyWatermark\": true,
  \"tiktokPostDetails\": \"string\",
  \"privacyLevel\": \"string\",
  \"promoteOtherBrand\": true,
  \"enableComment\": true,
  \"enableDuet\": true,
  \"enableStitch\": true,
  \"videoDisclosure\": true,
  \"promoteYourBrand\": true,
  \"gmbPostDetails\": \"string\",
  \"gmbEventType\": \"string\",
  \"title\": \"string\",
  \"offerTitle\": \"string\",
  \"startDate\": \"string\",
  \"year\": 123,
  \"month\": 123,
  \"day\": 123,
  \"startTime\": \"string\",
  \"hours\": 123,
  \"minutes\": 123,
  \"seconds\": 123,
  \"endDate\": \"string\",
  \"endTime\": \"string\",
  \"termsConditions\": \"string\",
  \"couponCode\": \"string\",
  \"redeemOnlineUrl\": \"string\",
  \"actionType\": \"string\",
  \"userId\": \"string\",
  \"linkedinPostDetails\": \"string\",
  \"pdfTitle\": \"string\",
  \"postAsPdf\": true,
  \"pinterestPostDetails\": \"string\",
  \"link\": \"string\",
  \"boardIds\": \"string\",
  \"property name*\": \"string\",
  \"shortenedLinks\": \"string\",
  \"facebookPostDetails\": \"string\",
  \"instagramPostDetails\": \"string\",
  \"collaborators\": \"string\",
  \"showOnFeed\": true,
  \"publishViaPushNotification\": true,
  \"publisherNote\": \"string\",
  \"youtubePostDetails\": \"string\",
  \"communityPostDetails\": \"string\",
  \"notifyAllGroupMembers\": true,
  \"postAsUser\": \"string\",
  \"newOrder\": \"string\",
  \"\": \"string\",
  \"variations\": \"string\",
  \"content\": \"string\",
  \"mentions\": \"string\",
  \"ogTags\": \"string\",
  \"primaryImage\": \"string\",
  \"_id\": \"string\",
  \"source\": \"string\",
  \"displayDate\": \"string\",
  \"createdAt\": \"string\",
  \"updatedAt\": \"string\",
  \"accountId\": \"string\",
  \"error\": \"string\",
  \"postId\": \"string\",
  \"publishedAt\": \"string\",
  \"approverUser\": \"string\",
  \"firstName\": \"string\",
  \"lastName\": \"string\",
  \"profilePhoto\": \"string\",
  \"phone\": \"string\",
  \"email\": \"string\",
  \"user\": \"string\",
  \"mediaOptimization\": true
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
  url := "https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/items/:itemId"
  payload := strings.NewReader(`{
  "locationId": "string",
  "sessionId": "string",
  "modifiedPostPayload": "string",
  "accountIds": "string",
  "summary": "string",
  "media": "string",
  "url": "string",
  "caption": "string",
  "originalUrl": "string",
  "watermarkedUrl": "string",
  "type": "string",
  "thumbnail": "string",
  "defaultThumb": "string",
  "id": "string",
  "optimizedUrl": "string",
  "optimizedType": "string",
  "isModified": true,
  "status": "string",
  "scheduleDate": "string",
  "selectedBestTime": "string",
  "createdBy": "string",
  "followUpComment": "string",
  "ogTagsDetails": "string",
  "metaImage": "string",
  "metaLink": "string",
  "ogTitle": "string",
  "ogDescription": "string",
  "postApprovalDetails": "string",
  "approver": "string",
  "requesterNote": "string",
  "approverNote": "string",
  "approvalStatus": "string",
  "scheduleTimeUpdated": true,
  "tags": "string",
  "categoryId": "string",
  "applyWatermark": true,
  "tiktokPostDetails": "string",
  "privacyLevel": "string",
  "promoteOtherBrand": true,
  "enableComment": true,
  "enableDuet": true,
  "enableStitch": true,
  "videoDisclosure": true,
  "promoteYourBrand": true,
  "gmbPostDetails": "string",
  "gmbEventType": "string",
  "title": "string",
  "offerTitle": "string",
  "startDate": "string",
  "year": 123,
  "month": 123,
  "day": 123,
  "startTime": "string",
  "hours": 123,
  "minutes": 123,
  "seconds": 123,
  "endDate": "string",
  "endTime": "string",
  "termsConditions": "string",
  "couponCode": "string",
  "redeemOnlineUrl": "string",
  "actionType": "string",
  "userId": "string",
  "linkedinPostDetails": "string",
  "pdfTitle": "string",
  "postAsPdf": true,
  "pinterestPostDetails": "string",
  "link": "string",
  "boardIds": "string",
  "property name*": "string",
  "shortenedLinks": "string",
  "facebookPostDetails": "string",
  "instagramPostDetails": "string",
  "collaborators": "string",
  "showOnFeed": true,
  "publishViaPushNotification": true,
  "publisherNote": "string",
  "youtubePostDetails": "string",
  "communityPostDetails": "string",
  "notifyAllGroupMembers": true,
  "postAsUser": "string",
  "newOrder": "string",
  "": "string",
  "variations": "string",
  "content": "string",
  "mentions": "string",
  "ogTags": "string",
  "primaryImage": "string",
  "_id": "string",
  "source": "string",
  "displayDate": "string",
  "createdAt": "string",
  "updatedAt": "string",
  "accountId": "string",
  "error": "string",
  "postId": "string",
  "publishedAt": "string",
  "approverUser": "string",
  "firstName": "string",
  "lastName": "string",
  "profilePhoto": "string",
  "phone": "string",
  "email": "string",
  "user": "string",
  "mediaOptimization": true
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

url = URI("https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/items/:itemId")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Put.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "locationId": "string",
  "sessionId": "string",
  "modifiedPostPayload": "string",
  "accountIds": "string",
  "summary": "string",
  "media": "string",
  "url": "string",
  "caption": "string",
  "originalUrl": "string",
  "watermarkedUrl": "string",
  "type": "string",
  "thumbnail": "string",
  "defaultThumb": "string",
  "id": "string",
  "optimizedUrl": "string",
  "optimizedType": "string",
  "isModified": true,
  "status": "string",
  "scheduleDate": "string",
  "selectedBestTime": "string",
  "createdBy": "string",
  "followUpComment": "string",
  "ogTagsDetails": "string",
  "metaImage": "string",
  "metaLink": "string",
  "ogTitle": "string",
  "ogDescription": "string",
  "postApprovalDetails": "string",
  "approver": "string",
  "requesterNote": "string",
  "approverNote": "string",
  "approvalStatus": "string",
  "scheduleTimeUpdated": true,
  "tags": "string",
  "categoryId": "string",
  "applyWatermark": true,
  "tiktokPostDetails": "string",
  "privacyLevel": "string",
  "promoteOtherBrand": true,
  "enableComment": true,
  "enableDuet": true,
  "enableStitch": true,
  "videoDisclosure": true,
  "promoteYourBrand": true,
  "gmbPostDetails": "string",
  "gmbEventType": "string",
  "title": "string",
  "offerTitle": "string",
  "startDate": "string",
  "year": 123,
  "month": 123,
  "day": 123,
  "startTime": "string",
  "hours": 123,
  "minutes": 123,
  "seconds": 123,
  "endDate": "string",
  "endTime": "string",
  "termsConditions": "string",
  "couponCode": "string",
  "redeemOnlineUrl": "string",
  "actionType": "string",
  "userId": "string",
  "linkedinPostDetails": "string",
  "pdfTitle": "string",
  "postAsPdf": true,
  "pinterestPostDetails": "string",
  "link": "string",
  "boardIds": "string",
  "property name*": "string",
  "shortenedLinks": "string",
  "facebookPostDetails": "string",
  "instagramPostDetails": "string",
  "collaborators": "string",
  "showOnFeed": true,
  "publishViaPushNotification": true,
  "publisherNote": "string",
  "youtubePostDetails": "string",
  "communityPostDetails": "string",
  "notifyAllGroupMembers": true,
  "postAsUser": "string",
  "newOrder": "string",
  "": "string",
  "variations": "string",
  "content": "string",
  "mentions": "string",
  "ogTags": "string",
  "primaryImage": "string",
  "_id": "string",
  "source": "string",
  "displayDate": "string",
  "createdAt": "string",
  "updatedAt": "string",
  "accountId": "string",
  "error": "string",
  "postId": "string",
  "publishedAt": "string",
  "approverUser": "string",
  "firstName": "string",
  "lastName": "string",
  "profilePhoto": "string",
  "phone": "string",
  "email": "string",
  "user": "string",
  "mediaOptimization": true
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
  "locationId": "string",
  "sessionId": "string",
  "modifiedPostPayload": "string",
  "accountIds": "string",
  "summary": "string",
  "media": "string",
  "url": "string",
  "caption": "string",
  "originalUrl": "string",
  "watermarkedUrl": "string",
  "type": "string",
  "thumbnail": "string",
  "defaultThumb": "string",
  "id": "string",
  "optimizedUrl": "string",
  "optimizedType": "string",
  "isModified": true,
  "status": "string",
  "scheduleDate": "string",
  "selectedBestTime": "string",
  "createdBy": "string",
  "followUpComment": "string",
  "ogTagsDetails": "string",
  "metaImage": "string",
  "metaLink": "string",
  "ogTitle": "string",
  "ogDescription": "string",
  "postApprovalDetails": "string",
  "approver": "string",
  "requesterNote": "string",
  "approverNote": "string",
  "approvalStatus": "string",
  "scheduleTimeUpdated": true,
  "tags": "string",
  "categoryId": "string",
  "applyWatermark": true,
  "tiktokPostDetails": "string",
  "privacyLevel": "string",
  "promoteOtherBrand": true,
  "enableComment": true,
  "enableDuet": true,
  "enableStitch": true,
  "videoDisclosure": true,
  "promoteYourBrand": true,
  "gmbPostDetails": "string",
  "gmbEventType": "string",
  "title": "string",
  "offerTitle": "string",
  "startDate": "string",
  "year": 123,
  "month": 123,
  "day": 123,
  "startTime": "string",
  "hours": 123,
  "minutes": 123,
  "seconds": 123,
  "endDate": "string",
  "endTime": "string",
  "termsConditions": "string",
  "couponCode": "string",
  "redeemOnlineUrl": "string",
  "actionType": "string",
  "userId": "string",
  "linkedinPostDetails": "string",
  "pdfTitle": "string",
  "postAsPdf": true,
  "pinterestPostDetails": "string",
  "link": "string",
  "boardIds": "string",
  "property name*": "string",
  "shortenedLinks": "string",
  "facebookPostDetails": "string",
  "instagramPostDetails": "string",
  "collaborators": "string",
  "showOnFeed": true,
  "publishViaPushNotification": true,
  "publisherNote": "string",
  "youtubePostDetails": "string",
  "communityPostDetails": "string",
  "notifyAllGroupMembers": true,
  "postAsUser": "string",
  "newOrder": "string",
  "": "string",
  "variations": "string",
  "content": "string",
  "mentions": "string",
  "ogTags": "string",
  "primaryImage": "string",
  "_id": "string",
  "source": "string",
  "displayDate": "string",
  "createdAt": "string",
  "updatedAt": "string",
  "accountId": "string",
  "error": "string",
  "postId": "string",
  "publishedAt": "string",
  "approverUser": "string",
  "firstName": "string",
  "lastName": "string",
  "profilePhoto": "string",
  "phone": "string",
  "email": "string",
  "user": "string",
  "mediaOptimization": true
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/items/:itemId' -Method 'PUT' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
