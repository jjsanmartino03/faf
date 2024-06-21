import { createApp } from 'vue'

import PrimeVue from 'primevue/config'
import 'primevue/resources/themes/aura-dark-lime/theme.css'
import 'primeicons/primeicons.css'
import '/node_modules/primeflex/primeflex.css'
import router from "./router";

import { createPinia } from 'pinia'

import App from './App.vue'

const pinia = createPinia()

createApp(App)
.use(router)
.use(PrimeVue)
.use(pinia)
.mount('#app')
