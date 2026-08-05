<!-- Image-left layout — afgeleid van .potx "Tekst en afbeelding 2" -->
<template>
  <div class="slidev-layout image-left">
    <img src="/shared/logos/npuls-logo.svg" class="npuls-logo" alt="Npuls" />
    <div class="il-image">
      <img v-if="image" :src="image" :alt="alt || ''" />
      <slot name="image" />
    </div>
    <div class="il-text"><slot /></div>
  </div>
</template>
<script setup lang="ts">
defineProps<{ image?: string, alt?: string }>()
</script>
<style scoped>
.image-left {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  padding-top: 4.5rem;
}
.il-image img { width: 100%; height: 100%; object-fit: cover; border-radius: 8px; }
</style>
