<!-- Two-column layout — afgeleid van .potx "Inhoud van twee" -->
<template>
  <div class="slidev-layout two-col">
    <img src="/shared/logos/npuls-logo.svg" class="npuls-logo" alt="Npuls" />
    <div class="tc-title"><slot name="title" /></div>
    <div class="tc-grid">
      <div class="tc-left"><slot name="left" /></div>
      <div class="tc-right"><slot name="right" /></div>
    </div>
  </div>
</template>
<style scoped>
.two-col { padding-top: 4rem; }
.tc-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 2.5rem; margin-top: 1.5rem; }
</style>
