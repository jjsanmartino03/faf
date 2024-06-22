import { createApp } from 'vue'

import PrimeVue from 'primevue/config'
import './style.css'
import 'primevue/resources/themes/aura-light-green/theme.css'
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
