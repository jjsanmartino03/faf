<script setup>
import Button from 'primevue/button';
</script>
<template>
  <main class="flex justify-content-center align-items-center h-screen">
    <div class="flex flex-column gap-4">
      <router-link to="/teams">
        <Button size="large">Equipos</Button>
      </router-link>
      <router-link to="/matches">
        <Button size="large">Partidos</Button>
      </router-link>
    </div>
  </main>
</template>
<style scoped>

</style>