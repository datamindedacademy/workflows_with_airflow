<script setup lang="ts">
defineProps<{ role?: string; photo?: string }>()
</script>

<template>
  <div class="slidev-layout dm-intro">
    <div class="dm-intro-left">
      <div class="dm-eyebrow">Nice to meet you</div>
      <slot />
      <div v-if="role" class="dm-intro-role">{{ role }}</div>
    </div>
    <div class="dm-intro-right">
      <div class="dm-intro-pill dm-intro-pill--a" />
      <div class="dm-intro-pill dm-intro-pill--b" />
      <img v-if="photo" :src="photo" class="dm-intro-photo" />
    </div>
    <DmFooter />
  </div>
</template>

<style scoped>
.dm-intro {
  background: #ffffff;
  height: 100%;
  display: grid;
  grid-template-columns: 1fr 1fr;
  align-items: center;
  padding: 56px;
  box-sizing: border-box;
  gap: 32px;
}
.dm-intro-left :deep(h1) { font-size: 44px; margin: 16px 0 8px; }
.dm-intro-role { font-size: 16px; color: var(--dm-premium); opacity: 0.75; }
.dm-intro-right { position: relative; height: 100%; }
.dm-intro-pill {
  position: absolute; border-radius: 9999px; background: var(--dm-connecting);
}
.dm-intro-pill--a { width: 120px; height: 220px; top: 20%; left: 12%; opacity: 0.9; }
.dm-intro-pill--b { width: 90px; height: 90px; bottom: 18%; right: 20%; opacity: 0.5; }
.dm-intro-photo {
  position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
  width: 240px; height: 240px; border-radius: 9999px; object-fit: cover;
  box-shadow: 0 16px 40px rgba(8, 6, 53, 0.25);
}
</style>
