import { createApp } from 'vue'

import PrimeVue from 'primevue/config'
import 'primevue/resources/themes/aura-light-teal/theme.css'
import 'primeicons/primeicons.css'
import '/node_modules/primeflex/primeflex.css'
import router from "./router";
import './style.css'

import { createPinia } from 'pinia'

import App from './App.vue'

const pinia = createPinia()

createApp(App)
.use(router)
.use(PrimeVue)
.use(pinia)
.mount('#app')
