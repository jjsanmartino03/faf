<script setup>
import {computed, onMounted, ref} from "vue";
import {useRoute} from "vue-router";
import { useToast } from "primevue/usetoast";

import Dialog from 'primevue/dialog'
import Breadcrumb from "primevue/breadcrumb";
import Button from "primevue/button";
import Tag from "primevue/tag";
import InputGroup from "primevue/inputgroup";
import InputText from "primevue/inputtext";
import DataTable from "primevue/datatable";
import Column from "primevue/column";
import ProgressSpinner from "primevue/progressspinner";
import FloatLabel from "primevue/floatlabel";
import Toast from 'primevue/toast';
import Avatar from 'primevue/avatar';


import {mockTeams} from "../../mocks/teams";
import {mockPlayers} from "../../mocks/players";

import {usePlayersStore} from "../../store/players";

const toast = useToast();
const route = useRoute();
const categoryYear = route.params.categoryYear;

const playersStore = usePlayersStore()

const team = mockTeams.find(team => team.id == route.params.teamId);

const visible = ref(false);

const items = ref([
  {label: 'Equipos', url: '/teams'},
  {label: team.name, url: '/teams/' + team.id},
  {label: 'Categoría ' + categoryYear}
])

const name = ref('');

const toggleVisible = ()=>{
  visible.value=!visible.value
}

const players = computed(() => playersStore.players)

const setStatePlayers = () => {
  players.value.forEach(player => {
    player.status_text = player.status ? 'Activo' : 'Inactivo'
  })
}

const onSubmit = async (e) => {
  e.preventDefault()
  await playersStore.createPlayer({
    name: name.value,
    team_category: parseInt(categoryYear),
  })
  await playersStore.getPlayers()
  setStatePlayers()
  visible.value = false
  name.value = ''
}

onMounted( async () => {
  await playersStore.getPlayers()
  setStatePlayers()
})

</script>

<template>
  <main class="flex flex-column justify-content-center align-items-center h-full px-4 gap-4">
    <header class="w-full">
      <Breadcrumb class="py-2 px-0" :model="items" >
      </Breadcrumb>
      <div class="flex pt-2 gap-2 justify-content-between pb-2 align-items-start ">
        <h1 class="mt-0">Categoría {{ categoryYear }}</h1>
        <Button label="Nuevo Jugador" icon="pi pi-plus" size="small" @click="toggleVisible"/>
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
          <Avatar icon="pi pi-user" class="mr-2" size="xlarge" shape="circle" />
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
          <router-link :to="categoryYear + '/players/' + slotProps.data.id">
            <Button icon="pi pi-pen-to-square" class="mr-2"/>
          </router-link>
        </template>
      </Column>
    </DataTable>
  </main>

<Dialog v-model:visible="visible" modal header="Crear Nuevo Jugador" :style="{ width: '25rem' }">
    <form @submit.prevent="onSubmit" class="flex flex-column w-full align-items-center justify-content-center">
      <div class="p-field mt-4">
        <FloatLabel>
          <label for="name">Nombre</label>
          <InputText required="true" id="name" v-model="name"/>
        </FloatLabel>
      </div>
      <div v-if="playersStore.statusCreatePlayer != 'loading'" class="flex justify-end gap-2 mt-4">
        <Button type="button" label="Cancelar" severity="secondary" @click="visible = false"></Button>
        <Button type="submit" label="Guardar"></Button>
      </div>
      <div v-else class="flex justify-content-center">
        <ProgressSpinner strokeWidth="4" style="width: 1.5rem; height: 1.5rem;"/>
      </div>
    </form>
</Dialog>
</template>