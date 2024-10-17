<script setup lang="ts">
import {computed, defineProps, onMounted, onUpdated, PropType, ref, toRaw, watch} from "vue";
import Button from "primevue/button";
import Dialog from "primevue/dialog";
import Calendar from "primevue/calendar";
import {useTeamsStore, Team} from "../../store/teams";
import ProgressSpinner from "primevue/progressspinner";
import {Cross, useCrossesStore} from "../../store/crosses";
import TeamSelect from "./TeamSelect.vue";
import {getDateFromString, getDateString} from "../../utils/dates";

const props = defineProps({
  onCompleteAction: {
    required: true,
    type: Function as PropType<() => void>,
  },
  editMode: {
    required: false,
    type: Boolean as PropType<boolean>,
    default: false
  },
  cross: {
    required: false,
    type: Object as PropType<Cross>,
    default: null
  }
})

const visible = ref(false);
const localTeam = ref<Team | null>(props.cross?.local_team ?? null);
const visitorTeam = ref<Team | null>(props.cross?.visitor_team ?? null);
const date = ref<Date | null>(props.cross ? getDateFromString(props.cross.date) : null)

const crossesStore = useCrossesStore()
const {statusGetTeams, getTeams, ...teamsStore} = useTeamsStore();


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

const onSubmit = async (e, editMode: boolean) => {
  e.preventDefault()

  let error = null;
  if (editMode) {
    error = await crossesStore.updateCross(props.cross.id, {
      date: getDateString(date.value)
    })
  } else {
    error = await crossesStore.createCross({
      local_team_id: localTeam.value?.id,
      visitor_team_id: visitorTeam.value?.id,
      date: getDateString(date.value)
    })
  }

  if (error) return

  props.onCompleteAction()
  visible.value = false
}
</script>

<template>
  <Button v-if="editMode" size="small" @click="visible = true" icon="pi pi-pen-square"/>
  <Button v-else label="Agregar Cruce" icon-pos="right" @click="visible = true" class="w-full" icon="pi pi-plus"/>

  <Dialog @hide="clear" class="mx-3 w-full md:w-6 lg:w-4" v-model:visible="visible" modal header="Crear cruce">
    <form @submit.prevent="(e) => onSubmit(e,editMode)"
          class="flex flex-column gap-3 w-full align-items-center justify-content-center">
      <div class="p-field w-full">
        <label>Equipo local</label>
        <TeamSelect :disabled="editMode" v-model="localTeam"/>
      </div>
      <div class="p-field w-full">
        <label>Equipo visitante</label>
        <TeamSelect :disabled="editMode" v-model="visitorTeam"/>
      </div>
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