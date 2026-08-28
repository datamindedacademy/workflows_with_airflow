<script setup lang="ts">
import wordlogo from '../assets/wordlogo-light.png'
</script>

<template>
  <div class="slidev-layout dm-dark dm-thanks">
    <DmBg variant="section" />
    <img :src="wordlogo" class="dm-thanks-logo" alt="Dataminded" />
    <div class="dm-thanks-body"><slot /></div>
    <DmFooter dark />
  </div>
</template>

<style scoped>
.dm-thanks {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 72px;
  box-sizing: border-box;
}
.dm-thanks-logo {
  position: absolute;
  top: 64px;
  left: 50%;
  transform: translateX(-50%);
  height: 30px;
}
.dm-thanks-body :deep(h1) { font-size: 56px; }
</style>
