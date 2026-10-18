# Verification completed October 15, 2026

RAG update: source-passages, cited explanations/steps, follow-up context, citation rejection, reviewed refund/payment content and import workflow are now included. Full hosted-model calls still require an API key.

The machine-readable record is `test-run-summary.json`. These results describe the local source package and do not certify an uncreated cloud deployment.

| Check | Actual result |
|---|---|
| TypeScript + Vite production build | Passed |
| Frontend Vitest API/component checks | 3 passed |
| Backend pytest acceptance/security/privacy/fallback checks | 22 passed |
| Backend statement coverage, including maintenance module | **92.51%**; 70% gate passed |
| Playwright Chromium | 3 passed |
| Playwright Firefox | 3 passed |
| Playwright WebKit | 3 passed |
| axe on tested login, student directory/saved/recent/chat/detail, admin notices and analytics views | Zero serious/critical findings in the passing scenarios |
| 390px mobile horizontal-overflow check | Passed in each tested browser |
| Synthetic offline routing, 100 name/tag-derived cases | 100% top-1, 100% top-3, 0 unknown offices; **not hosted-AI accuracy or an independent test set** |
| Frontend dependency audit after test-tool update | 0 reported vulnerabilities at audit time |
| Installed backend dependency audit | 0 known vulnerabilities in the audited local versions; re-audit the production image |
| Docker Compose configuration | Validated |

Screenshots in `screenshots/` were captured from the running application, not mockups: sign-in, directory, mobile and offline assistant.

## Not established by these results

* No API key or cloud credentials were supplied. No live OpenAI, Render, Vercel, Neon/Supabase, or BrowserStack deployment/run is claimed.
* Docker's engine was not running in this environment. The Compose file was validated, but images/containers and PostgreSQL migration/integration need the supplied Docker/CI check.
* Backend acceptance ran on isolated SQLite locally. The GitHub workflow supplies a PostgreSQL 16/pgvector job; that workflow has not been run on your repository here.
* No k6 50-user, OWASP ZAP, human SUS or service-discovery study has been completed. No fake users/ratings/hours are supplied as research evidence.
* Service source URLs, actual office hours, locations and contacts need team review. The draft seed records show explicit official-page instructions until curated.
* The generated 100-question dataset needs independent human label and paraphrase review before an AI grading claim.

Preserve actual CI reports, deployed commit/build identifiers, reviewed data sources, AI evaluation configuration and human study records for the course report. Current build/test results do not establish a named team member's historical contribution.
