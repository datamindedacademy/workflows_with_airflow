<script setup lang="ts">
/**
 * Header card matching the real template (e.g. Objectives / Solution / Outcomes).
 * A coloured header bar over a light body that holds slotted content.
 */
defineProps<{ header: string; tone?: 'violet' | 'navy' }>()
</script>

<template>
  <div class="dm-card">
    <div class="dm-card-head" :class="`dm-card-head--${tone ?? 'violet'}`">{{ header }}</div>
    <div class="dm-card-body">
      <slot />
    </div>
  </div>
</template>

<style scoped>
.dm-card {
  display: flex;
  flex-direction: column;
  border-radius: 8px;
  overflow: hidden;
}
.dm-card-head {
  font-weight: 700;
  font-size: 18px;
  text-align: center;
  color: #ffffff;
  padding: 10px 16px;
}
.dm-card-head--violet { background: var(--dm-connecting); }
.dm-card-head--navy { background: var(--dm-premium); }
.dm-card-body {
  background: var(--dm-surface);
  padding: 16px 18px;
  flex: 1;
  font-size: 15px;
}
.dm-card-body :deep(ul) { padding-left: 18px; margin: 0; }
.dm-card-body :deep(li) { margin-bottom: 8px; }
</style>
