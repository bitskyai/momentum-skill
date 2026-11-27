# Momentum plugin packaging plan

Goal: distribute the unchanged Momentum 1.3.0 skill through Claude, OpenAI, and skills.sh.
Architecture: Claude manifest and marketplace at repository root; portable OpenAI root manifest; both discover skills/momentum. Explicit ZIP allowlist prevents unrelated wrappers and files entering the upload.

- [x] Read current official publishing and manifest documentation.
- [x] Add documented platform manifests, publisher metadata, and the existing site icon.
- [x] Add eight manual behavioral review cases, install instructions, and submission TODOs.
- [x] Build and inspect ZIP; validate Claude and skills.sh discovery; confirm skill bytes unchanged.
- [x] Review packaging and prepare PR body with source citations and portal checklist.
- Delivery: commit and push this branch; open a PR to main. If blocked, preserve the prepared body as PR_BODY.md.

Constraints: do not edit skills/momentum/SKILL.md; retain MIT license and BitSky LLC identity; version 1.3.0. Do not invent policy URLs, legal attestations, country targeting, or test execution evidence.
