<script setup lang="ts">
import { ref,watch } from "vue";
import Dialog from "primevue/dialog";
import FileUpload from "primevue/fileupload";
import { defineProps } from "vue";
import { defineEmits } from "vue";
import Button from "primevue/button";
import { useTeamsStore } from "../../store/teams";

const {uploadImage,statusUploadImage} = useTeamsStore()

const props = defineProps({
    visible: {
        type: Boolean,
        default: false
    },
    onComplete: {
      type: Function,
      required: true
    },
    validationId: {
        type: Number,
        isRequired: true
    },
})

const visible = ref(false);
const image = ref<File | null>(null)
const src = ref<string | null>(null)

const emit = defineEmits(['update:visible'])

const onSubmit = async (e) => {
  e.preventDefault()
  let error = null
  if(!image.value) return
  error = await uploadImage(props.validationId,image.value)
  if (error) return

  props.onComplete && props.onComplete()
  visible.value = false
  image.value = null
  src.value = null
}

const onHide = () => {
    visible.value = false;
    image.value = null;
    src.value = null;
}

const onFileSelect = (event) => {
  const file = event.files[0];
  const reader = new FileReader();

  reader.onload = async (e) => {
    src.value = e.target.result as string;
  };

  image.value = file

  reader.readAsDataURL(file);
}

watch(() => props.visible, (newVal) => {
  visible.value = newVal;
});

watch(() => visible.value, (newVal) => {
    emit('update:visible', newVal);
});
</script>

<template>
    <Dialog class="max-w-full lg:w-6" v-model:visible="visible" header="Subir imagen de validación" @hide="onHide">
        <form @submit.prevent="(e) => onSubmit(e)"
            class="flex flex-column w-full align-items-center justify-content-center ">
            <div class="p-field ">
                <div class="card flex flex-column align-items-center gap-3">
                    <FileUpload accept="image/jpeg,image/png" mode="basic" @select="onFileSelect" customUpload auto
                        severity="secondary" class="p-button-outlined" />
                    <img v-if="src" :src="src" alt="Image" class="shadow-md rounded-xl w-full sm:w-64" />
                </div>
            </div>
            <div v-if="statusUploadImage != 'loading'" class="flex justify-end gap-2 mt-4">
                <Button type="button" label="Cancelar" severity="secondary" @click="visible = false"></Button>
                <Button type="submit" label="Guardar"></Button>
            </div>
            <div v-else class="flex justify-content-center">
                <ProgressSpinner strokeWidth="4" style="width: 1.5rem; height: 1.5rem;" />
            </div>
        </form>
    </Dialog>
</template>