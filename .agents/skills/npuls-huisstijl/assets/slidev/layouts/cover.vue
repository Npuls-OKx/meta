<!-- Cover layout — afgeleid van .potx "Titeldia" -->
<template>
  <div class="slidev-layout cover npuls-combo-pink-blue">
    <img src="/shared/logos/npuls-logo.svg" class="npuls-logo" alt="Npuls" />
    <div class="cover-content">
      <slot />
    </div>
    <img src="/shared/svg/concentric-rings.svg" class="npuls-accent" alt="" />
  </div>
</template>

<style scoped>
.cover {
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding-left: 3.5rem;
  padding-right: 3.5rem;
}
.cover-content :deep(h1) {
  font-size: 4rem;
  line-height: 1.05;
  max-width: 70%;
  color: var(--npuls-blue);
}
.cover-content :deep(h2) {
  font-size: 1.6rem;
  font-weight: 400;
  color: var(--npuls-blue);
  margin-top: 1rem;
  opacity: 0.85;
}
</style>
