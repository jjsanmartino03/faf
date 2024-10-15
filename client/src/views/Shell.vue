<script setup lang="ts">
import {RouterView, useRouter} from "vue-router";
import {useAuthStore} from "../store/auth.ts";
import {onMounted} from "vue";

const router = useRouter();
const authStore = useAuthStore();

onMounted(() => {
  authStore.getCurrentUser();
})

</script>

<template>
  <RouterView/>
</template>

<style scoped>

</style>