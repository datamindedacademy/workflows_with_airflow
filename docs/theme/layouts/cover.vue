<script setup lang="ts">
import wordlogo from '../assets/wordlogo-light.png'
defineProps<{ subtitle?: string }>()
</script>

<template>
  <div class="slidev-layout dm-dark dm-cover">
    <DmBg variant="cover" />
    <div class="dm-cover-main">
      <slot />
      <p v-if="subtitle" class="dm-cover-subtitle">{{ subtitle }}</p>
    </div>
    <img :src="wordlogo" class="dm-cover-logo" alt="Dataminded" />
  </div>
</template>

<style scoped>
.dm-cover { padding: 56px; height: 100%; box-sizing: border-box; position: relative; }
.dm-cover-main { position: absolute; top: 46%; left: 60px; transform: translateY(-50%); max-width: 62%; }
.dm-cover-main :deep(h1) { font-size: 52px; line-height: 1.1; }
.dm-cover-subtitle { margin-top: 20px; font-size: 20px; opacity: 0.9; }
.dm-cover-logo { position: absolute; bottom: 48px; left: 60px; height: 30px; }
</style>
