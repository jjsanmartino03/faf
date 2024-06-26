<script setup>
import {useRoute} from "vue-router";
import Breadcrumb from "primevue/breadcrumb";
import Button from "primevue/button";
import InputGroup from "primevue/inputgroup";
import InputText from "primevue/inputtext";
import DataTable from "primevue/datatable";
import {ref} from "vue";
import {mockTeams} from "../../mocks/teams";
import {mockPlayers} from "../../mocks/players";
import Column from "primevue/column";

const route = useRoute();
const categoryYear = route.params.categoryYear;

const team = mockTeams.find(team => team.id == route.params.teamId);


const items = ref([
  {label: 'Equipos', url: '/teams'},
  {label: team.name, url: '/teams/' + team.id},
  {label: 'Categoría ' + categoryYear}
])
</script>

<template>
  <main class="flex flex-column justify-content-center align-items-center h-full px-4 gap-4">
    <header class="w-full">
      <Breadcrumb class="py-2 px-0" :model="items"></Breadcrumb>
      <div class="flex pt-2 gap-2 justify-content-between pb-2 align-items-start ">
        <h1 class="mt-0">Categoría {{ categoryYear }}</h1>
        <Button label="Nuevo Jugador" icon="pi pi-plus" size="small"/>
      </div>
      <div class="flex gap-2">
        <InputGroup>
          <InputText placeholder="Ingresa tu búsqueda..."/>
          <Button label="Buscar"/>
        </InputGroup>
      </div>

    </header>
    <DataTable :value="mockPlayers" table-style="min-width: 100%; width: 100%" class="w-full">
      <Column header="Foto" class="w-2">
        <template #body="slotProps">
          <img :src="slotProps.data.photo" :alt="'Foto de ' + slotProps.data.name" class="w-4rem border-round"/>
        </template>
      </Column>
      <Column sortable field="name" header="Nombre" body-class="font-bold"></Column>
      <Column header="Acciones" body-class="font-bold">
        <template #body="slotProps">
          <Button v-if="slotProps.data.isEnabled" icon="pi pi-check" severity="success" class="mr-2" text disabled/>
          <Button v-else icon="pi pi-times" severity="danger" class="mr-2" text disabled/>

          <router-link :to="categoryYear + '/players/' + slotProps.data.id">
            <Button icon="pi pi-pen-to-square" class="mr-2"/>
          </router-link>
        </template>
      </Column>
    </DataTable>
  </main>
</template>