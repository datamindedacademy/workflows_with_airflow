<script setup lang="ts">
/** Numbered steps. `dir` = vertical (stacked, connected) or horizontal (big numbers + arrows). */
defineProps<{ dir?: 'vertical' | 'horizontal' }>()
</script>

<template>
  <div class="dm-steps" :class="`dm-steps--${dir ?? 'vertical'}`">
    <slot />
  </div>
</template>

<style scoped>
.dm-steps--vertical { display: flex; flex-direction: column; gap: 20px; }
.dm-steps--horizontal { display: flex; align-items: flex-start; gap: 12px; }
.dm-steps--horizontal > * { flex: 1 1 0; }
</style>
