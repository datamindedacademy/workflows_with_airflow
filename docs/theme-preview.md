---
theme: dataminded
title: Dataminded Theme Preview
fonts:
  serif: El Messiri
  sans: DM Sans
transition: slide-left
layout: cover
subtitle: Every layout and component, one per slide
---

# Theme <span class="dm-accent">Preview</span>

---
layout: default
label: Layouts
---

# layout: <span class="dm-accent">cover</span>

Full-bleed dark title slide. Props: `subtitle`. Used once, as the deck opener.

```md
---
layout: cover
subtitle: Your subtitle here
---

# Title <span class="dm-accent">here</span>
```

---
layout: agenda
label: Contents
---

# layout: <span class="dm-accent">agenda</span>

1. Numbered contents page
2. Props: `label`
3. Body must be a markdown `<ol>`
4. Rows get `01`, `02`, ... via CSS counters
5. Hairline divider under each row

---
layout: section
---

# layout: <span class="dm-accent">section</span>

---
layout: default
label: Layouts
---

# layout: <span class="dm-accent">default</span>

The workhorse content layout — this very slide uses it. Props: `label` (top-right tag).
First `<h1>` gets the hairline rule automatically.

---
layout: statement
---

# layout: <span class="dm-accent">statement</span>

<p class="text-lg mt-2 opacity-90">Dark, centered, no props — used for exercise/demo pointer slides</p>

---
layout: thanks
---

# layout: <span class="dm-accent">thanks</span>

---
layout: intro
role: Data Engineer, Data Minded
---

# layout: <span class="dm-accent">intro</span>

Two-column bio layout. Props: `role`, `photo` (image URL). Left: eyebrow + heading (this slot) + role.
Right: two violet pills, optional circular photo. **Not used in the Airflow deck** — available for
speaker-intro slides with a headshot.

---
layout: quote
---

# "A good quote goes here, <span class="dm-accent">centered</span> and large."

<!-- layout: quote — big centered serif quote on the cover background. No props, no other slots. -->

---
layout: cards
---

# layout: <span class="dm-accent">cards</span>

<template #cards>
<DmCard header="Card one" tone="navy">

- First point
- Second point

</DmCard>
<DmCard header="Card two" tone="violet">

- Another point
- And another

</DmCard>
<DmCard header="Card three" tone="navy">

- Third card
- Body content

</DmCard>
</template>

---
layout: values
---

# layout: <span class="dm-accent">values</span>

<template #badges>
<DmIconBadge icon="i-mdi-rocket-launch-outline" label="Speed" sub="Ship fast" />
<DmIconBadge icon="i-mdi-shield-check-outline" label="Trust" sub="Built to last" tone="dark" />
<DmIconBadge icon="i-mdi-account-group-outline" label="Team" sub="Work together" />
<DmIconBadge icon="i-mdi-lightbulb-on-outline" label="Craft" sub="Sweat the details" tone="dark" />
<DmIconBadge icon="i-mdi-earth" label="Impact" sub="Beyond the team" />
</template>

---
layout: section
---

# <span class="dm-accent">Components</span>

---
layout: default
label: Components
---

# DmColumns / <span class="dm-accent">DmColumn</span>

<DmColumns class="mt-6">
<DmColumn header="Navy header" tone="navy">

- `tone="navy"` → dark navy pill
- Great for "before" / "option A"

</DmColumn>
<DmColumn header="Violet header" tone="violet" divider>

- `tone="violet"` → violet pill
- `divider` adds a dashed left rule
- Great for "after" / "option B"

</DmColumn>
</DmColumns>

<p class="mt-4 text-sm opacity-70">Also: <code>tone="plain"</code> (no pill, just an underline) — see next slide.</p>

---
layout: default
label: Components
---

# DmColumns with <span class="dm-accent">tone="plain"</span>

<DmColumns class="mt-6" :gap="16">
<DmColumn tone="plain">

No header pill at all — just body content side by side. Used throughout the Airflow deck for plain
two-column bullet lists.

</DmColumn>
<DmColumn tone="plain" divider>

Second column, with `divider` for the dashed separator.

</DmColumn>
</DmColumns>

---
layout: default
label: Components
---

# <span class="dm-accent">DmBanner</span>

<DmBanner tone="violet" icon="i-mdi-lightbulb-outline" title="tone=&quot;violet&quot;" class="mt-6">
Full-width callout, filled violet background.
</DmBanner>

<DmBanner tone="navy" icon="i-mdi-alert-outline" title="tone=&quot;navy&quot;" class="mt-4">
Filled navy background.
</DmBanner>

<DmBanner tone="authentic" icon="i-mdi-thought-bubble-outline" title="tone=&quot;authentic&quot;" class="mt-4">
Light lavender background — the one used most often in the Airflow deck for asides/warnings.
</DmBanner>

---
layout: default
label: Components
---

# DmProcess / <span class="dm-accent">DmPhase</span>

<DmProcess class="mt-8">
<DmPhase label="Step one" />
<DmPhase label="Step two" />
<DmPhase label="Step three" />
<DmPhase label="Step four" />
</DmProcess>

<p class="mt-6 text-sm opacity-70">Chevron pipeline. Keep labels short — long text wraps awkwardly
inside the chevron shape (this is why the "why a scheduler" slide in the real deck was switched to
a mermaid diagram instead).</p>

---
layout: default
label: Components
---

# <span class="dm-accent">DmCard</span>

<DmColumns class="mt-6">
<DmColumn tone="plain">

<DmCard header="Objectives" tone="violet">

- Header bar + light body
- `tone="violet"` or `"navy"`

</DmCard>

</DmColumn>
<DmColumn tone="plain" divider>

<DmCard header="Outcomes" tone="navy">

- Same component, navy header
- Good for objective/solution/outcome triplets

</DmCard>

</DmColumn>
</DmColumns>

---
layout: default
label: Components
---

# <span class="dm-accent">DmInfoCard</span>

<DmColumns class="mt-6" :gap="16">
<DmColumn tone="plain">

<DmInfoCard icon="i-mdi-database-outline" title="Icon + title card" iconTone="violet">

Icon tile, bold title, and slotted body text or a bullet list.

</DmInfoCard>

</DmColumn>
<DmColumn tone="plain">

<DmInfoCard icon="i-mdi-cog-outline" title="Navy variant" iconTone="navy">

- Bullet
- Another bullet

</DmInfoCard>

</DmColumn>
</DmColumns>

---
layout: default
label: Components
---

# <span class="dm-accent">DmIconBadge</span>

<div class="flex justify-center gap-12 mt-10">
<DmIconBadge icon="i-mdi-rocket-launch-outline" label="Light tone" sub="tone=&quot;light&quot; (default)" />
<DmIconBadge icon="i-mdi-rocket-launch-outline" label="Dark tone" sub="tone=&quot;dark&quot;" tone="dark" />
</div>

<p class="mt-8 text-sm opacity-70 text-center">Circular icon + label + sub-label. Good for a row of
capability/value badges (see the <code>values</code> layout).</p>

---
layout: default
label: Components
---

# <span class="dm-accent">DmComparison</span>

<p class="text-sm opacity-70 mt-2">With <code>cols</code>:</p>

<DmComparison :rows="['Pros', 'Cons']" :cols="['Option A', 'Option B']" class="mt-2">
<template #r0c0>Fast to set up</template>
<template #r0c1>More flexible long-term</template>
<template #r1c0>Harder to scale</template>
<template #r1c1>Slower to set up</template>
</DmComparison>

<p class="text-sm opacity-70 mt-10">Without <code>cols</code> (single value column):</p>

<DmComparison :rows="['Risk', 'Mitigation']" class="mt-2">
<template #r0c0>Vendor lock-in</template>
<template #r1c0>Standardize on open formats</template>
</DmComparison>

---
layout: default
label: Components
---

# DmImpact / <span class="dm-accent">DmImpactRow</span>

<DmImpact class="mt-6">
<DmImpactRow icon="i-mdi-clock-fast" label="Speed">

Ships in days, not weeks — because we reuse platform patterns instead of rebuilding from scratch.

</DmImpactRow>
<DmImpactRow icon="i-mdi-shield-lock-outline" label="Trust">

Every deploy goes through the same review and rollback tooling.

</DmImpactRow>
</DmImpact>

---
layout: default
label: Components
---

# <span class="dm-accent">DmMatrix</span>

<div class="mt-4" style="height: 340px">
<DmMatrix
  xLabel="Effort" yLabel="Impact"
  xLow="Low" xHigh="High" yLow="Low" yHigh="High"
  :points="[{label: 'A', x: 20, y: 80}, {label: 'B', x: 70, y: 60}, {label: 'C', x: 50, y: 20}]"
/>
</div>

<p class="mt-4 text-sm opacity-70">2×2 assessment matrix — plots labelled points on an x/y field,
each coordinate 0–100 from the bottom-left origin.</p>

---
layout: default
label: Components
---

# <span class="dm-accent">DmStaircase</span>

<div class="mt-6" style="height: 300px">
<DmStaircase
  xLabel="Maturity" yLabel="Ownership"
  :steps="[
    {label: 'Ad hoc', tone: 'lilac'},
    {label: 'Managed', tone: 'yellow'},
    {label: 'Defined', tone: 'coral'},
    {label: 'Quantified', tone: 'magenta'},
    {label: 'Optimizing', tone: 'navy', note: 'target state'},
  ]"
/>
</div>

---
layout: default
label: Components
---

# DmSteps / <span class="dm-accent">DmStep (vertical)</span>

<DmSteps dir="vertical" class="mt-6">
<DmStep :n="1" label="First">

Set up the DAG folder and confirm the scheduler picks it up.

</DmStep>
<DmStep :n="2" label="Second">

Add your first task and verify it runs.

</DmStep>
</DmSteps>

---
layout: default
label: Components
---

# DmSteps / <span class="dm-accent">DmStep (horizontal)</span>

<DmSteps dir="horizontal" class="mt-8">
<DmStep :n="1" label="Extract">

Pull data from the source system.

</DmStep>
<DmStep :n="2" label="Transform">

Clean and reshape it.

</DmStep>
<DmStep :n="3" label="Load">

Write it to the warehouse.

</DmStep>
</DmSteps>

---
layout: default
label: Components
---

# <span class="dm-accent">DmFooter</span>

Rendered automatically by every layout — not something you add to slide content directly.

<div class="footer-demo-row mt-6">
<div class="footer-demo footer-demo--light">
<code>:page="true"</code>
<DmFooter :page="true" />
</div>
<div class="footer-demo footer-demo--dark">
<code>dark</code>
<DmFooter dark />
</div>
<div class="footer-demo footer-demo--light">
<code>(no props)</code>
<DmFooter />
</div>
</div>

<style>
.footer-demo-row { display: flex; gap: 16px; }
.footer-demo { position: relative; flex: 1; height: 120px; border-radius: 8px; padding: 10px; font-size: 12px; }
.footer-demo--light { background: var(--dm-surface); }
.footer-demo--dark { background: var(--dm-premium); color: #fff; }
</style>

---
layout: section
---

# <span class="dm-accent">Assets</span>

---
layout: default
label: Assets
---

# DmBg <span class="dm-accent">backgrounds</span>

Five bundled photography backgrounds behind <code>&lt;DmBg variant="..."/&gt;</code>, used by the
dark layouts (`cover`, `section`, `statement`, `quote`) — one full-bleed example per variant next.

---
layout: none
---

<div class="bg-preview">
<DmBg variant="cover" />
<span class="bg-preview-label">variant="cover" — used by layout: cover, quote</span>
</div>

---
layout: none
---

<div class="bg-preview">
<DmBg variant="section" />
<span class="bg-preview-label">variant="section" — used by layout: section, thanks</span>
</div>

---
layout: none
---

<div class="bg-preview">
<DmBg variant="stream-violet" />
<span class="bg-preview-label">variant="stream-violet" — used by layout: statement</span>
</div>

---
layout: none
---

<div class="bg-preview">
<DmBg variant="pills-violet" />
<span class="bg-preview-label">variant="pills-violet" — not used by any layout in this theme yet</span>
</div>

---
layout: none
---

<div class="bg-preview">
<DmBg variant="stream-light" />
<span class="bg-preview-label">variant="stream-light" — not used by any layout in this theme yet</span>
</div>

<style>
.bg-preview {
  position: relative;
  width: 100%;
  height: 100%;
}
.bg-preview-label {
  position: absolute;
  z-index: 10;
  top: 24px;
  left: 24px;
  right: 24px;
  background: rgba(8, 6, 53, 0.6);
  color: #fff;
  font-family: ui-monospace, monospace;
  font-size: 15px;
  padding: 8px 14px;
  border-radius: 6px;
  width: fit-content;
}
</style>

---
layout: default
label: Assets
---

# Logos &amp; <span class="dm-accent">brandmark</span>

Each mark shown on the background it's designed to sit on: light marks on dark, dark marks on light.

<div class="logo-grid mt-6">
<div class="logo-tile logo-tile--dark">
<img src="/assets-preview/wordlogo-light.png" alt="wordlogo-light" />
<code>wordlogo-light.png</code>
</div>
<div class="logo-tile logo-tile--light">
<img src="/assets-preview/wordlogo-dark.png" alt="wordlogo-dark" />
<code>wordlogo-dark.png</code>
</div>
<div class="logo-tile logo-tile--dark">
<img src="/assets-preview/wordlogo-light-mono.png" alt="wordlogo-light-mono" />
<code>wordlogo-light-mono.png</code>
</div>
<div class="logo-tile logo-tile--light">
<img src="/assets-preview/wordlogo-dark-mono.png" alt="wordlogo-dark-mono" />
<code>wordlogo-dark-mono.png</code>
</div>
<div class="logo-tile logo-tile--dark">
<img src="/assets-preview/brandmark.png" alt="brandmark" style="height: 26px; filter: brightness(0) invert(1)" />
<code>brandmark.png</code> <span class="opacity-60">(inverted, as DmFooter does on dark)</span>
</div>
</div>

<p class="mt-4 text-sm opacity-70"><code>brandmark.png</code> is the only one <code>DmFooter</code>
actually uses (CSS-inverted to white via <code>dark</code>); the four wordlogo variants back the
<code>cover</code>/<code>thanks</code> layouts or sit ready for decks that need a dark-background
lockup or a monochrome mark.</p>

<style>
.asset-grid, .logo-grid { display: flex; flex-wrap: wrap; gap: 16px; }
.asset-tile { width: 170px; text-align: center; font-size: 12px; }
.asset-swatch { height: 96px; border-radius: 8px; background-size: cover; background-position: center; margin-bottom: 6px; }
.logo-tile { width: 170px; text-align: center; font-size: 12px; border-radius: 8px; padding: 12px 8px; }
.logo-tile img { max-width: 100%; max-height: 44px; object-fit: contain; margin-bottom: 8px; }
.logo-tile--light { background: var(--dm-surface); }
.logo-tile--dark { background: var(--dm-premium); }
</style>

---
layout: thanks
---

# End of <span class="dm-accent">preview</span>
