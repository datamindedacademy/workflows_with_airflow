<script setup lang="ts">
import brandmark from '../assets/brandmark.png'
defineProps<{ page?: boolean; dark?: boolean }>()
</script>

<template>
  <div class="dm-footer">
    <span v-if="page" class="dm-footer-page">
      {{ $slidev.nav.currentPage }}
    </span>
    <img
      :src="brandmark"
      class="dm-footer-mark"
      :class="{ 'dm-footer-mark--white': dark }"
      alt="Dataminded"
    />
  </div>
</template>

<style scoped>
.dm-footer {
  position: absolute;
  right: 32px;
  bottom: 22px;
  display: flex;
  align-items: center;
  gap: 12px;
  z-index: 10;
}
.dm-footer-page {
  font-family: 'DM Sans', sans-serif;
  font-size: 12px;
  opacity: 0.6;
}
.dm-footer-mark {
  height: 26px;
  width: auto;
}
/* Turn the violet mark solid white on dark backgrounds */
.dm-footer-mark--white {
  filter: brightness(0) invert(1);
}
</style>
