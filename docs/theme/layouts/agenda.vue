<script setup lang="ts">
defineProps<{ label?: string }>()
</script>

<template>
  <div class="slidev-layout dm-agenda">
    <div v-if="label" class="dm-section-label">{{ label }}</div>
    <div class="dm-agenda-body">
      <slot />
    </div>
    <DmFooter :page="true" />
  </div>
</template>

<style scoped>
.dm-agenda {
  background: #ffffff;
  padding: 44px 56px 48px;
  height: 100%;
  box-sizing: border-box;
}
.dm-agenda-body :deep(h1:first-child) {
  border-bottom: 1px solid rgba(8, 6, 53, 0.85);
  padding-bottom: 12px;
  margin-bottom: 36px;
}
/* Ordered list becomes the numbered agenda: 01, 02, ... with hairline rows */
.dm-agenda-body :deep(ol) {
  counter-reset: dm-agenda;
  list-style: none;
  padding: 0;
  max-width: 760px;
  margin-left: auto;
}
.dm-agenda-body :deep(ol > li) {
  counter-increment: dm-agenda;
  border-bottom: 1px solid rgba(8, 6, 53, 0.18);
  padding: 16px 4px;
  font-size: 22px;
  display: flex;
  gap: 20px;
  align-items: baseline;
}
.dm-agenda-body :deep(ol > li)::before {
  content: counter(dm-agenda, decimal-leading-zero);
  color: var(--dm-connecting);
  font-weight: 700;
  min-width: 42px;
}
</style>
