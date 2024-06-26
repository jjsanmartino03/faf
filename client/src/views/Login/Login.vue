<script setup lang="ts">
import { ref } from 'vue';

import InputText from 'primevue/inputtext';
import Card from 'primevue/card';
import Button from 'primevue/button';
import ProgressSpinner from 'primevue/progressspinner';

import FloatLabel from 'primevue/floatlabel';

import SvgTrophy from './SvgTrophy.vue';
import { useRouter } from "vue-router";

const router = useRouter();


const primaryColor = ref(getComputedStyle(document.documentElement).getPropertyValue('--primary-color'));

const username = ref('');
const password = ref('');

const loading = ref(false);



const goTo = () => {
    loading.value = true;
    setTimeout(() => {
        if (username.value === 'delegado' && password.value === 'delegado') {
        router.push({
            name: 'matches'
        })
    }
        loading.value = false;
    }, 2000);
    
}

</script>

<template>
    <div class="flex">
        <div class="fixed flex justify-content-center align-items-center" style="width: 100%; height: 100vh;">
            <Card>
                <template #header>
                    <div class="text-center mt-2">
                        <div>
                            <SvgTrophy :width="'10rem'" :height="'10rem'" :color="primaryColor" />
                        </div>
                    </div>
                    <div class="flex justify-content-center">
                        <a href="#" class="text-primary no-underline">
                            Accede a tu cuenta
                        </a>
                    </div>
                </template>
                <template #content>
                    <div class="p-fluid">
                        <div class="p-field">
                            <FloatLabel>
                                <InputText id="username" v-model="username" />
                                <label for="username">Usuario</label>
                            </FloatLabel>
                        </div>
                        <div class="p-field mt-4">
                            <FloatLabel>
                                <InputText id="password" v-model="password" type="password" />
                                <label for="password">Clave</label>
                            </FloatLabel>
                        </div>
                        <div class="mt-3">
                            <span v-if="!loading">
                                <Button label="Entrar" @click="goTo" />
                            </span>
                            <span v-else>
                                <div class="flex justify-content-center">
                                    <ProgressSpinner strokeWidth="4" style="width: 1.5rem; height: 1.5rem;" />
                                </div>
                            </span>
                        </div>
                    </div>
                    <div class="flex justify-content-end mt-4">
                        <a href="#" class="text-primary no-underline">
                            ¿Olvidaste tu clave?
                        </a>
                    </div>
                </template>
            </Card>
        </div>
    </div>
</template>
<style scoped></style>