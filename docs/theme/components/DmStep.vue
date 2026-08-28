<script setup lang="ts">
/** One numbered step: a navy circle with the number, a bold label, and slotted body. */
defineProps<{ n: string | number; label?: string }>()
</script>

<template>
  <div class="dm-step">
    <div class="dm-step-circle">{{ n }}</div>
    <div class="dm-step-content">
      <div v-if="label" class="dm-step-label">{{ label }}</div>
      <div class="dm-step-body"><slot /></div>
    </div>
  </div>
</template>

<style scoped>
.dm-step { display: flex; align-items: flex-start; gap: 16px; }
.dm-step-circle {
  flex: none;
  width: 64px;
  height: 64px;
  border-radius: 9999px;
  background: var(--dm-premium);
  color: #fff;
  font-weight: 700;
  font-size: 22px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.dm-step-label { font-weight: 700; color: var(--dm-connecting); text-transform: uppercase; letter-spacing: 0.04em; margin-bottom: 6px; }
.dm-step-body { font-size: 15px; }
</style>
