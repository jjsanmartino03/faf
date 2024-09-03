<script setup>
import {ref} from "vue";
import Button from "primevue/button";
import Dialog from "primevue/dialog";
import FloatLabel from "primevue/floatlabel";
import InputText from "primevue/inputtext";

const visible = ref(false);
const name = ref('');
const logo = ref('');
</script>

<template>
  <Button label="Nuevo equipo" icon="pi pi-plus" class="mt-4" size="small" @click="visible = true"/>
  <Dialog v-model:visible="visible" modal header="Crear equipo" :style="{ width: '25rem' }">
    <form class="flex flex-column gap-3">
      <div class="p-field">
        <FloatLabel>
          <label for="name">Nombre</label>
          <InputText id="name" v-model="name"/>
        </FloatLabel>
      </div>
      <div class="p-field">
        <FloatLabel>
          <label for="logo">Escudo</label>
          <InputText id="logo" v-model="logo"/>
        </FloatLabel>
      </div>
      <div class="flex justify-end gap-2">
        <Button type="button" label="Cancel" severity="secondary" @click="visible = false"></Button>
        <Button type="button" label="Save" @click="visible = false"></Button>
      </div>
    </form>
  </Dialog>
</template>