<script setup lang="ts">
import { computed } from 'vue'
import cover from '../assets/cover-dark.jpg'
import section from '../assets/section-dark.jpg'
import streamViolet from '../assets/stream-violet.jpg'
import pillsViolet from '../assets/pills-violet.jpg'
import streamLight from '../assets/stream-light.jpg'

/**
 * Full-bleed real brand background image, bundled with the theme.
 * `variant` selects one of the official template backgrounds.
 */
const props = defineProps<{
  variant?: 'cover' | 'section' | 'stream-violet' | 'pills-violet' | 'stream-light'
}>()

const images: Record<string, string> = {
  cover,
  section,
  'stream-violet': streamViolet,
  'pills-violet': pillsViolet,
  'stream-light': streamLight,
}

const src = computed(() => images[props.variant ?? 'cover'])
</script>

<template>
  <div class="dm-bg" :style="{ backgroundImage: `url('${src}')` }" />
</template>

<style scoped>
.dm-bg {
  position: absolute;
  inset: 0;
  z-index: 0;
  background-size: cover;
  background-position: center;
}
</style>
