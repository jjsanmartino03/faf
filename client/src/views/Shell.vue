<script setup lang="ts">
import {RouterView, useRouter} from "vue-router";
import {useAuthStore} from "../store/auth.ts";
import {onMounted} from "vue";

const router = useRouter();
const authStore = useAuthStore();

onMounted(() => {
  // get current user if not in /login
  if (router.currentRoute.value.path !== '/login') {
    authStore.getCurrentUser()
  }
})

</script>

<template>
  <main class="bg-gray-100 flex flex-column align-items-center h-screen">
    <div class="p-2 gap-3 flex flex-column w-full lg:w-6 bg-white h-full justify-content-start px-3 py-2">
      <RouterView/>
    </div>
  </main>
</template>

<style scoped>

</style>