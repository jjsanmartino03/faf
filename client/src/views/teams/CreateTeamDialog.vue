<script setup>
import {ref} from "vue";
import Button from "primevue/button";
import Dialog from "primevue/dialog";
import FloatLabel from "primevue/floatlabel";
import InputText from "primevue/inputtext";
import {useTeamsStore} from "../../store/teams";
import ProgressSpinner from "primevue/progressspinner";

const visible = ref(false);
const name = ref('');
const logo_url = ref('');

const {createTeam, statusCreateTeam, getTeams} = useTeamsStore()


const onSubmit = async (e) => {
  e.preventDefault()
  await createTeam({
    name: name.value,
    logo_url: logo_url.value
  })
  await getTeams()
  visible.value = false
}
</script>

<template>
  <Button label="Nuevo equipo" icon="pi pi-plus" class="mt-4" size="small" @click="visible = true"/>
  <Dialog class="mx-3" v-model:visible="visible" modal header="Crear equipo" :style="{ width: '25rem' }">
    <form @submit.prevent="onSubmit" class="flex flex-column w-full align-items-center justify-content-center">
      <div class="p-field mt-4">
        <FloatLabel>
          <label for="name">Nombre</label>
          <InputText required="true" id="name" v-model="name"/>
        </FloatLabel>
      </div>
      <div class="p-field mt-4">
        <FloatLabel>
          <label for="logo">Url de la imagen</label>
          <InputText required="true" id="logo" v-model="logo_url"/>
        </FloatLabel>
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