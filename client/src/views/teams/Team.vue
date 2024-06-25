<script setup>
import {mockTeams} from "../../mocks/teams";
import {onMounted, ref} from "vue";
import {useRoute} from "vue-router";
import Button from "primevue/button";
import Column from "primevue/column";
import DataTable from "primevue/datatable";
import {mockCategories} from "../../mocks/categories.ts";

const route = useRoute()

const teamId = route.params.id

const team = mockTeams.find(team => team.id == teamId)


</script>
<template>
  <main v-if="team" class="flex w-full flex-column justify-content-center align-items-center h-full px-4 gap-4 pt-2">
    <header class="w-full flex gap-4 align-items-center">
      <img :src="team.logo" :alt="team.logo" class="w-6rem border-round"/>
      <h1>{{ team.name }}</h1>
    </header>
    <div class="w-full">
      <h2>Categorías</h2>
      <DataTable :value="mockCategories" table-style="min-width: 100%; width: 100%" class="w-full">
        <Column field="year" header="Categoría" body-class="font-bold">
          <template #body="slotProps">
            Cat. {{ slotProps.data.year }}
          </template>
        </Column>
        <Column header="Acciones" class="font-bold flex justify-content-center">
          <template #body="slotProps">
            <router-link :to="'/teams/' + team.id + '/categories/' + slotProps.data.year">
              <Button icon="pi pi-external-link" class="mr-2"/>
            </router-link>
          </template>
        </Column>
      </DataTable>
    </div>
  </main>
  <main v-else class="flex flex-column justify-content-center align-items-center h-full px-4 gap-4 pt-2">
    <h1>Equipo no encontrado</h1>
  </main>
</template>