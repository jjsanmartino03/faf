<script setup lang="ts">
import {computed, onMounted, ref} from "vue";
import {useRoute} from "vue-router";
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

const route = useRoute();
console.log(route.params.categoryId);
const playersStore = usePlayersStore()

const teamsStore = useTeamsStore()
const team = computed(() => teamsStore.team)
const visible = ref(false);

const categoryYear = computed(() =>
    team.value ? team.value.categories.find(category => category.id === parseInt(route.params.categoryId as string)).category : '')

const items = computed(() => [
  {label: 'Equipos', url: '/teams'},
  {label: team.value ? team.value.name : '', url: '/teams/' + (team.value ? team.value.id : '')},
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

onMounted(async () => {
  await teamsStore.getTeam(route.params.teamId)
  await playersStore.getPlayers(parseInt(route.params.categoryId as string))
})

</script>

<template>
  <main class="flex flex-column justify-content-start align-items-center h-full">
    <header class="w-full">
      <Breadcrumb class="py-2 px-0" :model="items">
      </Breadcrumb>
      <div class="flex pt-2 gap-2 justify-content-between pb-2 align-items-start ">
        <h1 class="mt-0">Categoría {{ categoryYear }}</h1>
        <CreatePlayerDialog :category-id="parseInt(route.params.categoryId as string)"/>
      </div>
      <div class="flex gap-2">
        <InputGroup>
          <InputText placeholder="Ingresa tu búsqueda..."/>
          <Button label="Buscar"/>
        </InputGroup>
      </div>

    </header>
    <DataTable :value="players" table-style="min-width: 100%; width: 100%" class="w-full">
      <Column header="Foto" class="w-2">
        <template #body="slotProps">
          <Avatar icon="pi pi-user" class="mr-2" size="xlarge" shape="circle"/>
        </template>
      </Column>
      <Column sortable field="name" header="Nombre" body-class="font-bold"></Column>
      <Column sortable field="status_text" header="Estado" body-class="font-bold">
        <template #body="slotProps">
          <Tag v-if="slotProps.data.status" value="Activo" severity="success"/>
          <Tag v-else value="Inactivo" severity="danger"/>
        </template>
      </Column>
      <Column header="Acciones" body-class="font-bold text-center">
        <template #body="slotProps">
          <router-link :to="route.params.categoryId + '/players/' + slotProps.data.id">
            <Button icon="pi pi-external-link" class="mr-2"/>
          </router-link>
          <CreatePlayerDialog :category-id="parseInt(route.params.categoryId as string)" :player="slotProps.data"
                              :edit-mode="true"/>
        </template>
      </Column>
      <template #empty> No se encontraron jugadores.</template>
    </DataTable>
  </main>
</template>