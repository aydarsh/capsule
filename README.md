# Capsule

**Wardrobe-first travel planning, entirely in your agent's chat.**

[Русская инструкция](README.ru.md) · [Download the skill](https://github.com/aydarsh/capsule/releases/latest)

Show your clothes, choose a destination, and build a connected plan: outfits, accommodation requirements, hotel options and a daily itinerary. Capsule uses your agent's available web search and image tools. There is no server, fixed destination, bundled hotel database, model API key, or background process to install.

## What you get

- Short, step-by-step conversation in your language.
- Outfits from your own photos, with consistent flat-lay images when your client supports reference-image editing.
- Accommodation requirements you confirm before comparison.
- Current-source research with links and clear unknowns; no invented rates or hotel replies.
- Daily places linked to outfits, travel legs and time to change clothes.
- Portable trip notes on request.

## Requirements

An agent that can load `SKILL.md`, understand your attachments and access the tools you need. Web search is needed for current travel facts. Photo-based image generation requires a compatible reference-image tool; a text outfit list is available without it. A subscription or tool charges are governed by your client. Installing the skill does not grant capabilities that the client lacks.

## Install in Codex

Clone once, then copy the complete skill directory. These commands are for macOS/Linux and refuse to replace an existing installation:

```sh
git clone https://github.com/aydarsh/capsule.git
cd capsule
mkdir -p "$HOME/.agents/skills"
if [ -e "$HOME/.agents/skills/capsule-travel" ] || [ -L "$HOME/.agents/skills/capsule-travel" ]; then
  echo "capsule-travel already exists; back it up before replacing it."
else
  cp -R skills/capsule-travel "$HOME/.agents/skills/capsule-travel"
fi
```

Open a new Codex chat and invoke `$capsule-travel`. On Windows, copy the `capsule-travel` folder into `.agents/skills` inside your user home, preserving its `references` and `agents` folders.

## Install in Claude Code

After cloning, run from the repository directory:

```sh
claude --plugin-dir "$PWD"
```

Invoke `/capsule:capsule-travel` in that session. For a standalone personal skill, copy `skills/capsule-travel` into `~/.claude/skills/` without replacing an existing folder, start a new session, and invoke `/capsule-travel`. Choose one method to avoid duplicate skills. No MCP configuration is required.

## Other clients

The release ZIP contains the complete `capsule-travel` directory with `SKILL.md` at its root. Import it only if the client supports custom Agent Skills, or extract it into the client's documented skill directory. An ordinary chat interface does not necessarily support installing a skill ZIP. Photo editing, browsing, voice input and cross-chat memory vary by client; universal compatibility is not promised.

Installation references: [Codex skills](https://developers.openai.com/codex/skills), [Claude Code skills](https://code.claude.com/docs/en/skills), [Claude Code plugins](https://code.claude.com/docs/en/plugins).

## Start a trip

Attach photos and send:

> Use $capsule-travel to help plan my trip. Start by asking where and when I'm going and reviewing the clothes I've attached. Let's choose outfits before looking for accommodation.

You can also start with descriptions instead of photos, skip wardrobe planning, or use accommodation you've already booked. The skill works with the destination you choose; research coverage depends on accessible sources.

## Facts, privacy and limitations

Prices are reported as live only when an offer can be checked for the exact dates, guests and rate. If sources are unavailable, the relevant fields remain unverified. Route estimates require a routing source; opening hours and dress codes need their own evidence. Choosing a hotel is not booking it. The skill does not autonomously contact hotels or make purchases.

Images are visualizations of your clothes, not exact product reproductions or guarantees of fit. Capsule adds no telemetry or service of its own. Your client and connected tools process the data you provide under their own terms. Trip information stays in the conversation unless you request an export; the skill does not provide a persistent database or cross-chat memory.

## Update or remove

For a copied skill, back up the installed folder, update the checkout with `git pull --ff-only`, then replace the copy with the complete `skills/capsule-travel` folder. To remove it, delete only that installed skill folder. For `--plugin-dir`, launch Claude Code without that option. The repository does not change your agent settings automatically.

## Maintain the package

Python 3.10+ is needed only for these maintainer commands, not for using the skill:

```sh
python3 scripts/package.py --check
python3 scripts/package.py
```

The second command writes `dist/capsule-travel.zip`. Checks cover packaging, relative references and metadata, not the accuracy of a model's travel advice. Verify real research and image output in the intended client before relying on them.

MIT license. Suggestions and reproducible issues are welcome; do not attach private travel documents, credentials or photos without permission.
