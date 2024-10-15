<script setup lang="ts">
import {computed, defineProps, onMounted, onUpdated, PropType, ref, toRaw, watch} from "vue";
import Button from "primevue/button";
import Dialog from "primevue/dialog";
import Calendar from "primevue/calendar";
import {useTeamsStore} from "../../store/teams";
import ProgressSpinner from "primevue/progressspinner";
import {Cross, useCrossesStore} from "../../store/crosses";
import TeamSelect from "./TeamSelect.vue";
import Team from "../../interfaces/team";
import {getDateString} from "../../utils/dates";

const props = defineProps({
  onCreateCross: {
    required: true,
    type: Function as PropType<() => void>,
  }
})

const visible = ref(false);
const localTeam = ref<Team | null>(null);
const visitorTeam = ref<Team | null>(null);
const date = ref<Date | null>(null);

const crossesStore = useCrossesStore()
const {statusGetTeams, getTeams, ...teamsStore} = useTeamsStore();


const onSubmit = async (e) => {
  e.preventDefault()

  const error = await crossesStore.createCross({
    local_team_id: localTeam.value?.id,
    visitor_team_id: visitorTeam.value?.id,
    date: getDateString(date.value)
  })

  if (error) return

  props.onCreateCross()
  visible.value = false
}
const teams = computed(() => teamsStore.teams)

onMounted(() => {
  getTeams()
})

const status = computed(() => crossesStore.statusCreateCross)

const clear = () => {
  localTeam.value = null
  visitorTeam.value = null
  date.value = null
}
</script>

<template>
  <Button label="Agregar Cruce" icon-pos="right" @click="visible = true" class="w-full" icon="pi pi-plus"/>
  <Dialog @hide="clear" class="mx-3 w-full md:w-6 lg:w-4" v-model:visible="visible" modal header="Crear cruce">
    <form @submit.prevent="onSubmit" class="flex flex-column gap-3 w-full align-items-center justify-content-center">
      <div class="p-field w-full">
        <label>Equipo local</label>
        <TeamSelect v-model="localTeam" :status-get-teams="statusGetTeams"/>
      </div>
      <div class="p-field w-full">
        <label>Equipo visitante</label>
        <TeamSelect v-model="visitorTeam" :status-get-teams="statusGetTeams"/>
      </div>
      <p>{{ crossesStore.statusCreateCross }}</p>
      <p>{{ status }}</p>
      <div class="p-field w-full">
        <Calendar :min-date="new Date()" placeholder="Elige una fecha" class="w-full" v-model="date"
                  dateFormat="dd/mm/yy" showIcon/>
      </div>
      <div v-if="status !== 'loading'" class="flex justify-end gap-2 mt-4">
        <Button type="button" label="Cancelar" severity="secondary" @click="visible = false"></Button>
        <Button :disabled="localTeam?.id === undefined  || visitorTeam?.id == undefined || !date" type="submit"
                label="Guardar"></Button>
      </div>
      <div v-else class="flex justify-content-center">
        <ProgressSpinner strokeWidth="4" style="width: 1.5rem; height: 1.5rem;"/>
      </div>
    </form>
  </Dialog>
</template>