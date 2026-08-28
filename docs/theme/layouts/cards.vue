<template>
  <div class="slidev-layout dm-cards">
    <div class="dm-cards-head"><slot /></div>
    <div class="dm-cards-grid">
      <slot name="cards" />
    </div>
    <DmFooter />
  </div>
</template>

<style scoped>
.dm-cards {
  background: #ffffff;
  height: 100%;
  padding: 48px 56px;
  box-sizing: border-box;
}
.dm-cards-head :deep(h1) { font-size: 40px; }
.dm-cards-grid {
  margin-top: 32px;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}
</style>
