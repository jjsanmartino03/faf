<script setup lang="ts">
import {RouterView, useRouter} from "vue-router";
import {useAuthStore} from "../store/auth.ts";
import {onMounted, ref, watch} from "vue";
import Button from 'primevue/button';

const router = useRouter();
const authStore = useAuthStore();

const showMenu = ref(false);
const isStaff = ref(false);

const menuOptions = ref([]);

const navigateTo = (route: string) => {
  router.push(route);
};

const logout = () => {
  authStore.logout();
  menuOptions.value = []; 
  navigateTo('/login');
};

const setMenuOptions = () => {
  isStaff.value = authStore.isAdmin;

  if(menuOptions.value.length == 0) {
    menuOptions.value.push(
      { name: 'Salir', icon: 'pi pi-sign-out', action: () => logout() },
      { name: 'Partidos', icon: 'pi pi-calendar', action: () => navigateTo('/matches') }
    );

    if (isStaff.value) {
      menuOptions.value.push(
        { name: 'Equipos', icon: 'pi pi-users', action: () => navigateTo('/teams') }
      );
    }
    menuOptions.value.reverse();
  }
};

watch(router.currentRoute, () => {
  showMenu.value = router.currentRoute.value.path !== '/' && router.currentRoute.value.path !== '/login';
});

watch(router.currentRoute, async () => {
  if (router.currentRoute.value.path !== '/login') 
    await checkRouteAndSetMenu();
});

const checkRouteAndSetMenu = async () => {
  if (router.currentRoute.value.path !== '/login') {
    await authStore.getCurrentUser();
  }
  showMenu.value = router.currentRoute.value.path !== '/' && router.currentRoute.value.path !== '/login';
  console.log(showMenu.value);
  setMenuOptions();
};

const getLabel = (name: string) => {
  if (window.innerWidth < 768) return null;
  return name;
};

onMounted(async () => {
  await checkRouteAndSetMenu();
});

</script>

<template>
  <main class="bg-gray-100 flex flex-column align-items-center"
        style="height: 100dvh"
    :class="{'pb-3': showMenu}"> 
    <div class="p-2 gap-3 flex flex-column w-full lg:w-6 bg-white h-full justify-content-start">
      <RouterView/>
    </div>  
    <div class="p-2 gap-3 flex fixed bg-teal-600 lg:w-6 justify-content-center bottom-0 r-5 w-full border-round-3xl mx-2"
        v-if="showMenu">
        <Button  
          v-for="option in menuOptions"
          :key="option.name"
          :icon="option.icon"
          :label="getLabel(option.name)"
          iconPos="left"
          @click="option.action()"
          class="mx-2 p-2 bg-teal-100 hover:bg-teal-200"
          rounded
          severity="secondary"
        />
    </div>
  </main>
</template>

<style scoped>
</style>