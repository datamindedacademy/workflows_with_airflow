<script setup lang="ts">
/** A single chevron phase block used inside DmProcess. */
defineProps<{ label: string }>()
</script>

<template>
  <div class="dm-phase">
    <span class="dm-phase-label">{{ label }}</span>
  </div>
</template>

<style scoped>
.dm-phase {
  position: relative;
  flex: 1 1 0;
  background: var(--dm-premium);
  color: #fff;
  font-weight: 700;
  font-size: 17px;
  height: 56px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 14px;
  padding: 0 12px;
  clip-path: polygon(0 0, calc(100% - 16px) 0, 100% 50%, calc(100% - 16px) 100%, 0 100%, 16px 50%);
}
.dm-phase:first-child { clip-path: polygon(0 0, calc(100% - 16px) 0, 100% 50%, calc(100% - 16px) 100%, 0 100%); }
.dm-phase:last-child { margin-right: 0; }
</style>
