<script setup lang="ts">
/**
 * 2x2 assessment matrix. Plots labelled points on an x/y field (each 0-100, origin bottom-left).
 * points: [{ label, x, y }]
 */
defineProps<{
  xLabel?: string
  yLabel?: string
  xLow?: string
  xHigh?: string
  yLow?: string
  yHigh?: string
  points: { label: string; x: number; y: number }[]
}>()
</script>

<template>
  <div class="dm-matrix">
    <div class="dm-matrix-yaxis">
      <span class="dm-matrix-ylabel">{{ yLabel }}</span>
      <span class="dm-matrix-yhi">{{ yHigh }}</span>
      <span class="dm-matrix-ylo">{{ yLow }}</span>
    </div>
    <div class="dm-matrix-field">
      <div class="dm-matrix-vline" />
      <div class="dm-matrix-hline" />
      <div
        v-for="p in points"
        :key="p.label"
        class="dm-matrix-point"
        :style="{ left: `${p.x}%`, bottom: `${p.y}%` }"
      >
        {{ p.label }}
      </div>
      <div class="dm-matrix-xaxis">
        <span>{{ xLow }}</span>
        <span class="dm-matrix-xlabel">{{ xLabel }}</span>
        <span>{{ xHigh }}</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.dm-matrix { display: flex; gap: 8px; height: 100%; }
.dm-matrix-yaxis {
  position: relative;
  width: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.dm-matrix-ylabel { writing-mode: vertical-rl; transform: rotate(180deg); font-size: 13px; font-weight: 600; }
.dm-matrix-yhi { position: absolute; top: 0; right: 26px; font-size: 12px; opacity: 0.6; white-space: nowrap; }
.dm-matrix-ylo { position: absolute; bottom: 24px; right: 26px; font-size: 12px; opacity: 0.6; white-space: nowrap; }
.dm-matrix-field {
  position: relative;
  flex: 1;
  background: var(--dm-surface);
  border-radius: 8px;
}
.dm-matrix-vline { position: absolute; left: 50%; top: 0; bottom: 24px; border-left: 1px dashed rgba(8,6,53,0.2); }
.dm-matrix-hline { position: absolute; left: 0; right: 0; top: calc(50% - 12px); border-top: 1px dashed rgba(8,6,53,0.2); }
.dm-matrix-point {
  position: absolute;
  transform: translate(-50%, 50%);
  width: 40px;
  height: 40px;
  border-radius: 9999px;
  background: var(--dm-premium);
  color: #fff;
  font-weight: 700;
  font-size: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.dm-matrix-xaxis {
  position: absolute;
  left: 0; right: 0; bottom: 2px;
  display: flex;
  justify-content: space-between;
  padding: 0 10px;
  font-size: 12px;
  opacity: 0.6;
}
.dm-matrix-xlabel { font-weight: 600; opacity: 1; }
</style>
