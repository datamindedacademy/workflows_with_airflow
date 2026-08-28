<script setup lang="ts">
/**
 * Row-labelled comparison grid (Pros/Cons/Advice, Risk/Mitigation, ...).
 * `rows` = the dark left-hand row labels; `cols` = optional column headers.
 * Cells are provided in the default slot, left-to-right, top-to-bottom.
 */
defineProps<{ rows: string[]; cols?: string[] }>()
</script>

<template>
  <div
    class="dm-cmp"
    :style="{ gridTemplateColumns: `140px repeat(${(cols?.length) || 1}, 1fr)` }"
  >
    <!-- header row (optional) -->
    <template v-if="cols && cols.length">
      <div class="dm-cmp-corner" />
      <div v-for="c in cols" :key="c" class="dm-cmp-colhead">{{ c }}</div>
    </template>
    <!-- body rows -->
    <template v-for="(r, i) in rows" :key="r">
      <div class="dm-cmp-rowlabel">{{ r }}</div>
      <div v-for="c in ((cols && cols.length) || 1)" :key="c" class="dm-cmp-cell">
        <slot :name="`r${i}c${c - 1}`" />
      </div>
    </template>
  </div>
</template>

<style scoped>
.dm-cmp { display: grid; gap: 14px; align-items: stretch; }
.dm-cmp-corner { }
.dm-cmp-colhead {
  text-align: center;
  font-weight: 700;
  color: var(--dm-premium);
  border-bottom: 1px solid var(--dm-connecting);
  padding-bottom: 6px;
}
.dm-cmp-rowlabel {
  background: var(--dm-premium);
  color: #fff;
  font-weight: 700;
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 10px;
}
.dm-cmp-cell {
  background: var(--dm-surface);
  border-radius: 8px;
  padding: 14px 16px;
  font-size: 14px;
}
</style>
