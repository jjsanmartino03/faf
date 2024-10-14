<script setup>
import {ref} from "vue";
import Button from "primevue/button";
import Dialog from "primevue/dialog";
import FloatLabel from "primevue/floatlabel";
import InputText from "primevue/inputtext";
import {useTeamsStore} from "../../store/teams";
import ProgressSpinner from "primevue/progressspinner";
import {useCrossesStore} from "../../store/crosses";

const visible = ref(false);
const name = ref('');
const logo_url = ref('');

const {statusCreateCross, getCrosses} = useCrossesStore()


const onSubmit = async (e) => {
  e.preventDefault()


}
</script>

<template>
  <Button label="Agregar Cruce" icon-pos="right" @click="visible = true" class="w-full" icon="pi pi-plus"/>
  <Dialog class="mx-3" v-model:visible="visible" modal header="Crear cruce" :style="{ width: '25rem' }">
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
      <div v-if="statusCreateCross != 'loading'" class="flex justify-end gap-2 mt-4">
        <Button type="button" label="Cancelar" severity="secondary" @click="visible = false"></Button>
        <Button type="submit" label="Guardar"></Button>
      </div>
      <div v-else class="flex justify-content-center">
        <ProgressSpinner strokeWidth="4" style="width: 1.5rem; height: 1.5rem;"/>
      </div>
    </form>
  </Dialog>
</template>