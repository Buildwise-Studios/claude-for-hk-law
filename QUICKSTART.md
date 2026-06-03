# Quick Start

**60 seconds.** This gets you to using your plugins.

## Install in Claude Cowork
1. [Install Claude Desktop](https://claude.com/download)
2. Get access to Claude Cowork
3. Follow the instructions in the video below:

https://github.com/user-attachments/assets/51394f0a-5277-4fe2-b81c-5c5e9ac876b5

## Install in Claude Code

1. **Open Claude Code** (in your terminal) or **Claude Cowork** (the desktop app). Not sure which you have? If you have a terminal window open with Claude in it, that's Claude Code.

2. **Add the marketplace.** In Claude Code, type `/plugin marketplace add ` (with a space at the end), then **drag the unzipped `claude-for-hk-law` folder onto the terminal window** — it'll fill in the path. Then press Enter.

   (Or type the full path: `/plugin marketplace add /Users/you/Desktop/claude-for-hk-law`)

3. **Install your plugin.** Pick the one that matches your work from the table below, then:
   ```
   /plugin install commercial-legal@claude-for-hk-law
   ```

4. **⚠️ Restart Claude Code.** Close and reopen. This step is not optional — the plugin isn't live until you restart.

5. **Run setup.** Takes 2 minutes (quick start) or 10-15 minutes (full).
   ```
   /commercial-legal:cold-start-interview
   ```

6. **Connect a research tool.** Citations are flagged unverified without one. The Hong Kong plugin ecosystem supports the following research connectors:
   - **Hong Kong e-Legislation** — official ordinances database (elegislation.gov.hk)
   - **HKLII** — Hong Kong Legal Information Institute (hklii.org)
   - **Judiciary of Hong Kong** — official judgments database (judiciary.hk)
   - In Cowork: Settings → Connectors. In Claude Code: the plugin lists research MCPs in its config; you'll be prompted to authorize them the first time a skill needs one.

## Install user-scoped, not project-scoped

When you run `/plugin install`, you may be asked whether to install for this project only or for all projects (user scope). **Pick user scope.**

It's counterintuitive: project scope feels safer. But project scope blocks the plugin from reading files outside the project folder — your briefs in Downloads, your contracts in Documents, your client files in Dropbox. Most skills need to read your files. User scope doesn't give the plugin any extra access to your files — the plugin can only read files you explicitly point it at or that are in the current directory. It just means the plugin works from any folder instead of one.

If you already installed project-scoped and want to switch: `/plugin uninstall <plugin>`, then `/plugin install <plugin>@claude-for-hk-law` from your home directory.

## Which plugin is for me?

| You are a… | Install… | First command |
|---|---|---|
| Commercial / corporate solicitor (HK) | `commercial-legal` | `/commercial-legal:review` |
| Privacy lawyer / DPO (HK) | `privacy-legal` | `/privacy-legal:use-case-triage` |
| Corporate / M&A solicitor (HK) | `corporate-legal` | `/corporate-legal:diligence-issue-extraction` |
| Employment lawyer / HR counsel (HK) | `employment-legal` | `/employment-legal:wage-hour-qa` |
| Product counsel / tech lawyer (HK) | `product-legal` | `/product-legal:is-this-a-problem` |
| IP solicitor / patent agent (HK) | `ip-legal` | `/ip-legal:clearance` |
| Litigator (in-house or firm, HK) | `litigation-legal` | `/litigation-legal:matter-intake` |
| Regulatory / compliance counsel (HK) | `regulatory-legal` | `/regulatory-legal:reg-feed-watcher` |
| AI governance lead (HK) | `ai-governance-legal` | `/ai-governance-legal:use-case-triage` |
| Clinic supervisor (HK law school) | `legal-clinic` | `/legal-clinic:cold-start-interview` |
| Law student (HK) | `law-student` | `/law-student:cold-start-interview` |
| Legal ops / looking for skills | `legal-builder-hub` | `/legal-builder-hub:registry-browser` |
| Basic Law specialist | `hk-basic-law` | `/hk-basic-law:cold-start-interview` |
| Companies / corporate (HK) | `hk-companies` | `/hk-companies:cold-start-interview` |
| Employment (HK) | `hk-employment` | `/hk-employment:cold-start-interview` |
| Litigation procedure (HK) | `hk-litigation-procedure` | `/hk-litigation-procedure:cold-start-interview` |
| Property / conveyancing (HK) | `hk-property` | `/hk-property:cold-start-interview` |
| Data privacy (HK PDPO) | `hk-data-privacy` | `/hk-data-privacy:cold-start-interview` |
| Intellectual property (HK) | `hk-intellectual-property` | `/hk-intellectual-property:cold-start-interview` |
| Arbitration (HK) | `hk-arbitration` | `/hk-arbitration:cold-start-interview` |
| Commercial law (HK) | `hk-commercial-law` | `/hk-commercial-law:cold-start-interview` |
| Competition (HK) | `hk-competition` | `/hk-competition:cold-start-interview` |
| Immigration (HK) | `hk-immigration` | `/hk-immigration:cold-start-interview` |
| Shipping / maritime (HK) | `hk-shipping-maritime` | `/hk-shipping-maritime:cold-start-interview` |
| Family law (HK) | `hk-family-law` | `/hk-family-law:cold-start-interview` |
| Trusts / estate (HK) | `hk-trusts-estate` | `/hk-trusts-estate:cold-start-interview` |
| National security law (HK) | `hk-nsl-rules` | `/hk-nsl-rules:cold-start-interview` |

## What you're installing

Each plugin learns your playbook through a setup interview, writes it to a practice profile file (`~/.claude/plugins/config/claude-for-hk-law/<plugin>/CLAUDE.md`), and every skill reads from it. The profile is yours — edit it, re-run setup, or tell a skill to update it.

**Every output is a draft for solicitor review.** The plugins flag what they're unsure about, mark citations by source, and gate anything irreversible. A solicitor reviews, verifies, and takes responsibility in accordance with the Hong Kong Solicitors' Guide to Professional Conduct. They make that review faster; they don't replace it.

## What's in the box

12 core practice-area plugins, 8 HK-native plugins, 5 managed-agent cookbooks, and connectors for Hong Kong e-Legislation, HKLII, and the Judiciary of Hong Kong. The full reference is in [README.md](README.md).

## Stuck?

- **"Command not found"** after install → you forgot step 4. Restart Claude Code.
- **"Run setup first"** → run `/<plugin>:cold-start-interview` before any other command.
- **Citations flagged `[verify]`** → connect a research tool (step 6). Without one, every cite is from training data, not a current database. Connect HKLII, Hong Kong e-Legislation, or the Judiciary portal.
- **"I can't read [file]"** → most often this means the plugin is project-scoped and the file is outside the project folder. See "Install user-scoped, not project-scoped" above — reinstall user-scoped or move the file into the project folder.
- **The plugin doesn't do X** → run `/legal-builder-hub:related-skills-surfacer` to find a better match, or check the plugin's README for "What this plugin does not do."
