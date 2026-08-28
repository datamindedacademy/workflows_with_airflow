<template>
  <div class="slidev-layout dm-dark dm-section">
    <DmBg variant="section" />
    <div class="dm-section-title"><slot /></div>
    <DmFooter dark />
  </div>
</template>

<style scoped>
.dm-section {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 56px;
  box-sizing: border-box;
}
.dm-section-title :deep(h1) { font-size: 54px; }
</style>
