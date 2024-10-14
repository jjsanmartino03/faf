<script setup lang="ts">
import Button from 'primevue/button';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import {useTeamsStore} from "../../store/teams.ts";
import {computed, onMounted} from "vue";
import CreateTeamDialog from "./CreateTeamDialog.vue";
import ProgressSpinner from "primevue/progressspinner";
import Breadcrumb from "primevue/breadcrumb";

const teamsStore = useTeamsStore()

onMounted(() => {

  console.dir(teamsStore)
  if (teamsStore) {
    teamsStore.getTeams()
  } else {
    console.error('teamsStore is not initialized');
  }
})
const teams = computed(() => teamsStore.teams)

const items = computed(() => [
  {label: 'Home', url: '/'},
  {label: 'Equipos', url: '/teams'},
])
</script>

<template>
  <main class="flex flex-column justify-content-center align-items-center h-full px-4 gap-4">
    <header class="w-full">
      <Breadcrumb class="py-2 px-0" :model="items">
      </Breadcrumb>
      <div class="flex gap-2 justify-content-between pb-2 align-items-start ">
        <h1>Equipos</h1>
        <CreateTeamDialog
        />
      </div>
      <!--      <div class="flex gap-2">
              <InputGroup>
                <InputText placeholder="Ingresa tu búsqueda..."/>
                <Button label="Buscar"/>
              </InputGroup>
            </div>-->

    </header>
    <DataTable :loading="teamsStore.statusGetTeams == 'loading'" :value="teamsStore.teams"
               table-style="min-width: 100%; width: 100%" class="w-full">

      <Column field="logo" header="Escudo" class="w-2">
        <template #body="slotProps">
          <img :src="slotProps.data.logo_url" :alt="slotProps.data.logo_url" class="w-4rem border-round"/>
        </template>
      </Column>
      <Column sortable field="name" header="Nombre" body-class="font-bold"></Column>
      <Column header="Acciones" body-class="font-bold">
        <template #body="slotProps">
          <router-link :to="'/teams/' + slotProps.data.id">
            <Button icon="pi pi-pen-to-square" class="mr-2"/>
          </router-link>
        </template>
      </Column>
      <template #loading>
        <div class="bg-white w-full h-full flex justify-content-center">
          <ProgressSpinner strokeWidth="4" style="width: 4rem; height: 4rem;"/>
        </div>
      </template>
      <template #empty> No se encontraron equipos.</template>
    </DataTable>
  </main>
</template>