<template>
  <div class="slidev-layout dm-dark dm-quote">
    <DmBg variant="cover" />
    <div class="dm-quote-body"><slot /></div>
    <DmFooter dark />
  </div>
</template>

<style scoped>
.dm-quote {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 72px;
  box-sizing: border-box;
  text-align: center;
}
.dm-quote-body {
  font-family: 'El Messiri', serif;
  font-size: 40px;
  font-weight: 700;
  max-width: 80%;
  line-height: 1.2;
}
</style>
