<script setup lang="ts">
/** Full-width callout banner (violet or light), with an optional icon and bold title. */
defineProps<{ tone?: 'violet' | 'authentic' | 'navy'; icon?: string; title?: string }>()
</script>

<template>
  <div class="dm-banner" :class="`dm-banner--${tone ?? 'violet'}`">
    <div v-if="icon" class="dm-banner-icon"><div :class="icon" /></div>
    <div class="dm-banner-text">
      <span v-if="title" class="dm-banner-title">{{ title }}</span>
      <slot />
    </div>
  </div>
</template>

<style scoped>
.dm-banner {
  display: flex;
  gap: 14px;
  align-items: center;
  border-radius: 12px;
  padding: 13px 18px;
}
.dm-banner--violet { background: var(--dm-connecting); color: #fff; }
.dm-banner--navy { background: var(--dm-premium); color: #fff; }
.dm-banner--authentic { background: var(--dm-authentic); color: var(--dm-premium); }
.dm-banner-icon {
  flex: none;
  width: 40px;
  height: 40px;
  border-radius: 10px;
  background: rgba(255, 255, 255, 0.18);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
}
.dm-banner--authentic .dm-banner-icon { background: rgba(84, 62, 220, 0.12); color: var(--dm-connecting); }
.dm-banner-title { font-weight: 700; display: block; margin-bottom: 2px; }
.dm-banner-text { font-size: 15px; line-height: 1.45; }
</style>
