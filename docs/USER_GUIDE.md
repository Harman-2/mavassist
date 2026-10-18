# User guide

## Student

Create an account with your own demo email/password. This project does not use UTA single sign-on. Never reuse your university password. After signing in:

1. **Explore resources:** search names, descriptions and tags. Select multiple category buttons to include any of those categories. Clear filters resets query and categories.
2. **View resource:** open a service for location, hours, contact, current notices, last-updated date, source and next steps. Draft seed records ask you to check the official page until reviewed.
3. **Saved resources:** bookmark a card or detail page. Remove the bookmark using the same button. Saved items are private to your account.
4. **Recently viewed:** opening a detail page updates your history. It keeps ten distinct services, newest first. Archived resources are hidden.
5. **Ask MavAssist:** use a question such as “I need help with tuition payment.” Do not enter personal/sensitive information. Answers explain the retrieved guidance and show cited sources and next steps. Follow-up questions can use the previous topic. The mode distinguishes AI with sources, source-based summaries/fallback, and clarification. Related offices appear below the answer. Verify the official resource before acting.
6. **Rate an answer:** choose Helpful or Not helpful once. Ratings feed anonymous aggregate analytics.
7. **Sign out:** ends your browser session. Tokens also expire after 60 minutes; sign in again when prompted.

## Administrator

An operator creates administrators using `python -m app.manage create-admin`; the public form creates only student accounts.

* **Manage resources / Services:** add/edit all displayed facts, source URL, tags and 2–3 next steps. Select a category. Check “Official source reviewed” only after reviewing current official information. Saving in RAG mode rebuilds the embedding. Archive hides the service from student lists/search/chat; restore reverses this.
* **Categories:** add/rename categories. Delete only unused categories; retained analytics references also block deletion to preserve history.
* **Notices:** choose an active service, enter title/text, and local start/end times. Times are sent with timezone offsets. Only notices whose dates cover the current time appear to students. Edit or remove notices as needed.
* **Usage insights:** apply a date range to see common search terms, viewed services, chatbot categories and helpfulness percentage. Empty ranges show no activity, not fabricated metrics.

## Accessibility

Keyboard navigation, visible focus, native labels, a skip-to-content link, native modal focus handling, reduced-motion support and responsive layouts are included. Screen readers receive loading/status/error feedback. Use browser zoom as needed. Automated checks cover the tested views; human keyboard/screen-reader and usability review remains necessary.
