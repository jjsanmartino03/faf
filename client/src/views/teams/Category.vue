<script setup>
import {computed, onMounted, ref} from "vue";
import {useRoute} from "vue-router";
import {useToast} from "primevue/usetoast";

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
import Avatar from 'primevue/avatar';

import {usePlayersStore} from "../../store/players";
import {useTeamsStore} from "../../store/teams";
import CreatePlayerDialog from "./CreatePlayerDialog.vue";

const route = useRoute();
console.log(route.params.categoryYear);
const playersStore = usePlayersStore()

const teamsStore = useTeamsStore()
const team = computed(() => teamsStore.team)
const visible = ref(false);

const categoryYear = computed(() => (team.value ? team.value.categories.find(category => category.id == route.params.categoryYear).category : ''), [team]);

const items = computed(() => [
  {label: 'Equipos', url: '/teams'},
  {label: team.value ? team.value.name : '', url: '/teams/' + (team.value ? team.value.id : '')},
  {label: 'Categoría ' + categoryYear.value}
], [team])
console.log(categoryYear);
const name = ref('');

const toggleVisible = () => {
  visible.value = !visible.value
}

const players = computed(() => playersStore.players)

if (players.value) {
  players.value.forEach(player => {
    player.status_text = player.status ? 'Activo' : 'Inactivo'
  })
}

const onSubmit = async (e) => {
  e.preventDefault()
  await playersStore.createPlayer({
    name: name.value,
    team_category: parseInt(route.params.categoryYear),
  })
  await playersStore.getPlayers(parseInt(route.params.categoryYear))
  visible.value = false
  name.value = ''
}

onMounted(async () => {
  await teamsStore.getTeam(route.params.teamId)
  await playersStore.getPlayers(parseInt(route.params.categoryYear))
})

</script>

<template>
  <main class="flex flex-column justify-content-start align-items-center h-full">
    <header class="w-full">
      <Breadcrumb class="py-2 px-0" :model="items">
      </Breadcrumb>
      <div class="flex pt-2 gap-2 justify-content-between pb-2 align-items-start ">
        <h1 class="mt-0">Categoría {{ categoryYear }}</h1>
        <CreatePlayerDialog :category-id="parseInt(route.params.categoryYear)"/>
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
          <router-link :to="categoryYear + '/players/' + slotProps.data.id">
            <Button icon="pi pi-external-link" class="mr-2"/>
          </router-link>
          <CreatePlayerDialog :category-id="parseInt(route.params.categoryYear)" :player="slotProps.data"
                              :edit-mode="true"/>
        </template>
      </Column>
    </DataTable>
  </main>
</template>