<script setup lang="ts">
/**
 * Ascending "responsibility" staircase of labelled boxes.
 * steps: [{ label, tone?, note? }] rendered bottom-left to top-right.
 * tone maps to the secondary palette (lilac, yellow, coral, magenta, navy).
 */
defineProps<{
  steps: { label: string; tone?: 'lilac' | 'yellow' | 'coral' | 'magenta' | 'navy'; note?: string }[]
  xLabel?: string
  yLabel?: string
}>()

const toneColor: Record<string, string> = {
  lilac: 'var(--dm-authentic)',
  yellow: 'var(--dm-yellow)',
  coral: 'var(--dm-coral)',
  magenta: 'var(--dm-magenta)',
  navy: 'var(--dm-premium)',
}
</script>

<template>
  <div class="dm-stair">
    <div v-if="yLabel" class="dm-stair-ylabel">{{ yLabel }}</div>
    <div class="dm-stair-field">
      <div
        v-for="(s, i) in steps"
        :key="s.label"
        class="dm-stair-step"
        :style="{
          left: `${(i / steps.length) * 100}%`,
          bottom: `${(i / steps.length) * 100}%`,
        }"
      >
        <span
          class="dm-stair-box"
          :style="{
            background: toneColor[s.tone ?? 'navy'],
            color: (s.tone === 'navy' || s.tone === 'magenta' || s.tone === 'coral') ? '#fff' : 'var(--dm-premium)',
          }"
        >{{ s.label }}</span>
        <span v-if="s.note" class="dm-stair-note">{{ s.note }}</span>
      </div>
      <div class="dm-stair-baseline" />
    </div>
    <div v-if="xLabel" class="dm-stair-xlabel">{{ xLabel }}</div>
  </div>
</template>

<style scoped>
.dm-stair { position: relative; height: 100%; padding-left: 24px; }
.dm-stair-ylabel {
  position: absolute; left: 0; top: 0; bottom: 30px;
  writing-mode: vertical-rl; transform: rotate(180deg);
  font-weight: 700; font-size: 14px; display: flex; align-items: center;
}
.dm-stair-field { position: relative; height: calc(100% - 24px); margin-left: 12px; }
.dm-stair-step { position: absolute; display: flex; align-items: center; gap: 12px; white-space: nowrap; }
.dm-stair-box {
  font-weight: 700;
  font-size: 14px;
  border-radius: 8px;
  padding: 10px 16px;
  display: inline-block;
}
.dm-stair-note { font-size: 13px; opacity: 0.75; }
.dm-stair-baseline { position: absolute; left: 0; right: 0; bottom: 0; border-bottom: 1px solid rgba(8,6,53,0.4); }
.dm-stair-xlabel { position: absolute; right: 0; bottom: 0; font-weight: 700; font-size: 14px; text-align: right; }
</style>
