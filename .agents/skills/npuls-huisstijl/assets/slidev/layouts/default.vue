<!-- Default content layout — afgeleid van .potx "Titel en tekst" -->
<template>
  <div class="slidev-layout default">
    <img src="/shared/logos/npuls-logo.svg" class="npuls-logo" alt="Npuls" />
    <div class="default-content">
      <slot />
    </div>
    <img src="/shared/svg/pulse-curve.svg" class="npuls-accent" alt="" />
    <div class="npuls-page-number"><slot name="pageNumber" /></div>
  </div>
</template>

<style scoped>
.default {
  padding-top: 5rem;
}
.default-content :deep(h1) {
  margin-bottom: 1rem;
}
</style>
