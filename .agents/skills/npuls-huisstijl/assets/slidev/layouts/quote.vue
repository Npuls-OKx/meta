<!-- Quote layout — afgeleid van .potx "Quote" -->
<template>
  <div class="slidev-layout quote npuls-combo-pink-blue">
    <img src="/shared/logos/npuls-logo.svg" class="npuls-logo" alt="Npuls" />
    <div class="q-content"><slot /></div>
    <img src="/shared/svg/concentric-rings.svg" class="npuls-accent" alt="" />
  </div>
</template>
<style scoped>
.quote { display: flex; align-items: center; justify-content: center; padding: 3rem 5rem; }
.q-content :deep(blockquote) { font-size: 2.2rem; border-left: 0; text-align: center; color: var(--npuls-blue); }
.q-content :deep(blockquote::before) { content: "\201C"; font-size: 4rem; display: block; line-height: 0.5; }
</style>
