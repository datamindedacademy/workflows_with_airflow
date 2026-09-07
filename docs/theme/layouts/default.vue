<script setup lang="ts">
defineProps<{
  label?: string
  background?: 'cover' | 'section' | 'stream-violet' | 'pills-violet' | 'stream-light'
}>()
</script>

<template>
  <div class="slidev-layout dm-default" :class="{ 'dm-dark': background }">
    <DmBg v-if="background" :variant="background" />
    <div v-if="label" class="dm-section-label">{{ label }}</div>
    <div class="dm-default-body">
      <slot />
    </div>
    <DmFooter :page="true" />
  </div>
</template>

<style scoped>
.dm-default {
  background: #ffffff;
  padding: 44px 56px 48px;
  height: 100%;
  box-sizing: border-box;
}
.dm-default-body {
  position: relative;
  z-index: 1;
}
/* The first heading becomes the title with the signature hairline rule.
   padding-right keeps long two-line titles clear of the top-right section label. */
.dm-default-body :deep(h1:first-child) {
  border-bottom: 1px solid rgba(8, 6, 53, 0.85);
  padding-bottom: 12px;
  margin-bottom: 24px;
  width: 100%;
  padding-right: 120px;
  box-sizing: border-box;
}
.dm-default.dm-dark .dm-default-body :deep(h1:first-child) {
  border-bottom-color: rgba(255, 255, 255, 0.85);
}
.dm-default.dm-dark .dm-section-label {
  color: #ffffff;
}
</style>
