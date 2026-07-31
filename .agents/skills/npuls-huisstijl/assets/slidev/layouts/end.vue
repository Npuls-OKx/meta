<!-- End slide — afgeleid van .potx master 2 "Einddia" -->
<template>
  <div class="slidev-layout end npuls-combo-blue-pink">
    <img src="/shared/logos/npuls-logo-white.svg" class="npuls-logo" alt="Npuls" />
    <div class="e-content"><slot>
      <h1>Bedankt</h1>
      <h2>Moving Education.</h2>
    </slot></div>
    <img src="/shared/svg/pulse-curve.svg" class="npuls-accent" alt="" />
  </div>
</template>
<style scoped>
.end { display: flex; flex-direction: column; justify-content: center; padding-left: 3.5rem; }
.e-content :deep(h1) { font-size: 5rem; color: var(--npuls-pink); line-height: 1; }
.e-content :deep(h2) { font-size: 1.8rem; color: var(--npuls-pink); opacity: 0.85; font-weight: 400; }
</style>
