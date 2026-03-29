# Contacts

Contacts
Documentation for Contacts API
📄️ Get Contact
Get Contact
📄️ Update Contact
Please find the list of acceptable values for the `country` field  <a href='https://highlevel.stoplight.io/docs/integrations/ZG9jOjI4MzUzNDIy-country-list' target='_blank'>here</a>
📄️ Delete Contact
Delete Contact
📄️ Upsert Contact
Please find the list of acceptable values for the `country` field  <a href='https://highlevel.stoplight.io/docs/integrations/ZG9jOjI4MzUzNDIy-country-list' target='_blank'>here</a><br/><br/>The Upsert API will adhere to the configuration defined under the “Allow Duplicate Contact” setting at the Location level. If the setting is configured to check both Email and Phone, the API will attempt to identify an existing contact based on the priority sequence specified in the setting, and will create or update the contact accordingly.<br/><br/>If two separate contacts already exist—one with the same email and another with the same phone—and an upsert request includes both the email and phone, the API will update the contact that matches the first field in the configured sequence, and ignore the second field to prevent duplication.
📄️ Get Contacts By BusinessId
Get Contacts By BusinessId
📄️ Create Contact
Please find the list of acceptable values for the `country` field  <a href='https://highlevel.stoplight.io/docs/integrations/ZG9jOjI4MzUzNDIy-country-list' target='_blank'>here</a>
📄️ Get Contacts
Get Contacts

## 💻 Code Snippets

```text

```

**Source:** [GHL Documentation](https://marketplace.gohighlevel.com/docs/ghl/contacts/contacts)
