---
title: "HighLevel PHP SDK"
source: "https://marketplace.gohighlevel.com/docs/sdk/php"
generated_at: "2026-03-28T17:50:27.821145"
tags: ["docs", "concept"]
---

# HighLevel PHP SDK

HighLevel PHP SDK
The
gohighlevel/api-client
composer package is the officially supported SDK for PHP 7.4+ projects. It wraps the full HighLevel API with PSR-18 friendly services, automatic OAuth token rotation, webhook helpers, and pluggable session storage.
Installation
​
composer require gohighlevel/api-client
Quick Start
​
Initialize with a Private Integration Token
​
<?php
require_once __DIR__ . '/vendor/autoload.php';
use HighLevel\HighLevel;
use HighLevel\HighLevelConfig;
$config = new HighLevelConfig([
'privateIntegrationToken' => $_ENV['GHL_PIT'],
]);
$ghl = new HighLevel($config);
Initialize with OAuth credentials
​
use HighLevel\HighLevel;
use HighLevel\HighLevelConfig;
$config = new HighLevelConfig([
'clientId' => $_ENV['GHL_CLIENT_ID'],
'clientSecret' => $_ENV['GHL_CLIENT_SECRET'],
]);
$ghl = new HighLevel($config);
Make your first API call
​
use HighLevel\Services\Contacts\Models\SearchBodyV2DTO;
$body = new SearchBodyV2DTO([
'locationId' => 'zBG0T99IsBgOoXUrcROH',
'pageLimit' => 1,
]);
$contactsResponse = $ghl->contacts->searchContactsAdvanced($body);
error_log(json_encode($contactsResponse, JSON_PRETTY_PRINT));
Session storage
​
Use
HighLevel\Storage\MongoDBSessionStorage
provided by SDK to use mongo as storage or extend it to store tokens in MySQL, PostgreSQL, Redis, etc:
<?php
use HighLevel\HighLevel;
use HighLevel\Storage\MongoDBSessionStorage;
$sessionStorage = new MongoDBSessionStorage(
$config['mongo_url'],
$config['mongo_db_name'],
$config['collection_name']
);
$ghl = new HighLevel([
'clientId' => $config['client_id'],
'clientSecret' => $config['client_secret'],
'sessionStorage' => $sessionStorage,
'logLevel' => 'warn'
]);
Webhook support
​
SDK provides webhook support which can be used as shown below. It will handle INSTALL and UNINSTALL events sent by HighLevel. It will generate token and store it in the db.
$payload = $request->getBody()->getContents();
$signature = $request->getHeaderLine('x-wh-signature');
$ghl->getWebhookManager()->processWebhook(
$payload, // pass raw request body as string here
$signature,
$_ENV['WEBHOOK_PUBLIC_KEY'],
$_ENV['GHL_CLIENT_ID']
);
Call
verifySignature
directly when you just need validation:
$ghl->getWebhookManager()->verifySignature(
$payload,
$signature,
$_ENV['WEBHOOK_PUBLIC_KEY']
);
Additional resources
​
You can find some SDK & additional examples here:
SDK
packagist
Examples

## Code Snippets

```

```

```prism-code
composer require gohighlevel/api-client
```

```prism-code
<?phprequire_once __DIR__ . '/vendor/autoload.php';use HighLevel\HighLevel;use HighLevel\HighLevelConfig;$config = new HighLevelConfig(['privateIntegrationToken' => $_ENV['GHL_PIT'],]);$ghl = new HighLevel($config);
```

```prism-code
use HighLevel\HighLevel;use HighLevel\HighLevelConfig;$config = new HighLevelConfig(['clientId' => $_ENV['GHL_CLIENT_ID'],'clientSecret' => $_ENV['GHL_CLIENT_SECRET'],]);$ghl = new HighLevel($config);
```

```prism-code
use HighLevel\Services\Contacts\Models\SearchBodyV2DTO;$body = new SearchBodyV2DTO(['locationId' => 'zBG0T99IsBgOoXUrcROH','pageLimit' => 1,]);$contactsResponse = $ghl->contacts->searchContactsAdvanced($body);error_log(json_encode($contactsResponse, JSON_PRETTY_PRINT));
```

```prism-code
<?phpuse HighLevel\HighLevel;use HighLevel\Storage\MongoDBSessionStorage;$sessionStorage = new MongoDBSessionStorage($config['mongo_url'],$config['mongo_db_name'],$config['collection_name']);$ghl = new HighLevel(['clientId' => $config['client_id'],'clientSecret' => $config['client_secret'],'sessionStorage' => $sessionStorage,'logLevel' => 'warn']);
```

```prism-code
$payload = $request->getBody()->getContents();$signature = $request->getHeaderLine('x-wh-signature');$ghl->getWebhookManager()->processWebhook($payload, // pass raw request body as string here$signature,$_ENV['WEBHOOK_PUBLIC_KEY'],$_ENV['GHL_CLIENT_ID']);
```

```prism-code
$ghl->getWebhookManager()->verifySignature($payload,$signature,$_ENV['WEBHOOK_PUBLIC_KEY']);
```

