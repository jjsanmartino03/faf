<script setup lang="ts">
import {ref} from 'vue';

import InputText from 'primevue/inputtext';
import Card from 'primevue/card';
import Button from 'primevue/button';
import ProgressSpinner from 'primevue/progressspinner';

import FloatLabel from 'primevue/floatlabel';

import SvgTrophy from './SvgTrophy.vue';
import {useRouter} from "vue-router";
import {useAuthStore} from "../../store/auth.ts";

const router = useRouter();

const primaryColor = ref(getComputedStyle(document.documentElement).getPropertyValue('--primary-color'));
const authStore = useAuthStore()
const username = ref('');
const password = ref('');

if (authStore.isAuthenticated) {
  /*router.push({
    name: 'teams'
  })*/
}


async function login(e) {
  e.preventDefault()
  const result = await authStore.login(username.value, password.value)

  if (result) {
    await router.push({
      name: 'teams'
    })
  }
}

const onKeydown = (e) => {
  if (e.key === 'Enter') {
    login(e);
  }
};

</script>

<template>
  <div class="flex">
    <div class="fixed flex justify-content-center align-items-center" style="width: 100%; height: 100vh;">
      <Card>
        <template #header>
          <div class="text-center mt-2">
            <div>
              <SvgTrophy :width="'10rem'" :height="'10rem'" :color="primaryColor"/>
            </div>
          </div>
          <div class="flex justify-content-center">
            <a href="#" class="text-primary no-underline">
              Accede a tu cuenta
            </a>
          </div>
        </template>
        <template #content>
          <form @submit.prevent="login" @keydown="onKeydown">
            <div class="p-fluid">
              <div class="p-field">
                <FloatLabel>
                  <InputText id="username" v-model="username"/>
                  <label for="username">Usuario</label>
                </FloatLabel>
              </div>
              <div class="p-field mt-4">
                <FloatLabel>
                  <InputText id="password" v-model="password" type="password"/>
                  <label for="password">Clave</label>
                </FloatLabel>
              </div>
              <div class="mt-2">
              <span v-if="authStore.status == 'error'" class="text-red-500 pt-4">
                Usuario y/o contraseña inválidos. Intente nuevamente
              </span>
              </div>
              <div class="mt-4">
              <span v-if="authStore.status!='loading'">
                                <Button label="Entrar" type="submit" />
              </span>
                <span v-else>
                <div class="flex justify-content-center">
                    <ProgressSpinner strokeWidth="4" style="width: 1.5rem; height: 1.5rem;"/>
                </div>
            </span>
              </div>
            </div>
          </form>
        </template>
      </Card>
    </div>
  </div>
</template>
<style scoped></style>