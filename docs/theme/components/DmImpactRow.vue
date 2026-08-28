<script setup lang="ts">
/** One row: a left label block (icon + title on a surface) and a right content panel. */
defineProps<{ icon?: string; label: string }>()
</script>

<template>
  <div class="dm-irow">
    <div class="dm-irow-label">
      <div v-if="icon" :class="icon" class="dm-irow-icon" />
      <div class="dm-irow-title">{{ label }}</div>
    </div>
    <div class="dm-irow-arrow" />
    <div class="dm-irow-body"><slot /></div>
  </div>
</template>

<style scoped>
.dm-irow { display: flex; align-items: stretch; gap: 0; }
.dm-irow-label {
  flex: none;
  width: 180px;
  background: var(--dm-surface);
  border-radius: 8px;
  padding: 14px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  gap: 8px;
}
.dm-irow-icon { width: 32px; height: 32px; color: var(--dm-connecting); }
.dm-irow-title { font-weight: 700; font-size: 15px; }
.dm-irow-arrow {
  flex: none;
  width: 0; height: 0;
  align-self: center;
  border-top: 10px solid transparent;
  border-bottom: 10px solid transparent;
  border-left: 12px solid var(--dm-surface);
}
.dm-irow-body {
  flex: 1;
  background: var(--dm-surface);
  border-radius: 8px;
  padding: 14px 18px;
  font-size: 14px;
}
.dm-irow-body :deep(p) { margin: 0 0 8px; }
</style>
