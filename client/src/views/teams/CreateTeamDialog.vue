<script setup lang="ts">
import {PropType, ref} from "vue";
import Button from "primevue/button";
import Dialog from "primevue/dialog";
import FloatLabel from "primevue/floatlabel";
import InputText from "primevue/inputtext";
import {useTeamsStore, Team} from "../../store/teams";
import ProgressSpinner from "primevue/progressspinner";
import FileUpload from "primevue/fileupload";

const visible = ref(false);
const props = defineProps({
  team: {
    type: Object as PropType<Team>,
    default: null
  },
  editMode: {
    type: Boolean,
    default: false
  },
})
const name = ref(props.team ? props.team.name : '');
const logo_url = ref(props.team ? props.team.logo_url : '');


const {createTeam, statusCreateTeam, getTeams, updateTeam} = useTeamsStore()


const onSubmit = async (e, editMode) => {
  e.preventDefault()

  let error = null
  if (editMode) {
    error = await updateTeam(props.team.id, {
      name: name.value,
      logo_url: logo_url.value
    })
  } else {
    error = await createTeam({
      name: name.value,
      logo_url: logo_url.value
    })
  }

  if (error) return

  await getTeams()
  visible.value = false
}

console.log(props.team);
</script>

<template>
  <Button v-if="editMode" @click="visible = true" icon="pi pi-pen-to-square"/>
  <Button v-else label="Nuevo equipo" icon="pi pi-plus" class="mt-4" size="small" @click="visible = true"/>
  <Dialog :draggable="false" class="mx-3" v-model:visible="visible" modal
          :header="editMode ? 'Actualizar equipo' : 'Crear equipo'" :style="{ width: '25rem' }">
    <form @submit.prevent="(e) => onSubmit(e,editMode)"
          class="flex flex-column w-full align-items-center justify-content-center">
      <div class="p-field mt-4">
        <FloatLabel>
          <label for="name">Nombre</label>
          <InputText required="true" id="name" v-model="name"/>
        </FloatLabel>
      </div>
      <div class="p-field mt-4 flex flex-column">
        <FloatLabel>
          <label for="logo">Url de la imagen</label>
          <InputText required="true" id="logo" v-model="logo_url"/>
        </FloatLabel>
        <!--<div>O</div>
<div class="card flex flex-column align-items-center gap-3">
          <FileUpload accept="image/jpeg,image/png" mode="basic" @select="onFileSelect" customUpload auto severity="secondary" class="p-button-outlined" />
          <img v-if="src" :src="src" alt="Image" class="shadow-md rounded-xl w-full sm:w-64" />
        </div>-->
      </div>
      <div v-if="statusCreateTeam != 'loading'" class="flex justify-end gap-2 mt-4">
        <Button type="button" label="Cancelar" severity="secondary" @click="visible = false"></Button>
        <Button type="submit" label="Guardar"></Button>
      </div>
      <div v-else class="flex justify-content-center">
        <ProgressSpinner strokeWidth="4" style="width: 1.5rem; height: 1.5rem;"/>
      </div>
    </form>
  </Dialog>
</template>