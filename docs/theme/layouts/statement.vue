<template>
  <div class="slidev-layout dm-dark dm-statement">
    <DmBg variant="stream-violet" />
    <div class="dm-statement-body"><slot /></div>
    <DmFooter dark />
  </div>
</template>

<style scoped>
.dm-statement {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 72px;
  box-sizing: border-box;
  text-align: center;
}
.dm-statement-body :deep(h1) { font-size: 52px; }
</style>
