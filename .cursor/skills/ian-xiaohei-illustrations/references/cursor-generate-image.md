# Cursor GenerateImage adapter

Cursor's `GenerateImage` tool often ignores subtle style cues and defaults to dark corporate infographics, SaaS dashboards, or numbered playbook posters. **Lead with hard negatives and white-background constraints** before describing the scene.

## Mandatory prompt block (prepend to every call)

Always start the `description` with this block verbatim (adjust labels only):

```text
STYLE LOCK — follow exactly:
- Pure flat WHITE background only (#FFFFFF). At least 35% empty white margin.
- Black HAND-DRAWN wobbly pen sketch on blank paper. Like doodles in a notebook.
- NOT an infographic. NOT a UI mockup. NOT a dashboard. NOT dark theme.
- NOT 3D isometric. NOT corporate poster. NOT numbered steps layout. NOT neon.
- NOT cute mascot marketing art. NOT children's cartoon. NOT PPT slide.

Character — Xiaohei (小黑) — visual only, never labeled on the image:
- Small solid-black blob, two white dot eyes, thin stick legs, blank deadpan face.
- Hand-drawn uneven body. Xiaohei MUST perform the core action (not standing beside a diagram).
- **Do NOT write "Xiaohei", "小黑", or character names anywhere on the image.** No speech bubbles naming the character. No meta captions like "Xiaohei doing X". The character is unnamed in the artwork.

Labels:
- {ENGLISH or CHINESE per user request}
- Max 5–8 short handwritten labels in red / orange / blue only.
- No title in the top-left corner. No structure-type heading on the image.

Aspect: 16:9 horizontal article illustration. One metaphor only.
```

## Label language

| User language | Label language |
|---|---|
| English article or explicit "English labels" | English handwritten labels |
| Chinese article, no preference | Chinese handwritten labels (default) |
| Mixed | Match the article's primary language |

## If batch 1 fails QA

Regenerate immediately — do not deliver dark infographics. Common failures:

| Failure | Fix |
|---|---|
| Dark blue/black background | Repeat `Pure flat WHITE background only` three times at top |
| SaaS dashboard / gate UI | Add `NOT a software UI. NOT a web app screenshot.` |
| Numbered playbook poster | Add `NOT numbered steps. NOT corporate playbook layout.` |
| Cute branded mascot | Add `deadpan, not cute. solid black blob, not a cat with hoodie` |
| Xiaohei is decoration | Regenerate with `Xiaohei actively doing: {verb}` as first composition line |

## File delivery

`GenerateImage` may write to `.cursor/projects/.../assets/` instead of the repo. After each image, copy to:

```text
assets/<article-slug>-illustrations/NN-topic.png
```

## English label template

```text
{paste STYLE LOCK block}

Theme: {theme}
Core idea: {one sentence}
Composition: {Xiaohei action + objects + flow}
Elements: {item1} / {item2} / {item3}

English handwritten labels (sparse):
{label1} / {label2} / {label3} / {label4}

Orange = flow arrows. Red = key emphasis. Blue = secondary notes.
```
