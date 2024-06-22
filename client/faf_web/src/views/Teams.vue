<script setup lang="ts">
import InputGroup from 'primevue/inputgroup';
import InputText from 'primevue/inputtext';
import Button from 'primevue/button';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import {mockTeams} from "../mocks/teams.ts";


</script>

<template>
  <main class="flex flex-column justify-content-center align-items-center h-full px-4 gap-4">
    <header class="w-full">
      <h1>Equipos</h1>
      <div class="flex">
        <InputGroup>
          <InputText placeholder="Ingresa tu búsqueda..."/>
          <Button label="Buscar"/>
        </InputGroup>
      </div>
    </header>
    <DataTable :value="mockTeams" table-style="min-width: 100%; width: 100%" class="w-full">
      <Column field="logo" header="Logo" class="w-2">
        <template #body="slotProps">
          <img :src="slotProps.data.logo" :alt="slotProps.data.logo" class="w-4rem border-round"/>
        </template>
      </Column>
      <Column sortable field="name" header="Nombre" body-class="font-bold"></Column>
      <Column header="Acciones" body-class="font-bold">
        <template #body="slotProps">
          <router-link :to="'/teams/' + slotProps.data.id">
            <Button label="Ver" class="mr-2"/>
          </router-link>
        </template>
      </Column>
    </DataTable>
  </main>
</template>

// https://source.boringavatars.com/marble/120/River