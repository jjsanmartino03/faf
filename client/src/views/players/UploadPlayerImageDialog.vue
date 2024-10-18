<script setup lang="ts">
import {PropType, ref} from "vue";
import Button from "primevue/button";
import Dialog from "primevue/dialog";
import FloatLabel from "primevue/floatlabel";
import InputText from "primevue/inputtext";
import FileUpload from "primevue/fileupload";
import {useTeamsStore, Team} from "../../store/teams";
import ProgressSpinner from "primevue/progressspinner";
import {usePlayersStore, Player} from "../../store/players.ts";

const visible = ref(false);
const props = defineProps({
  playerId: {
    type: Number,
    required: true
  }
})

const {getPlayer, statusUploadImage, uploadImage} = usePlayersStore()

const image = ref<File | null>(null)
const src = ref<string | null>(null)

function onFileSelect(event) {
  const file = event.files[0];
  const reader = new FileReader();

  reader.onload = async (e) => {
    src.value = e.target.result as string;
  };

  image.value = file

  reader.readAsDataURL(file);
}

const onSubmit = async (e) => {
  e.preventDefault()

  let error = null

  if(!image.value) return
  error = await uploadImage(props.playerId,image.value)

  if (error) return

  await getPlayer(props.playerId)
  visible.value = false
}

</script>

<template>
  <Button icon="pi pi-plus" rounded raised @click="visible = true" />
  <Dialog :draggable="false" v-model:visible="visible" modal header="Subir foto del jugador"
          :style="{ width: '25rem' }">
    <form @submit.prevent="(e) => onSubmit(e)"
          class="flex flex-column w-full align-items-center justify-content-center">
      <div class="p-field ">
        <div class="card flex flex-column align-items-center gap-3">
          <FileUpload accept="image/jpeg,image/png" mode="basic" @select="onFileSelect" customUpload auto severity="secondary" class="p-button-outlined" />
          <img v-if="src" :src="src" alt="Image" class="shadow-md rounded-xl w-full sm:w-64" />
        </div>
      </div>
      <div v-if="statusUploadImage != 'loading'" class="flex justify-end gap-2 mt-4">
        <Button type="button" label="Cancelar" severity="secondary" @click="visible = false"></Button>
        <Button type="submit" label="Guardar"></Button>
      </div>
      <div v-else class="flex justify-content-center">
        <ProgressSpinner strokeWidth="4" style="width: 1.5rem; height: 1.5rem;"/>
      </div>
    </form>
  </Dialog>
</template>