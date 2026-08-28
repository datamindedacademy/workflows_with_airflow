<template>
  <div class="slidev-layout dm-values">
    <div class="dm-values-head"><slot /></div>
    <div class="dm-values-row">
      <slot name="badges" />
    </div>
    <DmFooter />
  </div>
</template>

<style scoped>
.dm-values {
  background: #ffffff;
  height: 100%;
  padding: 48px 56px;
  box-sizing: border-box;
}
.dm-values-head :deep(h1) { font-size: 40px; }
.dm-values-row {
  margin-top: 48px;
  display: flex;
  justify-content: space-between;
  gap: 24px;
}
</style>
