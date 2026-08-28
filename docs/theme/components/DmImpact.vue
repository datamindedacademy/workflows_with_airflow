<script setup lang="ts">
/** Left icon-label rail + right content rows (the "value we deliver / impact" page). Wrap DmImpactRow children. */
</script>

<template>
  <div class="dm-impact">
    <slot />
  </div>
</template>

<style scoped>
.dm-impact { display: flex; flex-direction: column; gap: 16px; }
</style>
