<script setup lang="ts">
import {computed, onMounted, ref} from "vue";
import {useRoute, useRouter} from "vue-router";
import Breadcrumb from "primevue/breadcrumb";
import Button from "primevue/button";
import Tag from "primevue/tag";
import InputGroup from "primevue/inputgroup";
import InputText from "primevue/inputtext";
import DataTable from "primevue/datatable";
import Column from "primevue/column";
import Avatar from 'primevue/avatar';

import {usePlayersStore} from "../../store/players";
import {useTeamsStore} from "../../store/teams";
import CreatePlayerDialog from "./CreatePlayerDialog.vue";
import ProgressSpinner from "primevue/progressspinner";
import CustomBreadcrumb from "../../components/CustomBreadcrumb.vue";

const route = useRoute();
console.log(route.params.categoryId);
const playersStore = usePlayersStore()

const teamsStore = useTeamsStore()
onMounted(async () => {
  playersStore.getPlayers(parseInt(route.params.categoryId as string))
  teamsStore.getTeam(route.params.teamId)
})

const onCreatePlayer = () =>   playersStore.getPlayers(parseInt(route.params.categoryId as string))

const team = computed(() => teamsStore.team)
const visible = ref(false);
const router = useRouter();

const categoryYear = computed(() =>
    team.value ? team.value.categories.find(category => category.id === parseInt(route.params.categoryId as string)).category : '')
const apiUrl = import.meta.env.VITE_API_URL

const items = computed(() => [
  {label: 'Equipos', route: '/teams'},
  {label: team.value ? team.value.name : '', route: '/teams/' + (team.value ? team.value.id : '')},
  {label: 'Categoría ' + categoryYear.value}
])
console.log(categoryYear);
const name = ref('');

const players = computed(() => playersStore.players)

if (players.value) {
  players.value.forEach(player => {
    player.status_text = player.status ? 'Activo' : 'Inactivo'
  })
}

const onRowClick = (playerId) => {
  const { teamId, categoryId } = route.params;
  router.push(`/teams/${teamId}/categories/${categoryId}/players/${playerId}`);
}

</script>

<template>
  <main class="flex flex-column justify-content-start align-items-center h-full">
    <header class="w-full">
      <CustomBreadcrumb :model="items">
      </CustomBreadcrumb>
      <div class="flex pt-2 gap-2 justify-content-between pb-2 align-items-start ">
        <h1 class="mt-0">Categoría {{ categoryYear }}</h1>
        <CreatePlayerDialog :on-complete-action="onCreatePlayer" :category-id="parseInt(route.params.categoryId as string)"/>
      </div>
      <div class="flex gap-2">
        <InputGroup>
          <InputText placeholder="Ingresa tu búsqueda..."/>
          <Button label="Buscar"/>
        </InputGroup>
      </div>

    </header>
    <DataTable @row-click="slotProps => onRowClick(slotProps.data.id)" :loading="playersStore.statusGetPlayers === 'loading'" :value="players"
               table-style="min-width: 100%; width: 100%" class="w-full"
               selectionMode="single">
      <Column header="Jugador" sortable field="name" >
        <template #body="slotProps">
          <div class="flex gap-2 align-items-center">

          <Avatar v-if="!slotProps.data.image" icon="pi pi-user" class="mr-2 w-4rem" size="xlarge" shape="circle"/>
          <Avatar v-else :image="apiUrl+ 'media/players/'+ slotProps.data.id + '/'+slotProps.data.image" class="mr-2 w-4rem"
                  size="xlarge" shape="circle"/>
            <span>{{slotProps.data.name}}</span>
          </div>
        </template>
      </Column>
      <Column sortable field="status_text" header="Estado" body-class="font-bold">
        <template #body="slotProps">
          <Tag v-if="slotProps.data.status" value="Activo" severity="success"/>
          <Tag v-else value="Inactivo" severity="danger"/>
        </template>
      </Column>
      <template #loading>
        <div class="bg-white w-full h-full flex justify-content-center">
          <ProgressSpinner strokeWidth="4" style="width: 4rem; height: 4rem;"/>
        </div>
      </template>
      <template #empty> No se encontraron jugadores.</template>
    </DataTable>
  </main>
</template>