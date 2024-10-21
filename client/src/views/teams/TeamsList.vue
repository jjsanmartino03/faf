<script setup lang="ts">
import Button from 'primevue/button';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import {useTeamsStore} from "../../store/teams.ts";
import {computed, onMounted, ref} from "vue";
import CreateTeamDialog from "./CreateTeamDialog.vue";
import ProgressSpinner from "primevue/progressspinner";
import Breadcrumb from "primevue/breadcrumb";
import CustomBreadcrumb from "../../components/CustomBreadcrumb.vue";

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
const home = ref({
  icon: 'pi pi-home',
  route: '/home'
})
const items = computed(() => [
  {label: 'Equipos', route: '/teams'},
])
</script>

<template>
  <header class="w-full">
    <CustomBreadcrumb :home="home" :model="items">
    </CustomBreadcrumb>
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
          <Button icon="pi pi-external-link" class="mr-2"/>
        </router-link>
        <CreateTeamDialog :team="slotProps.data" :edit-mode="true" />
      </template>
    </Column>
    <template #loading>
      <div class="bg-white w-full h-full flex justify-content-center">
        <ProgressSpinner strokeWidth="4" style="width: 4rem; height: 4rem;"/>
      </div>
    </template>
    <template #empty> No se encontraron equipos.</template>
  </DataTable>

</template>