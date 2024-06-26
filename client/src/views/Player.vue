<script setup>
import InputText from "primevue/inputtext";
import Button from "primevue/button";
import InputGroup from "primevue/inputgroup";
import Breadcrumb from "primevue/breadcrumb";
import {onMounted, ref} from "vue";
import {mockPlayers} from "../mocks/players";
import {useRoute} from "vue-router";
import {mockTeams} from "../mocks/teams";

const route = useRoute()

const player = mockPlayers.find(player => player.id == route.params.playerId)
const isEnabled = ref(player.isEnabled)

const disablePlayer = () => {
  console.log('Player disabled')
  isEnabled.value = false
}

const enablePlayer = () => {
  isEnabled.value = true
}

const photosQuantity = ref(12)
const photosArray = new Array(photosQuantity.value)

const generateRandomString = () => {
  return Math.random().toString(36).substring(7); // Generate a random string
}

const playerId = route.params.playerId
const teamId = route.params.teamId
const categoryYear = route.params.categoryYear

const team = mockTeams.find(team => team.id == teamId)

const items = ref([
  {label: team.name, url: '/teams/' + team.id},
  {label: 'Categoría ' + categoryYear, url: '/teams/' + team.id + '/categories/' + categoryYear},
])

</script>
<template>
  <main class="flex flex-column justify-content-center align-items-center h-screen px-4 gap-2 w-full">
    <div class="w-full"><Breadcrumb class="py-2 h-min px-0 w-full" :model="items"/></div>
    <header class="w-full flex">

      <div class="flex pt-2 gap-2 justify-content-between pb-2 align-items-center ">
        <img :src="player.photo" :alt="'Foto de ' + player.name" class="w-6rem border-round"/>
        <h1 class="m-0">{{ player.name }}</h1>
        <Button v-if="isEnabled" icon="pi pi-check" severity="success" class="mr-2 text-4xl" icon-class="text-xl"
                text @click="disablePlayer"/>
        <Button v-else icon="pi pi-times" severity="danger" class="mr-2" text @click="enablePlayer"/>
      </div>

    </header>
    <div class="flex flex-column justify-content-between h-full pb-4">
      <div>
        <h2 class="mt-0">Fotos</h2>
        <div class="grid border-round-md align-items-center">
          <div v-for="_ in photosArray"
               class="col-3 bg-blue-100 border-2 align-items-center justify-content-center text-center">
            <img :src="'https://source.boringavatars.com/beam/120/'+ generateRandomString()" alt="Foto de jugador"
                 class="w-6rem border-round"/>
          </div>
        </div>
      </div>
      <div class="flex justify-content-center w-full">
        <Button icon="pi pi-plus" size="large" class="text-4xl w-8rem h-8rem" rounded raised/>

      </div>
    </div>
  </main>
</template>