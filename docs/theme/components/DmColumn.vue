<script setup lang="ts">
/** A single column with an optional coloured header pill, and a dashed divider on the left. */
defineProps<{ header?: string; tone?: 'navy' | 'violet' | 'plain'; divider?: boolean }>()
</script>

<template>
  <div class="dm-col" :class="{ 'dm-col--divider': divider }">
    <div
      v-if="header"
      class="dm-col-head"
      :class="`dm-col-head--${tone ?? 'navy'}`"
    >
      {{ header }}
    </div>
    <div class="dm-col-body">
      <slot />
    </div>
  </div>
</template>

<style scoped>
.dm-col { padding: 0 4px; }
.dm-col--divider { border-left: 1px dashed rgba(84, 62, 220, 0.5); padding-left: 20px; }
.dm-col-head {
  font-weight: 700;
  font-size: 16px;
  text-align: center;
  border-radius: 6px;
  padding: 8px 12px;
  margin-bottom: 16px;
}
.dm-col-head--navy { background: var(--dm-premium); color: #fff; }
.dm-col-head--violet { background: var(--dm-connecting); color: #fff; }
.dm-col-head--plain { color: var(--dm-connecting); border-bottom: 1px solid var(--dm-connecting); border-radius: 0; }
.dm-col-body { font-size: 15px; }
.dm-col-body :deep(p) { margin: 0 0 12px; }
</style>
