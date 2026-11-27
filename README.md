# Momentum

[Momentum](https://momentum.bitsky.ai/) helps developers discover and compare public GitHub repositories by total stars and star growth using dated daily snapshots. Filter by language, topic, or keyword over 1, 7, 30, 90, or 365 days.

## Claude Code marketplace

Run in Claude Code after this marketplace is available on the default branch:

```text
/plugin marketplace add bitskyai/momentum-skill
/plugin install bitsky-momentum@bitskyai-momentum
```

Try `/bitsky-momentum:momentum Find the fastest-growing Rust repositories this month.`
For local development: `claude --plugin-dir .`.

## ChatGPT and Codex

This repository contains a portable, skills-only OpenAI plugin. It does not yet have an approved directory listing. Once published, find **Momentum by BitSky** by **BitSky LLC** in the Plugins Directory and add it in ChatGPT or Codex where plugins are supported.

Maintainers can build the directory upload using the command in the [submission notes](docs/submission.md).

Upload `momentum-openai-plugin.zip` at [OpenAI Plugins](https://platform.openai.com/plugins), choose **Skills only**, and follow [submission notes](docs/submission.md). The ZIP contains only the portable manifest, unchanged skill, icon, and MIT license. Building it does not submit or publish it.

## skills.sh and other agents

```sh
npx skills add bitskyai/momentum-skill
```

The skill remains at `skills/momentum/SKILL.md`. To inspect local discovery without installing:

```sh
npx skills add . --list
```

Or paste into an agent: `Fetch and follow https://momentum.bitsky.ai/agent-setup/prompt.md to set me up for Momentum`.

## Usage and limits

Example prompts:

- Find the fastest-growing Rust repositories this month.
- Which AI-agent repositories gained the most stars this week?
- Compare star growth for react/react and vuejs/core.

The host needs web access. Full cohort intersections and longer lists need bulk downloads and local filtering. Momentum covers public repositories above the snapshot's star threshold; it cannot read private repositories or provide real-time counts. Answers should state the snapshot date, growth window, and matching repository count. Repository links point to GitHub. No account, API key, or MCP server is needed.

Support: [bitskyai@gmail.com](mailto:bitskyai@gmail.com). Publisher: BitSky LLC. Homepage: https://momentum.bitsky.ai/.

## Maintaining releases

The skill is synced from **star-growth-dashboard**; the latest copy is at https://momentum.bitsky.ai/agent-setup/SKILL.md. Do not hand-edit its content here. The upstream sync job must also bump `plugin.json` and `.claude-plugin/plugin.json` to match the skill version, and `.claude-plugin/marketplace.json`'s `metadata.version`. Current version: **1.3.0**. This repository documents that required sync change; it does not modify the upstream repository.

After a sync, validate Claude, rebuild and inspect the OpenAI ZIP, and rerun the [behavioral cases](docs/review-cases.md). Submit a new version through each portal; a Git push alone does not publish an OpenAI release.

MIT licensed. © 2026 BitSky LLC. The packaged icon is the existing Momentum [site icon](https://momentum.bitsky.ai/icon-512.png).
