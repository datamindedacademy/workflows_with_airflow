<script setup lang="ts">
defineProps<{ icon: string; label?: string; sub?: string; tone?: 'light' | 'dark' }>()
</script>

<template>
  <div class="dm-badge">
    <div class="dm-badge-circle" :class="`dm-badge-circle--${tone ?? 'light'}`">
      <div :class="icon" class="dm-badge-icon" />
    </div>
    <div v-if="label" class="dm-badge-label">{{ label }}</div>
    <div v-if="sub" class="dm-badge-sub">{{ sub }}</div>
  </div>
</template>

<style scoped>
.dm-badge { display: flex; flex-direction: column; align-items: center; gap: 12px; text-align: center; }
.dm-badge-circle {
  width: 104px;
  height: 104px;
  border-radius: 9999px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.dm-badge-circle--light {
  background: var(--dm-surface);
}
.dm-badge-circle--light .dm-badge-icon { color: var(--dm-connecting); }
.dm-badge-circle--dark {
  background: var(--dm-premium);
}
.dm-badge-circle--dark .dm-badge-icon { color: #ffffff; }
.dm-badge-icon { width: 46px; height: 46px; }
.dm-badge-label { font-size: 16px; font-weight: 700; color: var(--dm-premium); }
.dm-badge-sub { font-size: 13px; color: var(--dm-premium); opacity: 0.7; margin-top: -4px; }
</style>
