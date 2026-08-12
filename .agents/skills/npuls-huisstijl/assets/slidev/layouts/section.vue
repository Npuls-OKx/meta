<!-- Section divider — afgeleid van .potx master 2 "Sectiescheider" -->
<template>
  <div class="slidev-layout section npuls-combo-orange-black">
    <div class="s-content"><slot /></div>
    <img src="/shared/svg/starburst.svg" class="npuls-accent" alt="" />
  </div>
</template>
<style scoped>
.section { display: flex; flex-direction: column; justify-content: center; padding: 3rem 4rem; }
.s-content :deep(h1) { font-size: 5rem; color: var(--npuls-black); line-height: 1; }
.s-content :deep(h2) { font-size: 1.5rem; font-weight: 400; color: var(--npuls-black); opacity: 0.85; }
</style>
