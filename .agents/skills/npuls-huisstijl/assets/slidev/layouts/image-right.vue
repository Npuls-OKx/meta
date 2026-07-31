<!-- Image-right layout — afgeleid van .potx "Tekst en afbeelding 1" -->
<template>
  <div class="slidev-layout image-right">
    <img src="/shared/logos/npuls-logo.svg" class="npuls-logo" alt="Npuls" />
    <div class="ir-text"><slot /></div>
    <div class="ir-image">
      <img v-if="image" :src="image" :alt="alt || ''" />
      <slot name="image" />
    </div>
    <img src="/shared/svg/chevron.svg" class="npuls-accent" alt="" />
  </div>
</template>
<script setup lang="ts">
defineProps<{ image?: string, alt?: string }>()
</script>
<style scoped>
.image-right {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  padding-top: 4.5rem;
}
.ir-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 8px;
}
</style>
