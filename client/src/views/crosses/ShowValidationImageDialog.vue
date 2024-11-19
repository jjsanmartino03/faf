<script setup lang="ts">

import TeamSelect from "./TeamSelect.vue";
import Button from "primevue/button";
import ProgressSpinner from "primevue/progressspinner";
import Dialog from "primevue/dialog";
import Calendar from "primevue/calendar";
import {ref} from "vue";

const props = defineProps({
  validationId: {
    required: true,
    type: Number
  }
})

const apiUrl = import.meta.env.VITE_API_URL

const visible = ref(false);
</script>

<template>
  <Button size="small" @click="visible = true" icon="pi pi-image"/>

  <Dialog :draggable="false" @hide="visible = false" class="mx-3 w-full md:w-6 lg:w-4" v-model:visible="visible" modal header="Validación">
    <div class="w-full">

      <img class=" w-full " :src="`${apiUrl}media/validations/${props.validationId}.jpeg`" alt="validation image"/>
    </div>
  </Dialog>
</template>

<style scoped>

</style>