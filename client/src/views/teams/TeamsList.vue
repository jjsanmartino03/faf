<script setup lang="ts">
import InputGroup from 'primevue/inputgroup';
import InputText from 'primevue/inputtext';
import Button from 'primevue/button';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import {mockTeams} from "../../mocks/teams.ts";


</script>

<template>
  <main class="flex flex-column justify-content-center align-items-center h-full px-4 gap-4">
    <header class="w-full">
      <div class="flex gap-2 justify-content-between pb-2 align-items-start ">
        <h1>Equipos</h1>
        <Button label="Nuevo equipo" icon="pi pi-plus" class="mt-4" size="small"/>
      </div>
      <div class="flex gap-2">
        <InputGroup>
          <InputText placeholder="Ingresa tu búsqueda..."/>
          <Button label="Buscar"/>
        </InputGroup>
      </div>

    </header>
    <DataTable :value="mockTeams" table-style="min-width: 100%; width: 100%" class="w-full">
      <Column field="logo" header="Escudo" class="w-2">
        <template #body="slotProps">
          <img :src="slotProps.data.logo" :alt="slotProps.data.logo" class="w-4rem border-round"/>
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
    </DataTable>
  </main>
</template>