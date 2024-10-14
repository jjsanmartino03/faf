<script setup>
import {computed, onMounted, ref} from "vue";
import {useRoute} from "vue-router";
import Button from "primevue/button";
import Column from "primevue/column";
import DataTable from "primevue/datatable";
import {mockCategories} from "../../mocks/categories.ts";
import {useTeamsStore} from "../../store/teams";
import ProgressSpinner from "primevue/progressspinner";
import Breadcrumb from "primevue/breadcrumb";

const route = useRoute()

const teamsStore = useTeamsStore()
const team = computed(() => teamsStore.team)

const teamId = route.params.id

onMounted(async () => {
  teamsStore.getTeam(teamId)
})

const items = computed(() => [
  {label: 'Home', url: '/'},
  {label: 'Equipos', url: '/teams'},
  {label: team.value ? team.value.name : '', url: '/teams/' + teamId},
])

</script>
<template>
  <main v-if="team" class="flex w-full flex-column justify-content-center align-items-center h-full px-4 gap-4 pt-2">

    <header class="w-full">
      <Breadcrumb class="py-2 px-0" :model="items">
      </Breadcrumb>
      <div class="flex gap-4 justify-content-start pb-2 center ">
      <img :src="team.logo_url" :alt="team.logo_url" class="w-6rem border-round"/>
      <h1>{{ team.name }}</h1>
      </div>
    </header>
    <div class="w-full">
      <h2>Categorías</h2>
      <DataTable :value="team.categories" table-style="min-width: 100%; width: 100%" class="w-full">
        <Column field="year" header="Categoría" body-class="font-bold">
          <template #body="slotProps">
            Cat. {{ slotProps.data.category }}
          </template>
        </Column>
        <Column header="Acciones" class="font-bold flex justify-content-center">
          <template #body="slotProps">
            <router-link :to="'/teams/' + team.id + '/categories/' + slotProps.data.id">
              <Button icon="pi pi-external-link" class="mr-2"/>
            </router-link>
          </template>
        </Column>
      </DataTable>
    </div>
  </main>
  <main v-else class="flex flex-column justify-content-center align-items-center h-full px-4 gap-4 pt-2">
    <ProgressSpinner strokeWidth="4" style="width: 1.5rem; height: 1.5rem;"/>
  </main>
</template>