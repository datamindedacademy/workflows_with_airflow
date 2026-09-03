<script setup lang="ts">
/** Equal-width column row. Wrap DmColumn children. */
defineProps<{ gap?: number }>()
</script>

<template>
  <div class="dm-columns" :style="{ gap: `${gap ?? 24}px` }">
    <slot />
  </div>
</template>

<style scoped>
.dm-columns {
  display: flex;
  align-items: stretch;
}
.dm-columns > * { flex: 1 1 0; min-width: 0; }
</style>
