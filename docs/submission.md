# Momentum 1.3.0 submission notes

Prepared 2026-11-27 for BitSky LLC, contact bitskyai@gmail.com. These packages have not been submitted to either directory. Review cases are authored, not executed in the target chat hosts.

## Documentation used

- [Claude plugin submission](https://claude.com/docs/plugins/submit)
- [Claude directory publishing](https://claude.com/docs/directory/publish)
- [Claude plugin checklist](https://claude.com/docs/plugins/pre-submission-checklist)
- [Claude plugin manifest reference](https://code.claude.com/docs/en/plugins/manifest-reference) (redirect from `/docs/en/plugins-reference`)
- [Claude marketplace creation](https://code.claude.com/docs/en/plugin-marketplaces) and [marketplace field reference](https://code.claude.com/docs/en/plugins/marketplace-reference)
- [OpenAI package guide](https://developers.openai.com/plugins/build/plugins). Requested `/plugins/build/package` returned HTTP 404; this is the current destination linked by the submission guide.
- [OpenAI submission and field reference](https://developers.openai.com/plugins/deploy/submission#automatically-provide-submission-and-review-information)
- [OpenAI plugin guidelines](https://developers.openai.com/plugins/plugin-guidelines)

The OpenAI guide prefers portable root `plugin.json` with the Agent Plugins `$schema` and listing fields under `extensions.com.openai.interface`. Skills are discovered from `skills/`; there is no invented `skills` field in that portable manifest. Claude uses `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`.

OpenAI's five positive/three negative manifest review cases apply to initial MCP review. Plugin-level `review.test_cases` requires exactly one MCP server. This package has none: the requested cases live in [review-cases.md](review-cases.md), with expected behavior and host access identified, and are not embedded as invalid MCP review metadata.

## URL checks and deployment

| URL | Use | Status |
| --- | --- | --- |
| https://momentum.bitsky.ai/ | Website, homepage and documentation | HTTP 200 when checked 2026-11-27 |
| https://momentum.bitsky.ai/icon-512.png | Brand icon copied to assets/icon.png | HTTP 200 when checked 2026-11-27 |
| https://momentum.bitsky.ai/privacy.html | Privacy policy | Page being deployed; may return 404 |
| https://momentum.bitsky.ai/terms.html | Terms of service | Page being deployed; may return 404 |
| https://momentum.bitsky.ai/support.html | Support | Page being deployed; may return 404 |

The policy and support URLs are in both manifests using each platform's documented field names. Verify the deployed pages' contents and HTTP 200 before submission. OpenAI's skills-only package validation does not require all four listing URLs, but its guidelines require a published privacy policy. MIT LICENSE governs the code and is not a hosted service terms URL.

## Manual Claude portal checklist

- [ ] Use the intended BitSky account/organization at https://claude.ai/directory/manage on an eligible paid plan; connect a GitHub account with push access to the repository.
- [ ] Select **Submit new → Plugin bundle**.
- [ ] **Repository:** `https://github.com/bitskyai/momentum-skill`; **Plugin path:** leave blank (repository root); **Branch or tag:** `main` after merge (or `feat/marketplace-plugins` to validate this PR).
- [ ] Verify the deployed policy and support pages at the URLs above. Verify listing name Momentum, short description, icon, README and MIT license.
- [ ] Run portal **Validate** on the final commit; resolve blocking findings. Local CLI validation does not run the portal safety scan or policy review.
- [ ] **Data handling:** publisher must answer personal data read/storage, transfer to services outside declared connectors, retention, and intended use by people under 18 based on actual practices. The skill fetches public Momentum pages and bulk files using host tools, and has no bundled MCP server or plugin storage.
- [ ] **Compliance:** contact email `bitskyai@gmail.com`; authorized publisher completes all four acknowledgements.
- [ ] **Review and submit:** choose **GitHub push webhook** (requires repo admin setup) or **Scheduled check only**, confirm details, and submit for review. Configure webhook if selected. Publish the approved version separately; repo must be public before going live.

## Manual OpenAI portal checklist

- [ ] Use https://platform.openai.com/plugins in the intended organization and project (organization owner or Apps Management Write required); verify/select the **BitSky LLC developer identity**. Confirm contact `bitskyai@gmail.com` and public publisher name.
- [ ] Verify the deployed privacy, terms and support pages at the URLs above. Website is already populated and verified.
- [ ] **Upload new or existing plugin → Upload plugin:** select `momentum-openai-plugin.zip`; plugin type **Skills only**. No MCP endpoint, domain challenge, OAuth setup, or reviewer login is needed for this package.
- [ ] **Metadata & Skills:** verify imported name **Momentum by BitSky**, subtitle **Discover growing GitHub repos**, category **Developer Tools**, long description, icon, website, three starter prompts, and version **1.3.0**; wait for required skill scans and resolve findings.
- [ ] Confirm intended country availability in the portal; countries are deliberately omitted from the ZIP pending publisher choice. Confirm whether English-only listing is sufficient; translations are omitted.
- [ ] Run the eight behavioral cases in the intended hosts and record actual outcomes. They are manual acceptance material; MCP review cases, recording URL, and test credentials are not required for this skills-only submission.
- [ ] Review imported release notes. Complete any portal policy/commerce declarations and legal acknowledgements as the authorized publisher, then **Submit for review**. After approval select **Publish plugin** separately.

## Release maintenance

Keep both plugin versions and marketplace metadata.version synchronized with the upstream skill (currently 1.3.0). The star-growth-dashboard sync job must bump these wrappers too. This is documentation only; no upstream job is changed here. Claude tracks the chosen GitHub branch/tag, while each directory retains its own review/publication steps. Rebuild the full ZIP from the committed revision for each OpenAI update:

```sh
git archive --format=zip -o momentum-openai-plugin.zip HEAD plugin.json skills/momentum/SKILL.md assets/icon.png LICENSE
```
