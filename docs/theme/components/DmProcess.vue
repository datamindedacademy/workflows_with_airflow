<script setup lang="ts">
/** A horizontal band of chevron phases (roadmap-lite). Wrap DmPhase children. */
</script>

<template>
  <div class="dm-process">
    <slot />
  </div>
</template>

<style scoped>
.dm-process { display: flex; align-items: stretch; }
</style>
