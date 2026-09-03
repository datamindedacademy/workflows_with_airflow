<script setup lang="ts">
/** Icon card: a coloured icon tile, a title, and slotted body (text + optional bullets). */
defineProps<{ icon?: string; title: string; iconTone?: 'violet' | 'navy' }>()
</script>

<template>
  <div class="dm-info">
    <div v-if="icon" class="dm-info-icon" :class="`dm-info-icon--${iconTone ?? 'violet'}`">
      <div :class="icon" class="dm-info-glyph" />
    </div>
    <div class="dm-info-title">{{ title }}</div>
    <div class="dm-info-body"><slot /></div>
  </div>
</template>

<style scoped>
.dm-info {
  background: var(--dm-surface);
  border-radius: 12px;
  padding: 16px 16px 14px;
  display: flex;
  flex-direction: column;
  gap: 8px;
  height: 100%;
  box-sizing: border-box;
}
.dm-info-icon {
  width: 38px;
  height: 38px;
  border-radius: 9px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.dm-info-icon--violet { background: var(--dm-connecting); }
.dm-info-icon--navy { background: var(--dm-premium); }
.dm-info-glyph { width: 22px; height: 22px; color: #ffffff; }
.dm-info-title { font-weight: 700; font-size: 16px; color: var(--dm-premium); }
.dm-info-body { font-size: 13px; color: #3a3a44; line-height: 1.4; }
.dm-info-body :deep(ul) { padding-left: 18px; margin: 6px 0 0; }
.dm-info-body :deep(li) { margin-bottom: 6px; }
.dm-info-body :deep(p) { margin: 0 0 8px; }
</style>
