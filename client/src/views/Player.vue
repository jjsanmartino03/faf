<script setup lang="ts">
import InputText from "primevue/inputtext";
import Button from "primevue/button";
import InputGroup from "primevue/inputgroup";
import ProgressSpinner from "primevue/progressspinner";
import Breadcrumb from "primevue/breadcrumb";
import {computed, onMounted, ref} from "vue";
import {mockPlayers} from "../mocks/players";
import {useRoute} from "vue-router";
import {usePlayersStore} from "../store/players";
import {useTeamsStore} from "../store/teams.ts";

const route = useRoute()
const photosQuantity = ref(12)

const photosArray = new Array(photosQuantity.value)
const generateRandomString = () => {
  return Math.random().toString(36).substring(7); // Generate a random string
}

const playerId = route.params.playerId

const teamId = route.params.teamId
const categoryYear = route.params.categoryId
const playersStore = usePlayersStore()
const teamsStore = useTeamsStore()

const player = computed(() => playersStore.player)
const isEnabled = computed(() => player ? player.value.status : false)
onMounted(() => {
  playersStore.getPlayer(parseInt(playerId as string))
  teamsStore.getTeam(parseInt(teamId as string))
})

const team = computed(() => teamsStore.team)

const updatePlayerStatus = async (newStatus: boolean) => {
  const error = await playersStore.updatePlayerStatus(player.value.id, newStatus)
  if (!error) {
    player.value.status = newStatus
  }
}

const items = computed(() => [
  {label: 'Equipos', url: '/teams'},
  {label: team.value?.name, url: '/teams/' + team.value?.id},
  {label: 'Categoría ' + categoryYear, url: '/teams/' + team.value?.id + '/categories/' + categoryYear},
  {label: player.value?.name}
])

</script>
<template>
  <main v-if="playersStore.statusGetPlayer !== 'loading' && player"
        class="flex flex-column justify-content-center align-items-center gap-2 w-full">
    <div class="w-full">
      <Breadcrumb class="py-2 h-min px-0 w-full" :model="items"/>
    </div>
    <header class="w-full flex">

      <div class="flex pt-2 gap-2 justify-content-between pb-2 align-items-center ">
        <h1 class="m-0">{{ player.name }}</h1>
        <Button :loading="playersStore.statusCreatePlayer === 'loading'"
                :icon="isEnabled ? 'pi pi-check' : 'pi pi-times'" :severity="isEnabled ?'success' : 'danger'"
                class="mr-2 text-4xl" icon-class="text-xl"
                text @click="() =>updatePlayerStatus(!isEnabled)"/>
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
  <main v-else class="flex flex-column justify-content-center align-items-center h-full px-4 gap-4 pt-2">
    <ProgressSpinner strokeWidth="4" style="width: 1.5rem; height: 1.5rem;"/>
  </main>
</template>