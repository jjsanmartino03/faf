<script setup>
import {computed, onMounted, ref} from "vue";
import {useRoute, useRouter} from "vue-router";
import Button from "primevue/button";
import Column from "primevue/column";
import DataTable from "primevue/datatable";
import {useTeamsStore} from "../../store/teams";
import ProgressSpinner from "primevue/progressspinner";
import Breadcrumb from "primevue/breadcrumb";
import CustomBreadcrumb from "../../components/CustomBreadcrumb.vue";
import CreateTeamDialog from "./CreateTeamDialog.vue";

const route = useRoute()

const teamsStore = useTeamsStore()
const team = computed(() => teamsStore.team)

const teamId = route.params.id

onMounted(async () => {
  teamsStore.getTeam(teamId)
})

const home = ref({
  icon: 'pi pi-home',
  route: '/home'
})
const items = computed(() => [
  {label: 'Equipos', route: '/teams'},
  {label: team.value ? team.value.name : '', url: '/teams/' + teamId},
])
const router = useRouter();
const onCategoryClick = (team,id) => {
  router.push('/teams/' + team  .id + '/categories/' + id)
}
const onUpdateTeam = () => teamsStore.getTeam(teamId)
</script>
<template>
  <main v-if="team" class="flex w-full flex-column justify-content-start align-items-center h-full gap-4">

    <header class="w-full">
      <CustomBreadcrumb :home="home" :model="items">
      </CustomBreadcrumb>
      <div class="flex gap-4 justify-content-start pb-2 align-items-center ">
        <img :src="team.logo_url" :alt="team.logo_url" class="w-6rem border-round"/>
        <h1>{{ team.name }}</h1>
        <div><CreateTeamDialog :on-complete-action="onUpdateTeam" :team="team" :edit-mode="true" /></div>
      </div>
    </header>
    <div class="w-full">
      <h2>Categorías</h2>
      <DataTable @row-click="slotProps => onCategoryClick(team,slotProps.data.id)" :value="team.categories" table-style="min-width: 100%; width: 100%" class="w-full"
        selectionMode="single">
        <Column field="year" header="Categoría" body-class="font-bold">
          <template #body="slotProps">
            Cat. {{ slotProps.data.category }}
          </template>
        </Column>
      </DataTable>
    </div>
  </main>
  <main v-else class="flex flex-column justify-content-center align-items-center h-full px-4 gap-4 pt-2">
    <ProgressSpinner strokeWidth="4" style="width: 1.5rem; height: 1.5rem;"/>
  </main>
</template>